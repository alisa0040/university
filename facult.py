
from kafedra import Kafedra

class Facult():
    __list_kafedres = []

    # region init
    def __init__(self, name: str, abbriviatur: str, info: str):
        Facult.__chek_info(name)
        Facult.__chek_info(abbriviatur)
        Facult.__chek_info(info)

        self.__name = Facult.__chek_info(name)
        self.__abbriviatur = Facult.__chek_info(abbriviatur)
        self.__info = Facult.__chek_info(info)
    #endregion
    # region info
    @classmethod
    def __chek_info(cls, str_chek: str) -> str:
        while not (type(str_chek) == str and str_chek.isalpha()):
            str_chek = input('введите новую иформацию')
        else:
            return str_chek.lower()
    #endregion
    #region CRUD
    def list_kafedres_add(self, kafedres =None):
        if kafedres is None:
            '''
            метод может принимать объекты группы, если пустой инициализация происходить внутри
            '''
        self.__list_kafedres.append(kafedres)
        print(f'{kafedres.name} кафедра добавлена на факультет  ')

    def list_kafedres_update(self,kafedres):
        '''
        метод  принимает объекты класса группы
        '''
        pass

    def list_kafedres_delete(self, kafedres):
        '''
        метод  принимает объекты класса группы
        '''
        self.__list_kafedres.remove(kafedres)
        print(f'{kafedres.name} кафедра удалена с факультета  ')

    def list_kafedres_show(self):
        print(self.__list_kafedres[0])
    # endregion

k = Facult('mex', 'mexmat', 'it')
kafedra = Kafedra('мехмат','mexmat','it')

k.list_kafedres_add(kafedra)
