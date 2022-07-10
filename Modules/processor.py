# これは関数(メソッド)集
import functions


def load_data_list() -> list:
    return functions.data_list()


def load_data(file_name: str) -> list:  # データの読み込み
    try:
        data: list = functions.csv_load(file_name)
    except FileNotFoundError:
        return []
    else:
        return data


def activate() -> str:  # 起動の際の設定確認
    language, password, first: str = functions.config_load()
    if language != "en" or language != "ja":
        language = "en"
    return language, password, first


def create_data(file_name: str) -> str:  # データの作成
    functions.csv_write(file_name, [])
    return f"'{file_name}' has been successfully created,"


def register(file_name: str, word: str, meanings: list) -> str:  # 登録
    if word == '' or meanings == []:
        return "You must input not less than one word and one meaning."
    else:
        data: list = load_data(file_name)
        if find(file_name=file_name, mode="word", findkey=f'{word}') != f"There are no words registered for '{word}.'":
            return f"'{word}' has already been registered."
        else:
            newdata: list = [word]
            if len(meanings) == 1:
                meanings.append('')
            for meaning in meanings:
                newdata.append(meaning)
            data.append(word, newdata)
            return f"'{word}' has been successfully registered."


def data_input(file_name: str, new_data_path: str) -> list:  # 一括登録
    data: list = load_data(file_name)
    newdata: list = functions.csv_load(new_data_path)
    if newdata == []:
        return "There is no such file."
    else:
        for datum in newdata:
            if type(datum[1]) != list:
                return "It is invalid data."
            else:
                if len(datum[1]) == 1:
                    datum[1].append('')
                data.append(datum)
        functions.csv_write(file_name, data)
        return "Data all has been input."


def find(file_name: str, mode: str, find_key: str = None) -> str:  # 確認
    data: list = load_data(file_name)
    match mode:
        case "word":
            for datum in data:
                for meaning in datum[1]:
                    if meaning == find_key:
                        return datum[0]
                    else:
                        pass
            else:
                return f"There are no words registered for '{find_key}.'"
        case "meaning":
            for datum in data:
                if datum[0] == find_key:
                    return datum[1][0], datum[1][1]
                else:
                    pass
            else:
                return f"There are no meanings registered for '{find_key}.'"
        case "number":
            return f"{str(len(data))}pcs."


def edit(file_name: str, mode: str, original_word: str, word_or_meanings: list) -> str:  # 編集
    data: list = load_data(file_name)
    original: str = find(file_name, mode="word", find_key=f'{original_word}')
    if original == f"There are no words registered for '{original_word}.'":
        return f"{original_word} has not been registered."
    else:
        match mode:
            case "word":
                for count, datum in enumerate(data, 0):
                    if datum[0] == original_word:
                        index: int = count
                        data[index][0] = ''.join(word_or_meanings)
                        return f"Edited following: BEFORE -> '{original_word}', AFTER -> '{''.join(word_or_meanings)}'"
                    else:
                        pass
            case "meaning":
                for count, datum in enumerate(data, 0):
                    if datum[0] == original_word:
                        index: int = count
                        old_meaning: list = data[index][1]
                        data[index][1] = word_or_meanings
                        return f"Edited following: BEFORE -> '{old_meaning}', AFTER -> '{word_or_meanings}'"
                    else:
                        pass


def delete(file_name: str, word: str) -> str:  # 削除
    data: list = load_data(file_name)
    delete: str = find(file_name, mode="word", find_key=f'{word}')
    if delete == f"There are no words registered for '{word}.'":
        return f"'{word}' has not been registered."
    else:
        data.remove(word)
        return f"'{word}' has been deleted."


def help(mode: str) -> str:  # ヘルプ
    return functions.help_file_load(mode)


def delete_data(file_name: str) -> str:  # データの削除
    return functions.delete_file(file_name)


def data_output(file_name: str) -> str:  # データ出力
    return functions.output_file(file_name)
