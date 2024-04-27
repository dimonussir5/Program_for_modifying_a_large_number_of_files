import os

def add_space_to_end_of_files_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            with open(file_path, 'a') as file:  # Открываем файл в режиме добавления
                file.write(' ')  # Добавляем пробел в конец файла

# Замените 'path_to_your_folder' на путь к папке, в которой находятся файлы
folder_path = 'C://Users//New//Desktop//CR_1'
add_space_to_end_of_files_in_folder(folder_path)