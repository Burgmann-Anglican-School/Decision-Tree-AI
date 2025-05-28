from sklearn.tree import DecisionTreeClassifier
import pandas as panda
import matplotlib.pyplot as plots
from sklearn.tree import plot_tree
import numpy as num

class DecisionTree:
    def __init__(self):
        self.model = None
        self.visual = None
        self.criterion = 'entropy'
        self.max_depth = 4
        list_dealer = list(range(2, 12))*4
        list_dealer.append(2)
        list_dealer.append(3)
        print(len(list_dealer))
        data_sets = {'you_total':list(range(8,22))*3, 'dealer_initial': list_dealer, 'risk':(list(range(0, 3)))*14, 'future_choices':[]}
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
                data_sets['future_choices'].append('stand')
        print(data_sets['future_choices'])
        self.data_sets = data_sets
    def train(self):
        x_coordinate = self.visual[['you_total', 'dealer_initial', 'risk']]
        y_coordinate = self.visual[['future_choices']]
        self.model = DecisionTreeClassifier(criterion='entropy', max_depth=self.max_depth)
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
            print(decide)




modelling = DecisionTree()
modelling.decisions()
modelling.train()
modelling.visual_demonstration()
your_total = int(input('Your total:'))
dealer_initial = int(input('Dealer total: '))
risk = int(input('Risk: '))
print(modelling.case_tests([{'you_total': your_total, 'dealer_initial': dealer_initial, 'risk': risk}]))
