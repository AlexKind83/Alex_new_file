
i = 0
while True:
    try:
        guesses_number = int(input("Введите число от 1 до 100 \nЧисло 0 для выхода из игры: "))
        a = guesses_number
        number_to_guess = 73
        b = number_to_guess
        i += 1
        if a == b:
            print("\nВы угадали заданное число с", i, 'раза')
            break
        elif a < b or b < a:
            if 0 < a < b:
                if 63 <= a <= 72:
                    print("\nЗагаданное число меньше 'горячо'")
                if 53 <= a <= 62:
                    print("\nЗагаданное число меньше 'тепло'")
                if 1 <= a <= 52:
                    print("\nЗагаданное число меньше 'холодно'")
            elif b < a < 101:
                if 74 <= a <= 83:
                    print("\nЗагаданное число больше 'горячо'")
                if 84 <= a <= 93:
                    print("\nЗагаданное число больше 'тепло'")
                if 94 <= a <= 100:
                    print("\nЗагаданное число больше 'холодно'")
            elif a == 0:
                print("\nВы завершили игру")
                break
            else:
                print("\nНе корректный ввод числа \nчисло должно быть от 1 до 100")
                i -= 1
    except ValueError:
        print("\nНе корректный ввод данных \nЧисло должно быть цифрой")
    finally:
        print()
