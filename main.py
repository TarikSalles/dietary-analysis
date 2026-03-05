from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
import gspread
from google.oauth2.service_account import Credentials
from datetime import date
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve o index.html na raiz
@app.get("/")
def root():
    return FileResponse("index.html")

# ── CONFIG ────────────────────────────────────────────
CREDENTIALS_FILE = "projeto-de-analise-calorica-a287fc239d76.json"  # coloque seu JSON aqui
SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")
SHEET_NAME = os.getenv("SHEET_NAME", "Ganhos e Perdas")

def get_sheet():
    scopes = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds_json = os.getenv("GOOGLE_CREDENTIALS")
    if creds_json:
        creds = Credentials.from_service_account_info(json.loads(creds_json), scopes=scopes)
    else:
        creds = Credentials.from_service_account_file("service_account.json", scopes=scopes)
    client = gspread.authorize(creds)
    return client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)

@app.get("/config")
def config():
    return {"powerbi_url": os.getenv("POWERBI_URL", "")}


class Entrada(BaseModel):
    data: str
    refeicao: str
    calorias: float
    prato: Optional[str] = ""
    peso: Optional[float] = None

def get_sheet():
    scopes = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=scopes)
    client = gspread.authorize(creds)
    return client.open_by_key(SPREADSHEET_ID).worksheet(SHEET_NAME)

@app.post("/registrar")
def registrar(entrada: Entrada):
    try:
        sheet = get_sheet()
        linha = [
    entrada.data,
    entrada.refeicao,
    float(entrada.calorias),
    entrada.prato or "",
    float(entrada.peso) if entrada.peso is not None else "",
]
        sheet.append_row(linha, value_input_option='USER_ENTERED')
        return {"ok": True, "linha": linha}
    except FileNotFoundError:
        raise HTTPException(status_code=500, detail="service_account.json não encontrado")
    except Exception as e:
        print(f"ERRO: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
