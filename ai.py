d1, d2 = str(input('Dealer hand:')).split()

y1, y2 = str(input('Your hand:')).split()

t = game(d1, d2, y1, y2)

def game(d1, d2, y1, y2):
    cards = Deck()
    dealer = [d1, d2]
    player = [y1, y2]
    
    total = calculations(player)
    return total

def calculations(hand):
    total = 0
    ace = 0
    for card in hand:
        try:
            total += int(card)
        except:
            if card != 'Ace':
                total += 10
            elif card == 'Ace':
                if total > 11:
                    total += 11
                    ace += 1
                else:
                    total += 1
    while total > 21 and ace > 0:
        total -= 10
    return total


class Deck():
    def __init__(self):
        suits = ['Heart', 'Diamond', 
                 'Club', 'Spade']
        rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
        self.all_cards = []
        for i in suits:
            for a in rank:
                self.all_cards.append((i,a))
