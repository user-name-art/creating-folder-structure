import csv
import os


def read_csv(filename: str):
    with open (filename, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=',')
        all_data = []
        for row in reader:
            all_data.append(row)

        return all_data


def create_dir_month():
    month = input('Какой месяц нужен? \n')
    if not os.path.isdir(month):
        os.mkdir(month)
    
    return month


def create_dirs_districts(month, entities):
    os.chdir(month)

    for entity in entities:
        if not os.path.isdir(f'{entity["district"]}'):
            os.mkdir(f'{entity["district"]}')


def create_dirs_sirens(month, entities):
    os.chdir(month)

    for entity in entities:
        if not os.path.isdir(f'{entity["district"]}/{entity["siren"]}'):
            os.makedirs(f'{entity["district"]}/{entity["siren"]}')
