
archivo = open("../Unidad3/Archivos/ejemplo.csv","w")

listaNombres = [
    ["clemente",1],
    ["critobal",2],
    ["ana",3],
    ["rene",4],
    ["orozco",5],
    ["jorge",6],
    ["aquino",7],
    ["badillo",8],
    ["segoviano",9],
    ["salazar",10],
    ["eduardo",12],
    ["natalia",13],
    ["rodrigo",11],
    ["miguel",14],
    ["amando",15],
    ["raul",16],
    ["lexiss",17],
    ["mariana",18],
    ["angel",19],
    ["emmanuel",20],
    ["isacc",21],
    ["checo",22],
    ["paniagua",23]
]

print(listaNombres)

for datosNombre in listaNombres:
    for dato in datosNombre:
        archivo.write(str(dato) + ",")
    archivo.write("\n")

archivo.flush()
archivo.close()

