import time
import psycopg2
import os
from flask import Flask

app = Flask(__name__)

# Настройки БД
DB_NAME = os.getenv('POSTGRES_DB', 'my_db')
DB_USER = os.getenv('POSTGRES_USER', 'admin')
DB_PASS = os.getenv('POSTGRES_PASSWORD', 'secret')
DB_HOST = 'db-server'

def connect_db():
    while True:
        try:
            conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
            return conn
        except:
            print("База еще не готова, ждем...")
            time.sleep(2)

@app.route('/')
def hello():
    conn = connect_db()
    cur = conn.cursor()
    
    # Создаем таблицу и добавляем запись
    cur.execute("CREATE TABLE IF NOT EXISTS hits (id SERIAL PRIMARY KEY, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);")
    cur.execute("INSERT INTO hits DEFAULT VALUES RETURNING id;")
    hit_id = cur.fetchone()[0]
    conn.commit()
    
    cur.close()
    conn.close()
    
    return f"<h1>Привет!</h1><p>Ты посетитель №{hit_id} в этой базе данных.</p>"

if __name__ == "__main__":
    # Запускаем Flask на всех интерфейсах внутри контейнера
    app.run(host="0.0.0.0", port=5000)