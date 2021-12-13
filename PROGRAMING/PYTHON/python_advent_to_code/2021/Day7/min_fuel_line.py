def load_file(fname):
    with open(fname) as f:
        return [int(line) for line in f.readline().rstrip().split(',')]

#-------Part1 ----------
def get_fuel_expense(line_number, rockets):
    return sum([abs(rocket - line_number) for rocket in rockets])
#-------Part1 END ----------

#-------Part2 ----------
def get_fuel_expense2(line_number, rockets):
    return sum([sum([rock for rock in range(abs(rocket - line_number)+1)]) for rocket in rockets])
#-------Part2 END ----------



def cheapest_fuel(rockets):
    max_line, fuel_expense, results_line = rockets[-1], get_fuel_expense2(0, rockets[:]), 0
    for line in range(1,max_line+1):
        temp_fuel = get_fuel_expense2(line, rockets[:])
        if temp_fuel < fuel_expense:
            fuel_expense = temp_fuel
            results_line = line
    return fuel_expense, results_line


def main():
    fname = 'data'
    print(cheapest_fuel(sorted(load_file(fname))))

if __name__ == '__main__':
    main()
