# TIC TAC TOE GAME
'''
Half dynamic tic-tac-toe game,
No Choose of players,
'''

## IMPORTS ##
from copy import deepcopy

## FUNCTONS ##
def print_board(b):
    c = 0
    print('TIC TAC TOE BOARD:')
    print(f'{"":^3} {0:^3} {1:^3} {2:^3}')
    for x in b:
        print(f'    {"":-^13}')
        print(f'{c:^3}|{x[0]:^3}|{x[1]:^3}|{x[2]:^3}|')
        c += 1
    else:
        print(f'{"":^3} {"":-^13}')

def is_same(v, *args):
    return len(set(*args)) == 1 and list(set(*args))[0] == v

def check_h(b, v):
    return is_same(v, b[0]) or is_same(v, b[1]) or is_same(v, b[2])

def check_v(b, v):
    result = False
    for x in range(3):
        temp = []
        for y in range(3):
            temp.append(b[y][x])
        if is_same(v, temp):
            return True
    return result

def check_diagonal(b, v):
    result = False
    temp = []
    for x in range(3):
        temp.append(b[x][x])
    else:
        if is_same(v, temp):
            return True
    temp = []
    for x in range(1,4):
        temp.append(b[-x][x-1])
        # print(board[-x][x-1], end='')
    else:
        if is_same(v, temp):
            return True
    return result

def is_taken(b, p):
    return bool(b[p[0]][p[1]])

def if_won(b, v):
    return check_h(b, v) or check_diagonal(b, v) or check_v(b, v)

def if_draw(b):
    count = 0
    for x in b:
        count += x.count('')
    if count == 0:
        return True
    return False

def update_board(b, v, points):
    b[points[0]][points[1]] = v

def reset_v():
    return deepcopy(board),0,0

def validate_data(points):
    points = points.split()
    # Length must be equal to 2 (1 for row and 1 for column)
    if len(points) != 2: return False

    # Input must bw convertable to integers, if not return False
    try:
        points = [int(x) for x in points]
    except Exception as e:
        return False
    if not (all(map(lambda x: x>=0 and x<=2,points))): return False
    return points

## INITIAL DATA ##
board = [['','',''],['','',''],['','','']]
play_board = deepcopy(board)

players = ['Player_X','Player_O']
values = ['X','O']
p,val = 0, 0

## MAIN ##
def main():
    global board, play_board,players,values, p, val
    while True:
        print_board(play_board)

        points = input(f'{players[p]} Enter values : ')
        if points == 'q': break

        points = validate_data(points)
        if not points:
            print('Entered data not valid, try again'); continue

        if is_taken(play_board, points):
            print('Square is already taken. Try again')
            continue

        update_board(play_board, values[val], points)

        if if_won(play_board,values[val]):
            print(f'{players[p]} Won the GAME!')
            if input('Want to continue?: ').lower() == 'q':
                break
            else:
                play_board, p, val = reset_v()
        elif if_draw(play_board):
            print("'It's a DRAW")
            if input('Want to continue?: ').lower() == 'q':
                break
            else:
                play_board, p, val = reset_v()
        else:
            val = 0 if val == 1 else 1
            p = val

if __name__=='__main__':
    main()
