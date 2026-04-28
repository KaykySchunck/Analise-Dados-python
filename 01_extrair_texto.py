import pdfplumber
import os

# ============================================================
# SCRIPT 1 - EXTRAÇÃO DE TEXTO DOS PDFs
# CP Big Data - Análise de Planos de Governo 2012
# Candidatos: Carlos Giannazi (PSOL) e Levy Fidelix (PRTB)
# ============================================================

candidatos = {
    "giannazi": "giannazi.pdf",
    "fidelix":  "fidelix.pdf"
}

os.makedirs("outputs", exist_ok=True)

for nome, arquivo in candidatos.items():
    print(f"\n Extraindo texto de: {arquivo}")
    try:
        with pdfplumber.open(arquivo) as pdf:
            texto_completo = ""
            for pagina in pdf.pages:
                texto = pagina.extract_text()
                if texto:
                    texto_completo += texto + "\n"

        saida = f"outputs/{nome}_texto.txt"
        with open(saida, "w", encoding="utf-8") as f:
            f.write(texto_completo)

        print(f" Texto salvo em: {saida}")
        print(f"   Total de caracteres: {len(texto_completo)}")

    except FileNotFoundError:
        print(f" Arquivo '{arquivo}' não encontrado. Coloque o PDF na mesma pasta do script.")
