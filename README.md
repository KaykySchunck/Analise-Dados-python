# 📊 CP2 — Big Data: Análise de Planos de Governo

> Segundo Checkpoint da disciplina de **Big Data** — Curso de Tecnologia, 4ESPG  
> **Aluno:** Kayky Oliveira Schunck | **RM:** 99756

---

## 📌 Sobre o Projeto

Este projeto foi desenvolvido como avaliação acadêmica da disciplina de Big Data. O objetivo é aplicar técnicas de **processamento e análise de texto** sobre os planos de governo de candidatos das **Eleições Municipais de São Paulo 2012**, utilizando as funções de **MAP** e **REDUCE** para contagem de frequência de palavras e geração de gráficos comparativos.

---

## 🗳️ Candidatos Analisados

| Candidato | Partido | Situação |
|---|---|---|
| Carlos Giannazi | PSOL | Não eleito |
| Levy Fidelix | PRTB | Não eleito |

> Os candidatos foram escolhidos conforme critério do enunciado: **não eleitos e que não participaram do segundo turno**.

---

## 🔄 Pipeline do Projeto

```
PDF dos Planos de Governo
        ↓
01_extrair_texto.py    →  Extração do texto com pdfplumber
        ↓
02_map_reduce.py       →  Limpeza + MAP e REDUCE (contagem de palavras)
        ↓
03_graficos.py         →  Geração dos gráficos com matplotlib
        ↓
Gráficos individuais + Gráfico comparativo
```

---

## 📁 Estrutura do Projeto

```
CP-Big-Data/
│
├── pdf/
│   ├── giannazi.pdf          # Plano de governo - Carlos Giannazi
│   └── fidelix.pdf           # Plano de governo - Levy Fidelix
│
├── out/
│   ├── giannazi_texto.txt        # Texto extraído do PDF
│   ├── fidelix_texto.txt         # Texto extraído do PDF
│   ├── giannazi_frequencia.csv   # Resultado do MAP/REDUCE
│   ├── fidelix_frequencia.csv    # Resultado do MAP/REDUCE
│   ├── grafico_giannazi.png      # Gráfico individual
│   ├── grafico_fidelix.png       # Gráfico individual
│   └── grafico_comparativo.png   # Gráfico comparativo
│
├── 01_extrair_texto.py
├── 02_map_reduce.py
├── 03_graficos.py
├── .gitignore
└── README.md
```

---

## 📦 Bibliotecas Utilizadas

| Biblioteca | Versão | Uso |
|---|---|---|
| `pdfplumber` | latest | Extração de texto dos PDFs |
| `pandas` | latest | Organização dos dados de frequência |
| `matplotlib` | latest | Geração dos gráficos de barras |
| `unicodedata2` | latest | Remoção de acentos na limpeza do texto |
| `re` | nativa | Expressões regulares para limpeza |
| `functools` | nativa | Função `reduce` para o MAP/REDUCE |
| `collections` | nativa | Suporte à contagem de elementos |

### Instalação

```bash
pip install pdfplumber pandas matplotlib unicodedata2
```

---

## ▶️ Como Executar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/CP-Big-Data.git
cd CP-Big-Data
```

### 2. Crie e ative o ambiente virtual
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # Windows
source .venv/bin/activate       # Mac/Linux
```

### 3. Instale as dependências
```bash
pip install pdfplumber pandas matplotlib unicodedata2
```

### 4. Execute os scripts em ordem
```bash
python 01_extrair_texto.py
python 02_map_reduce.py
python 03_graficos.py
```

---

## 🗺️ Descrição dos Scripts

### `01_extrair_texto.py`
Lê os arquivos PDF dos planos de governo usando `pdfplumber` e salva o conteúdo textual em arquivos `.txt` na pasta `out/`.

### `02_map_reduce.py`
Realiza o pipeline de processamento de texto:
- **Limpeza:** remove acentos, pontuação e stopwords (artigos, preposições, palavras irrelevantes)
- **MAP:** transforma cada palavra em um par `(palavra, 1)` usando `map()`
- **REDUCE:** soma as ocorrências de cada palavra usando `reduce()` da biblioteca `functools`
- Salva o ranking de frequência em `.csv`

### `03_graficos.py`
Lê os arquivos `.csv` gerados e produz:
- Gráfico de barras individual para cada candidato (top 15 palavras)
- Gráfico comparativo lado a lado (top 10 palavras de cada candidato)

---

## 📊 Resultados

### Carlos Giannazi — PSOL
As palavras mais frequentes foram **paulo, cidade, politica, educacao** e **prefeitura**, indicando um plano voltado à transformação social, combate à corrupção e reforma política.

### Levy Fidelix — PRTB
As palavras mais frequentes foram **paulo, capital, saude, prefeitura** e **cidade**, indicando um plano voltado à infraestrutura urbana, saúde pública e mobilidade.

---

## 🎓 Informações Acadêmicas

| Campo | Detalhe |
|---|---|
| Disciplina | Big Data |
| Avaliação | Segundo Checkpoint (CP2) |
| Curso | Tecnologia em Análise e Desenvolvimento de Sistemas |
| Turma | 4ESPG |
| Aluno | Kayky Oliveira Schunck |
| RM | 99756 |
