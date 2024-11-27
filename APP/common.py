import configparser
import os.path


class SaveLoadConfig:
    def __init__(self, obj_class, save_values, path, file_name):
        self._config = configparser.ConfigParser()
        self.obj_class = obj_class
        self.obj_class_name = obj_class.get_name_class()
        self.save_values = save_values
        self.path = path
        self.file_name = file_name

    def save(self):
        _config_save = {}
        for key, value in self.obj_class.__dict__.items():
            if key in self.save_values:
                _config_save[key] = value
            self._config[self.obj_class_name] = _config_save

        with open(os.path.join(self.path, self.file_name), 'w') as config_file:
            self._config.write(config_file)

    def load(self):
        if os.path.isfile(os.path.join(self.path, self.file_name)):
            self._config.read(os.path.join(self.path, self.file_name))
            for key in self.obj_class.__dict__.keys():
                if key in self.save_values:
                    try:
                        value = self._config.get(self.obj_class_name, key)
                        setattr(self.obj_class, key, value)
                    except configparser.NoOptionError as e:
                        continue
        else:
            self.save()


