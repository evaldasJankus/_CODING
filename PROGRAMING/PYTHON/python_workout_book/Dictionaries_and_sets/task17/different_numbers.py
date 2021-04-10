def how_many_difference_number(number_list):
    return len(set(number_list))


#-------------------------BEYOND THE TASK--------------------------------------
def read_log_file(filename='log_file'):
    """
     Read through a server (e.g., Apache or nginx) log file. What were the different
    IP addresses that tried to access your server?
    """
    ips_set = set()
    ips_list = []
    with open(filename,'r') as f:
        for line in f:
            ips_set.add(line.partition(' ')[0])
            ips_list.append(line.partition(' ')[0])
    return ips_set, ips_list

def read_error_logs(filename='log_file'):
    """
     Reading from that same server log, what response codes were returned to
    users? The 200 code represents “OK,” but there are also 403, 404, and 500
    errors. (Regular expressions aren’t required here but will probably help.)
    """
    error_codes_set,error_codes_list = set(),[]
    with open(filename,'r') as f:
        for line in f:
            error_codes_set.add(line.split(' ')[8])
            error_codes_list.append(line.split(' ')[8])
    return error_codes_set, error_codes_list

def get_file_list(path=''):
    import os
    path = 'C:\Windows'
    # os.path.splitext(path)[:10] - padalina pilna kelia iki failo i dvi dalis, kelia i ki fialo ir pati failo pvadanima su galu
    return set([file.partition('.')[-1] for file in os.listdir(path)])


if __name__ == '__main__':
    # print(how_many_difference_number([1,1,1,2,4,3,4,7,3,7,]))
    # print(read_log_file())
    # print(read_error_logs())
    print(get_file_list())
