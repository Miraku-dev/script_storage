file_path = 'multiple.txt'
char_to_remove = ''  # символ (или набор символов), который необходимо удалить

# Считываем содержимое файла и удаляем выбранный символ (или набор символов), а также пустые строки
with open(file_path, 'r') as file:
    lines = file.readlines()
    updated_lines = [line.replace(char_to_remove, '').strip() for line in lines if line.strip()]

# Перезаписываем файл с обновленными строками
with open(file_path, 'w') as file:
    file.write('\n'.join(updated_lines))

print(f"Символ '{char_to_remove}' (или набор символов) и пустые строки успешно удалены из файла {file_path}.")
