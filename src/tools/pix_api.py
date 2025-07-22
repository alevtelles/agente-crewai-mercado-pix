import requests
from typing import Dict, List, Optional
from datetime import datetime
import os
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()

class PixAPIClient:
    def __init__(self):
        self.base_url = os.getenv("BCB_API_BASE_URL", 
                                 "https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata")
    
    def fetch_transactions_by_municipality(self, municipio: str, ano_mes: str) -> List[Dict]:
        """
        Busca transações Pix por município em um determinado mês
        
        Args:
            municipio: Nome do município (ex: 'SAO PAULO')
            ano_mes: Formato 'YYYY-MM' (ex: '2024-01')
        
        Returns:
            Lista de dados de transações
        """
        try:
            # Converter formato de data de YYYY-MM para YYYYMM
            database = ano_mes.replace('-', '')
            
            # Formato correto descoberto: Function com parâmetro DataBase
            url = f"{self.base_url}/TransacoesPixPorMunicipio(DataBase='{database}')"
            
            # Usar apenas $format e $top, sem filtro problemático
            params = {
                "$format": "json",
                "$top": "1000"  # Buscar mais registros para filtrar no código
            }
            
            print(f"🔍 Consultando API Pix: {municipio} em {ano_mes}")
            print(f"📡 URL: {url}")
            
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            all_results = data.get("value", [])
            
            # Filtrar por município no código Python (mais confiável)
            municipio_upper = municipio.upper().strip()
            filtered_results = [
                item for item in all_results 
                if item.get("Municipio", "").upper().strip() == municipio_upper
            ]
            
            print(f"📊 Total de registros na API: {len(all_results)}")
            print(f"✅ Registros filtrados para {municipio}: {len(filtered_results)}")
            
            return filtered_results
            
        except requests.exceptions.Timeout:
            print(f"⏰ Timeout ao consultar dados Pix para {municipio}")
            return []
        except requests.exceptions.RequestException as e:
            print(f"❌ Erro ao buscar dados Pix: {e}")
            return []
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            return []
    
    def fetch_transactions_by_state(self, estado: str, ano_mes: str) -> List[Dict]:
        """
        Busca transações Pix por estado em um determinado mês
        
        Args:
            estado: Sigla do estado (ex: 'SC')
            ano_mes: Formato 'YYYY-MM'
        
        Returns:
            Lista de dados de transações
        """
        try:
            url = f"{self.base_url}/TransacoesPixPorEstado"
            params = {
                "$filter": f"MesAno eq '{ano_mes}' and Estado eq '{estado}'",
                "$format": "json"
            }
            
            response = requests.get(url, params=params, timeout=30)
            response.raise_for_status()
            
            data = response.json()
            return data.get("value", [])
            
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar dados Pix por estado: {e}")
            return []
    
    def get_pix_statistics_summary(self, location: str, ano_mes: str, location_type: str = "municipio") -> Dict:
        """
        Obtém resumo estatístico das transações Pix
        
        Args:
            location: Nome do município ou estado
            ano_mes: Formato 'YYYY-MM'
            location_type: 'municipio' ou 'estado'
        
        Returns:
            Dicionário com estatísticas resumidas
        """
        if location_type == "municipio":
            data = self.fetch_transactions_by_municipality(location, ano_mes)
        elif location_type == "estado":
            data = self.fetch_transactions_by_state(location, ano_mes)
        else:
            return {"error": "Tipo de localização inválido"}
        
        if not data:
            return {"error": f"Nenhum dado encontrado para {location} em {ano_mes}. Tente períodos passados (ex: 2024-01) e nomes em maiúsculo (ex: SAO PAULO)"}
        
        # Processa os dados para criar resumo enriquecido
        total_vl_pf = sum(float(item.get('VL_PagadorPF', 0)) for item in data)
        total_qt_pf = sum(float(item.get('QT_PagadorPF', 0)) for item in data)
        total_vl_pj = sum(float(item.get('VL_PagadorPJ', 0)) for item in data)
        total_qt_pj = sum(float(item.get('QT_PagadorPJ', 0)) for item in data)
        
        summary = {
            "localização": location,
            "período": ano_mes,
            "tipo": location_type,
            "dados_encontrados": len(data),
            "resumo_financeiro": {
                "valor_total_pessoa_fisica": total_vl_pf,
                "quantidade_transacoes_pf": total_qt_pf,
                "valor_total_pessoa_juridica": total_vl_pj,
                "quantidade_transacoes_pj": total_qt_pj,
                "valor_total_geral": total_vl_pf + total_vl_pj,
                "quantidade_total_geral": total_qt_pf + total_qt_pj
            },
            "municipios_detalhados": [
                {
                    "municipio": item.get("Municipio"),
                    "estado": item.get("Estado"),
                    "ano_mes": item.get("AnoMes"),
                    "valor_pf": float(item.get('VL_PagadorPF', 0)),
                    "quantidade_pf": float(item.get('QT_PagadorPF', 0))
                }
                for item in data[:5]  # Apenas os primeiros 5 para resumo
            ],
            "timestamp_consulta": datetime.now().isoformat(),
            "status": "sucesso"
        }
        
        return summary