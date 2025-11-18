def order_fruit(input):
    items = list(input.items())
    max_to_min_list = sorted(items, key=lambda item: item[1], reverse=True)
    max_to_min = dict(max_to_min_list)
    print("Order Max to Min:", max_to_min)
    min_to_max_list = sorted(items, key=lambda item: item[1], reverse=False)
    min_to_max = dict(min_to_max_list)
    print("Order Min to Max:", min_to_max)
    
input_data = {'apple':3, 'orange':3, 'pineapple':10, 'bannana':4, 'mango':2}
order_fruit(input_data)
