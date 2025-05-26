from sklearn.tree import DecisionTreeClassifier
import pandas as panda
import matplotlib.pyplot as plots

class DecisionTree:
    def __init__(self):
        self.model = None
        self.visual = None
        self.criterion = 'entropy'
        self.max_depth = 4
        self.data_sets = {'you_total':list(range(8,22))*3, 'dealer': list(range(2,12))*4+[2,3], 'risk':[0, 1, 2]*14, 'future_choices':[]}
    for i in range(len(data_sets['you_total'])):
        you_val = data_sets['you_total'][i]
        dealer_val = data_sets['dealer'][i]
        if you_val <= 10:
            data_sets['future_choices'].append('hit')
        if you_val >= 18:
            data_sets['future_choices'].append('stand')
        else:
            if dealer_val >= 7:
                data_sets['future_choices'].append('hit')
            else:
                data_sets['future_choices'].append('stand')

    def train(self):
        x_coordinate = self.visual[['you_total', 'dealer_initial', 'risk']]
        y_coordinate = self.visual['future_choices']
        self.model = DecisionTreeClassifier(criterion='entropy', max_depth=self.max_depth)
        self.model.fit(x_coordinate, y_coordinate)
    
    def guess_new_card(self, risk, you, dealer):
        return self.model.predict([[you, dealer, risk]])

    def decisions(self):
        for i in range(len(data_sets['you_total'])):
            #risk = Data_Sets.data_sets['risk'][i]
            total_you = data_sets['you_total'][i] 
            dealer_inital = Data_Sets.data_sets['dealer'][i]

            if total_you >= 18: 
               Data_Sets.data_sets['future_choices'].append('stand')
            if total_you <= 11:
                Data_Sets.data_sets['future_choices'].append('hit')
            if 17 >= total_you >= 12 and dealer_inital >= 7:
                Data_Sets.data_sets['future_choices'].append('hit')
            if 17 >= total_you >= 12 and dealer_inital <= 7:
                Data_Sets.data_sets['future_choices'].append('stand')
            else:
                Data_Sets.data_sets['future_choices'].append('hit')
        self.visual= panda.DataFrame(Data_Sets.data_sets)

    def visual_demonstration(self):
        plots.figure(figsize=(10, 21))
        plots.plot_tree(self.model, feature_names = ['you_total', 'dealer_initial', 'risk'], class_names=self.model.classes, filled=True)
        plots.show() 
    
    def case_tests(self, inputs):
        for i in inputs:
            decide = self.guess_new_card(i['risk'], i['you_total'], i['dealer_initial'])
            print(decide)




modelling = DecisionTree()
modelling.decisions()
modelling.train()
modelling.visual_demonstration()
modelling.case_tests([{'you_total': 5, 'dealer_initial': 3, 'risk': 0}])
