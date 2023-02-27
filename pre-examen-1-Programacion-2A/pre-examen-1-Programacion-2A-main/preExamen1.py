# 1. preguntar si imprime archivo u objeto
# 2. si es archivo, preguntar tipo de papel y/o si es blanco/negro o a color
# 3. si es objeto, preguntar que objeto sera y que material utilizara

#  clases:  impresora, impresion, material
    

class tipoImpresora():
    def get_tipo_x_marca(self,m:str):
        match m:
            case "PANTUM":
                return "laser"
            case "Xerox":
                return "puntos"
            case "Cannon":
                return "inyeccion"
            case _:
                return "3-D"
                

class Hoja():
    def __init__(self,nombre:str,tamaño:str, gramaje:int, opacidad:str):
        self.nombre = nombre
        self.tamaño=tamaño
        self.gramaje=gramaje
        self.opacidad=opacidad

class Impresora(tipoImpresora):
    def __init__(self, nombre:str,marca:str):
        self.nombre=nombre
        self.marca=marca
    def indicar_tipo(self):
        return self.get_tipo_x_marca(self.marca)

class ObjetoParaImpresion3d():
    material = []
    aBs = {"nombre":'ABS',"tipo":"comun","consistencia":"rigida"}
    pla = {"nombre":'PLA',"tipo":"comun","consistencia":"rigida"}
    petg = {"nombre":'PET-g',"tipo":"comun","consistencia":"rigida"}
    poliC= {"nombre":'policarbonato',"tipo":"ingenieria","consistencia":"rigida"}
    asa= {"nombre":'ASA',"tipo":"ingenieria","consistencia":"rigida"}
    pcAbs= {"nombre":'PC/ABS',"tipo":"ingenieria","consistencia":"rigida"}
    tpu= {"nombre":'TPU',"tipo":"ingenieria","consistencia":"flexible"} #flexible
    polipro={"nombre":'polipropileno',"tipo":"ingenieria","consistencia":"rigida"}
    material.extend([aBs,pla,petg,poliC,asa,pcAbs,tpu,polipro])

class Material():
    def impresionArchivo(self,impresora:str):
        for p in papelDisponible:
            match impresora:
                case "Laser":
                    if p.nombre == "xerografico" or p.nombre == "bond" or p.nombre == "transparente":
                        return p
                case "de puntos":
                    if p.nombre == "continuo":
                        return p
                case "Inyeccion de tinta":
                    if p.nombre == "fotografico" or p.nombre == "mate":
                        return p
                case _:
                    return False

    def impresionObjeto(self,resistencia:str):
        i = ObjetoParaImpresion3d()
        materiales = i.material
        for m in materiales:
            if m["consistencia"] == resistencia:
                return m
            else:
                return False

class Impresion(Material,Hoja,Impresora):
    def __init__(self, tipo:str, papel:str=" ",materiales:str=" "):
        self.tipo=tipo
        self.papel=papel
        self.materiales=materiales
    
    def imprimiendo(self):    
        match self.tipo:
            case "archivo":
                for i in imp:
                    typ=i.indicar_tipo()
                    return i.nombre+"tipo de impresora"+typ
#impresora laser
papelDisponible =[]
xerografico= Hoja("xerografico","oficio",112,"90%")
bond = Hoja("bond","Carta",75,"100%") # impresora de laser
transparente = Hoja("transparente","1/2 pliego",20,"5%")
#impresora de de puntos
continuo= Hoja("continuo","1/8 pliego",60,"100%")
#impresora de inyeccion tinta
fotografico = Hoja("fotografico","1/4 pliego",170,"100%")
mate = Hoja("mate","A1",90,"95")
papelDisponible.extend([xerografico,bond,transparente,continuo,fotografico,mate])

#impresoras disponibles
imp = []
p2500w = Impresora("P2500W","PANTUM") #LASER
bm5100 = Impresora("BM5100FDW","PANTUM") #LASER
dfx9k =  Impresora("DFX-9000","Xerox") #PUNTOS
eco =  Impresora("EcoTank","Cannon") #inyeccion
maxify =  Impresora("MB5420","Cannon")#inyeccion
imp.extend([p2500w,bm5100,dfx9k,eco,maxify])

print("""
***************************************************
            ___  ___ _____  _   _  _   _
            |  \/  ||  ___|| \ | || | | |
            | .  . || |__  |  \| || | | |
            | |\/| ||  __| | . ` || | | |
            | |  | || |___ | |\  || |_| |
            \_|  |_/\____/ \_| \_/ \___/
***************************************************
**************SELECCIONE TIPO DE IMPRESION:********
***************************************************
**ARCHIVO............(1)
**OBJETO 3-D ............(2)
***************************************************""")
im= Impresion("archivo","bond")
print(im.imprimiendo())
#opcion = int(input())

