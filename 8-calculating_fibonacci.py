import time


def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci(pos-2)+fibonacci(pos-1)


for i in range(20, 55, 5):
    start = time.time()
    result = fibonacci(i)
    end = time.time()
    duration = end - start
    print(i, ' --- ', result, ' --- ', duration)
