from file import File
from folder import Folder
class Unix:
    def __init__(self):
        self.root = Folder('root')
        self.dirs = []
        self.current:Folder = self.root


    def mkdir(self, folder_name, path:str=None):
        if path is None:
            self.current.add_content(folder_name, Folder(folder_name))
            return
        path = path.split('/')

        current:Folder = self.root
        for directory in path:
            current = current.contents.get(directory, None)
            if current is None:
                print('No such directory')
                return
        if folder_name in current.contents:
            print('Folder already exists')
            return
        current.contents[folder_name] = Folder(folder_name)

    def ls(self):
        if self.current.contents:
            for number, content in enumerate(self.current.contents.values()):
                print(content.name, end=f"{" " if number % 10 != 9 else "\n"}")
            if len(self.current.contents) % 10 != 0:
                print()

    def cd(self, name='..')->None:
        if name == '..':
            self.dirs.pop()
            self.current = self.root
            for directory in self.dirs:
                self.current = self.current.contents.get(directory.name, None)
            return
        former_current = self.current
        self.current = self.current.contents.get(name, self.current)
        if self.current.name != name:
            print('No such directory')
            return
        if former_current == self.current:
            print('No such file or directory')
            return
        self.dirs.append(self.current)


    def touch(self, file_name, path:str=None):
        if path is None:
            self.current.contents[file_name] = File(file_name)
            return
        path = path.split('/')
        current: Folder = self.root
        for directory in path:
            current = current.contents.get(directory, None)
            if current is None:
                print('No such directory')
                return
        if file_name in current.contents:
            print('File already exists')
            return
        current.contents[file_name] = File(file_name)

    def file_commands(self,command:str, path:str, contents:list | str=None, line:int=None):
        path = path.split('/')
        file_name = path.pop()
        current:Folder = self.root
        for directory in path:
            current = current.contents.get(directory, None)
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

    def copy_move_file(self,command:str, source_path:str, destination_path:str)->None:
        source_path = source_path.split('/')
        source_path.pop(0)
        file_name = source_path.pop()
        current: Folder = self.root
        for directory in source_path:
            current = current.contents.get(directory, None)
            if current is None:
                print('No such directory')
                return
        file: File = current.contents.get(file_name, None)
        if file is None:
            print('No such file')
            return
        if command == 'mv':
            del current.contents[file_name]
        destination_path = destination_path.split('/')
        destination_path.pop(0)
        current: Folder = self.root
        for directory in destination_path:
            if directory == '':
                continue
            current = current.contents.get(directory, None)
            if current is None:
                print('No such directory')
        current.contents[file_name] = File(file_name, file.contents)

    def rename_file_folder(self, path:str, new_name:str)->None:
        path = path.split('/')
        current:Folder = self.root
        file_folder_name = path.pop()
        for directory in path:
            current = current.contents.get(directory, None)
            if current is None:
                print('No such directory')
                return
        file_folder:Folder | File = current.contents.get(file_folder_name, None)
        if file_folder is None:
            print('No such file or directory')
            return
        file_folder.name = new_name







