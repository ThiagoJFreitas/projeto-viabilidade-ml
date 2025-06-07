
import pytest
import pandas as pd
from viabilidade_modelo.core import prever_projetos

def test_prever_entrada_valida():
    novos = [
        {"investment": 100000, "expected_return": 150000, "impact_score": 7},
        {"investment": 300000, "expected_return": 500000, "impact_score": 10}
    ]
    resultado, metricas = prever_projetos(novos)
    assert not resultado.empty
    assert all(col in resultado.columns for col in ["viability", "probability"]), "Colunas esperadas não encontradas."
    assert 0.0 <= resultado["probability"].iloc[0] <= 1.0

def test_prever_entrada_invalida_coluna():
    novos = [{"investment": 100000, "expected_return": 150000}]  # falta impact_score
    with pytest.raises(ValueError):
        prever_projetos(novos)

def test_metricas_contem_accuracy():
    novos = [
        {"investment": 120000, "expected_return": 200000, "impact_score": 8}
    ]
    _, metricas = prever_projetos(novos)
    assert "accuracy" in metricas, "Métrica 'accuracy' não encontrada."
    assert isinstance(metricas["accuracy"], float)
