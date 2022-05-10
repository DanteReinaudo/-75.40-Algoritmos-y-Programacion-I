CONTRASEÑA = "FALOPA420"
paswor= input("Ingrese la contraseña para ganar un premio: ")
contador = 0
while paswor != CONTRASEÑA and contador < 5:
    contador += 1
    print("La contraseña no es correcta, intentelo nuevamente")
    paswor= input("Ingrese la contraseña para ganar un premio: ")
if paswor == CONTRASEÑA:
    print("Congratulations" * 420)
    print("Parabens pra voce garotinho, ha adivinado la contraseña")
else:
    print("Fracasadinhe no encontro la contraseña")