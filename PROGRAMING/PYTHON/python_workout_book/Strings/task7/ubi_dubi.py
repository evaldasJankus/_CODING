"""firstString = "abc"
secondString = "ghi"
thirdString = "abi"

print('habclilo'.translate(''.maketrans(firstString, secondString, thirdString)))
maketrans:
first value - string characters that should be changed
second value - string character that should change first value (should be of same length as first value)
thod value - string characters which should be remove from original string
"""

def ubi_dubi(word):
    '''
    In Ubbi Dubbi, every vowel (a, e, i, o, or u) is prefaced with ub. Thus milk becomes
    mubilk (m-ub-ilk) and program becomes prubogrubam (prub-ogrub-am).
    '''
    vowels = ('a', 'e', 'i', 'o', 'u')
    swap = 'ub'

    #Method 1
    # new_word = ''
    # for letter in word:
    #     if letter in vowels: new_word += swap+letter
    #     else: new_word += letter
    # return new_word

    #Method 2
    return ''.join([swap+letter if letter in vowels else letter for letter in word])

#-------------------------BEYOND THE TASK--------------------------------------
"""
 Handle capitalized words—If a word is capitalized (i.e., the first letter is capitalized, but
the rest of the word isn’t), then the Ubbi Dubbi translation should be similarly capitalized.
"""
def ubi_dubi_capitalize(word):
    vowels = ('a', 'e', 'i', 'o', 'u')
    swap = 'ub'

    new_word = ''.join([swap+letter if letter.lower() in vowels else letter for letter in word])
    if word.istitle(): return new_word.capitalize()
    return new_word

"""
 Remove author names—In academia, it’s common to remove the authors’ names
from a paper submitted for peer review. Given a string containing an article and
a separate list of strings containing authors’ names, replace all names in the
article with _ characters.
"""
def hide_authors(article, authors):
    for author in authors:
        if author in article:
            article = article.replace(author, '-'*len(author))
    return article

"""
 URL-encode characters—In URLs, we often replace special and nonprintable
characters with a % followed by the character’s ASCII value in hexadecimal. For
example, if a URL is to include a space character (ASCII 32, aka 0x20), we
replace it with %20. Given a string, URL-encode any character that isn’t a letter
or number. For the purposes of this exercise, we’ll assume that all characters
are indeed in ASCII (i.e., one byte long), and not multibyte UTF-8 characters. It
might help to know about the ord (http://mng.bz/EdnJ) and hex (http://mng
.bz/nPxg) functions. 
"""
def url_change(url):
    import string
    valid_char = string.ascii_lowercase + ':/.' + '0123456789'
    replace_symbol = '%'

    #Method 1
    return ''.join([replace_symbol + str(hex(ord(ch))[2:]) if not ch.lower() in valid_char else ch for ch in url])

    #Method 2
    # new_url = ''
    # for ch in url:
    #     if not ch.lower() in valid_char: new_url += replace_symbol + str(hex(ord(ch))[2:])
    #     else: new_url += ch
    # return new_url


if __name__=='__main__':

    # for word in ['Elephant','elephant', 'octopus', 'program', 'milk', 'soap']:
    #     print(word,'=>',ubi_dubi_capitalize(word))

    # article = 'Some article, and author of the article is Evaldas Jankus.\nSecond author of the article is Mindaugas Ponetauskas'
    # authors = ['Evaldas Jankus', 'Alberts Locmelis', 'Mindaugas Ponetauskas']
    # print(hide_authors(article, authors))

    url = 'file:///C:/Users/Efka/Desktop/Python_Workout_50_Essential_Exercises_by_Reuven_M_Lerner.pdf'
    print(url,'\n',url_change(url))
