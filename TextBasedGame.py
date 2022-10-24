#  Brent Artuch

def show_instructions():
    print()
    print('Welcome to the Zombie World War 2 Zombie Apocalypse!!\n')
    print('Collect all six perks to survive the night, else become an')
    print('experiment of Doctor Richtofen!!!')
    print('Move commands: go South, go North, go East, go West')
    print("Purchase Perks from the Machines: get 'Perk Name' ")
    print('To Exit Program Enter: Quit')
    print()

def show_status(current_room, inventory, item):
    print()
    print('You are in the', current_room)
    print('Perks:', inventory)
    print('Perk a Cola Machine:', item)
    print('-' * 30)

def main():
    rooms = {
        'Lobby': {'South': 'Alley', 'North': 'Upper Hall', 'West': 'Theatre', 'Item': 'QuickRevive'},
        'Alley': {'North': 'Lobby', 'West': 'Storage', 'Item': 'DoubleTap'},
        'Upper Hall': {'South': 'Lobby', 'West': 'Foyer', 'Item': 'MuleKick'},
        'Theatre': {'East:': 'Lobby', 'West': 'Stage', 'Item': 'Juggernog'},
        'Storage': {'East': 'Alley', 'Item': 'StaminUp'},
        'Foyer': {'East': 'Upper Hall', 'Item': 'SpeedCola'},
        'Stage': {'East': 'Theatre', 'West': 'Projector Room', 'Item': 'DerWunderfizz'},
        'Projector Room': {'East': 'Stage', 'Item': ''},
    }
    perk_list = ['QuickRevive', 'DoubleTap', 'MuleKick', 'Juggernog', 'StaminUp', 'SpeedCola', 'DerWunderfizz']
    inventory = []
    current_room = 'Lobby'
    show_instructions()

    while True:
        room_item = rooms[current_room]['Item']
        show_status(current_room, inventory, room_item)

        if current_room == 'Projector Room':
            print("You were overwhelmed by the Doctor's creations and have been zombified!!")
            print('Game Over..')
            break
        elif len(inventory) == 7:
            print('With your new found powers, you escape the horde!!')
            print('You Win!')
            break

        next_move = input('Enter your move: \n')
        tokens = next_move.split(' ')

        if (tokens[-1] == 'East' or 'West' or 'North' or 'South') and (tokens[0] == 'go'):
            if tokens[-1] not in rooms[current_room]:
                print("Can't go that way!")
                continue
            current_room = rooms[current_room][tokens[-1]]
        elif (tokens[-1] == rooms[current_room]['Item']) and (tokens[0] == 'get'):
            inventory.append(tokens[-1])
            rooms[current_room]['Item'] = 'Sold Out!!'
            print(tokens[-1], 'retrieved!')
            print()
        elif (tokens[-1] in perk_list) and (tokens[-1] != rooms[current_room]['Item']):
            print("Can't get", tokens[-1] + '!!')
        elif next_move == 'Quit':
            break
        else:
            print('Invalid Input!')

if __name__ == '__main__':
	main()

print('Thank you for playing!!')



