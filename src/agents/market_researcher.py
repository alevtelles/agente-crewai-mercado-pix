from crewai import Agent
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

load_dotenv()

def create_market_researcher():
    """Cria o agente pesquisador de mercado"""
    
    llm = ChatOpenAI(
        model="gpt-4",
        temperature=0.4,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    agent = Agent(
        role="Pesquisador de Mercado Financeiro",
        goal="Pesquisar e coletar informações relevantes sobre mercado financeiro, fintechs e sistema de pagamentos",
        backstory="""
        Você é um pesquisador experiente especializado em mercado financeiro brasileiro.
        Tem vasto conhecimento sobre fintechs, bancos digitais, sistemas de pagamento
        e tendências do setor financeiro. Você sabe onde encontrar informações confiáveis
        e como interpretar dados de mercado, notícias e relatórios setoriais.
        """,
        verbose=True,
        allow_delegation=False,
        llm=llm,
        max_iter=3,
        memory=True
    )
    
    def search_financial_news(query: str, limit: int = 5):
        """
        Função para buscar notícias financeiras relevantes
        
        Args:
            query: Termo de busca
            limit: Limite de resultados
        """
        try:
            # Simulação de busca de notícias - em produção usar APIs reais
            news_sources = [
                "InfoMoney", "Valor Econômico", "Estadão Economia", 
                "G1 Economia", "UOL Economia"
            ]
            
            # Retorna estrutura simulada de notícias
            results = []
            for i in range(min(limit, len(news_sources))):
                results.append({
                    "fonte": news_sources[i],
                    "titulo": f"Notícia sobre {query} - Fonte {news_sources[i]}",
                    "resumo": f"Informações relevantes sobre {query} encontradas em {news_sources[i]}",
                    "relevancia": "alta" if i < 2 else "média"
                })
            
            return {
                "query": query,
                "resultados": results,
                "total_encontrado": len(results)
            }
            
        except Exception as e:
            return {"error": f"Erro ao buscar notícias: {e}"}
    
    def get_market_indicators():
        """
        Obtém indicadores básicos de mercado
        """
        try:
            # Simulação de indicadores - em produção usar APIs financeiras reais
            indicators = {
                "selic": "10.75%",
                "ipca_mensal": "0.38%",
                "dolar": "R$ 5.89",
                "ibovespa": "125.430 pontos",
                "pix_crescimento": "15% ao ano",
                "fonte": "Simulado - usar APIs reais em produção"
            }
            
            return indicators
            
        except Exception as e:
            return {"error": f"Erro ao buscar indicadores: {e}"}
    
    # Retorna agente e funções separadamente
    return agent, search_financial_news, get_market_indicators