from group import Group


class Kafedra:

    __list_group = []

    # region init
    def __init__(self, name: str, abbriviatur: str, info: str):
        Kafedra.__chek_info(name)
        Kafedra.__chek_info(abbriviatur)
        Kafedra.__chek_info(info)

        self.name = Kafedra.__chek_info(name)
        self.__abbriviatur = Kafedra.__chek_info(abbriviatur)
        self.__info = Kafedra.__chek_info(info)
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

    def list_group_add(self,group = None):
        if group is None:
            '''
            метод может принимать объекты группы, если пустой инициализация происходить внутри
            '''
        self.__list_group.append(group)
        print(f'{group.name} группа добавлена на кафедру  ')


    def list_group_update(self,group):
        '''
        метод  принимает объекты класса группы
        '''
        pass



    def list_group_delete(self,group):
        '''
        метод  принимает объекты класса группы
        '''
        self.__list_group.remove(group)
        print(f'{group.name} группа удалена с кафедры  ')

        pass

    def list_group_show(self):
        print(self.__list_group[0])
    #endregion



k = Kafedra('mex', 'mexmat', 'it')
group = Group('111','mex','gggg')

k.list_group_add(group)
k.list_group_show()
