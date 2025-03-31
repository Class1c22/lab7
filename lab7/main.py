from app.io.input import input_console, read_file_builtin
from app.io.output import output_console, write_file_builtin


def main():
    text = input_console()
    output_console(f"Ви ввели: {text}")

    file_content = read_file_builtin("data/input.txt")
    output_console(f"Вміст файлу: {file_content}")
    write_file_builtin("data/output.txt", file_content)


if __name__ == "__main__":
    main()