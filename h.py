import requests


alphabets = 'esiarngtomlcdupmhbyfvwzxqj'

def checkSame(str1, str2):
    for i in range(len(str1)):
        if str1[i] != str2[i] and str2[i] != '_':
            return False
    for i in range(len(str1)):
        if str1[i] != str2[i] and str1[i] in guessed:
            return False
    return True

    


URL = "http://upe.42069.fun/U7b8u"
URLRESET = "http://upe.42069.fun/U7b8u/reset"
path = 'dict.txt'
f = open(path, 'r')
words = []


P_Data = {'email': "kanishapshah@gmail.com"}
p = requests.post(url=URLRESET, data = P_Data)
R_Data = p.json()
print(R_Data)

lists = f.readlines()
for i in range (len(lists)):
    words.append(lists[i].rstrip('\n'))

iterCount = 0
games = 0

while(iterCount < 100):
    status = ""
    guessed = 'e'
    r = requests.get(url=URL)

    data = r.json()

    state = data['state']
    status = data['status']
    remaining_guesses = data['remaining_guesses']

    print("New State: %s\n"%(state))


    P_Data = {'guess': 'e'}
    p = requests.post(url=URL, data = P_Data)

    R_Data = p.json()

    state = R_Data['state']
    status = R_Data['status']
    remaining_guesses = R_Data['remaining_guesses']
    win_rate = R_Data['win_rate']
    print(state)
    print(remaining_guesses)

    count = 1


    while (status != "FREE" and remaining_guesses != 1):
        P_Data = {'guess': alphabets[count]}
        guessed += alphabets[count]
        count += 1
        print(guessed)
        p = requests.post(url=URL, data = P_Data)
        R_Data = p.json()

        state = R_Data['state']
        status = R_Data['status']
        remaining_guesses = R_Data['remaining_guesses']
        win_rate = R_Data['win_rate']

        print(state)
        print(remaining_guesses)
        print(win_rate)
        print(status)

    statewords = state.split()
    stateWords = []
    for word in statewords:
        word = word.replace(',', '')
        word = word.replace('(', '')
        word = word.replace(')', '')
        stateWords.append(word)

    if (remaining_guesses == 1 and status != "FREE"):
        for i in range(len(stateWords)):
            if stateWords[i].isalpha() == False:
                for guessword in words:
                    if len(guessword) == len(stateWords[i]) and checkSame(guessword, stateWords[i]):
                        for ch in guessword:
                            if(status != "DEAD" and status != "FREE"):
                                print(guessword)
                                if(ch == '\''):
                                    continue
                                P_Data = {'guess': ch}
                                p = requests.post(url=URL, data = P_Data)
                                R_Data = p.json()
                                state = R_Data['state']
                                statewords = state.split()
                                stateWords = []
                                for word in statewords:
                                    word = word.replace(',', '')
                                    word = word.replace('(', '')
                                    word = word.replace(')', '')
                                    stateWords.append(word)
                                status = R_Data['status']
                                remaining_guesses = R_Data['remaining_guesses']
                                win_rate = R_Data['win_rate']
                                games = R_Data['games']
                                print(state)
                                print(remaining_guesses)
                                print(win_rate)
                                print(status)
                    
                        break

    
    while (status != "FREE" and status != "DEAD"):
        P_Data = {'guess': alphabets[count]}
        guessed += alphabets[count]
        count += 1
        p = requests.post(url=URL, data = P_Data)
        R_Data = p.json()
        state = R_Data['state']
        status = R_Data['status']
        remaining_guesses = R_Data['remaining_guesses']
        win_rate = R_Data['win_rate']
        games = R_Data['games']
        print(state)
        print(remaining_guesses)
        print(win_rate)
        print(status)


    print("Iter Count:")
    print(iterCount)
    iterCount += 1

print("\n\nFINALLY ")
print(games)
print(win_rate)


