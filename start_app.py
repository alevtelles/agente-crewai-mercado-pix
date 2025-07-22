#!/usr/bin/env python3
"""
Script para iniciar a aplicação Streamlit no ambiente virtual
"""

import subprocess
import sys
import os
from dotenv import load_dotenv

def check_venv():
    """Verifica se está rodando no ambiente virtual"""
    if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
        print("✅ Executando no ambiente virtual")
        return True
    else:
        print("⚠️  Não está no ambiente virtual!")
        print("💡 Para melhor isolamento, use: ./start_venv.sh")
        return False

def main():
    print("🚀 Iniciando Agent Mercado Pix...")
    print("=" * 50)
    
    # Verificar ambiente virtual
    check_venv()
    print()
    
    # Verificar configuração
    load_dotenv()
    
    if not os.getenv("OPENAI_API_KEY"):
        print("⚠️  ATENÇÃO: OPENAI_API_KEY não configurada!")
        print("📝 Configure no arquivo .env para usar funcionalidades completas")
        print()
    
    # Verificar dependências
    try:
        import streamlit
        print("✅ Streamlit instalado")
    except ImportError:
        print("❌ Streamlit não encontrado.")
        print("💡 Se usando ambiente virtual, execute: source venv/bin/activate && pip install streamlit")
        return
    
    try:
        import plotly
        print("✅ Plotly instalado")
    except ImportError:
        print("❌ Plotly não encontrado.")
        print("💡 Se usando ambiente virtual, execute: source venv/bin/activate && pip install plotly")
        return
    
    print("✅ Todas as dependências estão OK")
    print()
    print("🌐 Iniciando servidor Streamlit...")
    print("📱 Acesse: http://localhost:8501")
    print()
    print("Para parar o servidor, pressione Ctrl+C")
    print("=" * 50)
    
    # Iniciar Streamlit
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "streamlit_app.py",
            "--server.headless=true"
        ])
    except KeyboardInterrupt:
        print("\n👋 Aplicação finalizada pelo usuário")
    except Exception as e:
        print(f"\n❌ Erro ao iniciar aplicação: {e}")

if __name__ == "__main__":
    main()