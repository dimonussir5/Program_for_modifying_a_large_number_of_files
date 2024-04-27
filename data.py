import os

def replace_text_in_files(folder_path, search_text, replace_text, encodings=['utf-8', 'cp1252']):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            for encoding in encodings:
                try:
                    with open(file_path, 'r', encoding=encoding) as file:
                        content = file.read()

                    content = content.replace(search_text, replace_text)

                    with open(file_path, 'w', encoding=encoding) as file:
                        file.write(content)
                    break  # Если файл успешно прочитан, выходим из цикла по кодировкам
                except UnicodeDecodeError:
                    continue  # Пытаемся прочитать файл с следующей кодировкой
            else:
                print(f"Unable to decode {file_path}. Skipping...")

# Замените 'path_to_your_folder' на путь к папке, в которой находятся файлы
folder_path = 'C://Users//New//Desktop//CR_1'
search_text = '2023'
replace_text = '2024'
# Список кодировок, которые вы хотите попробовать
encodings = ['utf-8', 'cp1252']  # Добавьте другие кодировки, если нужно
replace_text_in_files(folder_path, search_text, replace_text, encodings)