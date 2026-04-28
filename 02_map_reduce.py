import unicodedata
import re
import os
from functools import reduce

# ============================================================
# SCRIPT 2 - LIMPEZA DE DADOS + MAP E REDUCE (Python Nativo)
# CP Big Data - Análise de Planos de Governo 2012
# Candidatos: Carlos Giannazi (PSOL) e Levy Fidelix (PRTB)
# ============================================================

# ------------------------------------------------------------
# STOPWORDS - palavras irrelevantes para a análise
# ------------------------------------------------------------
STOPWORDS = {
    "o", "a", "os", "as", "um", "uma", "uns", "umas",
    "de", "do", "da", "dos", "das", "em", "no", "na", "nos", "nas",
    "para", "por", "com", "sem", "sob", "sobre", "entre", "ate",
    "e", "ou", "mas", "porem", "que", "se", "ja", "nao", "nem",
    "nos", "ao", "aos", "sua", "seu", "seus", "suas",
    "este", "esta", "estes", "estas", "esse", "essa", "isso", "isto",
    "pelo", "pela", "pelos", "pelas", "num", "numa",
    "ser", "ter", "mais", "quando", "como", "tambem", "apenas",
    "todo", "toda", "todos", "todas", "cada", "sendo", "serao",
    "sera", "sao", "foi", "neste", "nesta", "deste", "desta",
    "novo", "nova", "novos", "novas", "maior", "bem", "vez",
    "alem", "ainda", "assim", "qual", "quais", "ha",
    "pdf", "creator", "pdf4free", "http", "wwwpdf4freecom",
}

# ------------------------------------------------------------
# Limpeza do texto
# ------------------------------------------------------------
def limpar_texto(texto):
    texto = unicodedata.normalize("NFKD", texto)
    texto = "".join(c for c in texto if not unicodedata.combining(c))
    texto = texto.lower()
    texto = re.sub(r"[^a-z\s]", " ", texto)
    texto = re.sub(r"\s+", " ", texto).strip()
    return texto

# ------------------------------------------------------------
# MAP: (palavra, 1)
# ------------------------------------------------------------
def map_palavras(palavras):
    return list(map(lambda p: (p, 1), palavras))

# ------------------------------------------------------------
# REDUCE: soma por palavra
# ------------------------------------------------------------
def reduce_contagem(pares):
    def reducer(acc, par):
        palavra, contagem = par
        acc[palavra] = acc.get(palavra, 0) + contagem
        return acc
    return reduce(reducer, pares, {})

# ------------------------------------------------------------
# Pipeline por candidato
# ------------------------------------------------------------
def processar_candidato(nome_candidato, caminho_txt):
    print(f"\n - Processando: {nome_candidato.upper()}")

    with open(caminho_txt, "r", encoding="utf-8") as f:
        texto_bruto = f.read()

    texto_limpo = limpar_texto(texto_bruto)
    print(f"    Limpeza concluída")

    palavras = [
        p for p in texto_limpo.split()
        if p not in STOPWORDS and len(p) > 2
    ]
    print(f"    Palavras após limpeza: {len(palavras)}")

    pares_mapeados = map_palavras(palavras)
    print(f"    MAP concluído: {len(pares_mapeados)} pares")

    contagem = reduce_contagem(pares_mapeados)
    print(f"    REDUCE concluído: {len(contagem)} palavras únicas")

    resultado = sorted(contagem.items(), key=lambda x: x[1], reverse=True)

    os.makedirs("outputs", exist_ok=True)
    saida = f"outputs/{nome_candidato}_frequencia.csv"
    with open(saida, "w", encoding="utf-8") as f:
        f.write("palavra,frequencia\n")
        for palavra, freq in resultado[:30]:
            f.write(f"{palavra},{freq}\n")

    print(f"    CSV salvo: {saida}")
    print(f"\n ==== Top 15 palavras - ===== {nome_candidato.upper()}:")
    print(f"{'Palavra':<20} {'Frequência':>10}")
    print("-" * 32)
    for palavra, freq in resultado[:15]:
        print(f"{palavra:<20} {freq:>10}")

    return resultado[:30]

# ------------------------------------------------------------
# Execução
# ------------------------------------------------------------
candidatos = {
    "giannazi": "outputs/giannazi_texto.txt",
    "fidelix":  "outputs/fidelix_texto.txt"
}

for nome, caminho in candidatos.items():
    if os.path.exists(caminho):
        processar_candidato(nome, caminho)
    else:
        print(f" Arquivo não encontrado: {caminho}. Execute o script 01 primeiro.")

print("\n MAP/REDUCE concluído! Arquivos CSV salvos em /outputs")