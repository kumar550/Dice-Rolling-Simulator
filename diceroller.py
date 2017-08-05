from random import randint

while True:
    number = randint(1, 6)
    print ("your had got a random die number: %s" % number)
    option = raw_input('Do u want to continue: ')

    if option.lower() in ['yes', 'y']:
        continue

    else:
        print ('Quitting now....')
        break
