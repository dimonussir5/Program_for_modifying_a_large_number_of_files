import os
import time

def change_file_modification_time(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            file_path = os.path.join(root, filename)
            # Получаем текущее время
            current_time = time.time()
            # Устанавливаем новую дату последнего изменения файла
            os.utime(file_path, (current_time, current_time))

# Замените 'path_to_your_folder' на путь к папке, в которой находятся файлы
folder_path = 'C://Users//New//Desktop//CR_1'
change_file_modification_time(folder_path)