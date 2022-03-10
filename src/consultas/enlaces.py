from src.config.db import mysql


class EnlaceModel():
    def crearUrl(self,urls,enlacecorto):
        cursor = mysql.get_db().cursor()
        cursor.execute('insert into links(name_link, linkcorto) values (%s,%s)',(urls,enlacecorto))
        mysql.get_db().commit()
        cursor.close()

    def find_link(self,link):
        cursor = mysql.get_db().cursor()
        cursor.execute('USE urls')
        cursor.execute('SELECT name_link from links where links.linkcorto = %s ',(link))
        islink = cursor.fetchone()
        mysql.get_db().commit()
        cursor.close()
        print(islink,link)
        return islink
        
 