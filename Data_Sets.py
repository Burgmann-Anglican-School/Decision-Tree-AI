def data_nodes():
    data_sets = {'you_total':list(range(8,22))*3, 'dealer': list(range(2,12))*4+[2,3], 'risk':[0, 1, 2]*14, 'future_choices':[]}
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
