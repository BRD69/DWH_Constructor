import configparser
import os


class StringCommand:
    def __init__(self, path):
        self._config = configparser.ConfigParser()
        self._path = path
        self._name_file_config = 'pattern_cmd.ini'
        self._symbol_split = '_&_'
        self._save_load_value = ["start_job",
                                 "start_prod_app",
                                 "stop_prod_app",
                                 "start_prod_wf",
                                 "start_test_wf", ]

        self.option_dmn = "_option_dmn"
        self.option_dis = "_option_dis"
        self.option_app = "_option_app"
        self.option_wf = "_option_wf"
        self.option_ps = "_option_ps"

        self.start_job = ""
        self.start_prod_app = ""
        self.stop_prod_app = ""
        self.start_prod_wf = ""
        self.start_test_wf = ""

        self.prefix_command_option = {
            "_option_dmn": "-DomainName",
            "_option_dis": "-ServiceName",
            "_option_app": "-Application",
            "_option_wf": "-Workflow",
            "_option_ps": "-ParameterSet",
        }

        self.start_job_prefix = {
            "_option_dmn": "-DomainName",
            "_option_dis": "-ServiceName",
            "_option_app": "-Application",
            "_option_wf": "-Workflow",
            "_option_ps": "-ParameterSet",
        }

        self.start_prod_app_prefix = {
            "_option_dmn": "-DomainName",
            "_option_dis": "-ServiceName",
            "_option_app": "-Application",
        }

        self.stop_prod_app_prefix = {
            "_option_dmn": "-DomainName",
            "_option_dis": "-ServiceName",
            "_option_app": "-Application",
        }

        self.start_prod_wf_prefix = {
            "_option_dmn": "-DomainName",
            "_option_dis": "-ServiceName",
            "_option_app": "-Application",
            "_option_wf": "-Workflow",
            "_option_ps": "-ParameterSet",
        }

        self.start_test_wf_prefix = {
            "_option_dmn": "-DomainName",
            "_option_dis": "-ServiceName",
            "_option_app": "-Application",
            "_option_wf": "-Workflow",
            "_option_ps": "-ParameterSet",
        }

        self.load_command()

    def _load_default_commands(self):
        self.start_job = (
            r"C:\SQLAgentJob\IPC\bat\infacmd_proxy.bat",
            f"wfs startWorkflow",
            f"-DomainName {self.option_dmn}",
            f"-ServiceName {self.option_dis}",
            f"-Application {self.option_app}",
            f"-Workflow {self.option_wf}",
            f"-ParameterSet {self.option_ps}",
            f"-Wait true",
        )
        print(self.start_job)
        self.start_prod_app = (
            r"start C:\Informatica\10.4.1\clients\DeveloperClient\infacmd\infacmd.bat",
            f"dis StartApplication",
            f"-DomainName {self.option_dmn}",
            f"-ServiceName {self.option_dis}",
            f"-Application {self.option_app}",
            f"-un ipc_user_p",
            f"-pd ipc725p ",
        )
        self.stop_prod_app = (
            r"start C:\Informatica\10.4.1\clients\DeveloperClient\infacmd\infacmd.bat",
            f"dis StopApplication",
            f"-DomainName {self.option_dmn}",
            f"-ServiceName {self.option_dis}",
            f"-Application {self.option_app}",
            f"-un ipc_user_p",
            f"-pd ipc725p",
        )
        self.start_prod_wf = (
            r"start /b C:\Informatica\10.4.1\clients\DeveloperClient\infacmd\infacmd.bat",
            f"wfs startWorkflow",
            f"-DomainName {self.option_dmn}",
            f"-ServiceName {self.option_dis}",
            f"-Application {self.option_app}",
            f"-Workflow {self.option_wf}",
            f"-ParameterSet {self.option_ps}",
            f"-sdn Native",
            f"-un ipc_user_p",
            f"-pd ipc725p",
            f"-Wait false",
        )
        self.start_test_wf = (
            r"start /b C:\Informatica\10.4.1\clients\DeveloperClient\infacmd\infacmd.bat",
            f"wfs startWorkflow",
            f"-DomainName {self.option_dmn}",
            f"-ServiceName {self.option_dis}",
            f"-Application {self.option_app}",
            f"-Workflow {self.option_wf}",
            f"-ParameterSet {self.option_ps}",
            f"-sdn Native",
            f"-un infa_user",
            f"-pd ipc725",
            f"-Wait false",
        )

    def save_command(self):
        _config_save = {}
        for key, value in self.__dict__.items():
            if key in self._save_load_value:
                _config_save[key] = f'{self._symbol_split}'.join(value)
        self._config[StringCommand.__name__] = _config_save

        with open(os.path.join(self._path, self._name_file_config), 'w') as configfile:
            configfile.write(f'# Символ разрыва: {self._symbol_split}\n')
            configfile.write('# Использовать следующие ключи опции:\n')
            configfile.write('# _option_dmn - DomainName\n')
            configfile.write('# _option_dis - ServiceName\n')
            configfile.write('# _option_app - Application\n')
            configfile.write('# _option_wf - Workflow\n')
            configfile.write('# _option_ps - ParameterSet\n\n')
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
                        _str_command = self._config.get(StringCommand.__name__, key)
                        _value_command = tuple(_str_command.split(self._symbol_split))
                        setattr(self, key, _value_command)
                    except configparser.NoOptionError as e:
                        continue
        else:
            self._load_default_commands()
            self.save_command()


if __name__ == '__main__':
    sc = StringCommand(os.getcwd())
    sc.load_command()
    print(sc.start_job)
