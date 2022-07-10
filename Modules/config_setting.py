# 設定変更内部処理
import configparser


def setting(language="en", password="None", first="False") -> str:
    config = configparser.ConfigParser()
    config["User"]["language"] = language
    config["password"] = password
    config["first"] = first
    with open(r'.\data\config\config.ini', 'w') as config_file:
        config.write(config_file)
    return "Config file has been successfully edited."
