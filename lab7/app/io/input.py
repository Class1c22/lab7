def input_console():
    return input("Введіть текст: ")

def read_file_builtin(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return "Помилка: Файл не знайдено"
    except Exception as e:
        return f"Помилка: {str(e)}"