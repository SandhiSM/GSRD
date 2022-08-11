# これは内部処理関数(インターナルメソッド)集
import csv
import datetime
import os
import shutil
import configparser
import traceback


ENC = "UTF-8"


def config_load() -> str:
    loader: configparser.ConfigParser = configparser.ConfigParser()
    loader.read(r".\data\config\config.ini")
    return loader["User"]["language"], loader["User"]["password"], loader["User"]["first"], loader["User"]["stoppage"]


def error_log() -> None:
    error: str = traceback.format_exc()
    time: str = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
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


def config_setting(first: str, language: str, password: str, stoppage: str) -> str:
    config = configparser.ConfigParser()
    config.read(r".\data\config\config.ini")
    config["User"]["language"] = language
    config["User"]["password"] = password
    config["User"]["first"] = first
    config["User"]["stoppage"] = stoppage
    with open(r'.\data\config\config.ini', 'w') as config_file:
        config.write(config_file)
    return "Settings are applied at the next startup."


def time() -> str:
    return datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')


def calc_stoppage(last_time: str, current_time: str) -> int:
    last_year, last_month, last_day, last_hour, last_minute = int(last_time[0:4]), int(
        last_time[5:7]), int(last_time[8:10]), int(last_time[11:13]), int(last_time[14:16])
    current_year, current_month, current_day, current_hour, current_minute = int(current_time[0:4]), int(
        current_time[5:7]), int(current_time[8:10]), int(current_time[11:13]), int(current_time[14:16])
    if current_year - last_year == 0:
        if current_month - last_month == 0:
            if current_day - last_day == 0:
                if current_hour - last_hour == 0:
                    return current_minute - last_minute
                else:
                    return 5
            else:
                return 5
        else:
            return 5
    else:
        return 5
