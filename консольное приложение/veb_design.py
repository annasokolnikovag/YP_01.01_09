import json

# функция для загрузки и сохранения данных
def load_data(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            print(f"Данные загружены из {filename}: {data}")
            return data
    except FileNotFoundError:
        print(f"Файл не найден: {filename}")
        return {}
    except json.JSONDecodeError:
        print(f"Ошибка в файле: {filename}")
        return {}

def save_data(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

# пустые списки для будущего сохранения в них информации
customers = {}
orders = {}
projects = {}
employees = {}
project_assignments = {}

# для основной страницы заказчиков
def customer_page(customers, orders, projects, customers_file, orders_file, projects_file):
    while True:
        print("\nСтраница заказчиков:")
        print("1: Регистрация нового заказчика")
        print("2: Просмотр заказчиков")
        print("3: Просмотр всех заказов")
        print("4: Изменить информацию о заказчике")
        print("5: Удалить заказчика")
        print("0: вернуться в главное меню")
        choice = input("Введите номер страницы: ")

        if choice == '1':
            register_customer(customers, customers_file)
        elif choice == '2':
            view_customers(customers)
        elif choice == '3':
            view_all_orders(orders)
        elif choice == '4':
            modify_customer_info(customers, customers_file)
        elif choice == '5':
            delete_customer(customers, orders, projects, customers_file, orders_file, projects_file)
        elif choice == '0':
            break
        else:
            print("Неправильный ввод")
    pass

# регистрация
def register_customer(customers, customers_file):
    customer_id = input("Введите ID заказчика: ")
    if customer_id in customers:
        print("Заказчик с таким ID уже имеется")
    else:
        name = input("Введите имя заказчика: ")
        email = input("Введите почту заказчика: ")
        customers[customer_id] = {'имя': name, 'почту': email}
        save_data(customers_file, customers)
        print("Регистрация завершена")
    pass

# вывод списка
def view_customers(customers):
    if customers:
        print("\nСписок заказчиков:")
        # для айди которые имеются в списке
        for customer_id, info in customers.items():
            print(f"ID: {customer_id}, Имя: {info['имя']}, Почта: {info['почту']}")
    else:
        print("Нет зарегистрированных заказчиков")

    pass

# просмотр заказов
def view_all_orders(orders):
    if orders:
        print("\nСписок заказов:")
        # для айди которые имеются в списке
        for customer_id, order in orders.items():
            print(f"ID заказчика: {customer_id}, Заказ: {order}")
    else:
        print("Отсутствуют заказы")

    pass

# изменение информации
def modify_customer_info(customers, customers_file):
    customer_id = input("Введите ID заказчика, которого хотите изменить: ")
    if customer_id in customers:
        print("Текущая информация:")
        print(f"Имя: {customers[customer_id]['имя']}, Почта: {customers[customer_id]['почту']}")
        name = input("Новое имя (пропустите если не хотите менять): ")
        email = input("Новая почта(пропустите если не хотите менять): ")
        if name:
            customers[customer_id]['имя'] = name
        if email:
            customers[customer_id]['почту'] = email
        save_data(customers_file, customers)
        print("Информация о заказчике обновлена")
    else:
        print("Заказчик не найден")
    pass

# удаление
def delete_customer(customers, orders, projects, customers_file, orders_file, projects_file):
    customer_id = input("Введите ID заказчика для удаления: ")
    if customer_id in customers:
        # удаление заказчика
        del customers[customer_id]
        save_data(customers_file, customers)
        print("Заказчик удален")
        # удалить связанные заказы
        if customer_id in orders:
            del orders[customer_id]
            save_data(orders_file, orders)
        # удалить связанные проекты
        projects_to_delete = [proj_id for proj_id, proj_info in projects.items() if proj_info.get('customer_id') == customer_id]
        for proj_id in projects_to_delete:
            del projects[proj_id]
        if projects_to_delete:
            save_data(projects_file, projects)
            print(f"Проект, связанный с заказчиком {customer_id} был удален")
    else:
        print("Заказчик не найден")


# для основной страницы проектов
def projects_page(projects, customers, employees, projects_file, employees_file):
    while True:
        print("\nСтраница проектов:")
        print("1: Создать новый проект")
        print("2: Просмотр всех проектов")
        print("3: Изменить информацию о проекте")
        print("4: Удалить проект")
        print("5: Назначить сотрудника в проект")
        print("6: Просмотр сотрудников, назначенных в проекте")
        print("0: Вернуться в главное меню")

        choice = input("Введите цифру страницы: ")

        if choice == '1':
            create_project(projects, customers, projects_file)
            continue
        elif choice == '2':
            view_projects(projects)
            continue
        elif choice == '3':
            modify_project_info(projects, projects_file)
            continue
        elif choice == '4':
            delete_project(projects, projects_file)
            continue
        if choice == '5':
            assign_employee_to_project(projects, employees, projects_file, employees_file)
            continue
        elif choice == '6':
            view_project_assignments(projects)
            continue
        elif choice == '0':
            break
        else:
            print("Неправильный ввод")
    pass

# создание проекта
def create_project(projects, customers, projects_file):
    project_id = input("Введите ID проекта: ")
    if project_id in projects:
        print("Проект уже существует")
    else:
        name = input("Введите название проекта: ")
        description = input("Введите описание проекта: ")
        customer_id = input("Введите ID заказчика этого проекта: ")
        # для айди которые имеются в списке
        if customer_id in customers:
            projects[project_id] = {'название': name, 'описание': description, 'ID заказчика': customer_id}
            save_data(projects_file, projects)
            print("Проект создан")
        else:
            print("Заказчик не найден")

    pass

# просмотр проектов
def view_projects(projects):
    if projects:
        print("\nПросмотр всех проектов:")
        # для айди которые имеются в списке
        for project_id, info in projects.items():
            print(f"ID проекта: {project_id}, Название: {info['название']}, Description: {info['описание']}, ID заказчика: {info['ID заказчика']}")
    else:
        print("Проекты отсутствуют")
    pass

# связать проект и работника
def assign_employee_to_project(projects, employees, projects_file, employees_file):
    project_id = input("Введите ID проекта, для которого хотите назначить сотрудника: ")
    if project_id not in projects:
        print("Проект не найден")
        return
    employee_id = input("Введите ID сотруника, которого хотите назначить: ")
    if employee_id not in employees:
        print("Работник не найден")
        return
    # добавление сотрудника в список связанных проектов
    if 'assigned_employees' not in projects[project_id]:
        projects[project_id]['assigned_employees'] = []
    if employee_id in projects[project_id]['assigned_employees']:
        print("Сотрудник уже назначен для этого проекта")
    else:
        projects[project_id]['assigned_employees'].append(employee_id)
        save_data(projects_file, projects)
        print("сотрудник успешно назначен")

# просмотр связанных проектов
def view_project_assignments(projects):
    project_id = input("Введите ID проекта, на который назначены сотрудники: ")
    if project_id in projects and 'assigned_employees' in projects[project_id]:
        assigned_employees = projects[project_id]['assigned_employees']
        print(f"Работники, связанные с проектом {project_id}: {', '.join(assigned_employees)}")
    else:
        print("Работники, связанные с проектом или проект отсутствуют")

# изменить информацию
def modify_project_info(projects, projects_file):
    project_id = input("Введите ID проекта, который хотите изменить: ")
    if project_id in projects:
        print("Текущая информация:")
        print(f"Название: {projects[project_id]['название']}, Описание: {projects[project_id]['описание']}")
        name = input("Новое название (пропустите, если не хотите изменять): ")
        description = input("Новое описание (пропустите, если не хотите изменять): ")
        if name:
            projects[project_id]['название'] = name
        if description:
            projects[project_id]['описание'] = description
        save_data(projects_file, projects)
        print("Информация о проекте обновлена")
    else:
        print("Проект не найден")
    pass

# удаление
def delete_project(projects, projects_file):
    project_id = input("Введите ID проекта, который хотите удалить: ")
    if project_id in projects:
        del projects[project_id]
        print("Проект удален")
        save_data(projects_file, projects)
    else:
        print("Проект не найден")

    pass

# для основной страницы работников
def employees_page(employees, employees_file):
    while True:
        print("\nСтраница работников:")
        print("1: Зарегистрировать нового работника")
        print("2: Просмотр работников по специальности")
        print("3: Изменить информацию о работнике")
        print("4: Удалить работника")
        print("0: Вернуться в главное меню")
        choice = input("Введите номер страницы: ")

        if choice == '1':
            register_employee(employees, employees_file)
        elif choice == '2':
            view_employees_by_specialty(employees)
        elif choice == '3':
            modify_employee_info(employees, employees_file)
        elif choice == '4':
            delete_employee(employees, employees_file)
        elif choice == '0':
            break
        else:
            print("Неправильный ввод")

    pass

# регистрация
def register_employee(employees, employees_file):
    employee_id = input("Введите ID работника: ")
    if employee_id in employees:
        print("Работник уже существует")
    else:
        name = input("Введите имя работника: ")
        specialty = input("Выберите специальность (1 – Программист, 2 – Дизайнер, 3 – Тестировщик): ")
        employees[employee_id] = {'имя': name, 'специальность': specialty}
        save_data(employees_file, employees)
        print("Работник зарегистрирован")

    pass

# просмотр работников по определенной специальности
def view_employees_by_specialty(employees):
    specialty_query = input("Введите номер специальности (1 – Программист, 2 – Дизайнер, 3 – Тестировщик): ")
    found = False
    for employee_id, info in employees.items():
        if info['специальность'] == specialty_query:
            print(f"ID: {employee_id}, Имя: {info['имя']}, Специальность: {info['специальность']}")
            found = True
    if not found:
        print("Отсутствуют работники с такой специальностью")

    pass

# изменить информацию
def modify_employee_info(employees, employees_file):
    employee_id = input("Введите ID работника, которого хотите изменить: ")
    if employee_id in employees:
        print("Текущая информация:")
        print(f"Имя: {employees[employee_id]['имя']}, Специальность: {employees[employee_id]['специальность']}")
        name = input("Новое имя(пропустите если не хотите изменить): ")
        specialty = input("Выберите специальность (1 – Программист, 2 – Дизайнер, 3 – Тестировщик, пропустите если не хотите изменить): ")
        if name:
            employees[employee_id]['имя'] = name
        if specialty:
            employees[employee_id]['специальность'] = specialty
        save_data(employees_file, employees)
        print("Информация о работнике обновлена")
    else:
        print("Работник не найден")

    pass

# удаление
def delete_employee(employees, employees_file):
    employee_id = input("Введите ID работника,которого хотите удалить: ")
    if employee_id in employees:
        del employees[employee_id]
        print("Работник удален")
        save_data(employees_file, employees)
    else:
        print("Работник не найден")

    pass

# главное меню
def main_menu():
    # пути к файлам
    customers_file = 'customers.json'
    orders_file = 'orders.json'
    projects_file = 'projects.json'
    employees_file = 'employees.json'

    # загрузка данных из
    customers = load_data(customers_file)
    orders = load_data(orders_file)
    projects = load_data(projects_file)
    employees = load_data(employees_file)

    while True:
        print("\nГлавное меню:")
        print("1: Страница заказчиков")
        print("2: Страница проектов")
        print("3: Страница работников")
        print("0: Выход")
        choice = input("Введите цифру страницы: ")

        if choice == '1':
            customer_page(customers, orders, projects, customers_file, orders_file, projects_file)
        elif choice == '2':
            projects_page(projects, customers, employees, projects_file, employees_file)
        elif choice == '3':
            employees_page(employees, employees_file)
        elif choice == '0':
            print("Выход из приложения")
            break
        else:
            print("Неправильный ввод")

if __name__ == "__main__":
    main_menu()
