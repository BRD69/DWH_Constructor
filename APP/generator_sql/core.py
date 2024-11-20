class Transliterator:
    def __init__(self):
        self.cyrillic = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
        self.latin = 'a|b|v|g|d|e|e|zh|z|i|i|k|l|m|n|o|p|r|s|t|u|f|kh|tc|ch|sh|shch||y||e|iu|ia'.split('|')

    # №1
    def get_tranlit(self, text):
        trantab = {k: v for k, v in zip(self.cyrillic, self.latin)}
        new_text = ''
        for ch in text:
            casefunc = str.capitalize if ch.isupper() else str.lower
            new_text += casefunc(trantab.get(ch.lower(), ch))
        return new_text


class PredefinedValues:
    scope_values = ('aero', 'blps', 'btmn', 'lgst', 'lubr', 'mbun')
    type_values = ('dim', 'fct')

    def __init__(self):
        self.scope_values = PredefinedValues.scope_values
        self.type_values = PredefinedValues.type_values


class ColumnFieldValues:
    def __init__(self, length, precision, scale, is_nullable, is_key, default_value):
        self.length = length
        self.precision = precision
        self.scale = scale
        self.is_nullable = is_nullable
        self.is_key = is_key
        self.default_value = default_value

    @staticmethod
    def default():
        return ColumnFieldValues(
            length='4000',
            precision='null',
            scale='null',
            is_nullable=2,
            is_key=0,
            default_value='null'
        )


class ValuesDataType:
    """
    Класс Значения типов поля data_type в TableSQLDataObjectColumn
    """

    def __init__(self):
        self.bigint = 'bigint'
        self.bit = 'bit'
        self.datetime2 = 'datetime2'
        self.decimal = 'decimal'
        self.int = 'int'
        self.nvarchar = 'nvarchar'
        self.time = 'time'
        self.uniqueidentifier = 'uniqueidentifier'

    def get_values(self):
        return tuple(self.__dict__.values())

    @staticmethod
    def get_default_value():
        return 'bigint'

    @staticmethod
    def get_values_type(type_str):
        if type_str in ['bigint', 'bit', 'datetime2', 'decimal', 'int', 'time', 'uniqueidentifier']:
            return ColumnFieldValues(length='null', precision='null', scale='null', is_nullable=2, is_key=0,
                                     default_value='null')
        elif type_str == 'nvarchar':
            return ColumnFieldValues(length='4000', precision='null', scale='null', is_nullable=2, is_key=0,
                                     default_value='null')
        else:
            return ColumnFieldValues.default()


class TableSQLDataObject:
    """
    Класс data.object
    """

    def __init__(self):
        self.scope = PredefinedValues.scope_values[0]
        self.object = ""
        self.type = PredefinedValues.type_values[0]
        self.source_system = ""
        self.source_type = ""
        self.domain = ""
        self.template = "base"
        self.dmt_view_source = "ods"
        self.comment = ""

    @staticmethod
    def get_scopes():
        return PredefinedValues.scope_values

    @staticmethod
    def get_types():
        return PredefinedValues.type_values

    def get_file_name(self):
        return f"{self.scope}_{self.source_system}_{self.object}"


class TableSQLDataObjectColumn:
    """
    Класс data.object_column
    """

    def __init__(self):
        self.column_name = ""
        self.data_type = ValuesDataType.get_default_value()
        self.length = ""
        self.precision = ""
        self.scale = ""
        self.is_nullable = 2
        self.is_key = 0
        self.default_value = ""
        self.source_name = ""
        self.description = ""
        self.comment = ""

        self.set_value_columns()

    def __str__(self):
        return str(self.__dict__)

    def get_columns(self):
        return tuple(self.__dict__.keys())

    def set_value_columns(self):
        values_data_type = ValuesDataType.get_values_type(self.data_type)
        for key, val in values_data_type.__dict__.items():
            setattr(self, key, val)

    def set_value_data_type(self, data_type_value):
        self.data_type = data_type_value
        self.set_value_columns()

    @staticmethod
    def get_values_data_type():
        return ValuesDataType().get_values()

    @staticmethod
    def get_values_type(type_str):
        return ValuesDataType.get_values_type(type_str)


if __name__ == '__main__':
    print(__name__)
