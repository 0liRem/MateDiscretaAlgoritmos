'''MATE DISCRETA

FECHA 13/8/2024

PROGRAMADOR: Olivier Viau
DESCRIPCION: Utilizando python realizar un programa de hashing utilizando el algoritmo presentado, se pedira al usuario ingresar el numero de memoria y los datos a guardar
Recusros: ChatGPT, w3schools

Historial de modificaciones

[000] 13/08/20204

'''


def adentro(mod,x,output):
    f=x-mod
    for f in range(x):#recorre el arreglo desde la siguiente posición
        if output[f]!="":
            pass
        else:
            return(f)
        
def inicio():
    try:
        x=input("Ingrese el numero de memoria que quiera usar \n")
        x=int(x)
        y=[] 
        output=[]
    except:
        print("Error ingrese un int")
    else:
        for i in range (x): #va a hacer un ciclo para que el usuario pueda ingresar los valores que se almacenaran el la memoria usando el metodo hash
            
            try:
                y.append(int(input("Ingrese el "+str(i)+" valor que quiere guardar ")))
                output.append("")
            except:
                pass

        for i in range(x):#ciclo para guardar los datos
            mod=int(y[i])%x#saca el valor del mod (es inecesario)
            
            if output[mod]!="":#en caso que haya un valor guardado va a buscar la siguiente posicion libre
                if output[mod]==y[i]:
                    pass
                else:
                    output[adentro(mod,x,output)]=y[i]
            else:
                output[mod]=y[i]
        print(output)
inicio()