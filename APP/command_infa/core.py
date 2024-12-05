import configparser
import os
from cryptography.fernet import Fernet

from APP.common import SaveLoadConfig
from settings import Settings


class ModeButton:
    run = 'run'
    view = 'view'
    copy = 'copy'


class SettingsCMD:
    def __init__(self, path):
        self._settings = Settings()
        self._path = path
        self._name_file_config = 'settings_cmd.ini'
        self._save_load_value = ["path_sql_agent",
                                 "path_informatica",
                                 "user_test",
                                 "password_test",
                                 "user_prod",
                                 "password_prod",
                                 "link_adm_infa_test",
                                 "link_adm_infa_prod",
                                 ]
        self._saver_loader = None

        self.path_sql_agent = ''
        self.path_informatica = ''
        self.user_test = self._settings.user
        self.password_test = ''
        self.user_prod = self._settings.user
        self.password_prod = ''
        self.link_adm_infa_test = 'https://spb99-etl-blt:8443/administrator/'
        self.link_adm_infa_prod = 'https://spb99-etl-blp:8443/administrator/'

        self.load_command()

    def get_encrypted_text(self, text):
        try:
            if text:
                cipher = Fernet(self._settings.secret_key)
                text_byte = bytes(text, 'utf-8')
                encrypted_text = cipher.encrypt(text_byte)
                return encrypted_text.decode('utf-8')
            else:
                return ''
        except Exception as e:
            print(str(e))
            return 'Error pass'

    def get_decrypted_text(self, text):
        try:
            if text:
                cipher = Fernet(self._settings.secret_key)
                text_byte = bytes(text, 'utf-8')
                decrypted_text = cipher.decrypt(text_byte)
                return decrypted_text.decode('utf-8')
            else:
                return ''
        except Exception as e:
            print(str(e))
            return 'Error pass'

    def set_path_sql_agent(self, value):
        self.path_sql_agent = value

    def set_path_informatica(self, value):
        self.path_informatica = value

    def set_user_test(self, value):
        self.user_test = value

    def set_password_test(self, value):
        self.password_test = self.get_encrypted_text(value)

    def set_user_prod(self, value):
        self.user_prod = value

    def set_password_prod(self, value):
        self.password_prod = self.get_encrypted_text(value)

    def get_path_sql_agent(self):
        return self.path_sql_agent

    def get_path_informatica(self):
        return self.path_informatica

    def get_user_test(self):
        return self.user_test

    def get_password_test(self):
        return self.get_decrypted_text(self.password_test)

    def get_user_prod(self):
        return self.user_prod

    def get_password_prod(self):
        return self.get_decrypted_text(self.password_prod)

    def get_link_adm_infa_test(self):
        return self.link_adm_infa_test

    def get_link_adm_infa_prod(self):
        return self.link_adm_infa_prod

    def get_name_class(self):
        return SettingsCMD.__name__

    def save_command(self):
        self._saver_loader = SaveLoadConfig(
            obj_class=self,
            save_values=self._save_load_value,
            path=self._path,
            file_name=self._name_file_config,
        )
        self._saver_loader.save()

    def load_command(self):
        self._saver_loader = SaveLoadConfig(
            obj_class=self,
            save_values=self._save_load_value,
            path=self._path,
            file_name=self._name_file_config,
        )
        self._saver_loader.load()

    def clear_command(self):
        self.path_sql_agent = ''
        self.path_informatica = ''
        self.user_test = ''
        self.password_test = ''
        self.user_prod = ''
        self.password_prod = ''
        self.save_command()
        self.load_command()


class TemplatesCMD:
    def __init__(self, path):
        self._config = configparser.ConfigParser()
        self._path = path
        self._name_file_config = 'template_cmd.ini'
        self._symbol_split = '#'
        self._save_load_value = ["sql_agent_job",
                                 "application",
                                 "workflow", ]

        self.option_path_sql_agent = '_option_path_sql_agent'
        self.option_path_informatica = '_option_path_informatica'
        self.option_start_stop_app = '_option_start_stop_app'
        self.option_dmn = "_option_dmn"
        self.option_dis = "_option_dis"
        self.option_app = "_option_app"
        self.option_wf = "_option_wf"
        self.option_ps = "_option_ps"
        self.option_user_name = "_option_user_name"
        self.option_user_pass = "_option_user_pass"
        self.option_wait = '_option_wait'

        self.sql_agent_job = ""
        self.application = ""
        self.workflow = ""

        self.load_command()

    def _load_default_commands(self):
        self.sql_agent_job = (
            f"{self.option_path_sql_agent}",
            f"wfs startWorkflow",
            f"-DomainName {self.option_dmn}",
            f"-ServiceName {self.option_dis}",
            f"-Application {self.option_app}",
            f"-Workflow {self.option_wf}",
            f"-ParameterSet {self.option_ps}",
            f"-Wait {self.option_wait}",
        )
        self.application = (
            f"start {self.option_path_informatica}",
            f"dis {self.option_start_stop_app}Application",
            f"-DomainName {self.option_dmn}",
            f"-ServiceName {self.option_dis}",
            f"-Application {self.option_app}",
            f"-SecurityDomain GAZPROM-NEFT.LOCAL",
            f"-UserName {self.option_user_name}",
            f"-Password {self.option_user_pass} ",
            f"-Wait {self.option_wait}",
        )
        self.workflow = (
            f"start /b {self.option_path_informatica}",
            f"wfs startWorkflow",
            f"-DomainName {self.option_dmn}",
            f"-ServiceName {self.option_dis}",
            f"-Application {self.option_app}",
            f"-Workflow {self.option_wf}",
            f"-ParameterSet {self.option_ps}",
            f"-SecurityDomain GAZPROM-NEFT.LOCAL",
            f"-UserName {self.option_user_name}",
            f"-Password {self.option_user_pass}",
            f"-Wait {self.option_wait}",
        )

    def save_command(self):
        _config_save = {}
        for key, value in self.__dict__.items():
            if key in self._save_load_value:
                _config_save[key] = f'{self._symbol_split}'.join(value)
        self._config[TemplatesCMD.__name__] = _config_save

        with open(os.path.join(self._path, self._name_file_config), 'w') as configfile:
            configfile.write(f'# Символ разрыва: {self._symbol_split}\n')
            configfile.write('# Использовать следующие ключи опции:\n')
            configfile.write('# _option_path_sql_agent - Путь SQL Agent\n')
            configfile.write('# _option_path_informatica - Путь Infomatica\n')
            configfile.write('# _option_start_stop_app - Start или Stop Application\n')
            configfile.write('# _option_dmn - DomainName\n')
            configfile.write('# _option_dis - ServiceName\n')
            configfile.write('# _option_app - Application\n')
            configfile.write('# _option_wf - Workflow\n')
            configfile.write('# _option_ps - ParameterSet\n')
            configfile.write('# _option_wait - Запуск приложения с ожиданием его завершения\n\n')
            self._config.write(configfile)

    def reset_command(self):
        self._load_default_commands()
        self.save_command()

    def load_command(self):
        if os.path.isfile(os.path.join(self._path, self._name_file_config)):
            self._config.read(os.path.join(self._path, self._name_file_config))
            for key, value in self.__dict__.items():
                if key in self._save_load_value:
                    try:
                        _str_command = self._config.get(TemplatesCMD.__name__, key)
                        _value_command = tuple(_str_command.split(self._symbol_split))
                        setattr(self, key, _value_command)
                    except configparser.NoOptionError as e:
                        continue
        else:
            self._load_default_commands()
            self.save_command()


if __name__ == '__main__':
    sc = TemplatesCMD(os.getcwd())
    sc.load_command()
