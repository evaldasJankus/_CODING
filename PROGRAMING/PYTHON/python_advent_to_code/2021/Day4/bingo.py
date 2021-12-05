def load_file(fname):
    with open(fname) as f:
        role_numbers = f.readline().rstrip().split(',')
        f.readline()
        boards, temp = [], []
        for line in f:
            if line.rstrip(): temp.append(line.rstrip().split())
            else:
                boards.append(temp)
                temp = []
        else:
            boards.append(temp)
        return role_numbers, boards

def print_boards(boards):
    for board in boards:
        print(board)

def mark_board(board, number):
    for row in board:
        if number in row:
            row[row.index(number)] += '+'
            break

def check_rows(rows):
    for row in rows:
        counter = sum([1 for item in row if item.endswith('+')])
        if counter == 5: return True
    return False

def check_columns(board):
    for index in range(len(board[0])):
        columns = [cols[index] for cols in board]
        counter = sum([1 for item in columns if item.endswith('+')])
        if counter == 5: return True
    return False

def check_if_board_win(board):
    return check_rows(board) or check_columns(board)

#--------------------PART1-------------------------
def mark_all_boards(boards, numbers):
    for number in numbers:
        for board in boards:
            mark_board(board, number)
            if check_if_board_win(board): return board, number


def final_score(board, number):
    unmarked_score = sum([int(item) for row in board for item in row if not item.endswith('+')])
    print(unmarked_score, number)
    print(unmarked_score * int(number))

#-------------END OF PART1-------------------------
# 662 * 96
# 63552

#--------------------PART2-------------------------
def mark_all_boards_part2(boards, numbers):
    temp_winer_boards = []
    for number in numbers:
        for board in boards:
            mark_board(board, number)
            if check_if_board_win(board) and not (board in temp_winer_boards):
                temp_winer_boards.append(board)
                if len(temp_winer_boards) == len(boards): return board, number


def final_score_part2(board, number):
    unmarked_score = sum([int(item) for row in board for item in row if not item.endswith('+')])
    print(unmarked_score, number)
    print(unmarked_score * int(number))
#-------------END OF PART2-------------------------

def main():
    file = 'data'
    role_numbers, boards = load_file(file)
    winner, number = mark_all_boards_part2(boards, role_numbers)
    print(winner, number)
    final_score_part2(winner, number)

if __name__ == '__main__':
    main()
