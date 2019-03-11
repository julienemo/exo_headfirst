greeting = 'Greeting'


def greet(name, message):
    global greeting
    greeting = 'Hi'
    print(greeting, name + '.', message)


greet('June', 'See you soon!')
print(greeting)
