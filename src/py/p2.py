map = []
move = []
xy = []
win = []
stop_it = False
n = int(input())
m = int(input())
j = int(int(input()) / 2)

for w in range(0, n):
    s = input()
    mc = []
    d = 0
    for i in s:
        mc.append(i)
        if i == 'x':
            move.append([w, d, j])
        d += 1
    map.append(mc)

for cords in move:
    for x in [-1, 1]:
        c1 = cords[0]
        c2 = cords[1]+x
        c3 = cords[2]
        if c2 < m and c2 >= 0 and c3 >= 0:
            if map[c1][c2] == '.':
                xy.append([c1, c2, c3])
            elif map[c1][c2] == 's':
                c3 = cords[2] - 1
                if c3 >= 0:
                    xy.append([c1, c2, c3])
                    # break
            elif map[c1][c2] == '@':
                win = [c1, c2, c3]
                stop_it = True

    for x in [-1, 1]:
        c1 = cords[0]+x
        c2 = cords[1]
        c3 = cords[2]
        if c1 < n and c1 >= 0 and c3 >= 0:
            if map[c1][c2] == '.':
                xy.append([c1, c2, c3])
            elif map[c1][c2] == 's':
                c3 = cords[2] - 1
                if c3 >= 0:
                    xy.append([c1, c2, c3])
            elif map[c1][c2] == '@':
                win = [c1, c2, c3]
                stop_it = True

    move.extend(xy)
    xy.clear()
    if stop_it:
        break

if win != [] and win[2] >= 0:
    print("SUCCESS")
else:
    print('IMPOSSIBLE')
