from crewai import Agent
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def create_executive_writer():
    """Cria o agente redator executivo"""
    
    llm = ChatOpenAI(
        model="gpt-4",
        temperature=0.3,
        api_key=os.getenv("OPENAI_API_KEY")
    )
    
    agent = Agent(
        role="Redator Executivo Sênior",
        goal="Consolidar dados e análises em relatórios executivos claros e acionáveis",
        backstory="""
        Você é um redator executivo experiente, especializado em comunicação
        corporativa e relatórios de inteligência de mercado. Tem habilidade
        excepcional para transformar dados complexos em narrativas claras
        e insights acionáveis para tomadores de decisão. Seu estilo é direto,
        profissional e focado em resultados.
        """,
        verbose=True,
        allow_delegation=False,
        llm=llm,
        max_iter=3,
        memory=True
    )
    
    def generate_executive_report(pix_data: dict, market_data: dict, analysis_data: dict):
        """
        Gera relatório executivo consolidado
        
        Args:
            pix_data: Dados do sistema Pix
            market_data: Dados de mercado
            analysis_data: Análise financeira
        """
        try:
            current_date = datetime.now().strftime("%d/%m/%Y")
            
            report = {
                "título": "Relatório de Inteligência de Mercado - Sistema Pix",
                "data": current_date,
                "período_análise": pix_data.get("período", "N/A"),
                "localização": pix_data.get("localização", "N/A"),
                "resumo_executivo": "",
                "seções": {},
                "conclusões": [],
                "recomendações_estratégicas": []
            }
            
            # Seção 1: Panorama Pix
            report["seções"]["panorama_pix"] = {
                "título": "Panorama do Sistema Pix",
                "conteúdo": f"""
                **Localização:** {pix_data.get('localização', 'N/A')}
                **Período:** {pix_data.get('período', 'N/A')}
                
                Os dados coletados através da API oficial do Banco Central 
                revelam o comportamento transacional do sistema Pix na região analisada.
                """,
                "indicadores": pix_data.get("estatísticas", {})
            }
            
            # Seção 2: Contexto de Mercado
            report["seções"]["contexto_mercado"] = {
                "título": "Contexto de Mercado",
                "conteúdo": """
                O cenário macroeconômico brasileiro apresenta indicadores
                que influenciam diretamente a adoção de pagamentos digitais.
                """,
                "indicadores": market_data if market_data else {}
            }
            
            # Seção 3: Análise Estratégica
            if analysis_data and "insights" in analysis_data:
                report["seções"]["análise_estratégica"] = {
                    "título": "Análise Estratégica",
                    "conteúdo": analysis_data.get("análise_executiva", ""),
                    "insights": analysis_data.get("insights", []),
                    "indicadores_chave": analysis_data.get("indicadores_chave", {})
                }
            
            # Resumo Executivo
            report["resumo_executivo"] = f"""
            Este relatório apresenta uma análise abrangente dos dados do sistema Pix
            para {report['localização']} no período de {report['período_análise']}.
            
            A análise combina dados oficiais do Banco Central com indicadores de mercado,
            fornecendo insights estratégicos para tomada de decisão.
            """
            
            # Conclusões
            report["conclusões"] = [
                "Sistema Pix mantém trajetória de crescimento consistente",
                "Adoção regional alinhada com tendências nacionais",
                "Oportunidades identificadas para expansão de serviços digitais"
            ]
            
            # Recomendações Estratégicas
            report["recomendações_estratégicas"] = [
                "Monitorar evolução mensal dos indicadores Pix",
                "Desenvolver produtos focados em pagamentos instantâneos",
                "Acompanhar movimentação da concorrência no segmento",
                "Investir em soluções de pagamento para pequenos negócios"
            ]
            
            return report
            
        except Exception as e:
            return {"error": f"Erro na geração do relatório: {e}"}
    
    def format_report_html(report_data: dict):
        """
        Formata relatório em HTML
        
        Args:
            report_data: Dados do relatório
        """
        try:
            html = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>{report_data.get('título', 'Relatório')}</title>
                <style>
                    body {{ font-family: Arial, sans-serif; margin: 40px; }}
                    h1 {{ color: #2c3e50; }}
                    h2 {{ color: #34495e; }}
                    .header {{ border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
                    .section {{ margin: 20px 0; }}
                    .insight {{ background: #ecf0f1; padding: 10px; margin: 5px 0; }}
                </style>
            </head>
            <body>
                <div class="header">
                    <h1>{report_data.get('título', 'Relatório')}</h1>
                    <p><strong>Data:</strong> {report_data.get('data', 'N/A')}</p>
                    <p><strong>Período:</strong> {report_data.get('período_análise', 'N/A')}</p>
                </div>
                
                <div class="section">
                    <h2>Resumo Executivo</h2>
                    <p>{report_data.get('resumo_executivo', '')}</p>
                </div>
            </body>
            </html>
            """
            
            return html
            
        except Exception as e:
            return f"<html><body><h1>Erro na formatação: {e}</h1></body></html>"
    
    # Retorna agente e funções separadamente
    return agent, generate_executive_report, format_report_html