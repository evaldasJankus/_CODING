def weather_report():
    choice = 1
    dict_weather = {}
    while choice:
        choice = input('Enter city: ')
        if not choice: continue

        #----------------------------------------------------------------------
        if choice in dict_weather:
            dict_weather[choice] += int(input('Enter fall in mililiters: '))
        else:
             dict_weather[choice] = int(input('Enter fall in mililiters: '))
        #----------------------------------------------------------------------
        # INSTEAD OF IF STRATEMENT CAN BE USED ONE LINE: rainfall[city_name] = rainfall.get(city_name,0) + int(mm_rain)
    else:
        for key, val in dict_weather.items():
            print(f'{key}: {val}')


#-------------------------BEYOND THE TASK--------------------------------------
"""
 Instead of printing just the total rainfall for each city, print the total rainfall and
the average rainfall for reported days. Thus, if you were to enter 30, 20, and 40
for Boston, you would see that the total was 90 and the average was 30.
"""
def weather_report_with_average():
    choice = 1
    dict_weather = {}
    while choice:
        choice = input('Enter city: ')
        if not choice: continue

        fall = int(input('Enter fall in mililitrs: '))
        dict_weather[choice] = (dict_weather.get(choice,(0,0))[0] + fall, dict_weather.get(choice,(0,0))[1]+1)
    else:
        for key, val in dict_weather.items():
            print(f'{key}: total:{val[0]} aver:{val[0]/val[1]}')

def log_file_read(filename='log_file'):
    """
     Open a log file from a Unix/Linux system—for example, one from the Apache
    server. For each response code (i.e., three-digit code indicating the HTTP
    request’s success or failure), store a list of IP addresses that generated that code.
    (https://kb.webtrends.com/articles/Information/Sample-Log-File-Apache-Extended-Log-File-Format/?l=en_US&fs=RelatedArticle)
    """
    response_codes = {}
    with open(filename,'r') as f:
        for line in f:
            line = line.split()
            # print(line)
            response_codes[line[8]] = response_codes.get(line[8],[]) + line[:1]
    return response_codes

"""
 Read through a text file on disk. Use a dict to track how many words of each
length are in the file—that is, how many three-letter words, four-letter words,
five-letter words, and so on. Display your results.
"""
def read_file_words(filename='text_file'):
    simbols = ['.',',','?','!','\n']
    word_list = {}
    with open(filename, 'r') as f:
        for line in f:
            for ch in simbols:
                line = line.replace(ch,'')
            line = line.split()
            for word in line:
                word_list[len(word)] = word_list.get(len(word), 0) + 1

    for number in word_list:
        print(f'Number of letters: {number} Number of word of same length: {word_list[number]}')
    print(word_list)



if __name__ == '__main__':
    # weather_report_with_average()
    # print(log_file_read())
    read_file_words()
