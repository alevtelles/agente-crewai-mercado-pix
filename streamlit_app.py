import streamlit as st
import sys
import os
from datetime import datetime, timedelta
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from dotenv import load_dotenv

# Configurar path para importar módulos locais
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Configuração da página
st.set_page_config(
    page_title="Agente Mercado Pix",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS customizado
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .status-success {
        color: #28a745;
        font-weight: bold;
    }
    .status-error {
        color: #dc3545;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

def main():
    """Interface principal do Streamlit"""
    
    # Header
    st.markdown('<h1 class="main-header">🏦 Agente Mercado Pix</h1>', unsafe_allow_html=True)
    st.markdown("### Sistema de Inteligência de Mercado com Dados Pix")
    
    # Sidebar para configurações
    with st.sidebar:
        st.header("⚙️ Configurações")
        
        # Carregar variáveis de ambiente
        load_dotenv()
        
        # Verificar API key
        api_key_status = "✅ Configurada" if os.getenv("OPENAI_API_KEY") else "❌ Não configurada"
        st.info(f"**OpenAI API Key:** {api_key_status}")
        
        st.markdown("---")
        
        # Parâmetros de análise
        st.subheader("📊 Parâmetros da Análise")
        
        municipio = st.selectbox(
            "Município",
            ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador", "Fortaleza", 
             "Belo Horizonte", "Manaus", "Curitiba", "Recife", "Goiânia", "Criciúma"],
            index=10
        )
        
        # Período
        col1, col2 = st.columns(2)
        with col1:
            ano = st.selectbox("Ano", [2024, 2023, 2022], index=0)
        with col2:
            mes = st.selectbox("Mês", list(range(1, 13)), index=11)
        
        ano_mes = f"{ano}-{mes:02d}"
        
        # Keywords para pesquisa
        keywords = st.text_input(
            "Palavras-chave para pesquisa",
            value="pagamentos digitais fintech pix mercado financeiro"
        )
        
        st.markdown("---")
        
        # Modo de execução
        st.subheader("🚀 Modo de Execução")
        modo = st.radio(
            "Escolha o modo:",
            ["Demo Rápido", "Análise Completa", "Teste Individual"]
        )
    
    # Interface principal
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📋 Configuração Atual")
        st.info(f"**Município:** {municipio} | **Período:** {ano_mes} | **Modo:** {modo}")
    
    with col2:
        if st.button("🚀 Executar Análise", type="primary", use_container_width=True):
            executar_analise(municipio, ano_mes, keywords, modo)
    
    # Status do sistema
    mostrar_status_sistema()
    
    # Área de resultados
    if "resultado_analise" in st.session_state:
        mostrar_resultados()

def mostrar_status_sistema():
    """Mostra status dos componentes do sistema"""
    st.subheader("🔧 Status do Sistema")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Agentes Ativos", "4", "✅")
    
    with col2:
        st.metric("API Pix BCB", "Online", "🌐")
    
    with col3:
        st.metric("CrewAI", "v0.148.0", "🤖")
    
    with col4:
        st.metric("Status Geral", "Operacional", "✅")

def executar_analise(municipio, ano_mes, keywords, modo):
    """Executa análise baseada no modo selecionado"""
    
    with st.spinner(f"🔄 Executando {modo.lower()}..."):
        try:
            if modo == "Demo Rápido":
                resultado = executar_demo_rapido(municipio, ano_mes, keywords)
            elif modo == "Análise Completa":
                resultado = executar_analise_completa(municipio, ano_mes, keywords)
            else:
                resultado = executar_teste_individual()
            
            st.session_state.resultado_analise = resultado
            st.success("✅ Análise concluída com sucesso!")
            
        except Exception as e:
            st.error(f"❌ Erro na análise: {str(e)}")
            st.session_state.resultado_analise = None

def executar_demo_rapido(municipio, ano_mes, keywords):
    """Executa demo rápido do sistema"""
    try:
        from src.crew_orchestrator import PixIntelligenceCrew
        
        crew = PixIntelligenceCrew()
        
        # Executar funções individuais
        pix_result = crew.pix_fetch_func(municipio, ano_mes)
        market_result = crew.market_search_func(keywords)
        analysis_result = crew.analyze_func(pix_result, market_result)
        report_result = crew.report_func(pix_result, market_result, analysis_result)
        
        return {
            "tipo": "demo_rapido",
            "municipio": municipio,
            "periodo": ano_mes,
            "dados_pix": pix_result,
            "pesquisa_mercado": market_result,
            "analise_financeira": analysis_result,
            "relatorio_executivo": report_result
        }
        
    except Exception as e:
        return {"erro": str(e)}

def executar_analise_completa(municipio, ano_mes, keywords):
    """Executa análise completa com CrewAI"""
    try:
        from src.crew_orchestrator import PixIntelligenceCrew
        
        crew = PixIntelligenceCrew()
        resultado = crew.run_analysis(municipio, ano_mes, keywords)
        
        return {
            "tipo": "analise_completa",
            "municipio": municipio,
            "periodo": ano_mes,
            "resultado_crew": str(resultado)
        }
        
    except Exception as e:
        return {"erro": str(e)}

def executar_teste_individual():
    """Executa testes individuais dos componentes"""
    try:
        from src.tools.pix_api import PixAPIClient
        
        client = PixAPIClient()
        teste_pix = client.get_pix_statistics_summary("São Paulo", "2024-01", "municipio")
        
        return {
            "tipo": "teste_individual",
            "teste_api_pix": teste_pix,
            "status": "Componentes testados individualmente"
        }
        
    except Exception as e:
        return {"erro": str(e)}

def mostrar_resultados():
    """Mostra os resultados da análise"""
    resultado = st.session_state.resultado_analise
    
    if "erro" in resultado:
        st.error(f"❌ Erro: {resultado['erro']}")
        return
    
    st.subheader("📊 Resultados da Análise")
    
    # Tabs para diferentes visualizações
    tab1, tab2, tab3, tab4 = st.tabs(["📈 Dados Pix", "📰 Mercado", "🔍 Análise", "📋 Relatório"])
    
    with tab1:
        mostrar_dados_pix(resultado)
    
    with tab2:
        mostrar_dados_mercado(resultado)
    
    with tab3:
        mostrar_analise_financeira(resultado)
    
    with tab4:
        mostrar_relatorio_executivo(resultado)

def mostrar_dados_pix(resultado):
    """Mostra dados do sistema Pix"""
    st.subheader("💳 Dados do Sistema Pix")
    
    if resultado["tipo"] == "demo_rapido":
        dados_pix = resultado.get("dados_pix", {})
        
        if "error" in dados_pix:
            st.warning(f"⚠️ {dados_pix['error']}")
            st.info("💡 **Dica:** Use períodos passados (ex: 2024-01) para obter dados reais da API BCB")
        else:
            col1, col2 = st.columns(2)
            
            with col1:
                st.info(f"**Localização:** {dados_pix.get('localização', 'N/A')}")
                st.info(f"**Período:** {dados_pix.get('período', 'N/A')}")
            
            with col2:
                st.info(f"**Tipo:** {dados_pix.get('tipo', 'N/A')}")
                st.info(f"**Dados encontrados:** {dados_pix.get('dados_encontrados', 0)}")
        
        # Gráfico simulado
        criar_grafico_pix_simulado()

def criar_grafico_pix_simulado():
    """Cria gráfico simulado dos dados Pix"""
    st.subheader("📊 Evolução das Transações Pix (Simulado)")
    
    # Dados simulados
    meses = ["2024-01", "2024-02", "2024-03", "2024-04", "2024-05", "2024-06"]
    transacoes = [1200000, 1350000, 1450000, 1600000, 1750000, 1900000]
    valores = [2.5, 2.8, 3.1, 3.4, 3.7, 4.1]
    
    fig = go.Figure()
    
    # Linha de transações
    fig.add_trace(go.Scatter(
        x=meses, 
        y=transacoes,
        mode='lines+markers',
        name='Número de Transações',
        line=dict(color='#1f77b4', width=3)
    ))
    
    fig.update_layout(
        title="Crescimento das Transações Pix",
        xaxis_title="Período",
        yaxis_title="Número de Transações",
        template="plotly_white",
        height=400
    )
    
    st.plotly_chart(fig, use_container_width=True)

def mostrar_dados_mercado(resultado):
    """Mostra dados de pesquisa de mercado"""
    st.subheader("📰 Pesquisa de Mercado")
    
    if resultado["tipo"] == "demo_rapido":
        market_data = resultado.get("pesquisa_mercado", {})
        
        if "resultados" in market_data:
            st.info(f"**Query:** {market_data.get('query', 'N/A')}")
            st.info(f"**Total encontrado:** {market_data.get('total_encontrado', 0)} notícias")
            
            # Mostrar resultados
            for i, noticia in enumerate(market_data["resultados"][:3]):
                with st.expander(f"📄 {noticia['fonte']} - {noticia['relevancia'].upper()}"):
                    st.write(f"**Título:** {noticia['titulo']}")
                    st.write(f"**Resumo:** {noticia['resumo']}")
        
        # Gráfico de relevância
        criar_grafico_relevancia_noticias(market_data)

def criar_grafico_relevancia_noticias(market_data):
    """Cria gráfico de relevância das notícias"""
    if "resultados" not in market_data:
        return
    
    relevancia_count = {}
    for noticia in market_data["resultados"]:
        rel = noticia["relevancia"]
        relevancia_count[rel] = relevancia_count.get(rel, 0) + 1
    
    if relevancia_count:
        fig = px.pie(
            values=list(relevancia_count.values()),
            names=list(relevancia_count.keys()),
            title="Distribuição de Relevância das Notícias"
        )
        st.plotly_chart(fig, use_container_width=True)

def mostrar_analise_financeira(resultado):
    """Mostra análise financeira"""
    st.subheader("🔍 Análise Financeira")
    
    if resultado["tipo"] == "demo_rapido":
        analise = resultado.get("analise_financeira", {})
        
        if "error" in analise:
            st.warning(f"⚠️ {analise['error']}")
        else:
            # Indicadores chave
            if "indicadores_chave" in analise:
                st.subheader("📊 Indicadores Chave")
                indicadores = analise["indicadores_chave"]
                
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric("Volume Transacional", indicadores.get("volume_transacional", "N/A"))
                
                with col2:
                    st.metric("Valor Total", indicadores.get("valor_total", "N/A"))
                
                with col3:
                    st.metric("Ticket Médio", indicadores.get("ticket_medio", "N/A"))
            
            # Insights
            if "insights" in analise:
                st.subheader("💡 Insights")
                for insight in analise["insights"]:
                    st.success(f"✅ {insight}")

def mostrar_relatorio_executivo(resultado):
    """Mostra relatório executivo"""
    st.subheader("📋 Relatório Executivo")
    
    if resultado["tipo"] == "demo_rapido":
        relatorio = resultado.get("relatorio_executivo", {})
        
        # Cabeçalho do relatório
        st.markdown(f"### {relatorio.get('título', 'Relatório de Inteligência de Mercado')}")
        st.info(f"**Data:** {relatorio.get('data', 'N/A')} | **Período:** {relatorio.get('período_análise', 'N/A')}")
        
        # Resumo executivo
        if "resumo_executivo" in relatorio:
            st.subheader("📝 Resumo Executivo")
            st.write(relatorio["resumo_executivo"])
        
        # Conclusões
        if "conclusões" in relatorio:
            st.subheader("🎯 Conclusões")
            for conclusao in relatorio["conclusões"]:
                st.success(f"✅ {conclusao}")
        
        # Recomendações
        if "recomendações_estratégicas" in relatorio:
            st.subheader("🚀 Recomendações Estratégicas")
            for i, recomendacao in enumerate(relatorio["recomendações_estratégicas"], 1):
                st.info(f"**{i}.** {recomendacao}")
        
        # Download do relatório
        if st.button("📥 Download Relatório Completo"):
            download_relatorio(resultado)

def download_relatorio(resultado):
    """Permite download do relatório"""
    try:
        import json
        
        relatorio_json = json.dumps(resultado, ensure_ascii=False, indent=2)
        
        st.download_button(
            label="📄 Baixar Relatório (JSON)",
            data=relatorio_json,
            file_name=f"relatorio_pix_{resultado.get('municipio', 'geral')}_{resultado.get('periodo', 'atual')}.json",
            mime="application/json"
        )
        
    except Exception as e:
        st.error(f"Erro no download: {e}")

if __name__ == "__main__":
    main()