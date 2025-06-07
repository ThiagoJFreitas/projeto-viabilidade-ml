
import os
import joblib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report
from typing import List, Tuple, Optional

def carregar_dados(caminho_csv: str) -> pd.DataFrame:
    """Carrega os dados dos projetos a partir de um arquivo CSV."""
    return pd.read_csv(caminho_csv)

def treinar_modelo(dados: pd.DataFrame, caminho_modelo: str) -> Tuple[LogisticRegression, StandardScaler, dict]:
    """Treina o modelo de Regressão Logística e salva modelo, scaler e métricas."""
    X = dados[["investment", "expected_return", "impact_score"]]
    y = dados["viability"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.3, random_state=42
    )

    modelo = LogisticRegression()
    modelo.fit(X_train, y_train)

    y_pred = modelo.predict(X_test)
    metricas = classification_report(y_test, y_pred, output_dict=True)

    joblib.dump(modelo, caminho_modelo)
    joblib.dump(scaler, caminho_modelo.replace(".joblib", "_scaler.joblib"))
    joblib.dump(metricas, caminho_modelo.replace(".joblib", "_metrics.joblib"))

    return modelo, scaler, metricas

def carregar_modelo_existente(caminho_modelo: str) -> Tuple[LogisticRegression, StandardScaler, dict]:
    """Carrega modelo, scaler e métricas previamente salvos."""
    modelo = joblib.load(caminho_modelo)
    scaler = joblib.load(caminho_modelo.replace(".joblib", "_scaler.joblib"))
    metricas = joblib.load(caminho_modelo.replace(".joblib", "_metrics.joblib"))
    return modelo, scaler, metricas

def prever_projetos(
    novos_projetos: List[dict], caminho_modelo: str = "logistic_model.joblib"
) -> Tuple[Optional[pd.DataFrame], dict]:
    """
    Treina o modelo se não existir ou o carrega, e realiza previsões para novos projetos.
    """
    if os.path.exists(caminho_modelo):
        modelo, scaler, metricas = carregar_modelo_existente(caminho_modelo)
    else:
        dados = carregar_dados("data/projects_data.csv")
        modelo, scaler, metricas = treinar_modelo(dados, caminho_modelo)

    if novos_projetos:
        df_novos = pd.DataFrame(novos_projetos)
        X_novos_scaled = scaler.transform(df_novos)
        previsoes = modelo.predict(X_novos_scaled)
        probabilidades = modelo.predict_proba(X_novos_scaled)[:, 1]

        df_novos["viability"] = previsoes
        df_novos["probability"] = probabilidades
        return df_novos, metricas

    return None, metricas
