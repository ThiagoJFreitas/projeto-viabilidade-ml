
from viabilidade_modelo.core import prever_projetos

# Exemplo de novos projetos (entrada válida)
novos_projetos = [
    {"investment": 200000, "expected_return": 300000, "impact_score": 6},
    {"investment": 150000, "expected_return": 180000, "impact_score": 9}
]

# Executa previsão
try:
    resultado, metricas = prever_projetos(novos_projetos)
    print("\nResultado das previsões:\n", resultado)
    print("\nAcurácia do modelo:", metricas['accuracy'])
except Exception as e:
    print("Erro durante a previsão:", e)
