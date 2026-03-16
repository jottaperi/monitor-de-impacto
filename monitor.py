import streamlit as st
import pandas as pd

st.set_page_config(page_title="EcoTrack - Monitor Ambiental", layout="wide")

st.title("🌍 EcoTrack: Sua Pegada de Carbono")

st.sidebar.header("Insira seus hábitos de hoje")
km_carro = st.sidebar.number_input("KM rodados de carro:", min_value=0.0)
carne_consumida = st.sidebar.number_input("Kg de carne consumida:", min_value=0.0)
energia_kwh = st.sidebar.number_input("Consumo de energia (kWh):", min_value=0.0)


co2_transporte = km_carro * 0.18
co2_alimentacao = carne_consumida * 27.0
co2_energia = energia_kwh * 0.09
total = co2_transporte + co2_alimentacao + co2_energia

st.subheader(f"Emissão Total de Hoje: {total:.2f} kg de CO2")

dados = pd.DataFrame({
    'Categoria': ['Transporte', 'Alimentação', 'Energia'],
    'CO2 (kg)': [co2_transporte, co2_alimentacao, co2_energia]
})

st.bar_chart(dados.set_index('Categoria'))

if total > 10:
    st.warning("⚠️ Sua pegada está acima da média diária recomendada!")
else:
    st.success("✅ Parabéns! Sua pegada está dentro de um nível sustentável.")