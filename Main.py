#Launch
def launch():
    print('\ndisplay launch message')

def menu_handler(menu):
    print('\n' + menu)
    choice = input('make a choice 1 or 2:\t')
    if choice == '1':
        return 1
    elif choice == '2':
        return 2
    else:
        print('Invalid input. Choose 1 or 2')
        return 0

#Playing
def playing(players):
    print('Playing game')
    return True

#main
#info management
players=[]
player = {'name':'', 'img': 0, 'w2g': '','mask':'','wrong':'','right':'', 'lost':False}
players.append(player)
menu_init = "First menu"
menu_end = "End menu"
#state: Launch
launch()

#state: Menu
loop_x = menu_handler(menu_init)
while loop_x != 2:
    if loop_x == 1:
        playing(players)
        loop_x = 0
    while loop_x == 0:
        loop_x = menu_handler(menu_end)

print("goodbye")
