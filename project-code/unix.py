from file import File
from folder import Folder
class Unix:
    def __init__(self):
        self.root = Folder('root')
        self.dirs = []
        self.current:Folder = self.root


    def mkdir(self, folder_name, path:str=None):
        if path is None:
            self.current.contents[folder_name] = Folder(folder_name)
            return
        path = path.split('/')
        current:Folder = self.current
        for directory in path:
            current = self.root.contents.get(directory, None)
            if current is None:
                print('No such directory')
                return
        current.contents[folder_name] = Folder(folder_name)



    def cd(self, name='..')->None:
        if name == '..':
            if self.current:
                self.dirs.pop()
                self.current = None
                for directory in self.dirs:
                    self.current = directory

        # if name in self.current.contents.keys():
        #     self.current = self.current.contents[name]
        self.current = self.current.contents.get(name, self.current)
        if self.current.name != name:
            print('No such directory')


    def touch(self, file_name, path:str=None):
        if path is None:
            self.current.contents[file_name] = File(file_name)
            return
        path = path.split('/')
        current: Folder = self.current
        for directory in path:
            current = self.root.contents.get(directory, None)
            if current is None:
                print('No such directory')
                return
        current.contents[file_name] = File(file_name)

    # def rm(self, path:str):
    #     path = path.split('/')
    #     file_name = path.pop()
    #     current:Folder = self.current
    #     for directory in path:
    #         current = self.root.contents.get(directory, None)
    #         if current is None:
    #             print('No such directory')
    #             return
    #     del current.contents[file_name]

    # def nwfiletxt(self, command, path:str, contents:list):
    #     path = path.split('/')
    #     file_name = path.pop()
    #     current:Folder = self.current
    #     for directory in path:
    #         current = self.root.contents.get(directory, None)
    #         if current is None:
    #             print('No such directory')
    #             return
    #
    #     file:File = current.contents.get(file_name, None)
    #     if file is None:
    #         print('no such file')
    #         return
    #     file.nwfiletxt_command(contents)
    #
    # def appendtxt(self, path:str, contents:list):
    #     path = path.split('/')
    #     file_name = path.pop()
    #     current:Folder = self.current
    #     for directory in path:
    #         current = self.root.contents.get(directory, None)
    #         if current is None:
    #             print('No such directory')
    #             return
    #
    #     file:File = current.contents.get(file_name, None)
    #     if file is None:
    #         print('no such file')
    #         return
    #     file.appendtxt_command(contents)

    def file_commands(self,command:str, path:str, contents:(list,str), line:int=None):
        path = path.split('/')
        file_name = path.pop()
        current:Folder = self.current
        for directory in path:
            current = self.root.contents.get(directory, None)
            if current is None:
                print('No such directory')
                return
        if command == 'rm':
            del current.contents[file_name]
            return
        file:File = current.contents.get(file_name, None)
        if file is None:
            print('no such file')
            return
        match command:
            case 'nwfiletxt':
                file.nwfiletxt_command(contents)
            case 'appendtxt':
                file.appendtxt_command(contents)
            case 'editline':
                file.editline_command(contents, line)
            case 'deline':
                file.deline_command(line)
            case 'cat':
                file.cat_command()






