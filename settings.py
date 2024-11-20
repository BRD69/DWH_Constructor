import os

PATH_APP = os.getcwd()


class Settings:
    def __init__(self):
        self._path = PATH_APP
        self.dir_tmp = os.path.join(PATH_APP, 'tmp')
        self.screen_width = 1200
        self.screen_height = 800
        self.title = "Конструктор DWH"

        self.create_dir()

    def get_size(self):
        return (self.screen_width, self.screen_height)

    def create_dir(self):
        if not os.path.isdir(self.dir_tmp):
            os.mkdir(self.dir_tmp)
