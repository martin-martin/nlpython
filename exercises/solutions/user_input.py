while True:
    message = input("enter your message: ")
    print(message)

    keep_going = input("more? enter yes/no: ")
    while keep_going not in ['yes', 'no']:
        keep_going = input("enter yes/no: ")
    if keep_going == 'no':
        break
