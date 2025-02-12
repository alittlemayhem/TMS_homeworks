import json
import os


class DataStorage:

    file = None

    def __init__(self, __path = None, content = None):
        self.status: str = 'disconnected'
        self.content: str = content
        self.__path: str = __path

    def _create_storage(self, __path, file):
        if os.path.exists(__path):
            file = open(__path, 'r')
        return file

    def connect(self, file):
        file = json.load(self.__path)
        self.status = 'connected'
        if os.path.exists(self.__path):
            self.content = file.read()
        else:
            self._create_storage(self.__path)

    def disconnect(self, file):
        file.close()
        print("File is closed!")


# TODO
class DataStorageWrite(DataStorage):
    def connect(self):
        pass

    def _create_storage(self):
        pass

    def append(self):
        pass