import json
import pymysql
from flask import Flask
from flask_cors import cross_origin

app = Flask(__name__)

connection = pymysql.connect(
    db='test',
    port=3306,
    host='localhost'
    user='theusername',
    password='thepassword'
)


@app.route("/comics/", methods=['GET'])
@cross_origin()
def getComics():
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT * FROM comics')
    data = cursor.fetchall()
    cursor.close()

    return json.dumps(data)


@app.route("/episodeof/<comic_id>", methods=['GET'])
@cross_origin()
def getEpisodes(comic_id: str):
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT id, comic_id, episode_name FROM episodes WHERE comic_id = %s', comic_id)
    data = cursor.fetchall()
    cursor.close()

    return json.dumps(data)


@app.route("/imageof/<episode_id>", methods=['GET'])
@cross_origin()
def getImages(episode_id: str):
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute('SELECT id, image_url FROM images WHERE episode_id = %s', episode_id)
    data = cursor.fetchall()
    cursor.close()

    return json.dumps(data)


if __name__ ==  '__main__':
    app.run(debug=True)
    connection.close()
