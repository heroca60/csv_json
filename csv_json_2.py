print("""\
Programa:   Master en Visual Analytics & Big Data
Curso:      Métodos de Captura y Almacenamiento de los Datos
Matrícula:  5191711 - 447942
Estudiante: Hendrick Rolando Calderón Aguirre
Actividad:  Laboratorio.  Administración de MONGO DB con Interfaz Gráfica, Transformación de CSV a JSON
""")
#Path del archivo original de lectura
origin_path = '/home/hendrick/Documentos/UNIR/SEMESTRE I/Métodos de Captura y Almacenamiento de los Datos/Actividades/Maori/Business operations rates, activities, annual.csv'
#Path del archivo transformado a CSV
destiny_path = '/home/hendrick/Documentos/UNIR/SEMESTRE I/Métodos de Captura y Almacenamiento de los Datos/Actividades/Maori/Business operations rates, activities, annual.json'
#Abriendo archivo original con privilegios de lectura
_file = open(origin_path,'r')
#Abriendo archivo destino con privilegios de escritura
_nfile = open(destiny_path,'w')
#Obteniendo encabezados del archivo
encabezado = _file.readline().split(",")
reg = _file.readlines()
cont = 1
_nfile.write("[\n")
for line in reg:
    ln = '{\n'
    if cont > len(reg):
        ln+=''
        break
    tmp = line.split(",")
    for x in range(0,len(encabezado)):
        if x != len(encabezado) - 1:
            ln+="\"" + encabezado[x].strip() + "\": " + tmp[x].strip() + ",\n"
        else:
            ln+="\"" + encabezado[x].strip() + "\":" + tmp[x].strip() + '\n'
    if cont < len(reg):
        ln+='},\n'
    else:         
        ln+='}\n]'
    #Escribiendo la nueva línea conformada en el archivo de destino
    _nfile.write(ln)
    cont += 1
#Cerrando archivos
_nfile.close()
_file.close()
print("Archivo generado en: " + destiny_path)