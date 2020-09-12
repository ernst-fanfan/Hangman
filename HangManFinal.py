import random

# game manager
def game(choice):#TODO mod for list[dict] data structure
    players = player_loader(choice)
    display_scores(players)

    for player in players:
        player['w2g'], player['mask'] = word_selector()

    still_playing = True
    while (still_playing):
        for player in players:
            if player['win'] == True or player['img'] == 6:
                still_playing = False
            else:
                turn(player)#TODO

#Win check
def win (guess):
    return not ("_" in guess)

# turn
def turn(player):#TODO mod for list[dict] data structure
    exitt = False
    while (not exitt):
        player_status(player)

        chosenLetter = input("Chose a letter:: ")
        if (chosenLetter in player['wrong'] or chosenLetter in player['mask']):
            print("You have chosen this one already!")
        else:
            # wrong guess
            if (not(chosenLetter in player['w2g'])):
                player['wrong'] += chosenLetter
                print("{} in not in the word".format(chosenLetter))
                player['img'] += 1
                #update_img(players,player)#TODO check if still needed
                player_status(player)
                if (player['img'] == 6):#TODO not sure if thius needs to be in a higher order fuction
                    print("The word was: {}".format(player['w2g']))
                exitt = True
            else:
                # right guess
                for i in range(len(player['w2g'])):
                    if (player['w2g'][i] == chosenLetter):
                        player['mask'] = swap(player['mask'], i, chosenLetter)
                print("{} is the word.".format(chosenLetter))
                player['win'] = win(player['mask'])
                player_status(player)
                exitt = True

# swapping letters at index
def swap(word, i, letter):
    letterLst = list(word)
    letterLst[i] = letter
    word = "".join(letterLst)
    return word

# status display
def player_status(player):#TODO DONE
    print("\n{}".format(player['name']))
    img_mng(player['img'])
    print(player['mask'])
    print("Chosen--> {}".format(player['wrong']))

# pick random word in dictionary
def word_selector():
    with open('wordlist.txt') as wordFile:
        wordList = wordFile.readlines()

    wordListFixed = []
    for word in wordList:
        wordListFixed.append(word.strip('\n'))

    wordPicked = random.choice(wordListFixed)

    placeHolder = ""
    for letter in wordPicked:
        placeHolder += '_'

    return wordPicked, placeHolder

# load player in dictionary
def player_loader(numOfPlayers):#TODO DONE
    players = []
    player = {'name':'', 'img': 0, 'w3g': '','mask':'','wrong':'','right':'', 'win?':False}
    for i in range(numOfPlayers):#TODO: mod dict to be a dict with in a dict DONE
        player['name'] = input("Player {} name:".format(i+1))
        players.append(player)
    return players

# menu
def menu():
    print("""
    \nMenu
    1: play Game
    2: End Game
    """)
    choice = int(input("\t:: "))
    if (choice == 1):
        return True, 1
    elif (choice == 2):
        return False, 2
    else:
        print("\nInvalid input!")
        return True, 0

# intro
def intro():
    print("""
    *************
    ***************
    *   Hang Man  *
    ***************
    by EZL Studios
    ***************
    ***************
    """)

# image manager
def img_mng(num):
    if (num == 0):
        print("""
            #######
            #     *
            #
            #
            #
            #
        ##########
        """)
    if (num == 1):
        print("""
            #######
            #     *
            #    (OO)
            #
            #
            #
        ##########
        """)
    if (num == 2):
        print("""
            #######
            #     *
            #    (OO)
            #     || 
            #      
            #
        ##########
        """)
    if (num == 3):
        print("""
            #######
            #     *
            #    (OO)
            #    /|| 
            #      
            #
        ##########
        """)
    if (num == 4):
        print("""
            #######
            #     *
            #    (OO)
            #    /||\            
            #      
            #
        ##########
        """)
    if (num == 5):
        print("""
            #######
            #     *
            #    (OO)
            #    /||\            
            #     /
            #
        ##########
        """)
    if (num == 6):
        print("""
            #######
            #     *
            #    (xx)
            #    /||\\
            #     /\\
            #
        ##########
        Game Over
        """)

def update_img(dict, player):
    if (dict[player][1] == 5):
        dict[player][1] += 1
        return False
    else:
        dict[player][1] += 1
        return True


# score tracker
def update_scores(dict, player):
    dict[player] [0]+= 1
    return dict

def display_scores(lst):#TODO mod for list[dict] data structure DONE
    if (lst == []):
        print("\nScoreboard is empty.\nPlease Update!")
    else:
        print("\nScores:")
        for player in lst:
            print("--> {}\t::\t{}".format(player['name'], player['score']))

def reset_scores(dict):
    dict.clear()
    return dict

# TODO main
exitt, choice = menu()
while(exitt):
    if (choice == 0):
        pass
    elif (choice == 2):
        break
    else:
        game(int(input("\nHow many players: ")))
    exitt, choice = menu()

print("END")

#test
# print(word_selector())