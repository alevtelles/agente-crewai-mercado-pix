# 🏦 Agente Mercado Pix

Sistema de Inteligência de Mercado que integra **dados reais do sistema Pix** com análise financeira utilizando **CrewAI** e **dados oficiais do Banco Central do Brasil**.

## 🏗️ Arquitetura

```
┌──────────────────────┐
│   Frontend (UI)      │
│   (Streamlit)        │
└─────────┬────────────┘
          │
          ▼
┌────────────────────────┐
│   Orquestrador         │
│   (CrewAI)             │
└─────┬──────┬───────────┘
      │      │
      ▼      ▼
┌───────────────┐  ┌──────────────┐
│ 4 Agentes AI  │  │ API Pix BCB  │
│ Especializados│  │ (Dados Pix)  │
└───────────────┘  └──────────────┘
```

## 🤖 Agentes CrewAI

1. **🎯 Especialista em Dados Pix** - Coleta estatísticas oficiais do Banco Central
2. **📰 Pesquisador de Mercado** - Busca informações sobre fintechs e tendências
3. **📊 Analista Financeiro** - Cruza dados e gera insights estratégicos
4. **📋 Redator Executivo** - Consolida relatórios profissionais

## 🚀 Instalação e Uso

### Método Recomendado (Script Automático)
```bash
# Clone o projeto
git clone <repository>
cd agent-mercado-pix

# Execute o script automático
./start_venv.sh
```

### Método Manual
```bash
# Criar ambiente virtual
python3 -m venv venv
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Configurar API Key
cp .env.example .env
# Editar .env com sua OPENAI_API_KEY

# Executar aplicação
python app.py              # Interface web (padrão)
python app.py --demo       # Demo rápido
python app.py --analysis   # Análise completa
```

## 📱 Interface Streamlit

A interface web oferece:

- **⚙️ Configurações** - Parâmetros de análise e município
- **📊 Dashboard** - Visualizações dos dados Pix
- **📈 Gráficos** - Evolução temporal e métricas
- **📋 Relatórios** - Download de análises completas

### Funcionalidades

- ✅ Seleção de município e período
- ✅ Três modos de execução (Demo, Completa, Teste)
- ✅ Visualizações interativas com Plotly
- ✅ Status em tempo real dos agentes
- ✅ Download de relatórios
- ✅ Interface responsiva e intuitiva

## 🎯 Modos de Uso

### Interface Web (Recomendado)
```bash
python app.py --web
# ou simplesmente
python app.py
```

### Demo Rápido
```bash
python app.py --demo
```

### Análise Completa
```bash
python app.py --analysis --municipio "SAO PAULO" --periodo "2024-01"
```

## 📊 API Dados Pix

O sistema utiliza a API oficial do Banco Central:
- **Endpoint**: `https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata`
- **Dados**: Transações Pix por município e período
- **Formato**: OData/JSON

### Exemplo de consulta:
```
TransacoesPixPorMunicipio?$filter=MesAno eq '2024-01' and Municipio eq 'São Paulo'&$format=json
```

## 🗂️ Estrutura do Projeto

```
agent-mercado-pix/
├── app.py               # 🚀 Ponto de entrada principal
├── streamlit_app.py     # 🌐 Interface web Streamlit
├── main.py              # 📊 CLI análise completa
├── run_demo.py          # ⚡ Demo rápido
├── start_app.py         # 🔧 Script alternativo
├── start_venv.sh        # 🐍 Script ambiente virtual
├── requirements.txt     # 📦 Dependências Python
├── .env.example         # ⚙️  Configuração exemplo
├── .gitignore          # 🙈 Arquivos ignorados
├── venv/               # 🏠 Ambiente virtual Python
├── src/
│   ├── agents/         # 🤖 4 agentes CrewAI especializados
│   ├── tasks/          # 📋 Definições de tarefas
│   ├── tools/          # 🔌 Integração API Pix BCB
│   └── crew_orchestrator.py  # 🎭 Coordenador principal
└── plano.md           # 📚 Documentação da arquitetura
```

## 🔑 Configuração

### Variáveis de ambiente (.env):
```env
OPENAI_API_KEY=sua_chave_openai_aqui
DATABASE_URL=postgresql://username:password@localhost/db
BCB_API_BASE_URL=https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata
```

## 📈 Funcionalidades Principais

### 🌐 Interface Web Streamlit
- Dashboard interativo e responsivo
- Configuração visual de parâmetros
- Gráficos em tempo real
- Download de relatórios

### 🤖 Análise com IA (CrewAI)
- 4 agentes especializados trabalhando em equipe
- Integração com dados reais do Banco Central
- Análise financeira automatizada
- Relatórios executivos profissionais

### 📊 Dados Oficiais Pix
- API oficial do Banco Central do Brasil
- Dados reais de transações por município
- Estatísticas financeiras detalhadas
- Informações atualizadas mensalmente

## 🎨 Interface Visual

A interface Streamlit inclui:
- 📊 Gráficos interativos (Plotly)
- 📋 Tabs organizadas por tipo de dados
- 🎛️ Sidebar com configurações
- 📥 Download de relatórios
- 🔄 Status em tempo real

## 🤝 Como Contribuir

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.

## 🆘 Suporte

Para dúvidas e suporte:
- 📧 Abra uma issue no repositório
- 📖 Consulte a documentação em `plano.md`
- 🧪 Execute os testes para verificar o ambiente

---

**Desenvolvido com ❤️ usando CrewAI, Streamlit e dados oficiais do Banco Central do Brasil.**
