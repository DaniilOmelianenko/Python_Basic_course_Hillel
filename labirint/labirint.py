labirint = [
    ['#', '#', '#', '#', '#', '#', '#', '#'],
    ['.', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '.', '#', '#', '#', '#'],
    ['#', '.', '#', '.', '#', '#', '#', '#'],
    ['#', '.', '#', '.', '#', '#', '#', '#'],
    ['#', '.', '#', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '#', '#', '.', '#'],
    ['#', '.', '.', '#', '.', '.', '.', '#'],
    ['#', '#', '#', '#', '.', '#', '#', '#'],
]
steps = []
a = int(input('vertical: '))
b = int(input('gorizontal: '))
start = labirint[a][b]
point = labirint
start = '#'
for i in range(25):
    tupik = 0
    exit_point = 0
    go_left = 'point'
    direction_a = 0
    direction_b = 0
    if go_left == 'point' or 'N' and direction_a == 0:
        while True:
            print(steps)
            if point[a - 1][b] == '.':
                go_left = 'W'
                direction_a = 1
                a -= 1
                steps.append([a, b])
                tupik = 0
            elif point[a - 1][b] == '#':
                tupik += 1
                print('#')
                break
            else:
                exit_point = 1
                break
    if go_left == 'point' or 'S' and direction_a == 0:
        while True:
            print(steps)
            if point[a + 1][b] == '.':
                go_left = 'E'
                direction_a = 1
                a += 1
                steps.append([a, b])
                tupik = 0
            elif point[a + 1][b] == '#':
                tupik += 1
                break
            else:
                exit_point = 1
                break
    if go_left == 'point' or 'E' and direction_b == 0:
        while True:
            print(steps)
            if point[a][b + 1] == '.':
                go_left = 'N'
                direction_b = 1
                b += 1
                steps.append([a, b])
                tupik = 0
            elif point[a][b + 1] == '#':
                tupik += 1
                break
            else:
                exit_point = 1
                break
    if go_left == 'point' or 'W' and direction_b == 0:
        while True:
            print(steps)
            if point[a][b - 1] == '.':
                go_left = 'S'
                direction_b = 1
                b -= 1
                steps.append([a, b])
                tupik = 0
            elif point[a][b - 1] == '#':
                tupik += 1
                break
            else:
                exit_point = 1
                break
    if tupik >= 3:
        point[a][b] = '#'
    if exit_point == 1:
        print('You have finished!')
        break
print('vishel')
