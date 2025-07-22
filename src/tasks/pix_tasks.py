from crewai import Task

def create_pix_data_task(agent, municipio: str = "Criciúma", ano_mes: str = "2025-06"):
    """Cria task para coleta de dados Pix"""
    
    task = Task(
        description=f"""
        Colete dados detalhados das transações Pix para o município de {municipio} 
        no período de {ano_mes}.
        
        Seu objetivo é:
        1. Acessar a API oficial do Banco Central
        2. Obter estatísticas completas de transações Pix
        3. Validar a qualidade dos dados coletados
        4. Preparar os dados para análise posterior
        
        Retorne um resumo estruturado contendo:
        - Volume total de transações
        - Valor movimentado
        - Comparações quando possível
        - Qualidade dos dados coletados
        """,
        agent=agent,
        expected_output="Relatório estruturado com estatísticas Pix validadas e preparadas para análise"
    )
    
    return task

def create_market_research_task(agent, keywords: str = "pagamentos digitais fintech"):
    """Cria task para pesquisa de mercado"""
    
    task = Task(
        description=f"""
        Realize uma pesquisa abrangente sobre o mercado financeiro brasileiro,
        focando em: {keywords}.
        
        Seu objetivo é:
        1. Coletar informações atuais sobre fintechs e pagamentos digitais
        2. Identificar tendências do setor financeiro
        3. Buscar indicadores macroeconômicos relevantes
        4. Mapear principais players do mercado
        
        Retorne um relatório contendo:
        - Principais notícias e desenvolvimentos recentes
        - Indicadores econômicos relevantes
        - Análise de tendências do setor
        - Contexto competitivo atual
        """,
        agent=agent,
        expected_output="Relatório de pesquisa de mercado com informações atualizadas e contextualizadas"
    )
    
    return task

def create_financial_analysis_task(agent):
    """Cria task para análise financeira"""
    
    task = Task(
        description="""
        Analise os dados coletados do sistema Pix e informações de mercado
        para gerar insights estratégicos profundos.
        
        Seu objetivo é:
        1. Cruzar dados Pix com contexto macroeconômico
        2. Identificar padrões e tendências relevantes
        3. Calcular métricas de crescimento e performance
        4. Gerar insights acionáveis para tomada de decisão
        
        Considere:
        - Sazonalidade dos dados
        - Comparações regionais quando possível
        - Impacto de fatores econômicos
        - Oportunidades e riscos identificados
        
        Retorne:
        - Análise detalhada dos dados
        - Indicadores-chave de performance
        - Insights estratégicos
        - Recomendações baseadas em dados
        """,
        agent=agent,
        expected_output="Análise financeira completa com insights estratégicos e recomendações acionáveis"
    )
    
    return task

def create_executive_report_task(agent):
    """Cria task para redação do relatório executivo"""
    
    task = Task(
        description="""
        Consolide todas as informações coletadas e análises realizadas
        em um relatório executivo profissional e acionável.
        
        Seu objetivo é:
        1. Integrar dados Pix, pesquisa de mercado e análise financeira
        2. Criar narrativa coesa e clara para executivos
        3. Destacar insights mais relevantes
        4. Apresentar recomendações estratégicas priorizadas
        
        O relatório deve conter:
        - Resumo executivo (máximo 2 parágrafos)
        - Seção de dados Pix com estatísticas principais
        - Contexto de mercado e tendências
        - Análise estratégica com insights
        - Conclusões e recomendações priorizadas
        
        Formato:
        - Linguagem executiva clara e objetiva
        - Dados apresentados de forma visual quando relevante
        - Foco em acionabilidade das recomendações
        - Estrutura lógica e fluida
        """,
        agent=agent,
        expected_output="Relatório executivo completo, profissional e acionável pronto para apresentação"
    )
    
    return task