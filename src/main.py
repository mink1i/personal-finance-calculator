operations = []

def add_operation():
    op_type = input("Тип (доход/расход): ").strip().lower()
    amount = float(input("Сумма: "))
    category = input("Категория: ").strip()
    date = input("Дата (ДД.ММ.ГГГГ): ").strip()
    operations.append({"type": op_type, "amount": amount, "category": category, "date": date})
    print("Операция сохранена!\n")

def show_operations():
    print("\n--- Операции ---")
    for op in operations:
        print(f"[{op['date']}] {op['type'].capitalize()}: {op['amount']} ({op['category']})")
    print()

def show_balance():
    income = sum(op['amount'] for op in operations if op['type'] == 'доход')
    expense = sum(op['amount'] for op in operations if op['type'] == 'расход')
    print(f"\nДоход: {income} | Расход: {expense} | Баланс: {income - expense}\n")

def main():
    while True:
        print("1. Добавить  2. Показать все  3. Баланс  4. Выход")
        choice = input("Выбор: ")
        if choice == "1": add_operation()
        elif choice == "2": show_operations()
        elif choice == "3": show_balance()
        elif choice == "4": break

if __name__ == "__main__":
    main()