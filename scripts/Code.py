

import os
import openpyxl
import pandas as pd

##Para leitura de arquivos Excel, instalei o openpyxl, que é a engine padrão do Pandas para .xlsx.

df_gdp = pd.read_excel(
    "data/GDP at market prices, current US$, millions, seas. adj..xlsx"
)

df_gdp.head()

df_gdp = df_gdp.dropna(how="all")

df_gdp = df_gdp.rename(columns={"Unnamed: 0": "Year"})

df_gdp_long = df_gdp.melt(
    id_vars="Year",
    var_name="Country",
    value_name="GDP_USD_Millions"
)
##Converter para formato LONG (ESSENCIAL)

##Limpeza final
df_gdp_long = df_gdp_long.dropna()
df_gdp_long["Year"] = df_gdp_long["Year"].astype(int)

##Validação
df_gdp_long.head()
df_gdp_long.info()

##O dataset veio em formato wide com cabeçalhos econômicos, então tratei linhas vazias, normalizei para formato long e preparei para análise e BI
##Preparei dados econômicos do World Bank, normalizei para formato long, tratei valores ausentes e deixei os tipos adequados para análise e visualização.


df_recent = df_gdp_long[df_gdp_long["Year"] >= 2015]
#Filtrando para um período recente

countries = ["Brazil", "United States", "World (WBG members)"]
df_focus = df_recent[df_recent["Country"].isin(countries)]
##Selecionando países chave

df_focus.groupby("Country")["GDP_USD_Millions"].describe()
##Análise rápida

import matplotlib.pyplot as plt

for country in countries:
    data = df_focus[df_focus["Country"] == country]
    plt.plot(data["Year"], data["GDP_USD_Millions"], label=country)

plt.legend()
plt.title("GDP Evolution (2015+)")
plt.xlabel("Year")
plt.ylabel("GDP (USD Millions)")
plt.show()
##GDP = PIB

df_recent = df_gdp_long[df_gdp_long["Year"] >= 2015]
df_recent = df_recent.sort_values(["Country", "Year"])


df_recent.to_csv("data/gdp_powerbi.csv", index=False)

