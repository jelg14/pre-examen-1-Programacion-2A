# 1. preguntar si imprime archivo u objeto
# 2. si es archivo, preguntar tipo de papel y/o si es blanco/negro o a color
# 3. si es objeto, preguntar que objeto sera y que material utilizara

#  clases:  impresora, impresion, material 

class TipoImpresora():
    impresoras=["Laser","de puntos","3D","Inyeccion de tinta"]

class Hoja():
    def __init__(self,nombre:str,tamaño:str, gramaje:int, opacidad:str):
        self.nombre = nombre
        self.tamaño=tamaño
        self.gramaje=gramaje
        self.opacidad=opacidad

class Impresora():
    def __init__(self, nombre:str, marca:str): 
        self.nombre=nombre
        self.marca=marca
    
class ObjetoParaImpresion3d():
    material = []
    aBs = {"nombre":'ABS',"tipo":"comun"}
    pla = {"nombre":'PLA',"tipo":"comun"}
    petg = {"nombre":'PET-g',"tipo":"comun"}
    poliC= {"nombre":'policarbonato',"tipo":"ingenieria"}
    asa= {"nombre":'ASA',"tipo":"ingenieria"}
    pcAbs= {"nombre":'PC/ABS',"tipo":"ingenieria"}
    tpu= {"nombre":'TPU',"tipo":"ingenieria"}
    polipro={"nombre":'polipropileno',"tipo":"ingenieria"}
    material.extend([aBs,pla,petg,poliC,asa,pcAbs,tpu,polipro])
    
class Material(Hoja,ObjetoParaImpresion3d):
    def impresionArchivo(self,impresora:str):
         match impresora:
             case "Laser":
                 return True
             case "de puntos":
                 return True
             case "3D":
                 return True
             case "Inyeccion de tinta":
                 return True
             case _:
                 return "el tipo de impresora solicitada no esta disponible"
        
    def impresionObjeto(self,resistencia:str):
        match resistencia:
             case "flexible":
                 return True
             case "rigida":
                 return True
             case _:
                 return "el tipo de impresora solicitada no esta disponible"
    

#class Impresion():
#impresora laser
papelDisponible =[]
xerografico= Hoja("xerografico","oficio",112,"90%")
bond = Hoja("bond","Carta",75,"100%") # impresora de laser
transparente = Hoja("transparente","1/2 pliego","5%")
#impresora de de puntos
continuo= Hoja("continuo","1/8 pliego",60,"100%")
#impresora de inyeccion tinta
fotografico = Hoja("fotografico","1/4 pliego",170,"100%")
mate = Hoja("mate","A1",90,"95")