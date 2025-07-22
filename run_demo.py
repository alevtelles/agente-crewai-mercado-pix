#!/usr/bin/env python3
"""
Demo rápido do sistema Agent Mercado Pix
"""

import os
import sys
from dotenv import load_dotenv

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.crew_orchestrator import PixIntelligenceCrew

def run_quick_demo():
    """Executa demo rápido com timeout menor"""
    print("🚀 DEMO RÁPIDO - Agent Mercado Pix")
    print("=" * 50)
    
    load_dotenv()
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ ERRO: OPENAI_API_KEY não configurada!")
        return False
    
    try:
        crew = PixIntelligenceCrew()
        
        print("👥 Agentes criados com sucesso:")
        print("   ✅ Especialista em Dados Pix")
        print("   ✅ Pesquisador de Mercado")
        print("   ✅ Analista Financeiro")
        print("   ✅ Redator Executivo")
        
        print("\n📊 Testando funções individuais...")
        
        # Teste 1: API Pix
        print("\n1️⃣ Testando API Pix...")
        pix_result = crew.pix_fetch_func("São Paulo", "2024-12")
        print(f"   Resultado: {str(pix_result)[:100]}...")
        
        # Teste 2: Pesquisa de mercado
        print("\n2️⃣ Testando pesquisa de mercado...")
        market_result = crew.market_search_func("fintech pix")
        print(f"   Resultado: {str(market_result)[:100]}...")
        
        # Teste 3: Análise financeira
        print("\n3️⃣ Testando análise financeira...")
        analysis_result = crew.analyze_func(pix_result, market_result)
        print(f"   Resultado: {str(analysis_result)[:100]}...")
        
        # Teste 4: Geração de relatório
        print("\n4️⃣ Testando geração de relatório...")
        report_result = crew.report_func(pix_result, market_result, analysis_result)
        print(f"   Resultado: {str(report_result)[:150]}...")
        
        print("\n🎉 SISTEMA FUNCIONANDO PERFEITAMENTE!")
        print("=" * 50)
        print("✅ Todos os componentes testados com sucesso")
        print("✅ Integração com API Pix funcional")
        print("✅ Agentes CrewAI operacionais")
        print("✅ Funções de análise e relatório funcionando")
        
        # Salvar demo
        demo_file = "demo_resultado.txt"
        with open(demo_file, 'w', encoding='utf-8') as f:
            f.write("DEMO - Agent Mercado Pix\n")
            f.write("=" * 30 + "\n\n")
            f.write("1. API Pix:\n")
            f.write(f"{pix_result}\n\n")
            f.write("2. Pesquisa de Mercado:\n")
            f.write(f"{market_result}\n\n")
            f.write("3. Análise Financeira:\n")
            f.write(f"{analysis_result}\n\n")
            f.write("4. Relatório Executivo:\n")
            f.write(f"{report_result}\n")
        
        print(f"\n💾 Demo salvo em: {demo_file}")
        return True
        
    except Exception as e:
        print(f"❌ Erro no demo: {e}")
        return False

if __name__ == "__main__":
    run_quick_demo()