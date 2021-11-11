# Module created by @Bleu-No / Bleu#7728

from datetime import datetime
from colorama import Fore, Style
from re import search
from time import time
from inspect import getfullargspec

class Blue:

    def __init__(self, filePath, fileName):
        self.start = time()
        self.fake_variables_array = ['printl']
        self.logs = []

        self.variables = {}

        self.imports = {}
        self.data = {}
        self.init_ = 0

        self.filePath = filePath
        self.content = None
        self.fileName = fileName

        self.options = {
            "bloque_request": False,
            "save_logs": False,
            "create_code": False
        }

        self.debug(f'{Fore.GREEN}INFO{Style.RESET_ALL}', 'Welcome to Blue Mysterium made by Bleu#7728 (v1.0) !')

        self.settings()

        print('\n\n')
        self.debug(f'{Fore.GREEN}INFO{Style.RESET_ALL}', 'Starting debug...')

        self.reading_file()
        self.define_fake_variables_and_function({
            "print": "printl"
        })
        self.execute_file()
        self.finding_variables()

        if self.options['save_logs'] == True:
            self.save_logs()

        if self.options['create_code'] == True:
            self.create_source_code()

        print('\n')

        self.end = time()
        self.debug(f'{Fore.BLUE}FINISH{Style.RESET_ALL}', f'Finish to debug file "{Fore.YELLOW}{self.fileName}{Style.RESET_ALL}" ! Time: {Fore.RED}{str(self.end - self.start)[slice(3)]}s{Style.RESET_ALL}.')

    def add_logs(self, text):
        if self.options['save_logs'] == False:
            return

        now = datetime.now().timetuple()
        self.logs.append(
            f'#SOURCE CODE [{now.tm_hour}:{now.tm_min}:{now.tm_sec}] {text}\n'
        )

    def debug(self, type, value, a=False) -> str:
        now = datetime.now().timetuple()
        return print(f'~{Fore.RED}{now.tm_hour}:{now.tm_min}:{now.tm_sec}{Style.RESET_ALL}{Fore.MAGENTA}~{Style.RESET_ALL} > {type} < {Fore.MAGENTA}<-->{Style.RESET_ALL} {Fore.YELLOW}{value}{Style.RESET_ALL}')

    def question_options(self, text, option):
        op = input(str(text)).lower()
        if op in ["y", "n"]:
            self.options[option] = True if op == "y" else False
        else:
            print(f'{Fore.RED}[ERROR] Invalid option !{Style.RESET_ALL}')
            exit()

    def settings(self):
        self.question_options(
            f'[{Fore.CYAN}QUESTION{Style.RESET_ALL}]{Fore.YELLOW} Do you want to block the requests? (Y/N) {Style.RESET_ALL}',
            'bloque_request'
        )
        self.question_options(
            f'[{Fore.CYAN}QUESTION{Style.RESET_ALL}]{Fore.YELLOW} Do you want to save the logs? (Y/N) {Style.RESET_ALL}',
            'save_logs'
        )
        self.question_options(
            f'[{Fore.CYAN}QUESTION{Style.RESET_ALL}]{Fore.YELLOW} Do you want the software to try to recreate the code? (Y/N) {Style.RESET_ALL}',
            'create_code'
        )

    def reading_file(self):
        self.debug(f'{Fore.GREEN}INFO{Style.RESET_ALL}', 'Opening and reading file...')

        with open(self.filePath, 'rb') as f:
            self.content = f.read().decode('latin-1')
            f.close()

    def define_fake_variables_and_function(self, v_name):
        self.debug(f'{Fore.GREEN}INFO{Style.RESET_ALL}', 'Defining fake variables and functions...')

        fake_variables = "";

        for name in v_name:
            fake_variables += f'{name}={v_name[name]};'

        self.content = f'{fake_variables}\n\n{self.content}';

    def finding_variables(self):
        print("\n")
        for name in self.variables:
            if "<function" in str(self.variables[name]):
                name_function_s = search(r"^<(function) ([a-zA-Z0-9]*) (at) ([a-zA-Z0-9]*)>$", str(self.variables[name]))
                name_function = name_function_s.group(2)
                code_function = name_function_s.group(4)
                if name_function in self.fake_variables_array:
                    continue
                
                self.data[self.init_] = {
                    'type': 'function',
                    'data': {
                        'name': name_function,
                        'code': code_function,
                    }
                }
                self.init_ += 1

                self.debug(f'{Fore.RED}DEBUG{Style.RESET_ALL}', f'{Fore.CYAN}VARIABLE_FUNCTION{Style.RESET_ALL}: {str(self.variables[name])} || {Fore.LIGHTMAGENTA_EX}NAME{Style.RESET_ALL}: {name}')
                self.add_logs(f'VARIABLE_FUNCTION: {str(self.variables[name])} || NAME: {name}\ndef {name}():\n\treturn')
            elif "<module" in str(self.variables[name]):
                match_import = search(r"^<(module) '([a-zA-Z0-9]*)' (from) '([a-zA-Z0-9:\\.]*)'>$", str(self.variables[name]))
                name_import = match_import.group(2)
                path_import = match_import.group(4)
                self.debug(f'{Fore.RED}DEBUG{Style.RESET_ALL}', f'{Fore.CYAN}IMPORT_FUNCTION{Style.RESET_ALL}: {name_import} || {Fore.LIGHTMAGENTA_EX}PATH{Style.RESET_ALL}: {path_import}')
                self.add_logs(f'IMPORT_FUNCTION: {name_import} || PATH: {path_import}\nimport {name_import}')
                self.imports[name_import] = path_import
            else:
                content_variable = str(f'{str(self.variables[name])[slice(4)]}... ({len(str(self.variables[name]))-4} characters)').replace("\n", "")
                
                if type(self.variables[name]) is bool or type(self.variables[name]) is int or type(self.variables[name]) is list:
                    self.add_logs(f'VARIABLE: {name} || CODE: {name} = "{content_variable}"; || VALUE: {content_variable}\n{name} = {self.variables[name]};')
                elif type(self.variables[name]) is str:
                    if len(self.variables[name]) > 10:
                        self.add_logs(f'VARIABLE: {name} || CODE: {name} = "{content_variable}"; || VALUE: {content_variable}\n{name} = """{self.variables[name]}""";')
                    else:
                        self.add_logs(f'VARIABLE: {name} || CODE: {name} = "{content_variable}"; || VALUE: {content_variable}\n{name} = "{self.variables[name]}";')
                else:
                    self.add_logs(f'VARIABLE: {name} || CODE: {name} = "{content_variable}"; || VALUE: {content_variable}\n{name} = "{self.variables[name]}";')

                self.data[self.init_] = {
                    'type': 'variable',
                    'data': {
                        'name': name,
                        'content': self.variables[name],
                    }
                }
                self.init_ += 1
                self.debug(f'{Fore.RED}DEBUG{Style.RESET_ALL}', f'{Fore.CYAN}VARIABLE{Style.RESET_ALL}: {name} || {Fore.LIGHTMAGENTA_EX}CODE{Style.RESET_ALL}: {name} = "{content_variable}"; || {Fore.GREEN}VALUE{Style.RESET_ALL}: {content_variable}', True)

    def execute_file(self):
        self.debug(f'{Fore.GREEN}INFO{Style.RESET_ALL}', 'Executing file and loading functions...')

        self.debug(f'{Fore.LIGHTYELLOW_EX}MODULE{Style.RESET_ALL}', 'Loading simple function...')

        global printl
        def printl(text):
            self.add_logs(f'FAKE_FUNCTION: print || CODE: print("{text}"); || VALUE: {text}\nprint("{text}");')
            self.data[self.init_] = {'type': 'fake_function','data': {'code': f'print("{text}");'}}
            self.init_ += 1
            return self.debug(f'{Fore.RED}DEBUG{Style.RESET_ALL}', f'{Fore.CYAN}FAKE_FUNCTION{Style.RESET_ALL}: print || {Fore.LIGHTMAGENTA_EX}CODE{Style.RESET_ALL}: print("{text}"); || {Fore.GREEN}VALUE{Style.RESET_ALL}: {text}')

        print('\n\n')
        exec(self.content, globals(), self.variables)

    def save_logs(self):
        print('\n')
        self.debug(f'{Fore.MAGENTA}LOGS{Style.RESET_ALL}', f'Saving logs... ( {len(self.logs)} log(s) )')

        with open(f'{self.fileName}_logs_{time()}.py', 'w') as f:
            for name in self.logs:
                f.write(f'{name}\n')
            f.close()

    def create_source_code(self):
        with open(f'{self.fileName}_debug.py', 'w') as f:
            for name_import in self.imports:
                f.write(f'import {name_import}\n')
            f.write('\n')

            for x in self.data:
                if self.data[x]['type'] == 'function':
                    print(getfullargspec(self.data[x]["data"]["name"]))
                    f.write(f'def {str(self.data[x]["data"]["name"])}(): \n\treturn\n\n')
                elif self.data[x]['type'] == 'variable':
                    if type(self.data[x]['data']['content']) is str:
                        if len(self.data[x]['data']['content']) > 10:
                            f.write(f'{self.data[x]["data"]["name"]} = """{self.data[x]["data"]["content"]}""";\n')
                        else:
                            f.write(f"{self.data[x]['data']['name']} = \"{self.data[x]['data']['content']}\";\n")
                    elif type(self.data[x]['data']['content']) is bool or type(self.data[x]['data']['content']) is int or type(self.data[x]['data']['content']) is list:
                        f.write(f"{self.data[x]['data']['name']} = {self.data[x]['data']['content']};\n")
                    else:
                        f.write(f"{self.data[x]['data']['name']} = \"{self.data[x]['data']['content']}\";\n")
                elif self.data[x]['type'] == "fake_function":
                    f.write(f'{self.data[x]["data"]["code"]}\n\n')
