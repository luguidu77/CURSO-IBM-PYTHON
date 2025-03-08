from math import pi 


def area(r): 
    
    if type(r) not in  [float, int]: 
        raise ValueError("Solo números enteros o de coma flotante")
    if r<0: 
        raise ValueError("No se permiten valores negativos")
    return  pi * (r ** 2) 
  
# Bloque de código que se ejecuta solo si este módulo se ejecuta directamente
if __name__ == '__main__':
    valores = [1, 3, 0, -1, -3, 2+3j, True, 'hola'] 
    for v in valores: 
        areaCalculada = area(v) 
        print('Para el valor', v, 'el área es', areaCalculada)