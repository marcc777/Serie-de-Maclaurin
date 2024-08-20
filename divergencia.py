# Divergencia de una serie infinita
""" una serie como 1 + 1 + 1 + ... """

def serie(n):
    s = 0

    for _ in range(n):
        s += 1

    print(s)

""" Esta serie sigue creciendo y nunca alcanza un valor finito, por lo tanto diverge """
serie(100)
