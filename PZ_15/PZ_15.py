"""
Вариант 5: Приложение БАНК
Таблица Клиент: Код клиента, Клиент (Ф.И.О.), Периодический платеж, 
Годовой %, Срок вклада, Пластиковая карта (логическое поле), Конечная сумма.
"""
import sqlite3

def init_db():
    conn = sqlite3.connect('bank.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY,
            full_name TEXT NOT NULL,
            periodic_payment REAL,
            annual_rate REAL,
            deposit_term INTEGER,
            has_card BOOLEAN,
            final_amount REAL
        )
    ''')
    conn.commit()
    return conn


def fill_data(conn):
    clients = [
        (1, 'Иванов И.И.', 5000.0, 10.5, 12, 1, 63000.0),
        (2, 'Петров П.П.', 2000.0, 8.0, 24, 0, 52000.0),
        (3, 'Сидоров С.С.', 10000.0, 12.0, 6, 1, 63600.0),
        (4, 'Кузнецов А.Н.', 1500.0, 7.5, 36, 0, 60000.0),
        (5, 'Смирнова О.В.', 3000.0, 9.0, 12, 1, 39000.0),
        (6, 'Попов М.А.', 7000.0, 11.0, 18, 1, 138000.0),
        (7, 'Васильев Д.С.', 4500.0, 8.5, 24, 0, 117000.0),
        (8, 'Павлов К.Е.', 8000.0, 10.0, 12, 1, 104000.0),
        (9, 'Соколов И.Б.', 2500.0, 7.0, 48, 0, 136000.0),
        (10, 'Михайлов В.Г.', 6000.0, 9.5, 6, 1, 37700.0)
    ]
    cursor = conn.cursor()
    cursor.executemany('''
        INSERT OR REPLACE INTO clients VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', clients)
    conn.commit()

def search_examples(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients WHERE full_name LIKE '%Иван%'")
    cursor.execute("SELECT * FROM clients WHERE annual_rate > 10 AND has_card = 1")
    cursor.execute("SELECT * FROM clients WHERE deposit_term BETWEEN 12 AND 24")
    return cursor.fetchall()

def update_examples(conn):
    cursor = conn.cursor()
    cursor.execute("UPDATE clients SET annual_rate = 11.0 WHERE id = 1")
    cursor.execute("UPDATE clients SET deposit_term = deposit_term + 6 WHERE has_card = 0")
    cursor.execute("UPDATE clients SET periodic_payment = 5500 WHERE final_amount > 100000")
    conn.commit()
 
def delete_examples(conn):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clients WHERE id = 10")
    cursor.execute("DELETE FROM clients WHERE deposit_term < 12")
    cursor.execute("DELETE FROM clients WHERE final_amount < 50000 AND has_card = 0")
    conn.commit()


def main():
    connection = init_db()
    fill_data(connection)
    
    print("примеры готовы")
    search_results = search_examples(connection)
    for row in search_results:
        print(row)
        
    update_examples(connection)
    print("данные обновлены")
    
    delete_examples(connection)
    print("лишние данные удалены")
    
    connection.close()


if __name__ == '__main__':
    main()
