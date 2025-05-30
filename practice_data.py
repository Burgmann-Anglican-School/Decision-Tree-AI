from sklearn.tree import DecisionTreeClassifier #https://www.datacamp.com/tutorial/decision-tree-classification-python
import pandas as panda #https://www.datacamp.com/tutorial/decision-tree-classification-python
import matplotlib.pyplot as plots #https://matplotlib.org/3.5.3/api/_as_gen/matplotlib.pyplot.html
from sklearn.tree import plot_tree #https://scikit-learn.org/stable/modules/generated/sklearn.tree.plot_tree.html
#This imports a large amount of libraries to be utilised for the decision tree model, to create the tree and for visulisation

class Cards: #This is an abstract class to instantiate the total of the cards from the user the dealer and the total amount of cards that exist to show my understanding of classes which is then inherited by the input_user and dealer_input classes
    def __init__(self, new_card, dealer_card): #This is an initialiser method to set up initial values for the class
        self.total = 0
        self.dealer_total = 0
        self.aces = 0
        self.dealer_aces = 0
        if new_card != None:
            self.new_card = new_card
        if dealer_card != None:
            self.dealer_card = dealer_card

class User_Inputs(Cards): #This is a child class of cards, which inherits the initial values like new_card, dealer_card, and total from the original class
    def __init__(self, new_card, dealer_initial):
        super().__init__(new_card, None)
        self.you_cards = []
    def add_card_you(self, new_card): #This is a method which adds the new card for the total of the user to be returned
        self.new_card = new_card
        self.you_cards.append(str(self.new_card))
        if self.new_card == 'K' or self.new_card == 'Q' or self.new_card == 'J':
            self.total += 10
        elif self.new_card == 'A':
            self.total += 11
            self.aces += 1
        elif self.new_card in ('2', '3', '4', '5', '6', '7', '8', '9'):
            self.total += int(self.new_card)
        
        while self.total > 21 and self.aces > 0:
            self.total -= 10
            self.aces -= 1 
        return self.total
    def return_cards(self): #This is a method to return the list back to the user
        return self.you_cards
class Dealer_Inputs(Cards): #This is another child class which manages the dealers inputs for their results
    def __init__(self, you_initial, dealer_cards):
        super().__init__(None, dealer_cards) #This accesses the parent class method which is labelled, in this scenario it is the initialiser method which then replaces the values which exist in the main initialiser and provides access to the parent attributes
        self.dealer_cards = []
    def add_card_dealer(self, dealer_card): #Another method but adds total for the dealer
        self.dealer_card = dealer_card
        self.dealer_cards.append(str(self.dealer_card)) #Adds the new card to the list of all the dealer's cards which exist
        if self.dealer_card == 'K' or self.dealer_card == 'Q' or self.dealer_card == 'J':
            self.dealer_total += 10
        elif self.dealer_card == 'A':
            self.dealer_total += 11
            self.dealer_aces += 1
        elif self.dealer_card in ('2', '3', '4', '5', '6', '7', '8', '9'):
            self.dealer_total += int(self.dealer_card)
        
        while self.dealer_total > 21 and self.dealer_aces > 0:
            self.dealer_total -= 10
            self.dealer_aces -= 1 
        return self.dealer_total
    def return_cards(self): #This is a method to return the list back to the user
        return self.dealer_cards


class DecisionTree: #This is a class to create the decision tree model for blackjack to predict future moves
    def __init__(self): #Initialises the class for the initial values to set up the decision tree
        self.model = None
        self.visual = None
        self.criterion = 'entropy' #This is a creteria to determine the best split of the decision tree to be assessed
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
        x_coordinate = self.visual[['you_total', 'dealer_initial', 'risk']] #Handles the inputs from the user which is the independent variables which is then utilised to be compared for the dependent variable
        y_coordinate = self.visual[['future_choices']] #Dependent variable which the model determines what value will be given here
        self.model = DecisionTreeClassifier(criterion='entropy', max_depth=self.max_depth) #Utilised for decision trees to determine if the model is in a good split based upon entropy, and ensuring that data is not overfit by setting the max depth
        self.model.fit(x_coordinate, y_coordinate)  #Trains the model for the x and y coordinates for the inputs
    
    def guess_new_card(self, risk, you, dealer): #This is a method which calls another function to predict the move based upon the current model
        return self.model.predict([[you, dealer, risk]])

    def decisions(self): 
        self.visual= panda.DataFrame(self.data_sets) #Inteprets a dictionary to be better understood and visualised by the DataFrame function

    def visual_demonstration(self): #This will manage what visually the data will look like for the decision tree creation
        plots.figure(figsize=(10, 21)) #This will plot out the decision tree in a certain size from 10 to 21
        plot_tree(self.model, feature_names = ['you_total', 'dealer_initial', 'risk'], class_names=self.model.classes_, filled=True) #This will plot out the tree based upon the different dictionary values, including names which will be included and entropy
        plots.show()  #This will draw the plot on an application to be read for the user
    
    def case_tests(self, inputs): #This is a method where the user provides an input to then input into the model to predict future moves
        for i in inputs:
            decide = self.guess_new_card(i['risk'], i['you_total'], i['dealer_initial'])
            return decide #New stand or hit will be provided based upon success in blackjack

def reset(): #This is a function to determine if the user wants to reset the game or not
    while True:
        play_again = str(input('Would you like to continue playing? (y/n) ')).lower()
        if play_again == 'y':
            return True
        if play_again == 'n':
            return False
        else:
            print('Invalid input')

def stand_hit_decide(): #This is a function which determines whether or not you would like a new card or not and allow for decisions to be made accordingly
    while True:
        decide = str(input('Do you want to stand or hit? (s(stand), h(hit)) '))
        if decide.lower() == 's':
            return False   
        if decide.lower() == 'h':
            return True
        else:
            print('Invalid input')


modelling = DecisionTree() #This creates an instance of this class
modelling.decisions()
modelling.train()
modelling.visual_demonstration() #This is the accessing and utilisation of the class for the modelling from the specific methods which is then utilised later to open up the methods to test values for

your_initial = str(input('Your initial card 1(Consider, K, Q, J as 10, and A as 11): '))
dealer_initial = str(input('Dealer initial card 1: '))
user = User_Inputs(your_initial, dealer_initial)
dealer = Dealer_Inputs(your_initial, dealer_initial)

your_total = user.add_card_you(your_initial)
all_cards = user.return_cards()
print(all_cards, your_total)
dealer_total = dealer.add_card_dealer(dealer_initial)
dealer_cards = dealer.return_cards()
print(dealer_cards, dealer_total)
your_initial = str(input('Your initial card 2(Consider, K, Q, J as 10, and A as 11): '))
dealer_initial = str(input('Dealer initial card 2: '))
your_total = user.add_card_you(your_initial)
all_cards = user.return_cards()
dealer_total = dealer.add_card_dealer(dealer_initial)
print(your_total, all_cards)
risk = int(input('Risk (0, 1, 2): '))
print(modelling.case_tests([{'you_total': your_total, 'dealer_initial': dealer_initial, 'risk': risk}]))
tf = True
while tf:
    your_initial = str(input('Your new card(Consider K, Q, J, A): '))
    your_total = user.add_card_you(your_initial)
    all_cards = user.return_cards()
    print(all_cards, your_total)
    if your_total == 21:
        print('You won')
        print(all_cards)
    if your_total > 21:
        print('You lost')
        break    
    risk = int(input('Risk (0, 1, 2): '))
    stand_hit = modelling.case_tests([{'you_total': your_total, 'dealer_initial': dealer_initial, 'risk': risk}]) #This accesses the instance of the class 'modelling' and then inputs specific inputs from the dictionary to then be inputted which is then accessed to determine the best output whether to hit or stand
    print(stand_hit)
    if 'stand' in stand_hit:
        decide = stand_hit_decide()
        if decide:
            tf = reset()
        else:
            tf = False
            dealer = str(input('Dealer stand or hit? '))
            if dealer.lower() == 's':
                dealer_final = int(input('What is the dealers final total: '))
                if dealer_final < your_total:
                    print('You won')
                    print(all_cards)
                else:
                    print('You lost')
                    print(all_cards)
                tf = reset() #This function allows you to decide whether or not you would like to keep playing
    else:
        continue

#All the above code is an algorithm to manage a game of black jack based upon the inputs from the user to determine whether to play or not