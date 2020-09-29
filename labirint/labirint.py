labirint = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['#', '#', '#', '#', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '.', '#', '#', '#', '#'],
    ['#', '.', '#', '.', '#', '#', '#', '#'],
    ['#', '.', '#', '.', '#', '#', '#', '#'],
    ['#', '.', '#', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '#', '.', '#'],
    ['.', '.', '.', '#', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#'],
]
steps = []
a = 1
b = -1
start = labirint[a][b]
# a = int(input('vertical: '))
# b = int(input('gorizontal: '))
point = labirint
go_left = 'point'
while True:
    tupik = 0
    exit_point = 0
    while go_left == 'point':
        if point[a - 1][b] == '.':
            go_left = 'W'
            a -= 1
            if a == 0:
                exit_point = 1
                break
            steps.append([a, b])
            break
        elif point[a + 1][b] == '.':
            go_left = 'E'
            a += 1
            if a == -1:
                exit_point = 1
                break
            steps.append([a, b])
            break
        elif point[a][b + 1] == '.':
            go_left = 'N'
            b += 1
            if b == -1:
                exit_point = 1
                break
            steps.append([a, b])
            break
        elif point[a][b - 1] == '.':
            go_left = 'S'
            b -= 1
            if b == 0:
                exit_point = 1
                break
            steps.append([a, b])
            break
    if go_left == 'N' and exit_point != 1:
        while True:
            print(steps)
            if point[a - 1][b] == '.':
                go_left = 'W'
                a -= 1
                if a == 0 and point[a][b] != start:
                    exit_point = 1
                    break
                steps.append([a, b])
                break
            elif point[a - 1][b] == '#':
                go_left = 'E'
                break
            # else:
            #     exit_point = 1
            #     break
    if go_left == 'S' and exit_point != 1:
        while True:
            print(steps)
            if point[a + 1][b] == '.':
                go_left = 'E'
                a += 1
                if a == -1 and point[a][b] != start:
                    exit_point = 1
                    break
                steps.append([a, b])
                break
            elif point[a + 1][b] == '#':
                go_left = 'W'
                break
            # else:
            #     exit_point = 1
            #     break
    if go_left == 'E' and exit_point != 1:
        while True:
            print(steps)
            if point[a][b + 1] == '.':
                go_left = 'N'
                b += 1
                if b == -1 and point[a][b] != start:
                    exit_point = 1
                    break
                steps.append([a, b])
                break
            elif point[a][b + 1] == '#':
                go_left = 'S'
                break
            # else:
            #     exit_point = 1
            #     break
    if go_left == 'W' and exit_point != 1:
        while True:
            print(steps)
            if point[a][b - 1] == '.':
                go_left = 'S'
                b -= 1
                if b == 0 and point[a][b] != start:
                    exit_point = 1
                    break
                steps.append([a, b])
                break
            elif point[a][b - 1] == '#':
                go_left = 'N'
                break
            # else:
            #     exit_point = 1
            #     break
    if tupik >= 3:
        point[a][b] = '#'
    if exit_point == 1:
        print('You have finished!')
        break
print('vishel')
