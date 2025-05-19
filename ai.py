initial_hand_dealer = []
initial_hand_you = []

d1, d2 = str(input('Dealer hand:')).split()

y1, y2 = str(input('Your hand:')).split()


def hand_determine(val1, val2, new_val):
    if new_val == None:
        if val1 == 'Ace' and val2 == 'Ace':
            total_possibility = [12, 2]
            return total_possibility
        if val1 == 'Ace' and val2 != 'Ace':
            if val2 == 'king' or val2 == 'jack' or val2 == 'queen' or val2 == '10': 
                total_possibility = [21]
                return total_possibility
        if val2 == 'Ace' and val1 != 'Ace':
            if val1 == 'king' or val1 == 'jack' or val1 == 'queen' or val1 == '10': 
                total_possibility = [21]
                return total_possibility
            