# これは内部処理関数集
import functions


def load_data_list() -> list:
    return functions.data_list()


def load_data(file_name: str) -> list:  # データの読み込み
    try:
        data = functions.csv_load(file_name)
    except FileNotFoundError:
        return []
    else:
        return data


def register(file_name: str, word: str, meanings: list) -> str:  # 登録
    if word == '' or meanings == []:
        return 'You must input not less than one word and one meaning.'
    else:
        data: list = load_data(file_name)
        if find(file_name=file_name, mode='word', findkey=f'{word}') != f'There are no words registered for {word}.':
            return f'"{word}" has already been registered.'
        else:
            newdata = [word]
            for meaning in meanings:
                newdata.append(meaning)
            data.append(word, newdata)
            return 'Success!'


def data_input(file_name: str, new_data_path: str) -> list:  # 一括登録
    data = load_data(file_name)
    newdata = functions.csv_load(new_data_path)
    if newdata == []:
        return 'There is no such file.'
    else:
        for datum in newdata:
            data.append(datum)
        functions.csv_write(file_name, data)
        return 'Success!'


def find(file_name: str, mode: str, find_key: str) -> str:  # 確認
    data: list = load_data(file_name)
    match mode:
        case 'word':
            for datum in data:
                for meaning in datum[1]:
                    if meaning == find_key:
                        return datum[0]
                    else:
                        pass
            else:
                return f'There are no words registered for {find_key}.'
        case 'meaning':
            for datum in data:
                if datum[0] == find_key:
                    return datum[1][0], datum[1][1]
                else:
                    pass
            else:
                return f'There are no meanings registered for {find_key}.'
        case 'number':
            return str(len(data)) + 'pcs.'


def edit(file_name: str, mode: str, word: str, meanings: list):  # 編集
    data = load_data(file_name)
    match mode:
        case 'word':
            pass
        case 'meaning':
            pass


def delete():
    pass


def help(mode: str) -> str:
    pass


def delete_data(file_name: str) -> str:
    pass


def data_output(file_path: str) -> str:
    pass
