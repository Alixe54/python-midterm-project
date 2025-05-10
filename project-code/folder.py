class Folder:
    def __init__(self, name, root: list= None):
        self.name = name
        self.contents = {}
        # self.root = root

    def add_content(self, name, content):
        self.contents[name] = content

    def navigate_in(self, name):
        if name not in self.contents:
            print('there is no such directory')
            return
        self.root.append(name)

    def navigate_out(self, name='..'):
        pass

    def search_content(self, name=None):
        for name in self.contents:
            pass

