from flaskext.mysql import MySQL
from src import app
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'academia.c1mebdhdxytu.us-east-1.rds.amazonaws.com'
app.config['MYSQL_DATABASE_USER'] = 'p6' 
app.config['MYSQL_DATABASE_PASSWORD'] = 'ALrUBIaLYcHR' 
app.config['MYSQL_DATABASE_DB'] = 'p6' 
mysql.init_app(app)
