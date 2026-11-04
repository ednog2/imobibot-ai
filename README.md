  ImobiBot AI

 Assistente imobiliário inteligente desenvolvido com Python, Streamlit e Google Gemini

O **ImobiBot AI** é um chatbot imobiliário que utiliza inteligência artificial generativa para auxiliar clientes na busca e comparação de imóveis, oferecendo respostas personalizadas em linguagem natural.

O projeto foi desenvolvido como demonstração prática de integração entre uma aplicação Python, uma API de inteligência artificial e um catálogo estruturado de imóveis.

 Funcionalidades

- Atendimento conversacional com inteligência artificial Google Gemini.
- Busca de imóveis por localização, quantidade de quartos e orçamento.
- Comparação de imóveis considerando preço, metragem e necessidades do cliente.
- Consulta a um catálogo local de imóveis em formato JSON.
- Links para anúncios imobiliários.
- Sistema de resposta alternativa caso a API de IA esteja indisponível.
- Interface interativa desenvolvida com Streamlit.

  Tecnologias utilizadas

- **Python:** lógica da aplicação e processamento de dados.
- **Streamlit:** interface web e chat interativo.
- **Google Gemini API:** geração de respostas com inteligência artificial.
- **Google GenAI SDK:** comunicação com os modelos Gemini.
- **JSON:** armazenamento dos imóveis disponíveis no catálogo.
- **Python-dotenv:** gerenciamento de variáveis de ambiente.

  Como funciona

1. O usuário envia uma mensagem pelo chatbot.
2. A aplicação interpreta os filtros da solicitação.
3. O sistema consulta o catálogo de imóveis.
4. As informações encontradas são encaminhadas ao Gemini.
5. A inteligência artificial elabora uma resposta em linguagem natural, utilizando os dados disponíveis.
6. Caso a API falhe, o sistema apresenta uma resposta alternativa baseada no catálogo.

O Gemini é responsável pela experiência conversacional, enquanto o Python realiza a consulta estruturada aos dados.

 Estrutura do projeto

```text
imobibot-ai/
├── app.py
├── catalogo.py
├── imoveis.json
├── requirements.txt
├── .gitignore
└── README.md
```

 💻 Como executar

**1. Clone o repositório:**

```bash
git clone https://github.com/ednog2/imobibot-ai.git
cd imobibot-ai
```

**2. Crie um ambiente virtual:**

```bash
python -m venv .venv
```

**3. Ative o ambiente virtual:**

No Windows:

```powershell
.\.venv\Scripts\Activate.ps1
```

**4. Instale as dependências:**

```bash
pip install -r requirements.txt
```

**5. Configure a chave da API:**

Crie um arquivo `.env` na raiz do projeto com:

```env
GEMINI_API_KEY=sua_chave_aqui
```

A chave pode ser obtida no Google AI Studio.

**6. Execute a aplicação:**

```bash
streamlit run app.py
```

O Streamlit exibirá o endereço local para acessar o chatbot pelo navegador.

 Dados imobiliários

O projeto utiliza um catálogo demonstrativo de imóveis da região de Gleba Palhano, em Londrina/PR, com referências a anúncios da imobiliária Santamérica.

Os dados são utilizados para fins de demonstração técnica. Valores, características e disponibilidade devem ser confirmados nas fontes originais.

 Segurança

A chave de API é armazenada em variável de ambiente e não deve ser publicada no repositório.

O arquivo `.gitignore` exclui arquivos sensíveis e o ambiente virtual.

 Possíveis evoluções

- Memória contextual entre mensagens.
- Integração com APIs e sistemas imobiliários.
- Atualização automática do catálogo.
- Agendamento de visitas.
- Filtros avançados e recomendações personalizadas.
- Implantação da aplicação em ambiente de nuvem.

Observações Sobre o projeto

Desenvolvido como projeto demonstrativo para um processo seletivo na área de tecnologia, combinando experiência no mercado imobiliário com aplicação prática de inteligência artificial e desenvolvimento de software, o catálogo se limita a anúncios imobiliários recentes e podem sofrer alterações durante o uso do chatbot.
