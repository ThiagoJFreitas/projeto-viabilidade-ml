
# 🤝 Contribuindo com o Projeto

Obrigado por querer contribuir com este projeto de Viabilidade de Projetos com Machine Learning!

Este repositório segue o modelo de branches baseado em **GitFlow**, com integração contínua via GitHub Actions.

---

## 🧭 Fluxo de Desenvolvimento (GitFlow)

Antes de começar, inicialize o GitFlow no seu repositório local (se ainda não o fez):

```bash
git flow init
```

### Respostas sugeridas:

- Branch de produção: `main`
- Branch de desenvolvimento: `develop`
- Prefixo de features: `feature/`
- Prefixo de hotfix: `hotfix/`
- Demais valores: pressione Enter

---

## 🚀 Como contribuir

### 1. Faça um fork do projeto
Crie uma cópia do repositório no seu GitHub.

### 2. Clone seu fork
```bash
git clone https://github.com/ThiagoJFreitas/projeto-viabilidade-ml.git
cd projeto-viabilidade-ml
```

### 3. Inicie uma nova feature com GitFlow
```bash
git flow feature start nome-da-sua-feature
```

### 4. Faça seus commits localmente

### 5. Finalize a feature
```bash
git flow feature finish nome-da-sua-feature
```

### 6. Faça push das alterações
```bash
git push origin develop
```

---

## ✅ Regras para Pull Requests

- Envie PRs sempre da sua `feature/*` para `develop`
- A CI será executada automaticamente
- Certifique-se de que os testes (`pytest`) estão passando:
```bash
pytest tests/
```

---

## 🧪 Como rodar os testes

Após instalar as dependências:

```bash
pytest tests/
```

---

## 📦 Publicação no PyPI

Este repositório também está pronto para ser empacotado e publicado. Se quiser colaborar com melhorias para distribuição, use:

```bash
chmod +x publish.sh
./publish.sh
```

---

## ☕ Apoie

Se este projeto te ajudar, considere apoiar:  
<a href="https://www.buymeacoffee.com/tjfreitas" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
