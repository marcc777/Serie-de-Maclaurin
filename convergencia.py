# Convergencia de una serie infinita:
"""

Cuando hablamos de una serie infinita, estamos sumando infinitos terminos.
La pregunta es: esa suma infinita tiene un valor finito?
si la respuesta es si, decimos que la serie converge.
si no decimos que diverge.

por ejemplo, considera la serie infinita: 1 + 1/2 + 1/4 + 1/8 + 1/16 + ...
a medida que sumas mas y mas terminos te acercas a un valor finito, en este caso 2.
por lo tanto esta serie converge a 2.
"""

def serie(n):
    s = 0
    for i in range(n):
        s += 1/2**i
    
    print(s)

serie(100000)
