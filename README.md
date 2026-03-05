# \# Análise Calórica e Progresso de Dieta

# 

# > Um sistema completo de rastreamento nutricional que combina inteligência artificial (Claude API), automação e visualização de dados para acompanhar sua dieta em tempo real.

# 

# ---

# 

# \## O que é isso?

# 

# DietPlanner nasceu de uma necessidade simples e pessoal minha, que é registrar minhas refeições diárias e entender padrões alimentares ao longo do tempo. O que começou como uma planilha manual evoluiu para um pipeline completo, desde o formulário de entrada até um dashboard interativo no Power BI, com cálculo automático de macronutrientes via Claude AI.

# 

# A ideia central é que o usuário não precise pensar em infraestrutura. Você registra o que comeu em detalhe de forma textual, uma estimativa das calorias consumidas e o sistema calcula os macros, armazena tudo e atualiza o dashboard automaticamente.

# 

# ---

# 

# \## Como funciona

# 

# ```

1. # Você preenche o formulário
2. # FastAPI recebe e salva no Google Sheets
3. # Apps Script detecta a entrada e chama a API do Claude
4. # Claude estima carboidratos, proteínas e gorduras com base no seu prato e quantidade de calorias estimadas
5. # Power BI Service lê os dados e atualiza o dashboard
6. # Você visualiza seu progresso em tempo real



# ```

# 

# O Google Sheets nesse caso funciona como banco de dados, o Power BI transforma os dados em gráficos úteis e o Claude faz o trabalho mais complexo de estimar nutrição sem que precise pesquisar cada alimento.

# 

# ---

# 

# \## Funcionalidades

# 

# \*\*Registro de refeições\*\*: formulário web simples com data, tipo de refeição, calorias, peso e descrição do prato. Suporte a modo Esteira, onde as calorias são automaticamente contabilizadas como negativas no balanço do dia.

# 

# \*\*Cálculo automático de macros\*\*: ao preencher o campo "Prato", o Apps Script aciona o Claude via API e salva estimativas de carboidratos, proteínas e gorduras diretamente na planilha.

# 

# \*\*Dashboard Power BI\*\*: visualizações de saldo metabólico, progresso de peso, distribuição de macronutrientes, calorias queimadas por semana e comparação de IMC ao longo do tempo, além de outros gráficos úteis.

# 

# \*\*TMB dinâmica\*\*: a Taxa Metabólica Basal é recalculada diariamente com base no peso atual, usando os dados de perfil (idade, altura, peso inicial e meta).

# 

# \*\*Atualização automática\*\*: o Power BI Service é configurado com atualização agendada diária (3 vezes ao dia), sem necessidade de abrir o Power BI Desktop.

# 

# ---

# 

# \## Tecnologias

# 

* # Frontend: HTML, CSS, JavaScript puro
* # Backend: Python + FastAPI
* # Banco de dados: Google Sheets via API
* # Automação de macros: Google Apps Script + Claude API
* # Visualização: Power BI Desktop
* # Hospedagem: Render

# 

# ---



