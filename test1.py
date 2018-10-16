import pymysql
import requests

connect = pymysql.Connect(
    host="localhost",
    port=3306,
    user="root",
    passwd="774841525",
    db="learn",
    charset="utf8mb4"
)
cursor = connect.cursor()
cursor.execute("DROP TABLE IF EXISTS car_articles")
sql ='''CREATE TABLE car_articles(
        articles_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
        articles_title TEXT NOT NULL,
        articles_marks TEXT NOT NULL,
        articles_content TEXT NOT NULL
        )AUTO_INCREMENT=1
    '''
cursor.execute(sql)
connect.close()
