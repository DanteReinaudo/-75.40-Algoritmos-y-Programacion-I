def Ingreso():
    chain=input("Ingrese una cadena de caracteres: ")
    return(chain)
def slicing(chain):
    print(chain[0:2])
    print(chain[-3:len(chain)])
    for i in range(0,len(chain),2):
        print(chain[i],end="")
    print()
def invierte_chain(chain):
    for i in range(len(chain)-1,-1,-1):
        print(chain[i],end="")
    print()
chain=Ingreso()
slicing(chain)
invierte_chain(chain)
print(chain,end="")
invierte_chain(chain)