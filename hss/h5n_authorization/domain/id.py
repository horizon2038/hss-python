class Id():
    def __init__(self, id: str):
        self.__value: str = self.__check_id(id)

    def __check_id(self, id: str):
        if id is None:
            raise Exception("Id is none")
        elif len(id) <= 3:
            raise Exception("Id is out of range")
        else:
            return id

    def get_id(self):
        return self.__value

    def equals(self, target_id: 'Id'):
        return self.get_id() == target_id.get_id()