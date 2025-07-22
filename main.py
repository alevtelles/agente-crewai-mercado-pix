#!/usr/bin/env python3
"""
Agente de Mercado Pix - Sistema de Inteligência de Mercado
Integra dados do sistema Pix com análise de mercado financeiro
"""

import os
import sys
from dotenv import load_dotenv

# Adicionar o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.crew_orchestrator import PixIntelligenceCrew

def main():
    """Função principal"""
    print("🏦 Agente de Mercado Pix - Sistema de Inteligência Financeira")
    print("=" * 60)
    
    # Carregar variáveis de ambiente
    load_dotenv()
    
    # Verificar se a API key do OpenAI está configurada
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ ERRO: OPENAI_API_KEY não configurada!")
        print("📝 Configure no arquivo .env baseado em .env.example")
        return
    
    # Criar orquestrador
    crew_orchestrator = PixIntelligenceCrew()
    
    # Mostrar status dos agentes
    status = crew_orchestrator.get_agents_status()
    print(f"👥 {status['total_agentes']} agentes ativos:")
    for name, desc in status['agentes'].items():
        print(f"   • {name}: {desc}")
    print()
    
    # Parâmetros da análise
    municipio = "Criciúma"
    ano_mes = "2025-06"
    keywords = "pagamentos digitais fintech pix mercado financeiro"
    
    print(f"📍 Município: {municipio}")
    print(f"📅 Período: {ano_mes}")
    print(f"🔍 Pesquisa: {keywords}")
    print("=" * 60)
    
    try:
        # Executar análise completa
        result = crew_orchestrator.run_analysis(
            municipio=municipio,
            ano_mes=ano_mes,
            keywords=keywords
        )
        
        print("\n" + "=" * 60)
        print("📊 RESULTADO DA ANÁLISE")
        print("=" * 60)
        
        if isinstance(result, dict) and "error" in result:
            print(f"❌ Erro: {result['error']}")
        else:
            # Extrair texto do resultado CrewOutput
            result_text = str(result)
            print(f"Resultado (tipo: {type(result)}):")
            print(result_text[:1000] + "..." if len(result_text) > 1000 else result_text)
            
            # Salvar resultado em arquivo
            output_file = f"relatorio_{municipio}_{ano_mes}.txt"
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"Relatório de Inteligência de Mercado Pix\n")
                f.write(f"Município: {municipio}\n")
                f.write(f"Período: {ano_mes}\n")
                f.write(f"Data de geração: {os.popen('date').read().strip()}\n\n")
                f.write(result_text)
            
            print(f"\n💾 Relatório salvo em: {output_file}")
        
    except KeyboardInterrupt:
        print("\n❌ Análise interrompida pelo usuário")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

def test_individual_agents():
    """Testa agentes individualmente"""
    print("🧪 MODO TESTE - Agentes Individuais")
    print("=" * 60)
    
    load_dotenv()
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ ERRO: OPENAI_API_KEY não configurada!")
        return
    
    crew = PixIntelligenceCrew()
    
    # Teste 1: Agente Pix
    print("\n1️⃣ Testando Agente Pix...")
    try:
        result_pix = crew.run_specific_task("pix", municipio="Criciúma", ano_mes="2025-06")
        print("✅ Agente Pix funcionando")
        print(f"Resultado: {str(result_pix)[:200]}...")
    except Exception as e:
        print(f"❌ Erro no Agente Pix: {e}")
    
    # Teste 2: Agente Market Research
    print("\n2️⃣ Testando Agente de Pesquisa...")
    try:
        result_market = crew.run_specific_task("market", keywords="fintech pagamentos")
        print("✅ Agente de Pesquisa funcionando")
        print(f"Resultado: {str(result_market)[:200]}...")
    except Exception as e:
        print(f"❌ Erro no Agente de Pesquisa: {e}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Agente de Mercado Pix")
    parser.add_argument("--test", action="store_true", help="Executar testes individuais")
    parser.add_argument("--municipio", default="Criciúma", help="Município para análise")
    parser.add_argument("--periodo", default="2025-06", help="Período (YYYY-MM)")
    
    args = parser.parse_args()
    
    if args.test:
        test_individual_agents()
    else:
        main()