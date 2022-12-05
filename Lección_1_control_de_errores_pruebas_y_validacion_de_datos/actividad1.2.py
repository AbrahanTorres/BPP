try:
    fichero = open("potencia.txt", "w")
    fichero.write("Una fórmula para calcular la potencia es P = T / t, donde 'T' equivale a 'trabajo' (en julios) y 't' se corresponde con el 'tiempo' (en segundos)\n")

except Exception as e:
    print("Ha ocurrido un error:", e)

finally:
    fichero.close()