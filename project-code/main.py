from unix import Unix
import pickle


def load_data():
    try:
        with open('project-code\\unix-data\\unix_data.bin', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return Unix()


def save_data(data):
    with open('project-code\\unix-data\\unix_data.bin', 'wb') as f:
        pickle.dump(data, f)


def main():
    unix = load_data()
    unix.current = unix.root
    unix.dirs.clear()
    supported_commands = ['mkdir', 'rm', 'touch', 'cd', 'nwfiletxt', 'appendtxt',
                          'editline', 'deline', 'cat', 'mv', 'cp', 'rename', 'ls']
    while True:

        command = input(f"/{"/" if unix.dirs else ""}{"/".join([directory.name for directory in unix.dirs])}/$").split()
        try:
            match command[0]:
                case 'mkdir':
                    try:
                        path = command[1]
                        name = command[2]
                    except IndexError:
                        name = command[1]
                        path = None

                    unix.mkdir(name, path)
                case 'ls':
                    try:
                        path = command[1]
                    except IndexError:
                        path = None
                    unix.ls(path)
                case 'cd':
                    try:
                        path = command[1]
                    except IndexError:
                        path = '..'
                    unix.cd(path)

                case 'touch':
                    try:
                        path = command[1]
                        name = command[2]
                    except IndexError:
                        name = command[1]
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
                    try:
                        line = int(command[2])
                    except ValueError:
                        print('first enter the path')
                        continue
                    edited_content = command[3]
                    unix.file_commands('editline', path, edited_content, line)
                case 'deline':
                    path = command[1]
                    try:
                        line = int(command[2])
                    except ValueError:
                        print('first enter the path')
                        continue
                    unix.file_commands('deline', path, line=line)
                case 'cat':
                    path = command[1]
                    unix.file_commands('cat', path)
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
                case 'rm':
                    path = command[1]
                    unix.file_commands('rm', path)
                case 'help':
                    for number, command_ in enumerate(supported_commands):
                        print(command_, end=f"\t{" " if number % 8 != 7 else "\n"}")
                    print()
                case 'exit':
                    break
                case _:
                    print(f'Unsupported command: {command[0]}')
        except IndexError:
            continue
        save_data(unix)


if __name__ == "__main__":
    main()
