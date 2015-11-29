massiv = range(10)
summa = 0
x = 1
if len(massiv) <= 0:
     print(0)
else:
     while x < len(massiv):
           summa = summa + massiv[x]
           x = x + 2
     resultat = summa * massiv[-1]
     print(resultat)

