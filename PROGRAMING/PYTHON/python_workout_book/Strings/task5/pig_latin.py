def pig_lating(word):
    # No matter if letter is lower or capital
    letters = ('a', 'e', 'i', 'o', 'u')
    add_end = ['way', 'ay']
    if word[0] in letters: return word + add_end[0]
    return word[1:] + word[0] + add_end[1]

#-------------------------BEYOND THE TASK--------------------------------------
"""
 Consider an alternative version of Pig Latin—We don’t check to see if the first letter
is a vowel, but, rather, we check to see if the word contains two different vowels.
If it does, we don’t move the first letter to the end. Because the word “wine”
contains two different vowels (“i” and “e”), we’ll add “way” to the end of it, giving us “wineway.” By contrast, the word “wind” contains only one vowel, so we
would move the first letter to the end and add “ay,” rendering it “indway.” How
would you check for two different vowels in the word? (Hint: sets can come in
handy here.)
"""
def pig_latin_diff_vowels(word):
    # if has 2 vowels, add 'way' to the end, else add first letter to the end
    # and then add 'ay' to the end
    vowels_count = set()
    vowels = ('a', 'e', 'i', 'o', 'u')
    add_end = ['way', 'ay']
    for letter in word:
        if letter in vowels:
            vowels_count.add(letter)
            if len(vowels_count)>= 2: return word + add_end[0]
    return word[1:] + word[0] + add_end[1]

"""
Handle punctuation—If a word ends with punctuation, then that punctuation
should be shifted to the end of the translated word.
"""
def pig_lating_capitalaized_punctuation(word):
    # will treat words if it is capitalized will return capitalized either
    # pay attention to punctuation as well
    letters = ('a', 'e', 'i', 'o', 'u')
    add_end = ['way', 'ay']
    ending = '' if word[-1].isalpha() else word[-1]
    if word[0].lower() in letters:
        if ending: return word[:-1] + add_end[0] + ending
        else: return word + add_end[0]

    if word[0].isupper():
        if ending: return word[1:-1].capitalize() + word[0].lower() + add_end[1] + ending
        else: return word[1:].capitalize() + word[0].lower() + add_end[1]
    else:
        if ending: return word[1:-1] + word[0] + add_end[1] + ending
        else: return word[1:] + word[0] + add_end[1]

"""
 Handle capitalized words—If a word is capitalized (i.e., the first letter is
capitalized, but the rest of the word isn’t), then the Pig Latin translation should be
similarly capitalized.
"""
def pig_lating_capitalaized(word):
    # will treat words if it is capitalized will rturn capitalized either
    letters = ('a', 'e', 'i', 'o', 'u')
    add_end = ['way', 'ay']
    if word[0].lower() in letters: return word + add_end[0]

    return (word[1:].capitalize() if word[0].isupper() else word[1:]) + word[0].lower() + add_end[1]

# Main function, testing
def main():
    word = ''
    while not word == 'q':
        word = input('Enter english word to output to Pig_Latin: ')
        if word == 'q': continue
        # print(f'"{word}", Pig_Latin=>"{pig_lating(word.lower())}"')
        print(f'"{word}", Pig_Latin=>"{pig_latin_diff_vowels(word)}"')
    else:
        print(f'{"Terminated":-^25}')

if __name__ == '__main__':
    main()
