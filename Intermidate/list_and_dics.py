def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {'Firstname': 'Luis', 'lastname': 'Cajero'}

    super_list = [
        {'Firstname': 'Luis', 'lastname': 'Cajero'},
        {'Firstname': 'Abril', 'lastname': 'Gonzalez'},
        {'Firstname': 'Leonardo', 'lastname': 'Ibarra'},
        {'Firstname': 'Samantha', 'lastname': 'Soto'},
    ]

    super_dict = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_nums': [-1, -2, -3, 0, 1],
        'floating_nums': [3.1, 5.6, 9.89, 7.8, 8.4]
    }

    for key, value in super_dict.items():
        print(key, ' - ', value)
if __name__ == '__main__':
    run()
