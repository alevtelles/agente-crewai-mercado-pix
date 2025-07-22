#!/bin/bash

echo "🚀 Iniciando Agent Mercado Pix no Ambiente Virtual"
echo "================================================="

# Verificar se o ambiente virtual existe
if [ ! -d "venv" ]; then
    echo "❌ Ambiente virtual não encontrado!"
    echo "📝 Criando ambiente virtual..."
    python3 -m venv venv
    echo "✅ Ambiente virtual criado"
fi

# Ativar ambiente virtual
echo "🔄 Ativando ambiente virtual..."
source venv/bin/activate

# Verificar se as dependências estão instaladas
echo "🔍 Verificando dependências..."
if ! python -c "import streamlit" 2>/dev/null; then
    echo "📦 Instalando dependências..."
    pip install -r requirements-minimal.txt
else
    echo "✅ Dependências já instaladas"
fi

# Verificar configuração
if [ ! -f ".env" ]; then
    echo "⚠️  Arquivo .env não encontrado!"
    echo "📝 Copiando exemplo de configuração..."
    cp .env.example .env
    echo "✏️  Configure sua OPENAI_API_KEY no arquivo .env"
fi

echo ""
echo "🎯 Escolha uma opção:"
echo "1) Interface Streamlit (Recomendado)"
echo "2) Demo Rápido CLI"
echo "3) Análise Completa CLI"
echo "4) Sair"

read -p "Digite sua escolha (1-4): " choice

case $choice in
    1)
        echo "🌐 Iniciando Interface Streamlit..."
        echo "📱 Acesse: http://localhost:8501"
        python app.py --web
        ;;
    2)
        echo "⚡ Executando Demo Rápido..."
        python app.py --demo
        ;;
    3)
        echo "🔍 Executando Análise Completa..."
        python app.py --analysis
        ;;
    4)
        echo "👋 Saindo..."
        ;;
    *)
        echo "❌ Opção inválida!"
        ;;
esac

echo ""
echo "📝 Para desativar o ambiente virtual, execute: deactivate"