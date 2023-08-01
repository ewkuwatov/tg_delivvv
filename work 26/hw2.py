import logging

# logging.warning("Hello world")


logging.basicConfig(filename='logs.log',
                    filemode='a',
                    format="%(name)s || %(message)s || %(asctime)s || ")

while True:
    try:
        name = str(input())
        age = int(input())
        print(name, age)
    except ValueError:
        logging.error('Bro, its error!')
        print('Error')