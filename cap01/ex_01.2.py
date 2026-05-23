#%%
## 1. Quantos segundos há em 42 minutos e 42 segundos

print(42*60+42)

# cap01/ex_01.py

minutos = 42
segundos = 42

total_segundos = minutos * 60 + segundos

print("Total de segundos:", total_segundos)


# %%
# 2. Quantas milhas ha em 10 quilômetros?
# Dica uma milha equivale a 1,61 quilômetro
milha = 1.61
quilometros = 10

total_milhas = quilometros / milha

print(total_milhas)


# %%
# 3. Se você correr 10 quilômetros em 42 minutos e 42 segundos,
# qual é o seu passo médio (tempo por milha em minutos e segundos)?
# qual é a velociade média em milhas por hora?

# Dados
km = 10
minutos = 42
segundos = 42
km_por_milha = 1.61

# Conversões
total_segundos = minutos * 60 + segundos
milhas = km / km_por_milha

# Passo médio (segundos por milha)
passo_segundos = total_segundos / milhas
passo_minutos = int(passo_segundos / 60)
passo_seg_restantes = passo_segundos % 60

# Velocidade média em milhas por hora
horas = total_segundos / 3600
velocidade_mph = milhas / horas

# Resultados
print("Passo médio:", passo_minutos, "minutos e", round(passo_seg_restantes, 1), "segundos por milha")
print("Velocidade média:", round(velocidade_mph, 2), "milhas por hora")