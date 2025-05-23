class File:
    def __init__(self, name, contents:list[str] = None, parent = None):
        if not name.endswith(".txt"):
            raise ValueError("file name must end with .txt")
        self.name = name
        self.contents = contents if contents is not None else []
        self.parent = parent

    def nwfiletxt_command(self, contents: list) -> None:
        self.contents.clear()
        for content in contents:
            self.contents.append(content)

    def appendtxt_command(self, contents: list) -> None:
        for content in contents:
            self.contents.append(content)

    def editline_command(self, content: str, line: int) -> None:
        if 1 <= line <= len(self.contents):
            self.contents[line - 1] = content
        else:
            raise IndexError("Line number out of range.")

    def deline_command(self, line: int) -> None:
        if 1 <= line <= len(self.contents):
            self.contents.pop(line - 1)
        else:
            raise IndexError("Line number out of range.")

    def cat_command(self) -> None:
        for content in self.contents:
            print(content)


    def rename_command(self, name: str) -> None:
        if not name.endswith(".txt"):
            raise ValueError("File name must end with .txt")
        self.name = name


   def __str__(self) -> str:
       return f"<File {self.name} - {len(self.contents)} lines>"
