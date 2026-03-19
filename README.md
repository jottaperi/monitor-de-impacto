# EcoTrack: Monitor de Impacto Ambiental

O **EcoTrack** é uma aplicação web interativa desenvolvida em Python que permite aos usuários calcular e visualizar sua pegada de carbono diária com base em hábitos de consumo. 

Este projeto foi construído para demonstrar habilidades em desenvolvimento web com Streamlit, manipulação de dados com Pandas e lógica de programação voltada para sustentabilidade.

##  Funcionalidades

* **Cálculo em Tempo Real:** Converte quilômetros rodados, consumo de carne e energia (kWh) em emissões de CO2.
* **Interface Intuitiva:** Barra lateral personalizada para inserção de dados.
* **Visualização de Dados:** Gráfico comparativo que identifica qual hábito mais contribui para a pegada de carbono do usuário.

##  Tecnologias Utilizadas

 **Python 3.x**
 **Streamlit:** Para a criação da interface web.
**Pandas:** Para a estruturação e organização dos dados.

## Fórmulas de Cálculo

Os cálculos de emissão seguem as seguintes métricas base:
**Transporte:** 0.18 kg de CO2 por km rodado.
**Alimentação:** 27.0 kg de CO2 por kg de carne consumida.
**Energia:** 0.09 kg de CO2 por kWh gasto.streamlit run monitor.py

# Como executar o projeto

1. Certifique-se de ter o Python instalado.
2. Instale as dependências necessárias:
   ```bash
   pip install streamlit
   streamlit run monitor.py
