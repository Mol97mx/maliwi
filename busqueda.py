#busca noticias en carpeta noticias, determina si se tiene las palabras clave en el texto si es asi
#almacena en la base de datos 
import glob, os, sqlite3
from datetime import datetime
#creamos la conexion con la base de datos
con=sqlite3.connect("db.sqlite3")
#creamos un cursor para la bd
c=con.cursor()
#accesar al archivo Pclave para saber que busca
pclave=open("Pclave.txt",'r',encoding='latin-1')
#coloca todas las claves en un arreglo para seguir buscando se almacenan en el arreglo clave[]
clave=pclave.read().split('\n')
pclave.close()
#accesar a la carpeta para encontrar las noticias 
os.chdir("noticias")
#mientras encuentra archivos de noticias buscara las palabras claves en la cabecera
for file in glob.glob("*.txt"):
	f = open (file,'r',encoding='latin-1')
	#Lee la primera linea donde esta el titulo de la noticia
	mensaje = f.readline()
	print(mensaje)
	#busca cada palabra clave en el titulo
	for palabra in clave:
	#si encuentra la palabra clave busca fecha, link y descripcion
		if mensaje.upper().find(palabra)>-1:
		#obtiene fecha y link
			fecha=f.readline()
			#print(f.readline())
			fuente=f.readline()
			#print(f.readline())
			#adquirir la descripcion
			descripcion=f.readline()
			#obtenemos estado, latitud y longitud de la poblacion para insertarlos en la base de datos
			for renglon in c.execute('''select * from Portafolio_ubicacion where municipio="Capital"'''):
				//print (renglon[1])
				if descripcion.find(renglon[1])>-1:
					try:
					#obtenemos fecha y hora para instertarlos en la base de datos
						time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
						if palabra=="DERRUMBE":
							#ejecutamos la insercion
							c.execute('''INSERT INTO Portafolio_evento (Tipo_evento, Tipo_material, fecha_inicio, fecha_fin, Fuente, created, updated, Estado, Municipio, Longitud, Latitud) VALUES ("DR", "R", ?, ?, ?, ?, ?, ?,"Desconocido",?,?)''',(fecha, fecha ,fuente, time, time, renglon[1], renglon [3],  renglon[4]))
						elif palabra=="HUNDIMIENTO":
							#ejecutamos la insercion
							c.execute('''INSERT INTO Portafolio_evento (Tipo_evento, Tipo_material, fecha_inicio, fecha_fin, Fuente, created, updated, Estado, Municipio, Longitud, Latitud) VALUES ("H", "R", ?, ?, ?, ?, ?, ?,"Desconocido",?,?)''',(fecha, fecha ,fuente, time, time, renglon[1], renglon [3],  renglon[4]))
						elif palabra=="SOCAVON":
							#ejecutamos la insercion
							c.execute('''INSERT INTO Portafolio_evento (Tipo_evento, Tipo_material, fecha_inicio, fecha_fin, Fuente, created, updated, Estado, Municipio, Longitud, Latitud) VALUES ("s", "R", ?, ?, ?, ?, ?, ?,"Desconocido",?,?)''',(fecha, fecha ,fuente, time, time, renglon[1], renglon [3],  renglon[4]))
						elif palabra=="DESPRENDIMIENTO":
							#ejecutamos la insercion
							c.execute('''INSERT INTO Portafolio_evento (Tipo_evento, Tipo_material, fecha_inicio, fecha_fin, Fuente, created, updated, Estado, Municipio, Longitud, Latitud) VALUES ("DP", "R", ?, ?, ?, ?, ?, ?,"Desconocido",?,?)''',(fecha, fecha ,fuente, time, time, renglon[1], renglon [3],  renglon[4]))
						else:
							#ejecutamos la insercion
							c.execute('''INSERT INTO Portafolio_evento (Tipo_evento, Tipo_material, fecha_inicio, fecha_fin, Fuente, created, updated, Estado, Municipio, Longitud, Latitud) VALUES ("RM", "R", ?, ?, ?, ?, ?, ?,"Desconocido",?,?)''',(fecha, fecha ,fuente, time, time, renglon[1], renglon [3],  renglon[4]))
					except sqlite3.IntegrityError as e:
						print('sqlite error: ', e.args[0]) # imprimir error de sql
					con.commit()#hacemos commit
			break
	f.close()#cerramos el archivo
con.close()#cerramos la conexion a la base de datos