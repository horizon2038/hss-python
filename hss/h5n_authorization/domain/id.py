class Id():
    def __init__(self, id: str):
        self.__value: str = self.__checkid(id)

    def __checkid(self, id: str):
        if id is None:
            raise Exception
        elif len(id) <= 3:
            raise Exception
        else:
            return id

    def getid(self):
        return self.__value

    def equals(self, targetid: 'Id'):
        if self.__value == targetid.__value:
            return True
        else:
            return False