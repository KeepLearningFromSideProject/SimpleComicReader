import json
import pymysql
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=['GET'])
def handler():
    connection = pymysql.connect(
        db='test',
        port=3306,
        host='localhost',
        user='theusername',
        password='thepassword'
    )
    
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM comics')
    data = cursor.fetchall()
    cursor.close()
    connection.close()

    return json.dumps(data)


if __name__ ==  '__main__':

    app.run(debug=True)
