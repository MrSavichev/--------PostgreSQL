import psycopg2  # Импортируем библиотеку, которая позволяет нам работать с PostgreSQL в Python
import time  # Импортируем библиотеку для работы со временем

def insert_rows():
    conn = None  # Инициализируем переменную для подключения к базе данных как None
    while True:  # Начинаем бесконечный цикл
        try:
            # Устанавливаем соединение с базой данных через HAProxy
            conn = psycopg2.connect(
                host="haproxy",  # Имя хоста, где HAProxy слушает соединения
                database="postgres",  # Имя базы данных
                user="postgres",  # Имя пользователя базы данных
                password="postgres"  # Пароль пользователя
            )
            cur = conn.cursor()  # Создаем курсор для выполнения операций с базой данных

            # Создаем таблицу, если она ещё не существует
            cur.execute("CREATE TABLE IF NOT EXISTS test_table (id SERIAL PRIMARY KEY, timestamp TIMESTAMPTZ DEFAULT NOW())")
            # Вставляем новую строку в таблицу
            cur.execute("INSERT INTO test_table (DEFAULT) VALUES (DEFAULT)")
            conn.commit()  # Применяем изменения в базе данных

            cur.close()  # Закрываем курсор
            conn.close()  # Закрываем соединение с базой данных
            print("Inserted a row.")  # Выводим сообщение о вставке строки
            time.sleep(5)  # Приостанавливаем выполнение на 5 секунд
        except Exception as error:  # Обрабатываем возникшие исключения
            print(f"Error: {error}")  # Выводим сообщение об ошибке
            if conn:  # Если соединение было установлено
                conn.close()  # Закрываем соединение
            time.sleep(5)  # Приостанавливаем выполнение на 5 секунд в случае ошибки

if __name__ == "__main__":
    insert_rows()  # Запускаем функцию insert_rows