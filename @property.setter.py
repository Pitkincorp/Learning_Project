class Square:
    def __init__(self,a):
        self.__side= a
        self.__perim= None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self,a):
        self.__side = a
        self.__perim = None

    @property
    def perim(self):
        if self.__perim is None:
            print('Calculate perim')
            self.__perim = self.side*4
        return self.__perim