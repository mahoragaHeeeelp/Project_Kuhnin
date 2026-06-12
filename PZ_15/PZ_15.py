"""
Вариант 5: Приложение БАНК
Таблица Клиент: Код клиента, Клиент (Ф.И.О.), Периодический платеж,
Годовой %, Срок вклада, Пластиковая карта (логическое поле), Конечная сумма.
"""
import sqlite3
from data import clients_data

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
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clients")
    cursor.executemany('INSERT INTO clients VALUES (?, ?, ?, ?, ?, ?, ?)', clients_data)
    conn.commit()
    print("база данных автоматически заполнена данными из data.py")

def print_table(records, headers):
    if not records:
        print("результат пуст.")
        return
    col_widths = []
    for i in range(len(headers)):
        w = max(len(str(row[i])) for row in records)
        col_widths.append(max(w, len(headers[i])))
    fmt = " | ".join(f"{{:<{w}}}" for w in col_widths)
    print(fmt.format(*headers))
    print("-+-".join("-" * w for w in col_widths))
    for row in records:
        row_list = list(row)
        if len(row_list) == 7 and isinstance(row_list[5], (int, bool)):
            row_list[5] = "да" if row_list[5] else "нет"
        print(fmt.format(*row_list))

def show_all(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM clients ORDER BY id")
    records = cursor.fetchall()
    print("все записи в таблице:")
    print_table(records, ["id", "фио", "платеж", "ставка", "срок", "карта", "сумма"])

def search_examples(conn):
    cursor = conn.cursor()
    print("результаты поиска (3 запроса):")

    print("\n1. поиск по фио (содержит 'иван'):")
    cursor.execute("SELECT * FROM clients WHERE full_name LIKE '%Иван%'")
    print_table(cursor.fetchall(), ["id", "фио", "платеж", "ставка", "срок", "карта", "сумма"])

    print("\n2. поиск: ставка > 10% и есть карта:")
    cursor.execute("SELECT * FROM clients WHERE annual_rate > 10 AND has_card = 1")
    print_table(cursor.fetchall(), ["id", "фио", "платеж", "ставка", "срок", "карта", "сумма"])

    print("\n3. поиск: срок вклада от 12 до 24 месяцев:")
    cursor.execute("SELECT * FROM clients WHERE deposit_term BETWEEN 12 AND 24")
    print_table(cursor.fetchall(), ["id", "фио", "платеж", "ставка", "срок", "карта", "сумма"])

def update_examples(conn):
    cursor = conn.cursor()
    print("результаты обновления (3 запроса):")

    cursor.execute("UPDATE clients SET annual_rate = 11.0 WHERE id = 1")
    print(f"обновлена ставка для id=1, затронуто строк: {cursor.rowcount}")

    cursor.execute("UPDATE clients SET deposit_term = deposit_term + 6 WHERE has_card = 0")
    print(f"увеличен срок для клиентов без карты, затронуто строк: {cursor.rowcount}")

    cursor.execute("UPDATE clients SET periodic_payment = 5500 WHERE final_amount > 100000")
    print(f"установлен платеж для вкладов > 100000, затронуто строк: {cursor.rowcount}")

    conn.commit()
    print("изменения сохранены в базе.")

def delete_examples(conn):
    cursor = conn.cursor()
    print("результаты удаления (3 запроса):")

    cursor.execute("DELETE FROM clients WHERE id = 10")
    print(f"удален клиент с id=10, затронуто строк: {cursor.rowcount}")

    cursor.execute("DELETE FROM clients WHERE deposit_term < 12")
    print(f"удалены вклады со сроком < 12, затронуто строк: {cursor.rowcount}")

    cursor.execute("DELETE FROM clients WHERE final_amount < 50000 AND has_card = 0")
    print(f"удалены записи с суммой < 50000 и без карты, затронуто строк: {cursor.rowcount}")

    conn.commit()
    print("изменения сохранены в базе.")

def main():
    connection = init_db()
    fill_data(connection)
    print("приложение запущено.")

    while True:
        print("\nменю:")
        print("1. показать таблицу")
        print("2. выполнить поиск")
        print("3. выполнить обновление")
        print("4. выполнить удаление")
        print("0. выход")

        choice = input("выберите действие: ").strip()

        if choice == '1':
            show_all(connection)
        elif choice == '2':
            search_examples(connection)
        elif choice == '3':
            update_examples(connection)
        elif choice == '4':
            delete_examples(connection)
        elif choice == '0':
            print("выход из программы.")
            break
        else:
            print("неверный ввод.")

    connection.close()

if __name__ == '__main__':
    main()
