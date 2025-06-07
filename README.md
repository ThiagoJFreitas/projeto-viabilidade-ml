
# 📈 Projeto de Viabilidade com Machine Learning

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Tests](https://github.com/seu-usuario/projeto-viabilidade-ml/actions/workflows/python-app.yml/badge.svg)

Este projeto utiliza Machine Learning para prever a **viabilidade de projetos** com base em investimento, retorno esperado e impacto social. Ideal para aprender como aplicar regressão logística, escalonamento e persistência de modelos em Python.

---

## 📁 Estrutura do Projeto

```
projeto-viabilidade-ml/
├── data/
│   └── projects_data.csv              # Base de dados para treino
├── notebooks/
│   └── 2.1.Viabilidade_Projeto.ipynb  # Versão interativa do projeto
├── tests/
│   └── test_modelo.py                 # Testes automatizados com pytest
├── viabilidade_modelo/
│   └── core.py                        # Código-fonte principal (funções de treino e previsão)
├── .github/
│   └── workflows/
│       └── python-app.yml             # Configuração de CI com GitHub Actions
├── main.py                            # Script de execução de exemplo
├── requirements.txt                   # Lista de dependências
├── README.md                          # Documentação principal
```

---

## 🚀 Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/projeto-viabilidade-ml.git
cd projeto-viabilidade-ml
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o exemplo

```bash
python main.py
```

---

## 🧠 O que este projeto ensina

- Leitura de dados com `pandas`
- Normalização com `StandardScaler`
- Treinamento com `LogisticRegression` (extensível para outros modelos)
- Avaliação com `classification_report`
- Salvamento e reuso de modelos com `joblib`
- Previsões com novos dados
- Estrutura modular e testável para projetos de ML

---

## 🧪 Testes automatizados

Este projeto inclui testes com [pytest](https://docs.pytest.org/).

### Para executar os testes:

```bash
pytest tests/
```

Os testes validam diferentes cenários de uso da função `prever_projetos`, incluindo entrada inválida e checagem de métricas.

---

## 🛠️ Integração Contínua (CI)

Este projeto possui CI configurado com **GitHub Actions** para rodar os testes automaticamente a cada push:

O workflow encontra-se em `.github/workflows/python-app.yml`.

---

## ☕ Apoie meu trabalho

Se este projeto te ajudou, considere me oferecer um café:

<a href="https://www.buymeacoffee.com/tjfreitas" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>

---

## 📦 Notas Técnicas (Avançado)

Se desejar transformar este projeto em um pacote publicável no PyPI:

- Arquivos disponíveis:
  - `setup.py`
  - `pyproject.toml`
  - `publish.sh`

### Gerar e publicar:

```bash
python -m build
pip install twine
twine upload dist/*
```

Ou use o script:

```bash
chmod +x publish.sh
./publish.sh
```

Esses arquivos estão no projeto mas não são essenciais para o uso principal.
