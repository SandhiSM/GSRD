# これは関数(メソッド)集
import csv
import datetime as dt
import os


ENC = 'UTF-8'


def error_log(error: str) -> None:
    time = dt.datetime.now(dt.timedelta(hours=9.0))
    with open(fr'.\data\crashlogfiles\{time}.txt', 'w', encoding=ENC, newline='') as log_file:
        log_file.write(error)


def csv_load(file_name: str) -> list:
    with open(fr'.\data\savefiles\{file_name}.csv', encoding=ENC) as csv_file:
        return [list(value) for value in csv.reader(csv_file)]


def csv_write(file_name: str, data: list) -> None:
    with open(fr'.\data\savefiles\{file_name}.csv', 'w', encoding=ENC, newline='') as csv_file:
        csv.writer(csv_file).writerows(data)


def data_list() -> list:
    path = r'..\data\savefiles'
    files = os.listdir(path)
    data_list = [file_name[:-4]
                 for file_name in files if os.path.isfile(os.path.join(path, file_name))]
    return data_list
