from crewai import Crew
from .agents.pix_agent import create_pix_agent
from .agents.market_researcher import create_market_researcher
from .agents.financial_analyst import create_financial_analyst
from .agents.executive_writer import create_executive_writer
from .tasks.pix_tasks import (
    create_pix_data_task,
    create_market_research_task,
    create_financial_analysis_task,
    create_executive_report_task
)

class PixIntelligenceCrew:
    """Orquestrador principal dos agentes CrewAI"""
    
    def __init__(self):
        """Inicializa todos os agentes e tasks"""
        # Criar agentes
        self.pix_agent, self.pix_fetch_func = create_pix_agent()
        self.market_researcher, self.market_search_func, self.market_indicators_func = create_market_researcher()
        self.financial_analyst, self.analyze_func, self.metrics_func = create_financial_analyst()
        self.executive_writer, self.report_func, self.html_func = create_executive_writer()
        
        # Lista de agentes para o crew
        self.agents = [
            self.pix_agent,
            self.market_researcher,
            self.financial_analyst,
            self.executive_writer
        ]
    
    def create_tasks(self, municipio: str = "Criciúma", ano_mes: str = "2025-06", 
                    keywords: str = "pagamentos digitais fintech pix"):
        """
        Cria todas as tasks necessárias para o relatório
        
        Args:
            municipio: Município para análise Pix
            ano_mes: Período no formato YYYY-MM
            keywords: Palavras-chave para pesquisa de mercado
        """
        self.tasks = [
            create_pix_data_task(self.pix_agent, municipio, ano_mes),
            create_market_research_task(self.market_researcher, keywords),
            create_financial_analysis_task(self.financial_analyst),
            create_executive_report_task(self.executive_writer)
        ]
        
        return self.tasks
    
    def run_analysis(self, municipio: str = "Criciúma", ano_mes: str = "2025-06",
                    keywords: str = "pagamentos digitais fintech pix"):
        """
        Executa análise completa com todos os agentes
        
        Args:
            municipio: Município para análise
            ano_mes: Período para análise
            keywords: Palavras-chave para pesquisa
            
        Returns:
            Resultado final da análise
        """
        try:
            # Criar tasks
            tasks = self.create_tasks(municipio, ano_mes, keywords)
            
            # Criar crew
            crew = Crew(
                agents=self.agents,
                tasks=tasks,
                verbose=True,
                memory=True,
                planning=True,
                max_rpm=10  # Limite de requisições por minuto
            )
            
            # Executar análise
            print(f"🚀 Iniciando análise para {municipio} - {ano_mes}")
            print(f"📊 Agentes ativos: {len(self.agents)}")
            print(f"📋 Tasks configuradas: {len(tasks)}")
            
            result = crew.kickoff()
            
            print("✅ Análise concluída com sucesso!")
            print(f"Tipo do resultado: {type(result)}")
            return result
            
        except Exception as e:
            print(f"❌ Erro na execução da análise: {e}")
            return {"error": str(e)}
    
    def run_specific_task(self, task_type: str, **kwargs):
        """
        Executa uma task específica
        
        Args:
            task_type: Tipo de task ('pix', 'market', 'analysis', 'report')
            **kwargs: Parâmetros específicos da task
        """
        try:
            if task_type == "pix":
                task = create_pix_data_task(
                    self.pix_agent, 
                    kwargs.get("municipio", "Criciúma"),
                    kwargs.get("ano_mes", "2025-06")
                )
                agent = self.pix_agent
                
            elif task_type == "market":
                task = create_market_research_task(
                    self.market_researcher,
                    kwargs.get("keywords", "pagamentos digitais")
                )
                agent = self.market_researcher
                
            elif task_type == "analysis":
                task = create_financial_analysis_task(self.financial_analyst)
                agent = self.financial_analyst
                
            elif task_type == "report":
                task = create_executive_report_task(self.executive_writer)
                agent = self.executive_writer
                
            else:
                return {"error": f"Tipo de task inválido: {task_type}"}
            
            # Executar task específica
            crew = Crew(
                agents=[agent],
                tasks=[task],
                verbose=True
            )
            
            result = crew.kickoff()
            return result
            
        except Exception as e:
            return {"error": f"Erro na execução da task {task_type}: {e}"}
    
    def get_agents_status(self):
        """Retorna status dos agentes"""
        return {
            "total_agentes": len(self.agents),
            "agentes": {
                "pix_agent": "Ativo - Especialista em dados Pix BCB",
                "market_researcher": "Ativo - Pesquisador de mercado financeiro", 
                "financial_analyst": "Ativo - Analista de tendências",
                "executive_writer": "Ativo - Redator de relatórios executivos"
            },
            "status": "Pronto para execução"
        }