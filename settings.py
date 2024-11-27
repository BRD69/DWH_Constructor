import os
import sys
from cryptography.fernet import Fernet

PATH_APP = os.getcwd()


class Settings:
    class Platforms:
        linux = ['linux', 'linux2']
        windows = ['win32', ]
        macos = ['darwin', ]

    def __init__(self):
        self._path = PATH_APP
        self.dir_tmp = os.path.join(PATH_APP, 'tmp')
        self.dir_settings = os.path.join(PATH_APP, 'settings')
        self.dir_udata = os.path.join(PATH_APP, 'udata')
        self.screen_width = 1200
        self.screen_height = 800
        self.title = "Конструктор DWH"
        self.platform = sys.platform
        self.secret_key_str = ''
        self.secret_key_byte = b''
        self.test = False

        self.create_dir()
        self.is_test()
        self.load_secret_key()

    def get_size(self):
        return (self.screen_width, self.screen_height)

    def create_dir(self):
        if not os.path.isdir(self.dir_tmp):
            os.mkdir(self.dir_tmp)
        if not os.path.isdir(self.dir_settings):
            os.mkdir(self.dir_settings)
        if not os.path.isdir(self.dir_udata):
            os.mkdir(self.dir_udata)

    def is_test(self):
        # процедура устанавливает тестовый режим
        # сделано для проверки выполнения команд по кнопке RUN
        if os.path.isfile(os.path.join(self.dir_settings, 'test.txt')):
            self.test = True
        else:
            self.test = False

    def load_secret_key(self):
        if os.path.isfile(os.path.join(self.dir_settings, 'sk.key')):
            file_secret = open(os.path.join(self.dir_settings, 'sk.key'), 'r')
            self.secret_key_str = file_secret.read()
            self.secret_key_byte = self.secret_key_str.encode('utf-8')
            file_secret.close()
        else:
            self.save_secret_key()

    def save_secret_key(self):
        with open(os.path.join(self.dir_settings, 'sk.key'), 'w') as file_secret:
            file_secret.write(Fernet.generate_key().decode('utf-8'))
        file_secret.close()
