from unix import Unix
unix = Unix()
command = ""
while command != "exit":
    command = input(f"/{"/" if unix.dirs else ""}{"/".join([directory.name for directory in unix.dirs])}/$").split()
    match command[0]:
        case 'mkdir':
            name = command[1]
            path = ""
            try:
                path = command[2]
            except IndexError:
                path = None
            unix.mkdir(name, path)
        case 'ls':
            unix.ls()
        case 'cd':
            name = command[1]
            unix.cd(name)

        case 'touch':
            name = command[1]
            path = None
            try:
                path = command[2]
            except IndexError:
                path = None
            if not name.endswith('.txt'):
                print('file extension must be .txt')
                continue
            unix.touch(name, path)
        case 'nwfiletxt':
            path = command[1]
            print('enter the lines(/end/means done)')
            content = input()
            contents = []
            while content != "/end/":
                contents.append(content)
                content = input()
            unix.file_commands('nwfiletxt', path, contents)
        case 'appendtxt':
            path = command[1]
            print('enter the lines(/end/means done)')
            content = input()
            contents = []
            while content != "/end/":
                contents.append(content)
                content = input()
            unix.file_commands('appendtxt', path, contents)
        case 'editline':
            path = command[1]
            line = int(command[2])
            edited_content = input()
            unix.file_commands('editline', path, edited_content, line)
        case 'cat':
            path = command[1]
            unix.file_commands('cat',path)
        case 'cp':
            source = command[1]
            destination = command[2]
            unix.copy_move_file('cp', source, destination)
        case 'mv':
            source = command[1]
            destination = command[2]
            unix.copy_move_file('mv', source, destination)
        case 'rename':
            path = command[1]
            name = command[2]
            unix.rename_file_folder(path, name)
