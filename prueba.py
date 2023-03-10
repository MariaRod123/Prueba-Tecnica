from sympy import limit, oo, Symbol

t = Symbol('t')
y = (t ** 2 - t + 1) / (t ** 2 + 1)

# t=semana
def calculoNivelOxigeno(t):
    y = (t ** 2 - t + 1) / (t ** 2 + 1)
    return y


y = 1  #nivel normal

#  1 semana después
print("Nivel de oxigeno luego de 1 semana:", calculoNivelOxigeno(1) / y * 100)

# 2 semanas despúes

print("Nivel de oxígeno después de 2 semanas:", calculoNivelOxigeno(2) / y * 100)

# 10 semanas después
print("Nivel de oxígeno después de 10 semanas:", calculoNivelOxigeno(10) / y * 100)

# Limite de la función para t--> + inf
print(' El límite es :', limit(y, t, oo))
