import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os

# ============================================================
# SCRIPT 3 - GERAÇÃO DOS GRÁFICOS
# CP Big Data - Análise de Planos de Governo 2012
# Candidatos: Carlos Giannazi (PSOL) e Levy Fidelix (PRTB)
# ============================================================

os.makedirs("outputs", exist_ok=True)

# ------------------------------------------------------------
# Configurações dos candidatos
# ------------------------------------------------------------
candidatos = {
    "giannazi": {
        "nome_completo": "Carlos Giannazi - PSOL",
        "cor": "#E63946",
        "csv": "outputs/giannazi_frequencia.csv"
    },
    "fidelix": {
        "nome_completo": "Levy Fidelix - PRTB",
        "cor": "#457B9D",
        "csv": "outputs/fidelix_frequencia.csv"
    }
}

# ------------------------------------------------------------
# Gráficos individuais (top 15 palavras por candidato)
# ------------------------------------------------------------
dados = {}

for nome, info in candidatos.items():
    if not os.path.exists(info["csv"]):
        print(f" Arquivo não encontrado: {info['csv']}. Execute o script 02 primeiro.")
        continue

    df = pd.read_csv(info["csv"]).head(15)
    dados[nome] = df

    fig, ax = plt.subplots(figsize=(12, 7))

    bars = ax.barh(
        df["palavra"],
        df["frequencia"],
        color=info["cor"],
        edgecolor="white",
        height=0.7
    )

    # Adiciona valores nas barras
    for bar, val in zip(bars, df["frequencia"]):
        ax.text(
            bar.get_width() + 0.1,
            bar.get_y() + bar.get_height() / 2,
            str(val),
            va="center",
            fontsize=10,
            color="#333333"
        )

    ax.invert_yaxis()
    ax.set_title(
        f"Frequência de Palavras no Plano de Governo\n{info['nome_completo']}",
        fontsize=14,
        fontweight="bold",
        pad=15
    )
    ax.set_xlabel("Número de Ocorrências", fontsize=12)
    ax.set_ylabel("Palavras", fontsize=12)
    ax.set_xlim(0, df["frequencia"].max() * 1.15)
    ax.grid(axis="x", linestyle="--", alpha=0.4)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.tight_layout()
    saida = f"outputs/grafico_{nome}.png"
    plt.savefig(saida, dpi=150, bbox_inches="tight")
    plt.close()
    print(f" Gráfico individual salvo: {saida}")

# ------------------------------------------------------------
# Gráfico comparativo (top 10 de cada candidato lado a lado)
# ------------------------------------------------------------
if len(dados) == 2:
    df_g = dados["giannazi"].head(10)
    df_f = dados["fidelix"].head(10)

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

    # --- Giannazi ---
    bars1 = ax1.barh(
        df_g["palavra"], df_g["frequencia"],
        color=candidatos["giannazi"]["cor"],
        edgecolor="white", height=0.7
    )
    for bar, val in zip(bars1, df_g["frequencia"]):
        ax1.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
                 str(val), va="center", fontsize=10)
    ax1.invert_yaxis()
    ax1.set_title("Carlos Giannazi - PSOL", fontsize=13, fontweight="bold",
                  color=candidatos["giannazi"]["cor"])
    ax1.set_xlabel("Número de Ocorrências", fontsize=11)
    ax1.set_ylabel("Palavras", fontsize=11)
    ax1.set_xlim(0, df_g["frequencia"].max() * 1.2)
    ax1.grid(axis="x", linestyle="--", alpha=0.4)
    ax1.spines["top"].set_visible(False)
    ax1.spines["right"].set_visible(False)

    # --- Fidelix ---
    bars2 = ax2.barh(
        df_f["palavra"], df_f["frequencia"],
        color=candidatos["fidelix"]["cor"],
        edgecolor="white", height=0.7
    )
    for bar, val in zip(bars2, df_f["frequencia"]):
        ax2.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
                 str(val), va="center", fontsize=10)
    ax2.invert_yaxis()
    ax2.set_title("Levy Fidelix - PRTB", fontsize=13, fontweight="bold",
                  color=candidatos["fidelix"]["cor"])
    ax2.set_xlabel("Número de Ocorrências", fontsize=11)
    ax2.set_ylabel("Palavras", fontsize=11)
    ax2.set_xlim(0, df_f["frequencia"].max() * 1.2)
    ax2.grid(axis="x", linestyle="--", alpha=0.4)
    ax2.spines["top"].set_visible(False)
    ax2.spines["right"].set_visible(False)

    fig.suptitle(
        "Análise Comparativa dos Planos de Governo\nEleições Municipais São Paulo 2012",
        fontsize=15, fontweight="bold", y=1.02
    )

    plt.tight_layout()
    saida_comp = "outputs/grafico_comparativo.png"
    plt.savefig(saida_comp, dpi=150, bbox_inches="tight")
    plt.close()
    print(f" Gráfico comparativo salvo: {saida_comp}")

print("\n Todos os gráficos gerados em /outputs!")
