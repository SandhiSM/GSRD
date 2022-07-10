# これは関数(メソッド)集
from Modules import functions


def error() -> None:  # 例外処理
    functions.error_log()


def activate() -> str:  # 起動の際の設定確認
    language, password, first = functions.config_load()
    if language != "en" or language != "ja":
        language = "en"
    return language, password, first


def load_data_list() -> list:  # 登録されているデータの一覧を表示
    return functions.data_list()


def create_data(file_name: str) -> str:  # データの作成
    data_list: list = load_data_list()
    if file_name not in data_list:
        functions.csv_write(file_name, [])
        return f"'{file_name}' has been successfully created,"
    else:
        return f"'{file_name}' has been successfully created."


def register(file_name: str, word: str, meanings: str) -> str:  # 登録
    if word == '' or meanings == '':
        return "You must input not less than one word and one meaning."
    else:
        data: list = load_data(file_name)
        if find(file_name=file_name, mode="confirm", find_key=f'{word}') != 'N':
            return f"'{word}' has already been registered."
        else:
            newdata: list = [word, meanings]
            data.append(newdata)
            functions.csv_write(file_name, data)
            return f"'{word}' has been successfully registered."


def data_input(file_name: str, input_file_name: str) -> list:  # 一括登録
    data: list = load_data(file_name)
    newdata: list = functions.csv_input(input_file_name)
    for datum in newdata:
        if type(datum[0]) != str or type(datum[1]) != str:
            return "It is invalid data."
        elif find(file_name, mode='confirm', find_key=f'{datum[0]}') != 'N':
            continue
        else:
            data += [datum]
    functions.csv_write(file_name, data)
    return "Data all has been input."


def find(file_name: str, mode: str, find_key: str = None) -> str:  # 確認
    data: list = load_data(file_name)
    match mode:
        case "word":
            for datum in data:
                if datum[1] == find_key:
                    return datum[0]
                else:
                    pass
                if datum[1] == find_key:
                    return datum[0]
                else:
                    pass
            else:
                return f"There are no words registered for '{find_key}.'"
        case "meaning":
            for datum in data:
                if datum[0] == find_key:
                    return datum[1]
                else:
                    pass
            else:
                return f"There are no meanings registered for '{find_key}.'"
        case "number":
            return f"{str(len(data))}pcs."
        case "confirm":
            for datum in data:
                if datum[0] == find_key:
                    return f'{find_key} has already registered.'
                else:
                    pass
            else:
                return 'N'


def edit(file_name: str, mode: str, original_word: str, word_or_meanings: str) -> str:  # 編集
    data: list = load_data(file_name)
    if find(file_name, mode="confirm", find_key=f'{original_word}') == 'N':
        return f"{original_word} has not been registered."
    else:
        match mode:
            case "word":
                for index, datum in enumerate(data, 0):
                    if datum[0] == original_word:
                        data[index][0] = word_or_meanings
                        functions.csv_write(file_name, data)
                        return f"Edited following: BEFORE -> '{original_word}', AFTER -> '{word_or_meanings}'"
                    else:
                        pass
            case "meaning":
                for index, datum in enumerate(data, 0):
                    if datum[0] == original_word:
                        old_meaning: list = data[index][1]
                        data[index][1] = word_or_meanings
                        functions.csv_write(file_name, data)
                        return f"Edited following: BEFORE -> '{old_meaning}', AFTER -> '{word_or_meanings}'"
                    else:
                        pass


def delete(file_name: str, word: str) -> str:  # 削除
    data: list = load_data(file_name)
    if find(file_name, mode="confirm", find_key=f'{word}') == 'N':
        return f"'{word}' has not been registered."
    else:
        for index, datum in enumerate(data, 0):
            if datum[0] == word:
                del data[index]
                functions.csv_write(file_name, data)
                return f"'{word}' has been deleted."
            else:
                pass


def help(mode: str, language: str) -> str:  # ヘルプ
    return functions.help_file_load(mode, language)


def delete_data(file_name: str) -> str:  # データの削除
    return functions.delete_file(file_name)


def data_output(file_name: str) -> str:  # データ出力
    return functions.output_file(file_name)


def load_data(file_name: str) -> list:  # データの読み込み, この関数集内でしか使用されない
    data: list = functions.csv_load(file_name)
    return data
