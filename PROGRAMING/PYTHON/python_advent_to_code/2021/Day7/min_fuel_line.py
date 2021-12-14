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

# def get_fuel_expense3(line_number, dict_fuels):
#     # print([abs(k - line_number) * dict_fuels[k] for k,v in dict_fuels])
#     return sum([abs(k - line_number) * dict_fuels[k] for k in dict_fuels])
#
# def get_fuel_expense4(line_number, dict_fuels):
#     return sum([sum([rock for rock in range(abs(k - line_number)+1)]) * dict_fuels[k] for k in dict_fuels])
#
# def cheapest_fuel(rockets):
#     dict_fuels = {rocket:rockets.count(rocket) for rocket in set(rockets)}
#     keys = list(set(rockets))
#     fuel_expense = get_fuel_expense4(473, dict_fuels)
#     max_line = 473
#     # for line in keys[1:]:
#     #     temp_fuel = get_fuel_expense4(line, dict_fuels)
#     #     if temp_fuel < fuel_expense:
#     #         fuel_expense = temp_fuel
#     #         max_line = line
#     return fuel_expense, max_line

def main():
    fname = 'data'
    print(cheapest_fuel(sorted(load_file(fname))))

if __name__ == '__main__':
    main()
