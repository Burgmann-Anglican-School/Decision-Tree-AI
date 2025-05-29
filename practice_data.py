from sklearn.tree import DecisionTreeClassifier #https://www.datacamp.com/tutorial/decision-tree-classification-python
import pandas as panda #https://www.datacamp.com/tutorial/decision-tree-classification-python
import matplotlib.pyplot as plots #https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html
from sklearn.tree import plot_tree #https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html

class Cards: #This is a class to instantiate the total of the cards from the user the dealer and the total amount of cards that exist to show my understanding of classes
    def __init__(self, new_card, dealer_card): #This is an initialiser method to set up initial values for the class
        self.total = 0
        self.dealer_total = 0
        self.you_cards = []
        self.dealer_cards = []
        self.new_card = new_card
        self.dealer_card = dealer_card
        self.aces = 0
        self.dealer_aces = 0
    def add_card_you(self): #This is a method which adds the new card for the total of the user to be returned
        self.you_cards.append(str(self.new_card)) 
        if self.new_card == ('K' or 'Q' or 'J'):
            self.total += 10
        elif self.new_card == 'A':
            self.total += 11
            self.aces += 1
        elif self.total > 21 and self.aces > 0:
            self.total -= 10
            self.aces -= 1 
        elif self.total > 21 and self.aces == 0: #Different conditions to determine what to do with the different totals of the cards
            return False
        return self.total
    def add_card_dealer(self): #Another method but adds total for the dealer
        self.you_cards.append(str(self.dealer_card)) #Adds the new card to the list of all the dealer's cards which exist
        if self.dealer_card.upper() == ('K' or 'Q' or 'J'):
            self.dealer_total += 10
        elif self.dealer_card.upper() == 'A':
            if (self.dealer_total + 11) >= 21:
                self.dealer_total += 1
            else:
                self.dealer_total += 11
                self.dealer_aces += 1
        elif self.dealer_total > 21 and self.dealer_aces > 0:
            self.dealer_total -= 10
            self.dealer_aces -= 1 
        elif self.dealer_total > 21 and self.dealer_aces == 0:
            return False
        return self.dealer_total
    def return_cards(self): #This is a method to return the list back to the user
        return self.you_cards


class DecisionTree: #This is a class to create the decision tree model for blackjack to predict future moves
    def __init__(self):
        self.model = None
        self.visual = None
        self.criterion = 'entropy'
        self.max_depth = 4  
        list_dealer = list(range(2, 12))*4
        list_dealer.append(2)
        list_dealer.append(3)
        data_sets = {'you_total':list(range(8,22))*3, 'dealer_initial': list_dealer, 'risk':(list(range(0, 3)))*14, 'future_choices':[]}  #This is a dictionary which should have the same length in the array, of 42 values otherwise it cannot be used to plot a decision tree
        for i in range(len(data_sets['you_total'])):
            you_val = data_sets['you_total'][i]
            dealer_val = data_sets['dealer_initial'][i]
            if you_val <= 10:
                data_sets['future_choices'].append('hit')
            elif you_val >= 18:
                data_sets['future_choices'].append('stand')
            elif 17 >= you_val >= 11 and dealer_val >= 7:
                data_sets['future_choices'].append('hit')
            else:
                data_sets['future_choices'].append('stand') #This is a decision model to determine which is the best move for each scenario which is then stored in the future moves based upon the input from the user
        self.data_sets = data_sets
    def train(self):
        x_coordinate = self.visual[['you_total', 'dealer_initial', 'risk']]
        y_coordinate = self.visual[['future_choices']]
        self.model = DecisionTreeClassifier(criterion='entropy', max_depth=self.max_depth) #
        self.model.fit(x_coordinate, y_coordinate)
    
    def guess_new_card(self, risk, you, dealer):
        return self.model.predict([[you, dealer, risk]])

    def decisions(self):
        self.visual= panda.DataFrame(self.data_sets)

    def visual_demonstration(self):
        plots.figure(figsize=(10, 21))
        plot_tree(self.model, feature_names = ['you_total', 'dealer_initial', 'risk'], class_names=self.model.classes_, filled=True)
        plots.show() 
    
    def case_tests(self, inputs):
        for i in inputs:
            decide = self.guess_new_card(i['risk'], i['you_total'], i['dealer_initial'])
            return decide

def reset():
    while True:
        play_again = str(input('Would you like to stop playing? (y/n) ')).lower()
        if play_again == 'y':
            return True
        if play_again == 'n':
            return False
        else:
            print('Invalid input')

def stand_hit_decide():
    while True:
        decide = str(input('Do you want to stand or hit? (s, h)'))
        if decide.lower() == 's':
            return False   
        if decide.lower() == 'h':
            return True
        else:
            print('Invalid input')


modelling = DecisionTree()
modelling.decisions()
modelling.train()
modelling.visual_demonstration()

aces = 0
your_initial = str(input('Your initial card 1(Consider, K, Q, J as 10, and A as 11): '))
dealer_initial = str(input('Dealer initial card 1: '))
your_total = Cards(your_initial, dealer_initial).add_card_you()
your_initial = str(input('Your initial card 2(Consider, K, Q, J as 10, and A as 11): '))
dealer_initial = str(input('Dealer initial card 2: '))
dealer_total = Cards(your_initial, dealer_initial).add_card_dealer()
risk = int(input('Risk (0, 1, 2): '))
print(modelling.case_tests([{'you_total': your_total, 'dealer_initial': dealer_initial, 'risk': risk}]))
tf = True
while tf:
    add_total = str(input('Your new card(Consider K, Q, J, A): '))
    your_total = Cards(add_total, dealer_initial).add_card_you()
    all_cards = Cards(add_total, dealer_initial).return_cards()
    if your_total == 21:
        print('You won')
        print(all_cards)
    if your_total == False:
        print('You lost a')
        break    
    risk = int(input('Risk (0, 1, 2): '))
    stand_hit = modelling.case_tests([{'you_total': your_total, 'dealer_initial': dealer_initial, 'risk': risk}])
    print(stand_hit)
    if 'stand' in stand_hit:
        decide = stand_hit_decide()
        if decide:
            tf = reset()
        else:
            tf = False
            dealer = str(input('Dealer stand or hit? '))
            if dealer.lower() == 'stand':
                dealer_final = int(input('What is the dealers final total: '))
                if dealer_final < your_total:
                    print('You won')
                    print(all_cards)
                else:
                    print('You lost')
                    print(all_cards)
                tf = reset()
    else:
        continue