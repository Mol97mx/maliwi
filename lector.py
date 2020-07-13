#  importa todas las noticias de un rss feed y las escribe en archivos
import feedparser
#apuntamos el parser a la url seleccionada se podria hacer un ciclo para acceder a mas de una url
d=feedparser.parse('https://www.excelsior.com.mx/rss.xml')
#mientras el rss tenga entradas
for item in d.entries:
 #creamos un archivo con el titulo de la noticia
 archivo=open('noticias/'+item.title+'.txt','w',newline='',encoding='utf8')
 #escribimos el titulo, la fecha de publicacion, el link y la descripcion en el archivo
 archivo.write(item.title+"\n"+item.published+"\n"+item.link+"\n"+item.description.rstrip('\n'))
 #cerramos el archivo
 archivo.close()