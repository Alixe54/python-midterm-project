class File:
    def __init__(self, name, contents:list[str] = None):
        self.name = name
        self.contents = contents if contents is not None else []

    def nwfiletxt_command(self, contents: list) -> None:
        self.contents.clear()
        for content in contents:
            self.contents.append(content)

    def appendtxt_command(self, contents: list) -> None:
        for content in contents:
            self.contents.append(content)

    def editline_command(self, content: str, line: int) -> None:
        for i in range(len(self.contents)):
            if i + 1 == line:
                self.contents[i] = content
                return
        print('index out of range')

    def deline_command(self, line: int) -> None:
        for i in range(len(self.contents)):
            if i + 1 == line:
                self.contents.pop(i)
                return
        print('index out of range')

    def cat_command(self) -> None:
        for content in self.contents:
            print(content)


    def rename_command(self, name: str) -> None:
        self.name = name

