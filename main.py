from flask import Flask
from flask_mysqldb import MySQL
import yaml
app = Flask(__name__)

db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

app.config['SECRET_KEY'] = '87a9871e86fcd34c7620bda875fc37ef'

@app.route('/edit/<int:id>')
def edit(i):
    cur=mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM users WHERE id=%s", i)
    if resultValue > 0:
        userDetails = cur.fetchone()
        cur.close()
        return

if __name__ == "__main__":
    app.run(debug=True)