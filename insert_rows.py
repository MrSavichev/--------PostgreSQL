import psycopg2  # Импортируем библиотеку, которая позволяет нам работать с PostgreSQL в Python
import time  # Импортируем библиотеку для работы со временем
import logging # Импортируем библиотеку для логирования

logging.basicConfig(level=logging.INFO) # Настраиваем логирование

def insert_rows():
    conn = None  # Инициализируем переменную для подключения к базе данных как None
    while True:  # Начинаем бесконечный цикл
        try:
            # Подключаемся к HAProxy по порту 5000
            conn = psycopg2.connect(
                host="172.20.0.2",  # Подключаемся через имя контейнера HAProxy
                port=5000,  # Указываем порт HAProxy
                database="postgres",  # Имя базы данных
                user="postgres",  # Имя пользователя базы данных
                password="postgres"  # Пароль пользователя
            )
            cur = conn.cursor()  # Создаем курсор для выполнения операций с базой данных

            # Создаем таблицу, если она ещё не существует
            cur.execute("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, timestamp TIMESTAMPTZ DEFAULT NOW())")
            # Вставляем новую строку в таблицу
            cur.execute("INSERT INTO test_table DEFAULT VALUES")
            conn.commit() # Сохраняем изменения
            cur.close() # Закрываем курсор
            conn.close() # Закрываем подключение
            logging.info("Inserted a row.") # Выводим сообщение в лог
            time.sleep(5) # Пауза 5 секунд
        except psycopg2.OperationalError as e: # Обрабатываем ошибки
            logging.error(f"Operational error: {e}") # Выводим сообщение в лог
            if conn: # Если подключение существует
                conn.close() # Закрываем подключение
            time.sleep(5) # Пауза 5 секунд
        except Exception as e: # Обрабатываем остальные ошибки
            logging.error(f"Unexpected error: {e}") # Выводим сообщение в лог
            if conn: # Если подключение существует
                conn.close() # Закрываем подключение
            time.sleep(5) # Пауза 5 секунд

if __name__ == "__main__":
    insert_rows()  # Запускаем функцию insert_rows