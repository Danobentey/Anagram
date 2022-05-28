def find_anagram (word, anagram):
    a = sorted(word)
    b = sorted(anagram)
    if a == b:
        print ('This is an Anagram')
        return True
    else:
        print ('This is not an Anagram')
        return False

find_anagram ('silent', 'listen')
find_anagram ('fam', 'mof')