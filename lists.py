if __name__ == '__main__':
    N = int(input())
    list = []
    for _ in range(N):
        command = input()
        if 'insert' in command:
            command = command.split(' ')
            list.insert(int(command[1]), int(command[2]))
        elif 'append' in command:
            command = command.split(' ')
            list.append(int(command[1]))
        elif 'print' in command:
            print(list)
        elif 'remove' in command:
            command = command.split(' ')
            list.remove(int(command[1]))
        elif 'sort' in command:
            list.sort()
        elif 'reverse' in command:
            list.reverse()
        elif 'pop' in command:
            list.pop()
