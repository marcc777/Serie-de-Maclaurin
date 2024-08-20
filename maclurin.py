def facto(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * facto(n-1)

def sin_taylor(n, x):
    s = 0
    for i in range(n):
        s += (((-1)**i) * (x**(2*i + 1))) / facto(2*i + 1)
    print(s)

""" a medida que agregas mas terminos (iteras mas veces), la aproximacion a sin(x) mejora """
# pero, pero:
""" los numeros en una computadora tienen una presicion finita. A partir de cierto punto, los terminos que estas sumando se vuelven tan pequeños que no cambian significativamente el resultado """
""" cada termino adicional que agregas aumenta el tiempo de computo. Si bien cada termino mejora la presicion el beneficio se reduce a medida que sumas mas terminos """
# Convergencia:
""" la serie de taylor converge mas rapidamente para valores cercanos al punto de expansion... """
n = 50
for i in range(1, n+1, 1):
    sin_taylor(i, 3.141592653589793/2)  # Esto deberia aproximarse a sin(pi/2) que es 1


# Hay un limite:
""" generalmente, despues de un cierto numero de terminos, la mejora en la presicion minima """
""" no hay un limite teorico en cuanto a cuantos terminos puedes sumar, la serie es infinita y cuantos mas terminos sumes mas precisa sera la aproximacion. """


# LA CONTRADICCION EN LOS DATOS ES POR LAS LIMITANTES DEL EQUIPO.
