from sklearn.tree import DecisionTreeClassifier
import pandas as panda
import Data_Sets
import matplotlib.pyplot as plots

class DecisionTree:
    def __init__(self):
        self.model = None
        self.visual = None
        self.criterion = 'entropy'
        self.max_depth = 4

    def train(self):
        x_coordinate = self.visual['you_total']
        y_coordinate = self.visual['future_choices']
        self.model = DecisionTreeClassifier(criterion='entropy', max_depth=self.max_depth)
        self.model.fit(x_coordinate, y_coordinate)
    
    def guess_new_card(self, risk, you, dealer):
        return self.model.predict([[you, dealer, risk]])

    def decisions(self):
        for i in range(len(Data_Sets.data['future_choices'])):
            risk = Data_Sets.data['risk'][i]
            total_you = Data_Sets.data['you_total'][i] 
            dealer_inital = Data_Sets.data['dealer'][i]

            if total_you >= 18: 
               Data_Sets.data_sets['Future_choices'].append('stand')
            if total_you <= 11:
                Data_Sets.data_sets['Future_choices'].append('hit')
            if 18 >= total_you >= 11 and dealer_inital >= 7:
                Data_Sets.data_sets['Future_choices'].append('hit')
            if 18 >= total_you >= 11 and dealer_inital <= 7:
                Data_Sets.data_sets['Future_choices'].append('stand')
            else:
                Data_Sets.data_sets['Future_choices'].append('hit')
        self.visual= panda.DataFrame(Data_Sets.data_sets)

    def visual_demonstration(self):
        plots.figure(figsize=(0, 21))
        plots.plot_tree(self.model, values = ['total_you', 'dealer_initial', 'risk'], names=self.model.classes, filled=True)
        plots.show() 

