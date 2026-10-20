
def show_menu():
    print("""
1 — вывести всех клиентов
2 — вывести клиентов заданной марки
3 — изменить сумму обслуживания
4 — удалить клиента
5 — найти самую дорогую машину
6 — удалить машины старше n лет
7 — сгруппировать клиентов по марке
0 — выход
""")
    match input("\nВыберите пункт меню: "):
        case "1":
            pass

        case "2":
            pass

        case "3":
            pass

        case "4":
            pass

        case "5":
            pass

        case "6":
            pass

        case "7":
            pass

        case "0":
            return False
        case _:
            print("Неверный пункт меню")

    return True


def main():
    processing = True
    while processing:
        processing = show_menu()


if __name__ == "__main__":
    main()
