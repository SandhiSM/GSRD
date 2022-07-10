# これは内部処理関数(インターナルメソッド)集
import csv
import datetime as dt
import os
import shutil
import configparser
import sys


ENC = "UTF-8"


def config_load() -> str:
    loader: configparser.ConfigParser = configparser.ConfigParser()
    loader.read(r".\data\config\config.ini")
    return loader["User"]["language"], loader["User"]["password"], loader["User"]["first"]


def error_log() -> None:
    error = str(sys.exc_info())
    time = dt.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    with open(fr".\data\crashlogfiles\{time}.txt", 'w', encoding=ENC, newline='') as log_file:
        log_file.write(error)


def csv_load(file_name: str) -> list:
    with open(fr".\data\savefiles\{file_name}.csv", encoding=ENC) as csv_file:
        return [list(value) for value in csv.reader(csv_file)]


def csv_input(file_name: str) -> list:
    with open(fr".\data\inputfiles\{file_name}.csv", encoding=ENC) as csv_file:
        return [list(value) for value in csv.reader(csv_file)]


def csv_write(file_name: str, data: list) -> None:
    with open(fr".\data\savefiles\{file_name}.csv", 'w', encoding=ENC, newline='') as csv_file:
        csv.writer(csv_file).writerows(data)


def help_file_load(mode: str, language: str) -> str:
    with open(fr".\data\helpfiles\{language}\{mode}.txt", encoding=ENC) as help_file:
        return help_file.read()


def data_list() -> list:
    PATH: str = r".\data\savefiles"
    files: list = os.listdir(PATH)
    data_list: list = [file_name[:-4]
                       for file_name in files if os.path.isfile(os.path.join(PATH, file_name))]
    return data_list


def delete_file(file_name: str) -> str:
    os.remove(fr".\data\savefiles\{file_name}.csv")
    return f"File: '{file_name}' has been deleted."


def output_file(file_name: str) -> str:
    shutil.copy(fr".\data\savefiles\{file_name}.csv",
                fr".\data\outputfiles\{file_name}.csv")
    return f"File: {file_name} has been copied."
