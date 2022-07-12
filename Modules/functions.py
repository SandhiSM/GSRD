# これは内部処理関数(インターナルメソッド)集
import csv
import datetime
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
    time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    with open(fr".\data\crashlogfiles\{time}.txt", 'w', encoding=ENC, newline='') as log_file:
        log_file.write(error)


def csv_load(file_name: str) -> list:
    with open(fr".\data\savefiles\{file_name}.csv", encoding=ENC) as csv_file:
        return [list(value) for value in csv.reader(csv_file)]


def csv_input(file_path: str) -> list:
    with open(file_path, encoding=ENC) as csv_file:
        return [list(value) for value in csv.reader(csv_file)]


def csv_write(file_name: str, data: list) -> None:
    with open(fr".\data\savefiles\{file_name}.csv", 'w', encoding=ENC, newline='') as csv_file:
        csv.writer(csv_file).writerows(data)


def help_file_load(mode: str, language: str) -> str:
    with open(fr".\data\helpfiles\{language}\{mode}.txt", encoding=ENC) as help_file:
        return help_file.read()


def get_data_list() -> list:
    PATH: str = r".\data\savefiles"
    files: list = os.listdir(PATH)
    data_list: list = [file_name[:-4]
                       for file_name in files if os.path.isfile(os.path.join(PATH, file_name))]
    return data_list


def get_help_list(language: str) -> list:
    PATH: str = fr".\data\helpfiles\{language}"
    files: list = os.listdir(PATH)
    help_list: list = [file_name[:-4]
                       for file_name in files if os.path.isfile(os.path.join(PATH, file_name))]
    return help_list


def delete_file(file_name: str) -> str:
    os.remove(fr".\data\savefiles\{file_name}.csv")
    return f"File: '{file_name}' has been deleted."


def output_file(file_path: str) -> str:
    shutil.copy(file_path, fr".\data\outputfiles\{file_path}.csv")
    return f"File: {file_path} has been copied."


def config_setting(first: str, language: str, password: str) -> str:
    config = configparser.ConfigParser()
    config.read(r".\data\config\config.ini")
    config["User"]["language"] = language
    config["User"]["password"] = password
    config["User"]["first"] = first
    with open(r'.\data\config\config.ini', 'w') as config_file:
        config.write(config_file)
    return "Config file has been successfully edited."
