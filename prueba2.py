from tkinter import *


### Opción 1 "Instancia de Clase Tk"

#instancia de objeto Tk
Ventana1 = Tk()
Ventana1.title('Ventana 1')
### Acá iría todo el programa
Ventana1.mainloop()

###############################################################################

### Alternativa 2 nueva clase "heredando clase Tk"

class Ventana2(Tk):
    def __init__(self):
        Tk.__init__(self)
        Tk.title(self, 'Ventana 2')
        Tk.mainloop(self)
        ### Acá iría el programa

#instancia de objeto Ventana2 (que heredó de Tk)
Ventana2()
