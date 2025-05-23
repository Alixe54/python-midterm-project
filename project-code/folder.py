from file import File


class Folder:
    def __init__(self, name, parent_folder, contents: dict = None):
        self.name = name
        self.contents = contents if contents is not None else {}
        self.parent_folder: Folder = parent_folder

    def add_content(self, name, content):
        self.contents[name] = self.copy_folder_item(name, content)

    def delete_content(self, name):
        del self.contents[name]

    def copy_folder_item(self, name, file_folder):
        if isinstance(file_folder, File):
            return File(name, file_folder.contents.copy())
        folder = Folder(name, self)
        for content in file_folder.contents.values():
            if isinstance(content, File):
                folder.contents[content.name] = File(content.name, content.contents.copy())
            elif isinstance(content, Folder):
                folder.contents[content.name] = self.copy_folder_item(content.name, content)
        return folder
