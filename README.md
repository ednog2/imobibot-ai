ImobiBot AI

Chatbot imobiliário desenvolvido em Python + Streamlit, integrado à API Google Gemini para responder perguntas sobre imóveis em linguagem natural.

Como executar

1. Clone o repositório:

git clone https://github.com/ednog2/imobibot-ai.git
cd imobibot-ai

2. Instale as dependências:

pip install -r requirements.txt

3. Configure sua chave do Gemini:

Crie um arquivo .env na pasta do projeto:

GEMINI_API_KEY=sua_chave_aqui

A chave pode ser obtida no Google AI Studio.

4. Inicie o chatbot:

streamlit run app.py

Abra o endereço local exibido no terminal, normalmente http://localhost:8501.

Tecnologias

Python, Streamlit, Google Gemini API, Google GenAI SDK e JSON.

Observações

O catálogo é demonstrativo, com referências a anúncios imobiliários de Londrina/PR no dia 04/11/2026

A chave da API não é incluída no repositório por segurança.
