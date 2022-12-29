from utils import read_csv, create_dir_month, create_dirs_districts, create_dirs_sirens


if __name__ == '__main__':
    month = create_dir_month()

    actual_data = read_csv('rsu.csv')

    choise = int(input('Какую структуру папок нужно создать? \n 1 - районы \n 2 - районы + рсу \n'))

    if choise == 1:
        create_dirs_districts(month, actual_data)
    elif choise == 2:
        create_dirs_sirens(month, actual_data)
    else:
        print('Читаем внимательно, только 1 или 2.')