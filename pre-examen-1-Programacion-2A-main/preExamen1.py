# 1. preguntar si imprime archivo u objeto
# 2. si es archivo, preguntar tipo de papel y/o si es blanco/negro o a color
# 3. si es objeto, preguntar que objeto sera y que material utilizara

#  clases:  impresora, impresion, material


class Hoja():
    def __init__(self,nombre:str,tamaño:str, gramaje:int, opacidad:str):
        self.nombre = nombre
        self.tamaño=tamaño
        self.gramaje=gramaje
        self.opacidad=opacidad
    
    def compatible(self,nombrePapel:str):
        if(nombrePapel == "xerografico" or nombrePapel == "bond" or nombrePapel == "transparente"):
            return "Laser"
        elif (nombrePapel == "continuo"):
            return "Puntos"
        elif(nombrePapel=="fotografico" or nombrePapel == "mate"):
            return "Inyeccion"
        elif(nombrePapel=="TPU" or nombrePapel=="PET-G2"): 
            return "3D-flexible"
        else: return "3D-rigido"

class Impresora():
    def __init__(self, nombre:str,marca:str,tipo:str):
        self.nombre=nombre
        self.marca=marca
        self.tipo = tipo

class ObjetoParaImpresion3d():
    material = []
    aBs = {"nombre":'ABS',"tipo":"comun","consistencia":"rigida","color":"rojo"}
    pla = {"nombre":'PLA',"tipo":"comun","consistencia":"rigida","color":"verde"}
    petg = {"nombre":'PET-G2',"tipo":"comun","consistencia":"flexible","color":"amarillo"}
    poliC= {"nombre":'policarbonato',"tipo":"ingenieria","consistencia":"rigida","color":"blanco"}
    tpu= {"nombre":'TPU',"tipo":"ingenieria","consistencia":"flexible","color":"gris"} #flexible
    material.extend([aBs,pla,petg,poliC,tpu,])

class Material(Hoja):
    def impresionArchivo(self,impresora:str, papel:str):
        if(impresora == self.compatible(papel)):
            return True

    def impresionObjeto(self,impresora:str,material:str):
        if(impresora == self.compatible(material)):
            return True

class Impresion(Material,Hoja,Impresora):
    def __init__(self, tipo:str, papel:str=" ",materiales:str=" "):
        self.tipo=tipo
        self.papel=papel
        self.materiales=materiales

    def imprimiendo(self):
        impresoras = imp
        papeles = papelDisponible
        if self.tipo == "archivo":
            for i in imp:
                verificarCompatibilidad =self.impresionArchivo(i.tipo,self.papel)
                while verificarCompatibilidad == True:
                    for p in papeles:
                        while p.nombre == self.papel:
                            return "NOMBRE DE IMPRESORA: "+i.nombre+" MARCA: "+i.marca+" TIPO DE IMPRESORA: "+i.tipo+'\n'+"Hoja a utilizar: "+p.nombre+" gramaje: "+str(p.gramaje)+"g/m2"+" opacidad: "+p.opacidad
        elif self.tipo == "objeto":
            o3d = ObjetoParaImpresion3d().material
            for i in imp:
                verificarCompatibilidad = self.impresionObjeto(i.tipo,self.materiales)
                while verificarCompatibilidad == True:
                    for o in o3d:
                        while o["nombre"] == self.materiales:
                            return "NOMBRE DE IMPRESORA: "+i.nombre+" MARCA: "+i.marca+" TIPO DE IMPRESORA: "+i.tipo+'\n'+" material a utilizar: "+o["nombre"]+ \
                                " tipo: "+o["tipo"]+" consistencia: "+o["consistencia"]+" Color: "+o["color"]


#impresora laser
papelDisponible =[]
xerografico= Hoja("xerografico","oficio",112,"90%")
bond = Hoja("bond","Carta",75,"100%")
transparente = Hoja("transparente","1/2 pliego",20,"5%")
#impresora de de puntos
continuo= Hoja("continuo","1/8 pliego",60,"100%")
#impresora de inyeccion tinta
fotografico = Hoja("fotografico","1/4 pliego",170,"100%")
mate = Hoja("mate","A1",90,"95")
papelDisponible.extend([xerografico,bond,transparente,continuo,fotografico,mate])

#impresoras disponibles
imp = []
p2500w = Impresora("P2500W","PANTUM","Laser")
bm5100 = Impresora("BM5100FDW","PANTUM","Laser")
dfx9k =  Impresora("DFX-9000","Xerox","Puntos")
eco =  Impresora("EcoTank","Cannon","Inyeccion")
maxify =  Impresora("MB5420","Cannon","Inyeccion")
ender3 = Impresora("CREALITY ENDER-3","CREALITY","3D-flexible")#materiales flexibles
anet8 = Impresora("ANET-A8","ANET","3D-rigido")
imp.extend([p2500w,bm5100,dfx9k,eco,maxify,ender3,anet8])

print("""
***************************************************
            ___  ___ _____  _   _  _   _
            |  \/  ||  ___|| \ | || | | |
            | .  . || |__  |  \| || | | |
            | |\/| ||  __| | . ` || | | |
            | |  | || |___ | |\  || |_| |
            \_|  |_/\____/ \_| \_/ \___/
***************************************************
""")
while(True):
    print("""
**************SELECCIONE TIPO DE IMPRESION:********
***************************************************
**ARCHIVO...................(1)
**OBJETO 3-D ...............(2)
**Salir de la aplicacion....(3)
***************************************************""")
#im= Impresion("archivo","bond")
#print(im.imprimiendo())
    opcion = int(input())
    match opcion:
        case 1:
            print("""indique el papel que desea utilizar para realizar la impresion:
                  ** PAPELES DISPONIBLES:
                  **......xerografico
                  **......bond
                  **......transparente
                  **......continuo
                  **......fotografico
                  **......mate""")
            decision = str(input())
            if(decision.lower() == "xerografico" or decision.lower() == "bond" or decision.lower() == "transparente" or decision.lower() == "continuo"
            or decision.lower() == "fotografico" or decision.lower() == "mate"):
                im = Impresion("archivo",decision)
                print(im.imprimiendo())
            else:
                print("ERROR: el papel que solicita no esta disponible")
        case 2:
            print("""indique el material que desea utilizar para la impresion 3D:
                  ** MATERIALES DISPONIBLES:
                  **......ABS
                  **......PLA
                  **......PET-G
                  **......Policarbonato
                  **......TPU
                  """)
            decision = str(input())
            if(decision.upper() == "ABS" or decision.upper() == "PLA" or decision.upper() == "PET-G" or decision.lower() == "policarbonato"
            or decision.upper() == "TPU"):
                im = Impresion("objeto"," ",decision)
                print(im.imprimiendo())
            else:
                print("ERROR: el papel que solicita no esta disponible")
        case 3:
            print("...Adios")
            break
        case _:
            print("ERROR: opcion no disponible") 
