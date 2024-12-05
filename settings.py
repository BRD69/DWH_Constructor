import getpass
import os
import sys
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode

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
        self.user = getpass.getuser()
        self.hash_key = ''
        self.secret_key = ''
        self.test = False

        self.create_dir()
        self.is_test()
        self.load_secret_key()

    @staticmethod
    def remove_non_alphanumeric(text):
        return ''.join(char for char in text if char.isalnum())

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

    def _secret_key(self):
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=self.user.encode('utf-8'),
            iterations=100000,
            backend=default_backend()
        )
        self.secret_key = urlsafe_b64encode(kdf.derive(self.hash_key.encode('utf-8')))

    def load_secret_key(self):
        if os.path.isfile(os.path.join(self.dir_settings, 'sk.key')):
            file_secret = open(os.path.join(self.dir_settings, 'sk.key'), 'r')
            self.user = getpass.getuser()
            # self.user = 'Test.User'
            self.hash_key = file_secret.read()
            self._secret_key()
            file_secret.close()
        else:
            self.save_secret_key()

    def save_secret_key(self):
        with open(os.path.join(self.dir_settings, 'sk.key'), 'w') as file_secret:
            file_secret.write(Fernet.generate_key().decode('utf-8'))
        file_secret.close()
