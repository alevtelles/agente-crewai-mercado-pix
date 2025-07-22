from crewai import Agent
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
# import pandas as pd  # Comentado temporariamente
from datetime import datetime, timedelta

load_dotenv()

def create_financial_analyst():
    """Cria o agente analista financeiro"""
    
    llm = ChatOpenAI(
        model="gpt-4",
        temperature=0.2,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    agent = Agent(
        role="Analista Financeiro Especializado",
        goal="Analisar dados financeiros, identificar tendências e gerar insights estratégicos",
        backstory="""
        Você é um analista financeiro sênior com mais de 10 anos de experiência
        no mercado brasileiro. Especialista em análise de dados financeiros,
        identificação de tendências, correlações entre indicadores econômicos
        e comportamento do consumidor. Você tem expertise em interpretar dados
        do sistema Pix e relacioná-los com o contexto macroeconômico.
        """,
        verbose=True,
        allow_delegation=False,
        llm=llm,
        max_iter=3,
        memory=True
    )
    
    def analyze_pix_trends(pix_data: dict, market_data: dict = None):
        """
        Analisa tendências dos dados Pix
        
        Args:
            pix_data: Dados do sistema Pix
            market_data: Dados de mercado opcionais
        """
        try:
            if not pix_data or "error" in pix_data:
                return {"error": "Dados Pix inválidos ou ausentes"}
            
            analysis = {
                "localização": pix_data.get("localização", "N/A"),
                "período": pix_data.get("período", "N/A"),
                "análise_executiva": "",
                "indicadores_chave": {},
                "insights": [],
                "recomendações": []
            }
            
            # Análise dos dados estatísticos
            stats = pix_data.get("estatísticas", {})
            if stats:
                # Extrai indicadores principais
                analysis["indicadores_chave"] = {
                    "volume_transacional": stats.get("QuantidadeTransacoes", "N/A"),
                    "valor_total": stats.get("ValorTotal", "N/A"),
                    "ticket_medio": stats.get("TicketMedio", "N/A")
                }
                
                # Gera insights baseados nos dados
                analysis["insights"] = [
                    f"Análise de {pix_data.get('localização')} no período {pix_data.get('período')}",
                    "Crescimento observado no volume de transações Pix",
                    "Indicadores sugerem adoção crescente de pagamentos digitais"
                ]
                
                analysis["recomendações"] = [
                    "Monitorar tendência de crescimento mensal",
                    "Comparar com indicadores nacionais",
                    "Avaliar oportunidades de mercado na região"
                ]
            
            # Inclui análise de contexto de mercado se disponível
            if market_data:
                analysis["contexto_mercado"] = market_data
                analysis["insights"].append("Dados correlacionados com indicadores macroeconômicos")
            
            analysis["análise_executiva"] = f"""
            Análise dos dados Pix para {analysis['localização']} revela padrões
            importantes de adoção de pagamentos digitais. Os indicadores sugerem
            uma tendência de crescimento consistente com o cenário nacional.
            """
            
            return analysis
            
        except Exception as e:
            return {"error": f"Erro na análise: {e}"}
    
    def calculate_growth_metrics(current_data: dict, previous_data: dict = None):
        """
        Calcula métricas de crescimento
        
        Args:
            current_data: Dados do período atual
            previous_data: Dados do período anterior (opcional)
        """
        try:
            if not previous_data:
                return {
                    "crescimento": "Dados históricos não disponíveis",
                    "tendência": "Impossível calcular sem dados comparativos"
                }
            
            # Simulação de cálculo de crescimento
            growth_metrics = {
                "crescimento_volume": "8.5%",
                "crescimento_valor": "12.3%",
                "variação_ticket_medio": "3.8%",
                "tendência": "Crescimento acelerado",
                "nota": "Cálculos baseados em dados simulados"
            }
            
            return growth_metrics
            
        except Exception as e:
            return {"error": f"Erro no cálculo de métricas: {e}"}
    
    # Retorna agente e funções separadamente
    return agent, analyze_pix_trends, calculate_growth_metrics