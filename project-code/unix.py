from file import File
from folder import Folder


class Unix:
    def __init__(self):
        self.root = Folder('root', self)
        self.dirs = []
        self.current: Folder = self.root

    def mkdir(self, folder_name, path: str = None):
        folder = self.path_management(path)
        if folder_name in folder.contents:
            print('folder already exists')
            return
        folder.add_content(folder_name, Folder(folder_name, folder))

    def ls(self, path: str = None):
        folder: Folder = self.path_management(path)
        if folder is None:
            print('No such directory')
            return

        if path is None:
            if self.current.contents:
                folder = self.current
        if folder is None:
            print('No such directory')
            return
        for number, content in enumerate(folder.contents.values()):
            print(content.name, end=f"{" " if number % 10 != 9 else "\n"}")
        if len(folder.contents) % 10 != 0:
            print()

    def cd(self, name='..') -> None:
        if name == '..':
            self.dirs.pop()
            self.current = self.current.parent_folder
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

    def touch(self, file_name, path: str = None):
        folder = self.path_management(path)
        if file_name in folder.contents:
            print('file already exists')
            return
        folder.add_content(file_name, File(file_name))

    def file_commands(self, command: str, path: str, contents: list | str = None, line: int = None):
        folder = self.path_management(path)
        if folder is None:
            print('No such directory')
            return
        file_name = path.split('/').pop()
        if not file_name.endswith('.txt'):
            folder = folder.parent_folder
        if command == 'rm':
            folder.delete_content(file_name)
            return
        file: File = folder.contents.get(file_name, None)
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

    def copy_move_file(self, command: str, source_path: str, destination_path: str) -> None:

        folder = self.path_management(source_path)
        if folder is None:
            print('No such directory')
            return
        file_name = source_path.split('/').pop()
        parent_folder = folder.parent_folder
        destination_folder = self.path_management(destination_path)
        if not destination_folder:
            print('No such directory')
            return
        if not file_name.endswith('.txt'):
            folder_name = file_name
            if folder_name in destination_folder.contents:
                print('folder already exists')
                return
            if command == 'mv':
                if destination_folder in folder.contents.values():
                    print('the destination folder is subfolder of the source folder')
                    return
                parent_folder.delete_content(folder_name)
            destination_folder.add_content(folder_name, Folder(folder_name, folder.contents.copy()))
            return

        if file_name in destination_folder.contents:
            print('file already exists')
            return

        file: File = folder.contents.get(file_name, None)
        if file is None:
            print('No such file')
            return
        if command == 'mv':
            folder.delete_content(file_name)
        destination_folder.add_content(file_name, File(file_name, file.contents.copy()))

    def rename_file_folder(self, path: str, new_name: str) -> None:
        current_folder = self.path_management(path)
        if current_folder is None:
            print('No such directory')
            return
        file_folder_name = path.split('/').pop()
        if not file_folder_name.endswith('.txt'):
            current_folder = current_folder.parent_folder
        file_folder: Folder | File = current_folder.contents.get(file_folder_name, None)
        if file_folder is None:
            print('No such file or directory')
            return
        temp_name = file_folder.name
        file_folder.name = new_name
        current_folder.delete_content(temp_name)
        current_folder.add_content(new_name, file_folder)

    def path_management(self, path: str):
        if path is None:
            return self.current
        path = path.split('/')
        current: Folder = self.current
        if path[0] == '':
            path.pop(0)
            current = self.root
            if not path:
                return current
            if path[-1] == '':
                return current
        if path[-1].endswith('.txt'):
            path.pop()
        for directory in path:
            current = current.contents.get(directory, None)
            if current is None:
                return None
        return current
