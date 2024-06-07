import csv
import requests
import re
import tldextract
import time
import os
from joblib import Parallel, delayed
from pathlib import Path

tempo_inicial = time.time()

def ler_csv_para_lista(nome_arquivo):
    dados = []
    try:
        with open(nome_arquivo, mode='r', encoding='utf-8') as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv)
            for linha in leitor_csv:
                dados.append(linha[0])  # Supondo que a URL está na primeira coluna
    except FileNotFoundError:
        print(f"O arquivo {nome_arquivo} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo {nome_arquivo}: {e}")
    return dados

def is_rd_station_used(url):
    try:
        response = requests.get(url, timeout=10)  # Adiciona um timeout de 10 segundos
        response.raise_for_status()
        content = response.text

        # Verificar scripts ou meta tags relacionados ao RD Station no conteúdo HTML
        rd_station_patterns = [
            r'rdstation\.com',
            r'rdstation-cdn\.com',
            r'RDStationForms'
        ]

        for pattern in rd_station_patterns:
            if re.search(pattern, content, re.IGNORECASE):
                return "s"
        return "n"
    except requests.RequestException as e:
        print(f"Erro ao acessar {url}: {e}")
        return f"erro: {e}"

def verificar_site_e_salvar(site, arquivo_saida):
    # Usar tldextract para garantir a extração do domínio correto
    extracted = tldextract.extract(site)
    full_domain = f"{extracted.domain}.{extracted.suffix}"
    full_url = f"http://{full_domain}" if not site.startswith(('http://', 'https://')) else site

    print(f"Verificando: {full_url}...")
    usa_rd_station = is_rd_station_used(full_url)

    try:
        with open(arquivo_saida, mode='a', newline='', encoding='utf-8') as arquivo_csv:
            escritor_csv = csv.writer(arquivo_csv)
            escritor_csv.writerow([site, usa_rd_station])  # Escreve o site e se usa ou não RD Station
    except Exception as e:
        print(f"Erro ao escrever no arquivo {arquivo_saida}: {e}")

def verificar_sites_e_salvar_csv(sites, nome_arquivo_saida):
    Parallel(n_jobs=-1)(delayed(verificar_site_e_salvar)(site, nome_arquivo_saida) for site in sites)

input: str ='sites.csv'
output: str = 'resultados_sites_paralelo.csv'

nome_arquivo_entrada = Path(__file__).parent / input

nome_arquivo_saida = Path(__file__).parent / output


nome_arquivo = os.path.normpath(nome_arquivo_entrada)
nome_arquivo_saida = os.path.normpath(nome_arquivo_saida)


sites_para_verificar = ler_csv_para_lista(nome_arquivo)
verificar_sites_e_salvar_csv(sites_para_verificar, nome_arquivo_saida)

print(f"Demorou: {time.time() - tempo_inicial}")

