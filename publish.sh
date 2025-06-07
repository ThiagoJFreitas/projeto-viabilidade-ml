
#!/bin/bash

# Verifica se twine e build estão instalados
echo "🔍 Verificando dependências..."
pip install --quiet --upgrade build twine

# Remove builds anteriores
echo "🧹 Limpando diretórios antigos..."
rm -rf build/ dist/ *.egg-info

# Gera os arquivos de distribuição
echo "⚙️ Gerando pacotes com build..."
python -m build

# Publica no PyPI
echo "🚀 Publicando com twine..."
twine upload dist/*

echo "✅ Publicação concluída!"
