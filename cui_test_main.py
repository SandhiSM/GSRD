# GUI実装前の内部関数の動作確認用プログラム
from Modules import processor

TEST_FILE_NAME = "test3"
try:
    language, password, first = processor.activate()  # これはGUIアプリケーション上で使う変数なのでここでは無視
    data_list = processor.load_data_list()
    output_create = processor.create_data(TEST_FILE_NAME)
    output_register1 = processor.register(
        TEST_FILE_NAME, 'test0', 'テスト0')
    output_register2 = processor.register(TEST_FILE_NAME, 'test1', 'テスト1')
    output_register3 = processor.register(TEST_FILE_NAME, 'test0', 'かぶり')
    output_input = processor.data_input(
        file_name=TEST_FILE_NAME, input_file_name='test4')
    output_find1 = processor.find(TEST_FILE_NAME, mode='word', find_key='テスト1')
    output_find2 = processor.find(
        TEST_FILE_NAME, mode='word', find_key='見つからないよ')
    output_find3 = processor.find(
        TEST_FILE_NAME, mode='meaning', find_key='test0')
    output_find4 = processor.find(
        TEST_FILE_NAME, mode='meaning', find_key='ないよ')
    output_edit1 = processor.edit(
        TEST_FILE_NAME, mode='word', original_word='test1', word_or_meanings='テスト1')
    output_edit2 = processor.edit(
        TEST_FILE_NAME, mode='word', original_word='ないよ', word_or_meanings='ない')
    output_edit3 = processor.edit(TEST_FILE_NAME, mode='meaning',
                                  original_word='test0', word_or_meanings='てすと0')
    output_edit4 = processor.edit(
        TEST_FILE_NAME, mode='meaning', original_word='ない', word_or_meanings='ないからね')
    output_delete1 = processor.delete(TEST_FILE_NAME, 'test2')
    output_delete2 = processor.delete(TEST_FILE_NAME, 'ないから')
    # 面倒なのでhelpはパス
    output_output = processor.data_output(TEST_FILE_NAME)
    output_data_delete = processor.delete_data(TEST_FILE_NAME)
except Exception:
    processor.error()
else:
    print(language, password, first, data_list, output_create, output_register1, output_register2, output_register3, output_input, output_find1, output_find2,
          output_find3, output_find4, output_edit1, output_edit2, output_edit3, output_edit4, output_delete1, output_delete2, output_output, output_data_delete, sep='\n')

# 成功した
