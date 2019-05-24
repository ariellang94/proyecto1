from tkinter import Tk
from tkinter import filedialog as fd

def contar_palabras(texto):
    texto = texto.split()
    count = 0
    for i in texto:
        count += 1

    return count

if __name__ == "__main__":

    print("SELECCIONAR EL ARCHIVO DE TEXTO \n para contar las palabras")

    try:
        Tk().withdraw()
        texto_in = open(fd.askopenfilename(title="Abrir archivo de texto",
        initialdir=".", filetypes=[("Archivo de texto","*.txt")]), "r")
    except:
        quit()
    texto_r = texto_in.read()
    texto_in.close()
    print("\n"+texto_r+"\n")

    salida = contar_palabras(texto_r)
    print("Este texto contiene {} palabras".format(salida))

    input("Presione <Enter> para cerrar")

    
