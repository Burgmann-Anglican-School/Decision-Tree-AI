def activity(d1, d2, y1, y2):
    your_hand = [y1, y2]
    dealer_hand = [d1, d2]
    total = Game(your_hand, dealer_hand, d1, d2, y1, y2)
    total.remove_card()
    total.calculations()
    total.calculations_dealer()
    while True:
        print(total.hit_stand(), total.display())
        total.new_card()
        total.remove_card()
        total.calculations()
        total.calculations_dealer()
        if total.bust() == 'You lost':
            break
    return total

def reset():
    while True:
        tf = str(input('Do you want to play again? (y, n)'))
        if tf == 'y':
            return True
        if tf == 'n':
            return False
        else:
            continue
class Game:
    def __init__(self, your_hand, dealer_hand, d1, d2, y1, y2):
        suits = ['Heart', 'Diamond', 'Club', 'Spade']
        rank = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.all_cards = {'2':4, '3':4, '4':4, '5':4, '6':4, '7':4, '8':4, '9':4, '10':4, 'J':4, 'Q':4, 'K':4, 'A':4}
        self.y1, self.y2, self.d1, self.d2 = y1, y2, d1, d2
        self.hand = your_hand
        self.dealer = dealer_hand
        self.total_you = 0
        self.total_dealer = 0
        self.ace = 0
        self.ace_dealer = 0
    def remove_card(self):
        self.all_cards[self.y1] -= 1
        self.all_cards[self.y2] -= 1
        self.all_cards[self.d1] -= 1
        self.all_cards[self.d2] -= 1
    def hit_stand(self):
        if self.total_you >= 17:
            return 'Stand'
        elif self.total_you <= 11:
            return 'Hit'
        elif self.total_dealer >= 7:
            return 'Hit'
        else:
            return 'Hit'
        
    def display_hand(self):
        print(self.hand)
    def calculations_dealer(self):
        for card in self.dealer:
            try:
                self.total_dealer += int(card)
            except:
                if card != 'Ace':
                    self.total_dealer += 10
                elif card == 'Ace':
                    if self.total_dealer > 11:
                        self.total_dealer += 11
                        ace += 1
                    else:
                        self.total_dealer += 1
        while self.total_dealer > 21 and self.ace_dealer > 0:
            self.total_dealer -= 10

    def calculations(self):
        for card in self.hand:
            if card == '2':
                self.total_you += 2
            if card == '3':
                self.total_you += 3
            if card == '4':
                self.total_you += 4
            if card == '5':
                self.total_you += 5
            if card == '6':
                self.total_you += 6
            if card == '7':
                self.total_you += 7
            if card == '8':
                self.total_you += 8
            if card == '9':
                self.total_you += 9
            elif card == 'K' or card == 'Q' or card == 'J':
                self.total_you += 10
            elif card == 'Ace':
                if self.total_you > 11:
                    self.total_you += 11
                    ace += 1
                else:
                    self.total_you += 1
        while self.total_you > 21 and self.ace > 0:
            self.total_you -= 10
    def __str__(self):
        return(str(self.total_you))
    def new_card(self):
        new_card = str(input('Enter new card: '))
        self.hand.append(new_card)
    def bust(self):
        if self.total_you > 21:
            return 'You lost'

tf = True
while tf:
    d1, d2 = str(input('Dealer hand:')).split()

    y1, y2 = str(input('Your hand:')).split()
    print(d1, d2, y1, y2)
    t = activity(d1, d2, y1, y2)
    print(t)
    tf = reset()
