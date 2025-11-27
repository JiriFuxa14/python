# školní plánovač

def show_menu():
    print("\nŠkolní plánovač")
    print("1. Přidat úkol")
    print("2. Zobrazit všechny úkoly")
    print("3. Smazat úkol")
    print("4. Ukončit")

def add_task(tasks):
    task = input("Zadejte nový úkol: ")
    tasks.append(task)
    print("Úkol přidán.")

def view_tasks(tasks):
    if not tasks:
        print("Žádné úkoly nejsou k dispozici.")
    else:
        print("\nSeznam úkolů:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_number = int(input("Zadejte číslo úkolu ke smazání: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Úkol '{removed_task}' byl smazán.")
            else:
                print("Neplatné číslo úkolu.")
        except ValueError:
            print("Zadejte platné číslo.")

def main():
    tasks = []
    while True:
        show_menu()
        choice = input("Vyberte možnost: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        else:
            print("Neplatná volba, zkuste to znovu.")