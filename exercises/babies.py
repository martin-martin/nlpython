from pprint import pprint

babies = {'Chloe': '5lbs', 'Hertha': '6lbs',
        'John': '4lbs',
        'Claire': '6lbs',
        'Johnathan': '4lbs',
        'Cleeear': '6lbs',
            'Mum': {
                'John': '4lbs',
                'Claire': '6lbs',
                'Johnathan': '4lbs',
                'Matroschka': {
                    'Harold': '3lbs',
                    'Maude': '3lbs',
                }
            }}

for k, v in babies.items():
    if type(v) == dict:
        print(k)
        pprint(v)
    else:
        print(k, v)

#pprint(babies)
