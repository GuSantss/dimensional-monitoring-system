# IMPORTAÇÃO DE BIBLIOTECAS
import pandas as pd

status = []

# LEITURA DE PLANILHA
df = pd.read_excel("exercicio.xlsx")

# CLASSIFICAÇÃO DE MEDIDAS
for i, l in df.iterrows():
    cota = l["COTA"]
    lim_max = l["LIM MAX"]
    lim_min = l["LIM MIN"]
    medido = l["MEDIDO"]

    faixa = lim_max - lim_min
    margem = faixa * 0.16
    alerta_max = lim_max - margem
    alerta_min = lim_min + margem

    if medido > lim_max or medido < lim_min:
        status.append("VERMELHO")
    elif medido < lim_max and medido > alerta_max or medido > lim_min and medido < alerta_min:
        status.append("ALERTA")
    else:
        status.append("OK")

df["STATUS"] = status
df["ALERTA MAX"] = df["LIM MAX"].round(3) - (df["LIM MAX"] - df["LIM MIN"]) * 0.16
df["ALERTA MIN"] = df["LIM MIN"].round(3) + (df["LIM MAX"] - df["LIM MIN"]) * 0.16

contagem = df["STATUS"].value_counts()
percentual = (df["STATUS"].value_counts() / len(df)) * 100
problemas = contagem.get("ALERTA", 0) + contagem.get("VERMELHO", 0)


titulo = "RESUMO DA ANÁLISE"
largura = 30

# RESUMO DA ANÁLISE
print("=" * largura)
print(f"{titulo:^{largura}}")
print("=" * largura)

print(f"Total de Cotas: {len(df)}\n")
print(f"🟢 OK: {contagem.get("OK", 0)} ({percentual.get("OK", 0):.2f}%)")
print(f"🟡 ALERTA: {contagem.get("ALERTA", 0)} ({percentual.get("ALERTA", 0):.2f}%)")
print(f"🔴 VERMELHO: {contagem.get("VERMELHO", 0)} ({percentual.get("VERMELHO", 0):.2f}%)")
print(f"\n⚠️  Necessitam atenção: {problemas} ({(problemas / len(df)) * 100}%)")
print(f"\nData da Análise: {pd.Timestamp.now():%d/%m/%Y %H:%M}")

# df.to_excel("formatado.xlsx", index=False)
