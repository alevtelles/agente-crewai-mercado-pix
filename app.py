#!/usr/bin/env python3
"""
Aplicação principal do Agent Mercado Pix
Ponto de entrada único para todas as funcionalidades
"""

import argparse
import sys
import os

def run_streamlit():
    """Executa interface Streamlit"""
    import subprocess
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "streamlit_app.py"])
    except KeyboardInterrupt:
        print("\n👋 Aplicação finalizada")

def run_demo():
    """Executa demo rápido"""
    from run_demo import run_quick_demo
    run_quick_demo()

def run_analysis(municipio="Criciúma", periodo="2025-06"):
    """Executa análise completa"""
    from main import main as run_main
    # Simular argumentos
    sys.argv = ["main.py", "--municipio", municipio, "--periodo", periodo]
    run_main()

def main():
    parser = argparse.ArgumentParser(
        description="Agent Mercado Pix - Sistema de Inteligência Financeira",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python app.py --web                    # Interface Streamlit
  python app.py --demo                   # Demo rápido
  python app.py --analysis               # Análise completa
  python app.py --analysis --municipio "São Paulo" --periodo "2024-01"
        """
    )
    
    parser.add_argument("--web", action="store_true", 
                       help="Executar interface web Streamlit")
    parser.add_argument("--demo", action="store_true", 
                       help="Executar demo rápido")
    parser.add_argument("--analysis", action="store_true", 
                       help="Executar análise completa")
    parser.add_argument("--municipio", default="Criciúma", 
                       help="Município para análise")
    parser.add_argument("--periodo", default="2024-01", 
                       help="Período (YYYY-MM)")
    
    args = parser.parse_args()
    
    if not any([args.web, args.demo, args.analysis]):
        # Default: interface web
        print("🚀 Iniciando interface web Streamlit...")
        print("💡 Use --help para ver outras opções")
        run_streamlit()
    elif args.web:
        run_streamlit()
    elif args.demo:
        run_demo()
    elif args.analysis:
        run_analysis(args.municipio, args.periodo)

if __name__ == "__main__":
    main()