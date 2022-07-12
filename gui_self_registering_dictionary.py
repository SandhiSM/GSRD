# これはGUIの部分
import PySimpleGUI
from Modules import Processor


# 定数定義
FONT: str = "sans-serif"
MENU: list = [PySimpleGUI.Menu([
    ["&Create"],
    ["&Register"],
    ["&Input"],
    ["&Find"],
    ["&Edit"]
    ["&Delete"],
    ["&Help"],
    ["Delete Data"],
    ["&Output"],
    ["&Setting"],
    ["&Terminate"],
    ["Initialize"]
], font=FONT)]
HEADER: list = [PySimpleGUI.T("Select a file.", font=FONT), PySimpleGUI.Spin(Processor.load_data_list(
), readonly=True, font=FONT, tooltip="DATA", k="-DATA-", expand_x=True, expand_y=True)]

# レイアウトの定義
LAYOUT_FIRST: list = [
    [PySimpleGUI.T(
        "First of all, you must create a file to use this app.", font=FONT)],
    [PySimpleGUI.T("Enter the name of the file you want to create.", font=FONT), PySimpleGUI.In(font=FONT, tooltip="FILE NAME",
                                                                                                k="-FILENAMEFIRST-", expand_x=True, expand_y=True)],
    [PySimpleGUI.B("Submit", font=FONT, tooltip="Submit",
                   k="-SUBMITFIRST-", expand_x=True, expand_y=True)]
]
LAYOUT_INTRODUCTION: list = [
    MENU,
    [PySimpleGUI.T("Welcome to GSRD! ", font=FONT)],
    [PySimpleGUI.T("Select a mode from the menu above.", font=FONT)]
]
LAYOUT_PASSWORD: list = [
    [PySimpleGUI.T("Enter password.", font=FONT), PySimpleGUI.In(
        font=FONT, k="-PASSWORDINPUT-", expand_x=True, expand_y=True)],
    [PySimpleGUI.B("Submit", font=FONT, tooltip="Submit",
                   k="-SUBMITPASSWORD-", expand_x=True, expand_y=True)],
]
LAYOUT_CREATE: list = [
    MENU,
    [PySimpleGUI.T("Enter the name of the file you want to create.", font=FONT), PySimpleGUI.In(font=FONT, tooltip="FILE NAME",
                                                                                                k="-FILENAMECREATE-", expand_x=True, expand_y=True)],
    [PySimpleGUI.B("Submit", font=FONT, tooltip="Submit",
                   k="-SUBMITCREATE-", expand_x=True, expand_y=True)],
    [PySimpleGUI.In(font=FONT, tooltip="Result", k="-RESULTCREATE-",
                    readonly=True, expand_x=True, expand_y=True)]
]
LAYOUT_REGISTER: list = [
    MENU,
    HEADER,
    [PySimpleGUI.T("Enter the word you want to register.", font=FONT),
     PySimpleGUI.In(font=FONT, tooltip="WORD", k="-WORDREGISTER-", expand_x=True, expand_y=True)],
    [PySimpleGUI.T("Enter its meaning.", font=FONT),
     PySimpleGUI.In(font=FONT, tooltip="MEANING", k="-MEANINGREGISTER-", expand_x=True, expand_y=True)],
    [PySimpleGUI.B("Submit", font=FONT, k="-SUBMITREGISTER-",
                   tooltip="Submit", expand_x=True, expand_y=True)],
    [PySimpleGUI.In(font=FONT, tooltip="Result", readonly=True,
                    k="-RESULTREGISTER-", expand_x=True, expand_y=True)]
]
LAYOUT_INPUT: list = [
    MENU,
    HEADER,
    [PySimpleGUI.T("Select the path where the data is located.", font=FONT)],
    [PySimpleGUI.FileBrowse(file_types=(("CSV files", "*.csv")),
                            initial_folder=r".\data\inputfiles", font=FONT, k="-FILEPATHINPUT"), PySimpleGUI.In(font=FONT, readonly=True, tooltip="file path", expand_x=True, expand_y=True)],
    [PySimpleGUI.B("Submit", tooltip="Submit", font=FONT,
                   k="-SUBMITINPUT-", expand_x=True, expand_y=True)],
    [PySimpleGUI.In(font=FONT, tooltip="Result", readonly=True,
                    k="-RESULTINPUT-", expand_x=True, expand_y=True)]
]
LAYOUT_FIND: list = [
    MENU,
    HEADER,
    [PySimpleGUI.T("Select mode.", font=FONT),
     PySimpleGUI.R("WORD", group_id="SELECTMODEFIND", default=True, tooltip="Search for words by meaning.", k="-WORDFIND-", font=FONT, expand_x=True, expand_y=True,
                   enable_events=True), PySimpleGUI.R("MEANING", group_id="SELECTMODEFIND", font=FONT, tooltip="Search for a meaning from a word.", k="-MEANINGFIND-", expand_x=True, expand_y=True, enable_events=True),
     PySimpleGUI.R("NUMBER", group_id="SELECTMODEFIND", tooltip="Confirmation of the number of pieces registered in the dictionary.", k="-NUMBERFIND-", font=FONT, expand_x=True, expand_y=True, enable_events=True)],
    [PySimpleGUI.In("Enter meaning of word you want to find.", font=FONT, k="-MESSAGEBRANCHINGFIND-", readonly=True, expand_x=True, expand_y=True),
     PySimpleGUI.In(font=FONT, tooltip="Enter the meaning of the word you want to search for or the word for which you want to search.", k="-WORD|MEANINGFIND-", expand_x=True, expand_y=True)],
    [PySimpleGUI.B("Submit", tooltip="Submit", font=FONT,
                   k="-SUBMITFIND-", expand_x=True, expand_y=True)],
    [PySimpleGUI.In(font=FONT, tooltip="Result", readonly=True,
                    k="-RESULTFIND-", expand_x=True, expand_y=True)]
]
LAYOUT_EDIT: list = [
    MENU,
    HEADER,
    [PySimpleGUI.T("Select mode.", font=FONT),
     PySimpleGUI.R("WORD", group_id="SELECTMODEEDIT", default=True, tooltip="Edit the word.",
                   k="-WORDEDIT-", font=FONT, expand_x=True, expand_y=True, enable_events=True),
     PySimpleGUI.R("MEANING", group_id="SELECTMODEEDIT", tooltip="Edit the meaning.", k="-MEANINGEDIT-", font=FONT, expand_x=True, expand_y=True, enable_events=True)],
    [PySimpleGUI.T("Enter the original word.", font=FONT), PySimpleGUI.In(
        font=FONT, tooltip="Enter the original word.", k="-ORIGINALWORDEDIT-", expand_x=True, expand_y=True)],
    [PySimpleGUI.In("Enter the word.", readonly=True, font=FONT, k="-MESSAGEBRANCHINGEDIT-", expand_x=True, expand_y=True),
     PySimpleGUI.In(font=FONT, tooltip="Enter the word or meaning you want to edit.", k="-WORD|MEANINGEDIT-", expand_x=True, expand_y=True)],
    [PySimpleGUI.B("Submit", tooltip="Submit", font=FONT,
                   k="-SUBMITEDIT-", expand_x=True, expand_y=True)],
    [PySimpleGUI.In(tooltip="Result", font=FONT, readonly=True,
                    k="-RESULTEDIT", expand_x=True, expand_y=True)]
]
LAYOUT_DELETE: list = [
    MENU,
    HEADER,
    [PySimpleGUI.T("Enter the word you want to delete."), PySimpleGUI.In(
        font=FONT, tooltip="Enter the word you want to delete.", k="-WORDDELETE-", expand_x=True, expand_y=True)],
    [PySimpleGUI.B("Submit", tooltip="Submit", font=FONT,
                   k="-SUBMITDELETE-", expand_x=True, expand_y=True)],
    [PySimpleGUI.In(tooltip="Result", readonly=True, font=FONT,
                    k="-RESULTDELETE-", expand_x=True, expand_y=True)]
]
LAYOUT_HELP: list = [
    MENU,
    [PySimpleGUI.T("Which help do you need?", font=FONT)],
    [PySimpleGUI.Spin(Processor.load_help_list(language="en"), readonly=True, k="-HELP-",
                      tooltip="Select help.", font=FONT, expand_x=True, expand_y=True)],
    [PySimpleGUI.B("Submit", tooltip="Submit", font=FONT,
                   k="-SUBMITHELP-", expand_x=True, expand_y=True)],
    [PySimpleGUI.In(tooltip="Result", font=FONT, readonly=True,
                    k="-RESULTHELP-", expand_x=True, expand_y=True)]
]
LAYOUT_DELETE_DATA: list = [
    MENU,
    [PySimpleGUI.T("Which data do you want to delete?", font=FONT)],
    [PySimpleGUI.Spin(Processor.load_data_list(), readonly=True, k="-DELETEDATA-",
                      tooltip="Select data.", font=FONT, expand_x=True, expand_y=True)],
    [PySimpleGUI.B("Submit", tooltip="Submit", font=FONT,
                   k="-SUBMITDELETEDATA-", expand_x=True, expand_y=True)],
    [PySimpleGUI.In(font=FONT, tooltip="Result", readonly=True,
                    k="-RESULTDELETEDATA-", expand_x=True, expand_y=True)]
]
LAYOUT_OUTPUT: list = [
    MENU,
    HEADER,
    [PySimpleGUI.T("Select a file for the output.", font=FONT)],
    [PySimpleGUI.FileBrowse(file_types=(
        ("CSV files", "*.csv")), initial_folder=r".\data\savefiles", font=FONT, k="-FILEOUTPUT-"), PySimpleGUI.In(font=FONT, tooltip="Full path", readonly=True, expand_x=True, expand_y=True)]
    [PySimpleGUI.B("Submit", font=FONT, tooltip="Submit",
                   k="-SUBMITOUTPUT-", expand_x=True, expand_y=True)],
    [PySimpleGUI.In(tooltip="Result", font=FONT, readonly=True,
                    k="-RESULTOUTPUT-", expand_x=True, expand_y=True)]
]
LAYOUT_SETTING: list = [
    MENU,
    [PySimpleGUI.T("Select language.", font=FONT), PySimpleGUI.Radio("English", group_id="LANGUAGE", default=True, font=FONT,
                                                                     k="-ENGLISHSETTING-"), PySimpleGUI.Radio("Japanese", group_id="LANGUAGE", font=FONT, k="-JAPANESESETTING-")],
    [PySimpleGUI.T(
        "If you wanted to set a password, please enter it.", font=FONT), PySimpleGUI.In(font=FONT, tooltip="Password", k="-PASSWORDSETTING-", password_char='*', expand_x=True, expand_y=True)],
    [PySimpleGUI.B("Submit", tooltip="Submit", font=FONT,
                   k="-SUBMITSETTING-", expand_x=True, expand_y=True)],
    [PySimpleGUI.In(tooltip="Result", readonly=True, font=FONT,
                    k="-RESULTSETTING-", expand_x=True, expand_y=True)]
]
LAYOUT_TERMINATE: list = [
    MENU,
    [PySimpleGUI.T(
        "Press the button below to exit this application.", font=FONT)],
    [PySimpleGUI.B("Terminate", tooltip="Exit this app.", font=FONT,
                   k="-TERMINATE-", expand_x=True, expand_y=True)]
]
LAYOUT_INITIALIZE: list = [
    MENU,
    [PySimpleGUI.T("INITIALIZE", font=FONT)],
    [PySimpleGUI.B("INITIALIZE", tooltip="INITIALIZE", font=FONT,
                   k="-INITIALIZE-", expand_x=True, expand_y=True)]
]

# ウィンドウの定義
WINDOW_FIRST: PySimpleGUI.Window = PySimpleGUI.Window(
    "GSRD: FIRST", layout=LAYOUT_FIRST, font=FONT, no_titlebar=True, finalize=True, grab_anywhere=True)
WINDOW_INTRODUCTION: PySimpleGUI.Window = PySimpleGUI.Window(
    "GSRD: INTRODUCTION", layout=LAYOUT_INTRODUCTION, font=FONT, no_titlebar=True, finalize=True, grab_anywhere=True)
WINDOW_PASSWORD: PySimpleGUI.Window = PySimpleGUI.Window(
    "GSRD: PASSWORD", layout=LAYOUT_PASSWORD, font=FONT, no_titlebar=True, finalize=True, grab_anywhere=True)
WINDOW_CREATE: PySimpleGUI.Window = PySimpleGUI.Window(
    "GSRD: CREATE", layout=LAYOUT_CREATE, font=FONT, no_titlebar=True, finalize=True, grab_anywhere=True)
WINDOW_REGISTER: PySimpleGUI.Window = PySimpleGUI.Window(
    "GSRD: REGISTER", layout=LAYOUT_REGISTER, font=FONT, no_titlebar=True, finalize=True, grab_anywhere=True)
WINDOW_INPUT: PySimpleGUI.Window = PySimpleGUI.Window(
    "GSRD: INPUT", layout=LAYOUT_INPUT, font=FONT, no_titlebar=True, finalize=True, grab_anywhere=True)
WINDOW_FIND: PySimpleGUI.Window = PySimpleGUI.Window(
    "GSRD: FIND", layout=LAYOUT_FIND, font=FONT, no_titlebar=True, finalize=True, grab_anywhere=True)
WINDOW_EDIT: PySimpleGUI.Window = PySimpleGUI.Window(
    "GSRD: EDIT", layout=LAYOUT_EDIT, font=FONT, no_titlebar=True, finalize=True, grab_anywhere=True)
WINDOW_DELETE: PySimpleGUI.Window = PySimpleGUI.Window(
    "GSRD: DELETE", layout=LAYOUT_DELETE, font=FONT, no_titlebar=True, finalize=True, grab_anywhere=True)
WINDOW_HELP: PySimpleGUI.Window = PySimpleGUI.Window(
    "GSRD: HELP", layout=LAYOUT_HELP, font=FONT, no_titlebar=True, finalize=True, grab_anywhere=True)
WINDOW_DELETE_DATA: PySimpleGUI.Window = PySimpleGUI.Window(
    "GSRD: DELETE DATA", layout=LAYOUT_DELETE_DATA, font=FONT, no_titlebar=True, finalize=True, grab_anywhere=True)
WINDOW_OUTPUT: PySimpleGUI.Window = PySimpleGUI.Window(
    "GSRD: OUTPUT", layout=LAYOUT_OUTPUT, font=FONT, no_titlebar=True, finalize=True, grab_anywhere=True)
WINDOW_SETTING: PySimpleGUI.Window = PySimpleGUI.Window(
    "GSRD: SETTING", layout=LAYOUT_SETTING, font=FONT, no_titlebar=True, finalize=True, grab_anywhere=True)
WINDOW_TERMINATE: PySimpleGUI.Window = PySimpleGUI.Window(
    "GSRD: TERMINATE", layout=LAYOUT_TERMINATE, font=FONT, no_titlebar=True, finalize=True, grab_anywhere=True)
WINDOW_INITIALIZE: PySimpleGUI.Window = PySimpleGUI.Window(
    "GSRD: INITIALIZE", layout=LAYOUT_INITIALIZE, font=FONT, no_titlebar=True, finalize=True, grab_anywhere=True)


# 画面遷移用の関数
def windows_change(remain_window: PySimpleGUI.Window) -> None:
    WINDOW_FIRST.hide()
    WINDOW_INTRODUCTION.hide()
    WINDOW_PASSWORD.hide()
    WINDOW_CREATE.hide()
    WINDOW_REGISTER.hide()
    WINDOW_INPUT.hide()
    WINDOW_FIND.hide()
    WINDOW_EDIT.hide()
    WINDOW_DELETE.hide()
    WINDOW_HELP.hide()
    WINDOW_DELETE_DATA.hide()
    WINDOW_OUTPUT.hide()
    WINDOW_SETTING.hide()
    WINDOW_TERMINATE.hide()
    WINDOW_INITIALIZE.hide()
    remain_window.un_hide()


# 例外を処理するため関数にしておく
def gui_self_registering_dictionary():
    language, password, first = Processor.activate()
    running: bool = True
    initial: bool = True
    while running:
        window, event, values = PySimpleGUI.read_all_windows()
        if initial:
            if first == "True":
                Processor.config_set(language='en', password='None')
                windows_change(remain_window=WINDOW_FIRST)
            elif password != 'None':
                windows_change(remain_window=WINDOW_PASSWORD)
            else:
                windows_change(remain_window=WINDOW_INTRODUCTION)
        else:
            match event:
                case "Create":
                    windows_change(remain_window=WINDOW_CREATE)
                case "Register":
                    windows_change(remain_window=WINDOW_REGISTER)
                case "Input":
                    windows_change(remain_window=WINDOW_INPUT)
                case "Find":
                    windows_change(remain_window=WINDOW_FIND)
                case "Edit":
                    windows_change(remain_window=WINDOW_EDIT)
                case "Delete":
                    windows_change(remain_window=WINDOW_DELETE)
                case "Help":
                    windows_change(remain_window=WINDOW_HELP)
                case "Delete Data":
                    windows_change(remain_window=WINDOW_DELETE_DATA)
                case "Output":
                    windows_change(remain_window=WINDOW_OUTPUT)
                case "Setting":
                    windows_change(remain_window=WINDOW_SETTING)
                case "Terminate":
                    windows_change(remain_window=WINDOW_TERMINATE)
                case "Initialize":
                    windows_change(remain_window=WINDOW_INITIALIZE)
                case "-SUBMITFIRST-":
                    if values["-FILENAMEFIRST-"] != '':
                        result = Processor.create_data(
                            values["-FILENAMEFIRST-"])
                        PySimpleGUI.popup(result, title="Success!",
                                          font=FONT, keep_on_top=True)
                        windows_change(remain_window=WINDOW_INTRODUCTION)
                    else:
                        PySimpleGUI.popup("ERROR: You must enter file name.",
                                          title="ERROR!", keep_on_top=True, font=FONT)
                case "-SUBMITPASSWORD-":
                    if values["-PASSWORDINPUT-"] == password:
                        PySimpleGUI.popup("Authentication Success.",
                                          title="Success!", font=FONT, keep_on_top=True)
                        windows_change(remain_window=WINDOW_INTRODUCTION)
                    else:
                        PySimpleGUI.popup("It is wrong password.",
                                          title="Error!", font=FONT, keep_on_top=True)
                case "-SUBMITCREATE-":
                    if values["-FILENAMECREATE-"] == '':
                        window["-RESULTCREATE-"].update("Enter the file name!")
                    else:
                        result = Processor.create_data(
                            values["-FILENAMECREATE-"])
                        window["-RESULTCREATE-"].update(result)
                case "-SUBMITREGISTER-":
                    result = Processor.register(
                        file_name=values["-DATA-"], word=values["-WORDREGISTER-"], meaning=values["-MEANINGREGISTER-"])
                    window["-RESULTREGISTER-"].update(result)
                    window["-WORDREGISTER-"].update('')
                    window["-MEANINGREGISTER-"].update('')
                case "-SUBMITINPUT-":
                    if values["-FILEPATHINPUT-"] == r".\data\inputfiles":
                        window["-RESULTINPUT-"].update(
                            "Specify the source of the data to be imported.")
                    else:
                        result = Processor.data_input(
                            file_name=values["-DATA-"], input_file_path=values["-FILEPATHINPUT-"])
                        window["-RESULTINPUT-"].update(result)
                case "-WORDFIND-":
                    window["-MESSAGEBRANCHINGFIND-"].update(
                        "Enter the meaning of the word you want to find.")
                case "-MEANINGFIND-":
                    window["-MESSAGEBRANCHINGFIND-"].update(
                        "Enter the word of meaning you want to find.")
                case "-NUMBERFIND-":
                    window["-WORD|MEANINGFIND-"].update(disabled=True)
                case "-SUBMITFIND-":
                    if values["-WORD|MEANINGFIND-"] == '':
                        window["-RESULTFIND-"].update(
                            "You must enter word or meaning.")
                    else:
                        if values["-WORDFIND-"]:
                            result = Processor.find(
                                file_name=values["-DATA-"], mode="word", find_key=values["-WORD|MEANINGFIND-"])
                            window["-RESULTFIND-"].update(result)
                        else:
                            result = Processor.find(
                                file_name=values["-DATA-"], mode="meaning", find_key=values["-WORD|MEANINGFIND-"])
                            window["-RESULTFIND-"].update(result)
                case "-SUBMITEDIT-":
                    if values["-ORIGINALWORDEDIT-"] == '' or values["-WORD|MEANINGEDIT-"] == '':
                        window["-RESULTEDIT-"].update(
                            "You must enter word or meaning.")
                    else:
                        if values["-WORDEDIT-"]:
                            result = Processor.edit(
                                file_name=values["-DATA-"], mode="word", original_word=values["-ORIGINALWORDEDIT-"], word_or_meaning=values["-WORD|MEANINGEDIT-"])
                            window["-RESULTEDIT-"].update(result)
                        else:
                            result = Processor.edit(
                                file_name=values["-DATA-"], mode="meaning", original_word=values["-ORIGINALWORDEDIT-"], word_or_meaning=values["WORD|MEANINGEDIT-"])
                            window["-RESULTEDIT-"].update(result)
                case "-SUBMITDELETE-":
                    if values["-WORDDELETE-"] == '':
                        window["-RESULTDELETE-"].update(
                            "Enter a word you want to delete.")
                    else:
                        confirm = PySimpleGUI.popup_yes_no(
                            "Do you really want to delete it?", title="confirm", font=FONT, keep_on_top=True)
                        if confirm == "yes":
                            result = Processor.delete(
                                file_name=values["-DATA-"], word=values["-WORDDELETE-"])
                            window["-RESULTDELETE-"].update(result)
                        else:
                            window["-RESULTDELETE-"].update("Canceled.")
                case "-SUBMITHELP-":
                    result = Processor.help(
                        mode=values["-HELP-"], language=language)
                    window["-RESULTHELP-"].update(result)
                case "-SUBMITDELETEDATA-":
                    confirm = PySimpleGUI.popup_yes_no(
                        "Do you really want to delete it?", title="confirm", font=FONT, keep_on_top=True)
                    if confirm == "yes":
                        result = Processor.delete_data(
                            file_name=values["-DELETEDATA-"])
                        window["-RESULTDELETEDATA-"].update(result)
                    else:
                        window["-RESULTDELETEDATA-"].update("Canceled.")
                case "-SUBMITOUTPUT-":
                    if values["-FILEOUTPUT-"] == r".\data\savefiles":
                        window["-RESULTOUTPUT-"].update("Select file.")
                    else:
                        result = Processor.data_output(
                            file_path=values["-FILEOUTPUT-"])
                        window["-RESULTOUTPUT-"].update(result)
                case "-SUBMITSETTING":
                    if values["-PASSWORDSETTING-"] == '':
                        if values["-ENGLISHSETTING-"]:
                            result = Processor.config_set(
                                language="en", password="None")
                            window["-RESULTSETTING-"].update(result)
                        else:
                            result = Processor.config_set(
                                language="ja", password="None")
                            window["-RESULTSETTING-"].update(result)
                    else:
                        password_confirm = PySimpleGUI.popup_get_text(
                            "Retype password", title="confirm", password_char='*')
                        if password_confirm == values["-PASSWORDSETTING-"]:
                            if values["-ENGLISHSETTING-"]:
                                result = Processor.config_set(
                                    language="en", password=values["-PASSWORDSETTING-"])
                                window["-RESULTSETTING-"].update(result)
                            else:
                                result = Processor.config_set(
                                    language="ja", password=values["-PASSWORDSETTING-"])
                                window["-RESULTSETTING-"].update(result)
                        else:
                            window["-RESULTSETTING-"].update(
                                "The first and second inputs are different.")
                case "-TERMINATE-":
                    running = False
                case "-INITIALIZE":
                    confirm = PySimpleGUI.popup_yes_no(
                        "Do you really want to initialize this app?", title="confirm", font=FONT, keep_on_top=True)
                    if confirm == "yes":
                        Processor.initialize()
                        PySimpleGUI.popup(
                            "Initialized.", title="Success!", font=FONT, keep_on_top=True)
                        windows_change(remain_window=WINDOW_FIRST)
                    else:
                        PySimpleGUI.popup(
                            "Canceled.", title="Canceled.", font=FONT, keep_on_top=True)


# 例外処理
if __name__ == "__main__":
    try:
        gui_self_registering_dictionary()
    except Exception:
        Processor.error()
