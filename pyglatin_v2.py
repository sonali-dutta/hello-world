print "Welcome to Pig Latin Translator!"
pyg = "ay"
cluster = ['sm', 'st', 'gl', 'tr', 'sn', 'sh', 'ch', 'ph', 'br', 'fr', 'bl', 'gr', 'sl', 'cl', 'pl', 'fl', 'pr', 'cr', 'dr']
inputsentence = raw_input()

if len(inputsentence) > 0:
    inputsentence = inputsentence.split()
    newsentence = []
    for word in inputsentence:
        word = word.lower()
        firstletter = word[0]
        if firstletter in ('aeiou'):
            new_word = str(word) + pyg
        elif word[:2] in cluster:
            new_word = str(word[2:]) + str(word[:2]) + pyg
        elif word.isalpha() == False:
            new_word = str(word)
        else:
            new_word = str(word[1:]) + str(firstletter) + pyg
        newsentence.append(new_word)
    print ' '.join(newsentence)
else:
    print "Please enter valid sentence"
