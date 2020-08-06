import pickle

class FileLoader:

    def __init__(self):
        pass

    def save(self, obj):
        pass

    def load(self):
        pass


class PickleLoader(FileLoader):

    def save(self, obj):
      pickle.dump(obj, "saved_object.pickle")

    def load(self):
        return pickle.load("saved_object.pickle")


class TextLoader(FileLoader):

    def save(self, obj):
        # Write save in some other way
        pass


class User:

    def __init__(self, loader):
        self.loader = loader

    def foo(self):
        # Do stuff
        a = [1, 2, 3]
        self.loader.save(a)


user = User(PickleLoader())
user.foo()
