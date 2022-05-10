class Materia():
    def __init__(self,lista):
        self.lista=lista
        self.codigo=lista[0]
        self.nombre=lista[1]
        self.creditos=lista[2]
class Carrera():
    def __init__(self,listaC):
        self.listaC=listaC
        self.listaAprobadas=[]
        
    def aprobar(self,listacodigo):
        materiaaprobada=""
        for i in range (0,len(self.listaC)):
            if self.listaC[i].codigo == listacodigo[0]:
                materiaaprobada=self.listaC[i].nombre
                aprobado=(materiaaprobada,self.listaC[i].creditos,listacodigo[1])
                self.listaAprobadas.append(aprobado)
        if materiaaprobada=="":
            print("La materia ingresada no figura en el programa de la carrera")
        
    def __str__(self):
        if len(self.listaAprobadas) !=0:
            creditostotales=0
            notatotal=0
            aprobadas=[]
            for i in range(0,len(self.listaAprobadas)):
                creditostotales=creditostotales+self.listaAprobadas[i][1]
                notatotal=notatotal+self.listaAprobadas[i][2]
                aprobadas.append(self.listaAprobadas[i][0])
            promedio=notatotal/len(self.listaAprobadas)
            print("Total de creditos: ",creditostotales)
            print("Promdedio total: ",promedio)
            print("Materias aprobadas: ", aprobadas)
        else:
            print("No se aprobo nada")
        
analisis2 = Materia(["61.03", "Análisis 2", 8])
fisica2 = Materia(["62.01", "Física 2", 8])
algo1 = Materia(["75.40", "Algoritmos 1", 6])
c = Carrera([analisis2, fisica2, algo1])
c.aprobar(["61.03",10])
c.aprobar(["75.40",8])
c.__str__()