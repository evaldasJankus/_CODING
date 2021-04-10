# Main point of task:import collections.Counter() and collections.Counter().most_common()
from collections import Counter

def most_repeated_letters(words):
    # Find word which has most common letters in word
    # Method 1
    # return sorted([(Counter(word).most_common(1)[-1][-1],word) for word in words])[-1][-1]

    # Method 2
    # return max([(Counter(word).most_common(1)[-1][-1],word) for word in words])[1]

    # Method 3 (recomended by book)
    def return_max_letter(word):
        return Counter(word).most_common(1)[0][1]
    return max(words, key=return_max_letter)

#-------------------------BEYOND THE TASK--------------------------------------
"""
 Instead of finding the word with the greatest number of repeated letters, find
the word with the greatest number of repeated vowels.
"""
def most_common_vowel(words):
    # Find word whcih has most comon vowels in word
    def most_common_letter(word):
        vowels = ('a', 'e', 'i', 'o', 'u')
        c = Counter(word)
        return max([c[v] for v in vowels])
    return max(words,key=most_common_letter)

# NOTE: Kadangi neturiu Unix systemos, tia vietoj failo skaitymo imituosim input
# is paprasto sting list, kur kiekviena lsit atstovaus viena passwd fail eilute
'''
#           PAVYZDYS KAIP ATRODO /ETC/PASSWD ZEMIAU:
# fred:6k/7KCFRPNVXg:508:10:% Fredericks:/usr2/fred:/bin/csh
# root:!:0:0::/:/usr/bin/ksh
# account:password:UID:GID:GECOS:directory:shell
# root:x:0:0:root:/root:/bin/bash
# bin:x:1:1:bin:/bin:/sbin/nologin
# testK:x:2222:2222::/home/testK:/bin/bash
# testtest:x:2223:2223::/home/testtest:/bin/bash
# nobody:!:4294967294:4294967294::/:
# lpd:!:9:4294967294::/:
# lp:*:11:11::/var/spool/lp:/bin/false
# invscout:*:200:1::/var/adm/invscout:/usr/bin/ksh
# nuucp:*:6:5:uucp login user:/var/spool/uucppublic:/usr/sbin/uucp/uucico
# paul:!:201:1::/home/paul:/usr/bin/ksh
# jdoe:*:202:1:John Doe:/home/jdoe:/usr/bin/ksh
'''
'''Write a program to read /etc/passwd on a Unix computer. The first field contains
the username, and the final field contains the user’s shell, the command interpreter.
Display the shells in decreasing order of popularity, such that the most popular
shell is shown first, the second most popular shell second, and so forth.
 For an added challenge, after displaying each shell, also show the usernames
(sorted alphabetically) who use each of those shells.'''
#------------------------------------------------------------------------------
def shell_etc_passwd(filename):
    shells = []
    with open(filename,'r') as f:
        for line in f:
            line = line.replace('\n','').split(':')
            shells.append((line[0],line[-1]))

    c = Counter([ shell[-1] for shell in shells])

    def temp():
        users = []
        for shel in c.most_common():
            users.append(sorted([x[0] for x in shells if x[1] == shel[0]]))
        return users
    sh = [x[0] for x in c.most_common()]
    st_line = ''.join(['BASH: '+x[0] + ', USERS=> '+ ','.join(x[1]) + '\n' for x in zip(sh,temp())])
    return st_line
    # return [shell[0] for shell in c.most_common()]  # Retunrs most often values of shell in order

    # return sorted(shells, key=c.most_common(1))

def shells_sorted_by_shell_useability_number(filename):
    shells = []
    with open(filename,'r') as f:
        for line in f:
            line = line.replace('\n','').split(':')
            shells.append((line[0],line[-1]))

    c = Counter([ shell[-1] for shell in shells])

    def temp(shel):
        return c[shel[-1]]
    # return sorted(shells, key=temp, reverse=True)   # Sorting list by most often repeated value
    return sorted(shells, key=lambda x: (temp(x),x[0]), reverse=True)  # Lamba function for sorting buy two values (first what we get from fucntion temp, second for value name)




if __name__ == '__main__':
    # print(most_common_vowel(['this', 'ananas','binininis','is', 'an', 'elementary', 'test', 'example']))
    print(shells_sorted_by_shell_useability_number('etc_passwd'))
    # print(shell_etc_passwd('etc_passwd'))
