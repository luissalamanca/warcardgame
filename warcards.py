# Coding utf-8
import secrets
import random
from random import shuffle
from os import system, name
from threading import Thread
import keyword
import time
import os


# Defaults
Player = 1
war_one = {}
war_two = {}
wincards_one = []
wincards_two = []
player1list = []
player2list = []

faceCards = {
"""
.------.
|A.--. |
| (\\/) |
| :\\/: |
| '--'A|
`------'
""": 1,
"""
.------.
|2.--. |
| (\\/) |
| :\\/: |
| '--'2|
`------'
""": 2,
"""
.------.
|3.--. |
| :(): |
| ()() |
| '--'3|
`------'
""": 3,
"""
.------.
|4.--. |
| :/\\: |
| :\\/: |
| '--'4|
`------'
""": 4,
"""
.------.
|5.--. |
| :/\\: |
| (__) |
| '--'5|
`------'
""": 5,
"""
.------.
|6.--. |
| (\\/) |
| :\\/: |
| '--'6|
`------'
""": 6,
"""
.------.
|7.--. |
| :(): |
| ()() |
| '--'7|
`------'
""": 7,
"""
.------.
|8.--. |
| :/\\: |
| :\\/: |
| '--'8|
`------'
""": 8,
"""
.------.
|9.--. |
| :/\\: |
| (__) |
| '--'9|
`------'
""": 9,
"""
.------.
|10.-. |
| :/\\: |
| :\\/: |
| '-'10|
`------'
""": 10,
"""
.------.
|J.--. |
| :(): |
| ()() |
| '--'J|
`------'
""": 11,
"""
.------.
|Q.--. |
| (\\/) |
| :\\/: |
| '--'Q|
`------'
""": 12,
"""
.------.
|K.--. |
| :/\\: |
| :\\/: |
| '--'K|
`------'
""": 13
}

faceValues = {
        'A': 1, 'J': 11, 'Q': 12, 'K': 13,
        '2': 2, '3': 3, '4': 4, '5': 5, '6':6,
        '7': 7, '8':8, '9':9, '10':10
}

win = """
 __     ______  _    _  __          _______ _   _ _ 
 \ \   / / __ \| |  | | \ \        / |_   _| \ | | |
  \ \_/ | |  | | |  | |  \ \  /\  / /  | | |  \| | |
   \   /| |  | | |  | |   \ \/  \/ /   | | | . ` | |
    | | | |__| | |__| |    \  /\  /   _| |_| |\  |_|
    |_|  \____/ \____/      \/  \/   |_____|_| \_(_)                                          
"""

def createDeck():
    Deck = [] 

    for i in range(4):
        for card in faceValues:
            Deck.append(faceValues[card])
    shuffle(Deck)
    return Deck

def war_zone(player1, player2):

    if len(war_one) == 1 or len(war_two) == 1:

        print('\n\n---- WAR CARD ZONE ----')
        for f, v in faceCards.items():
            for a, b in war_one.items():
                if v == b:
                    print(f'\n{player1} card (Player 1): {f}')

        for f, v in faceCards.items():
            for c, d in war_two.items():
                if v == d:
                    print(f'{player2} card (Player 2): {f}') 
        print('-----------------------\n')

def the_rules():
    
    rules = """Each player turns up a card and the player with the 
higher card takes both cards and puts them in won card deck. If both 
players match the cards, it is War. Each player picks two more cards 
including the match card, the last one with the higher number takes all cards 
(six cards). The player with most of the cards will win the game. If you 
match the cards lefting one or two cards from your principal deck, the program 
automatically will pick the random cards from you winner deck. The player with
the fewest cards loses the game and the player with most cards wins the game."""

    play = """1 - The game is for two players.
2 - Each player has to type the name.
3 - Each player turn has to type 'y' or 'Y' to play the game.
4 - If player type 'quit' when is its turn, ends the game.
6 - Be patient and don't despair.
5 - Ok. Let's go and play the game. Good luck."""

    print('\n\n--------------------------- GAME INFORMATION --------------------------')
    print('\nGAME RULES\n\n')
    print(rules)
    print('\n\nHOW TO PLAY\n\n')
    print(play)
    print('\n\nPress Ctrl + C to quit the game information.')
    print('-----------------------------------------------------------------------')


def three_cards(player, flist, flistindex, slist, slistindex, principal):

    print(f'CONGRATULATIONS, {player.upper()} WINS ALL THE CARDS!')
   
    flist += slist
    principal.extend(flist)

    if len(player1list) < 2:

        for index1 in sorted(flistindex, reverse=True):
            del wincards_one[index1]

        player1list.clear()

        if len(player2list) > 2:

            for index2 in sorted(slistindex, reverse=True):
                del player2list[index2]
        else:
            
            for index2 in sorted(slistindex, reverse=True):
                del wincards_two[index2]

            player2list.clear()
    
    elif len(player2list) < 2:

        for index2 in sorted(slistindex, reverse=True):
            del wincards_two[index2]

        player2list.clear()

        if len(player1list) > 2:

            for index1 in sorted(flistindex, reverse=True):
                del player1list[index1]

        else:   

            for index1 in sorted(flistindex, reverse=True):
                del wincards_one[index1]

            player1list.clear()
            
    else:

        for index1 in sorted(flistindex, reverse=True):
            del player1list[index1]
        
        for index2 in sorted(slistindex, reverse=True):
            del player2list[index2]
        


def winner_match(player1, player2, playerlist, winlist):

    print('--------------------------------------------------')
    print(f'{player1} you lose!')
    print(f'CONGRATULATIONS {player2}')
    print(win)
    print('the game.')
    print('--------------------------------------------------')

    ncards = len(playerlist) + len(winlist)

    Player = 1

    play_again()

def play_again():

    while True:

        question = input('\nDo you want to play again? [y/n] ')

        if question == 'y' or question == 'Y':

            del player1list[:]
            del player2list[:]
            del wincards_one[:]
            del wincards_two[:]
            war_one.clear()
            war_two.clear()
            
            main()

        elif question == 'n'or question == 'N':

                print('\nHope you come back soon. Bye bye.')

                quit()
        else: 

            print('\nPlease type \'y\' for yes or \'n\' for no.')


def get_match_cards(playerlist, wincards, random_number, lst, idx, val):

    if Player == 1 or Player == 2:

        if len(playerlist) == 1 and len(wincards) >= 2:
            lst.append(val)
            playerlist.pop(idx)
            rsample = random.sample(list(enumerate(wincards)), 2)
            flistt = [item[1] for item in rsample]
            list_idx = [item[0] for item in rsample]
            lst.extend(flistt)
            random_number.extend(list_idx)
        elif len(playerlist) == 2 and len(wincards) >= 1:
            playerlist.pop(idx)
            lst.append(val)
            rsample = random.sample(list(enumerate(wincards)), 1)
            flistt = [item[1] for item in rsample]
            list_idx = [item[0] for item in rsample]
            sumlists = playerlist + flistt
            lst.extend(sumlists)
            random_number.extend(list_idx)

            for x, y in war_one.items():
                for w, z in war_two.items():
                    if y != z:
                        playerlist.clear()

        else:
            lst.append(val)
            playerlist.pop(idx)
            rsample = random.sample(list(enumerate(playerlist)), 2)
            flistt = [item[1] for item in rsample]
            list_idx = [item[0] for item in rsample]
            lst.extend(flistt)
            random_number.extend(list_idx)

def winner_cards(player1, player2):
    global Player
    
    ff = []
    ss = []
    flist = []
    slist = []

    breaker = False
 
    for x, y in war_one.items():
        for w, z in war_two.items():
            
            if y > z:
                winner = player1 + ' wins both cards!!'
                print(winner.upper())
                wincards_one.extend([y, z])
            
            elif y < z:
                winner = player2 + ' wins both cards!!'
                print(winner.upper())
                wincards_two.extend([y, z])

            elif y == z:
                
                player1list.insert(x, y)
                player2list.insert(w, z)

                #del player1list[x]
                #del player2list[w]

                displaying_cards(player1, player2)

                if len(player1list) == 1 and len(wincards_one) < 2:

                    winner_match(player1, player2, player1list, wincards_one)

                elif len(player2list) == 1 and len(wincards_two) < 2:

                    winner_match(player2, player1, player2list, wincards_two)

                elif len(player1list) == 0 and len(wincards_one) <= 2:
                    
                    winner_match(player1, player2, player1list, wincards_one)
               
                elif len(player2list) == 0 and len(wincards_two) <= 2:
                    
                    winner_match(player2, player1, player2list, wincards_two)

                elif len(player1list) == 2 and len(wincards_one) == 0:
                    
                    winner_match(player1, player2, player1list, wincards_one)
                
                elif len(player2list) == 2 and len(wincards_two) == 0:
                    
                    winner_match(player2, player1, player2list, wincards_two)

                elif len(player1list) == 0 and len(wincards_one) == 0:
                    
                    winner_match(player1, player2, player1list, wincards_one)

                elif len(player2list) == 0 and len(wincards_two) == 0:
                    
                    winner_match(player2, player1, player2list, wincards_two)
                
                else: 

                    print('\nBOTH PLAYERS MATCHING THE CARDS! THIS IS A WAR!!\n')
                    print('-----------------------------------------------------------------------')
                    print('You both are going to pick two more cards from your decks.')
                    print('Including the match card, the third card is greater will win all cards.')
                    print('If in the third card you both match again, nobody wins the cards.')
                    print('-----------------------------------------------------------------------\n\n')

                    while True:
                        qt1 = input(f'{player1}, pick two more cards, please. (Press y or Y): ')

                        if qt1 == 'y' or qt1 == 'Y':
                            
                            get_match_cards(player1list, wincards_one, ff, flist, x, y)

                            print(f'\n--- {player1.upper()} THREE CARDS ---')
                            player_decks(flist) 
                            print('--------------------------\n')


                            while True:
                                qt2 = input(f'{player2}, pick two more cards, please. (Press y or Y): ')
                                
                                if qt2 == 'y' or qt2 == 'Y':
                                    
                                    get_match_cards(player2list, wincards_two, ss, slist, w, z)

                                    print(f'\n--- {player2.upper()} THREE CARDS ---')
                                    player_decks(slist) 
                                    print('------------------------\n')

                                    if flist[2] > slist[2]:
                                        
                                        three_cards(player1, flist, ff, slist, ss, wincards_one)

                                        #displaying_cards(player1, player2)

                                        breaker = True
                                        break 

                                    elif flist[2] < slist[2]:
                                        
                                        three_cards(player2, flist, ff, slist, ss, wincards_two)

                                        #displaying_cards(player1, player2)       

                                        breaker = True
                                        break         

                                    elif flist[2] == slist[2]:
                                        
                                        player1list.insert(x, y)
                                        player2list.insert(w, z)

                                        print('\nYou both match the last card!')
                                        print('Nobody wins the battle.')

                                        breaker = True
                                        break
                                else:
                                    print(f'\n{player2}, please type \'y\'or \'Y\' to select three random cards.\n')
                            
                            if breaker == True:
                                break
                                    
                        else:
                            print(f'\n{player1}, please type \'y\'or \'Y\' to select three random cards.\n')

def player_decks(playerdeck):

    for y in playerdeck:
        for i, v in faceValues.items():
            if y == v:
                y = i
                print(y, end = " ")
    print(f'|Total cards: {len(playerdeck)}|')

def displaying_cards(player1, player2):

    print('\n----------- DECK CARDS -----------')
    print(f'{player1} deck cards: ')
    player_decks(player1list)
    print(f'{player2} deck cards: ')
    player_decks(player2list)

    if len(wincards_one) or len(wincards_two) > 1:
        print('\n\n----------- WON CARDS ------------')
        print(f'{player1} deck cards: ')
        player_decks(wincards_one)
        print(f'{player2} deck cards: ')
        player_decks(wincards_two)  


    if (len(player1list) == 0 and len(wincards_one) > 1):

        print(f'\n{player1}, now you are going to use your win cards deck.')
        
    elif (len(player2list) == 0 and len(wincards_two) > 1):
        
        print(f'\n{player2}, now you are going to use your win cards deck.')
    else:
        pass


def error_message(player):

    message = 'you must type \'y\' or \'Y\' for playing. \nIf you want to end the game, only type \'--quit\'. Try again please!\n'
    print(f'\n{player}, {message}')

def quit_game(player):

    print('\nYou are about to end the game.')

    while True:
        question = input('\nAre you sure you want to end the game? [y/n] ')
        if question == 'y' or question == 'Y':
            print('Quitting the game...')
            time.sleep(1.5)
            print(f'{player} quit the game. Bye bye...')
            quit()
        else:
            if question == 'n' or question == 'N':
                print(f'\n{player}, continue the game.')
                break
            else:
                print('\nPlease make sure you type the right key.')


def displaying_results(player1, player2, q, playerlist, warcard):

    global Player

    breaker = False

    if (q == 'y' or q == 'Y') and (Player == 1 or Player == 2):
        selected_card = secrets.choice(playerlist)
        index = playerlist.index(selected_card)
        if len(war_one) == 0 or len(war_two) == 0:
            warcard.update({index: selected_card})

        else: 

            if Player == 1 and war_one != {}:
                
                warcard.popitem()
                
                if war_one == {}:

                    warcard.update({index: selected_card})

                    if war_two != {}:

                        war_two.popitem()

        for sort_list in sorted(enumerate(playerlist), reverse=True):
            sortlist = list(sort_list)
            if sortlist[0] == index:
                del playerlist[index]
        
        #os.system('clear')
        war_zone(player1, player2)
        winner_cards(player1, player2) 

        if Player == 1:
            
            Player = 2  
        
        else:
            
            Player = 1

        displaying_cards(player1, player2)

    
    elif q == '--help':
        os.system('clear')
        while True:
            os.system('clear')
            try:
                the_rules()
                time.sleep(1)
            except KeyboardInterrupt:
                print ('\r  ')
                print('Type \'--resume\' to return the game.')
                print('Type \'--quit\' to quit the game.')
                
                while True:
                    
                    qt = input('\nDo you want to continue with the game? ')
                    
                    if qt == '--resume':
                        os.system('clear')
                        war_zone(player1, player2)
                        displaying_cards(player1, player2)
                        
                        breaker = True
                        break
                
                    elif qt == '--quit':
                        print('Quitting the game...')
                        time.sleep(1)
                        if Player == 1:
                            print(f'{player1} quit the game. Bye bye...')
                        else:
                            print(f'{player2} quit the game. Bye bye...')
                    
                        quit()

                        breaker = True
                        break
                    else:
                        print('\nPlease insert the keywords to quit or continue with the game.')

                if breaker == True:
                    break

    elif q == '--quit':
        if Player == 1:
            quit_game(player1)
        else:
            quit_game(player2)
    else: 
        if Player == 1:
            error_message(player1)
        else:
            error_message(player2)

def lets_play(player1, player2):

    global Player
    
    cards = createDeck()
    num_cards = len(cards)
    middle_list = num_cards // 2  

    for first_list in cards[:middle_list]:
        player1list.append(first_list)
        
    for second_list in cards[middle_list:]:
        player2list.append(second_list)

    print('\nStarting the game...')
    time.sleep(1.3)
    print('Making decks for players...\n')
    time.sleep(1.3)

    print('--------------------------------------------------------------')
    print('Please read some instructions before playing.')
    print('You can type the keywords \'--help\' or \'--quit\' to end the game.')
    print('--------------------------------------------------------------')

    displaying_cards(player1, player2)

    while True: 
                        
        if ((len(player1list) == 0 and len(wincards_one) > 1) and (len(player2list) == 0 and len(wincards_two) > 1)):
            print('\n\n--------------------')
            print('KEEP GOING PLAYING!!')
            print('May the best win!!')
            print('--------------------')

            player1list.extend(wincards_one)
            player2list.extend(wincards_two)

            wincards_one.clear()
            wincards_two.clear()
        
        elif ((len(player1list) == 0 and len(wincards_one) >= 1) or (len(player2list) == 0 and len(wincards_two) >= 1)):
            
            if len(player1list) == 0 and len(wincards_one) >= 1:
                player1list.extend(wincards_one)
                wincards_one.clear()
            else:
                if len(player2list) == 0 and len(wincards_two) >= 1:
                    player2list.extend(wincards_two)
                    wincards_two.clear()

        else:
            
            if ((len(player1list) == 0 and len(wincards_one) == 0) or (len(player2list) == 0 and len(wincards_two) == 0)):

                if len(player1list) == 0 and len(wincards_one) == 0:
                    print(f'\n{player2},')
                    print(win)
                    print('the game.')

                    Player = 1

                    play_again()
                else:
                    if len(player2list) == 0 and len(wincards_two) == 0:
                        print(f'\n{player1},')
                        print(win)
                        print('the game.')

                        Player = 1

                        play_again()

        if Player == 1: 

            q = input(f'\n{player1}, it\'s your turn. Pick your card (Press y or Y): ')

            displaying_results(player1, player2, q, player1list, war_one)

        else:

            q = input(f'\n{player2}, it\'s your turn. Pick your card (Press y or Y): ')

            displaying_results(player1, player2, q, player2list, war_two)

                       
def main():
    print('\n\n-------------------------------------')
    print('-------- Welcome to WarCards --------')
    print('---- Game made by Luis Salamanca ----')
    print('-------------------------------------\n')

    player1 = input('Please insert name Player 1: ')    
    player2 = input('Please insert name Player 2: ')

    lets_play(player1, player2)

if __name__ == '__main__':
    main()