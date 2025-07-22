from crewai import Agent
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from ..tools.pix_api import PixAPIClient

load_dotenv()

def create_pix_agent():
    """Cria o agente especializado em dados Pix do Banco Central"""
    
    llm = ChatOpenAI(
        model="gpt-4",
        temperature=0.3,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    pix_client = PixAPIClient()
    
    agent = Agent(
        role="Especialista em Dados Pix",
        goal="Coletar e analisar estatísticas de transações Pix do Banco Central do Brasil",
        backstory="""
        Você é um especialista em dados financeiros do sistema Pix brasileiro.
        Tem acesso às APIs oficiais do Banco Central e conhece profundamente
        os padrões de pagamentos instantâneos no país. Sua expertise inclui
        análise de volumes transacionais, tendências regionais e sazonalidade
        dos pagamentos Pix.
        """,
        verbose=True,
        allow_delegation=False,
        llm=llm,
        max_iter=3,
        memory=True
    )
    
    # Adiciona função customizada para buscar dados Pix
    def fetch_pix_data(municipio: str, ano_mes: str, estado: str = None):
        """
        Função personalizada para buscar dados Pix
        
        Args:
            municipio: Nome do município (opcional se estado fornecido)
            ano_mes: Período no formato 'YYYY-MM'
            estado: Sigla do estado (opcional)
        """
        if municipio and not estado:
            return pix_client.get_pix_statistics_summary(municipio, ano_mes, "municipio")
        elif estado and not municipio:
            return pix_client.get_pix_statistics_summary(estado, ano_mes, "estado")
        elif municipio:
            return pix_client.get_pix_statistics_summary(municipio, ano_mes, "municipio")
        else:
            return {"error": "É necessário fornecer município ou estado"}
    
    # Retorna agente e função separadamente
    return agent, fetch_pix_data