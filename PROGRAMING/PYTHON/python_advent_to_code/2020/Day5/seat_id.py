rows = range(128)
cols = 8
options = ['F','B','L','R']

def load_file(fname):
    with open(fname) as f:
        for line in f:
            yield line.rstrip()

def get_seat_number(seat):
    row = range(128)
    col = range(8)
    # print(seat)
    for r in seat[:7]:
        lower, upper = 0 if r == 'F' else len(row)//2, len(row)//2 if r == 'F' else len(row)
        # print(lower, upper, row)
        row = row[lower:upper]
    # print(row, len(row))
    # else:
    #     row = row[0 if seat[:7] == 'F' else 1]
    for r in seat[7:]:
        lower, upper = 0 if r == 'L' else len(col)//2, len(col)//2 if r == 'L' else len(col)
        col = col[lower:upper]
    # print(col, len(col), col[1])
    # else:
    #     col = col[0 if seat[7:] == 'L' else 1]
    return row[0], col[0]

def get_seats(fname):
    return [get_seat_number(seat) for seat in load_file(fname)]
    # return get_seat_number('BBFFBBFRRR')

def get_biggest_seat_id(seats):
    # print(seats)
    return max(seat[0] * 8 + seat[1] for seat in seats)

def missing_seats(seats, rows=range(128), cols=range(8)):

    all_seats = [(row,col) for row in rows for col in cols]
    # print(len(seats), len(all_seats))
    free_seats = [seat for seat in all_seats if seat not in seats]
    free_seats = [(seat,(seat[0] * 8 + seat[1])) for seat in free_seats[8:-8]]
    for x in range(len(free_seats)-2):
        if free_seats[x][1] + 1 == free_seats[x+1][1] or free_seats[x+1][1]+1 == free_seats[x+2][1]: pass
        else:
            print(free_seats[x+1])
    # return free_seats

def main():
    # print(get_biggest_seat_id(get_seats('seat_data')))
    # print(missing_seats(get_seats('seat_data')))
    missing_seats(get_seats('seat_data'))

if __name__ == '__main__':
    main()
