def load_file(fname):
    with open(fname) as f:
        return [line.rstrip() for line in f]

def process_data(entries):
    dict_val = []
    temp_dict = {}
    for entry in entries:
        if not entry:
            dict_val.append(temp_dict)
            temp_dict = {}
            continue
        for kv in entry.split():
            temp_dict[kv.split(':')[0]] = kv.split(':')[1]
    else:
        dict_val.append(temp_dict)
    return dict_val

def filter_data(entries):
    print('Length:', len(entries))
    valid_pass, not_valid_pass = [],[]
    for entry in entries:
        if (len(entry) == 7 and 'cid' not in entry) or len(entry) == 8:
            valid_pass.append(entry)

    return valid_pass

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.
def is_valid_by_rules(entries):
    print(len(entries))
    def valid_values(entry):
        keys = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
        if ((int(entry[keys[0]]) >= 1920 and int(entry[keys[0]]) <= 2002) and (int(entry[keys[1]]) >= 2010 and int(entry[keys[1]]) <= 2020) and (int(entry[keys[2]]) >= 2020 and int(entry[keys[2]]) <= 2030) and (len(entry[keys[-1]]) == 9 and entry[keys[-1]].isdigit()) and (entry[keys[5]] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])):
            height_unit = 'cm' if entry[keys[3]][-2:] == 'cm' else 'in' if entry[keys[3]][-2:] == 'in' else False
            if not height_unit: return False
            if ((height_unit == 'cm' and (int(entry[keys[3]][:-2]) >= 150 and int(entry[keys[3]][:-2]) <= 193)) or (height_unit == 'in' and (int(entry[keys[3]][:-2]) >= 59 and int(entry[keys[3]][:-2]) <= 76))):
                if entry[keys[4]][0] != '#' or len(entry[keys[4]]) > 7: return False
                print(entry[keys[4]])
                for ch in entry[keys[4]][1:]:
                    if ch not in ['0','1','2','3','4','5','6','7','8','9'] and ch not in ['a','b','c','d','e','f']: return False

                return True
        return False
    return len([entry for entry in entries if valid_values(entry)])

def main():
    print(is_valid_by_rules(filter_data(process_data(load_file('pasports_data')))))

if __name__ == '__main__':
    main()
