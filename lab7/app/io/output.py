def output_console(text):
    print(text)

def write_file_builtin(filename, text):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(str(text))
        return True
    except Exception as e:
        print(f"Помилка запису у файл: {str(e)}")
        return False