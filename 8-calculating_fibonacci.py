import time
fibs = {}
fibs[0] = 0
fibs[1] = 1


def get_pos_fib(pos):
    global fibs
    if pos in fibs:
        result = fibs[pos]
    else:
        result = get_pos_fib(pos - 1) + get_pos_fib(pos - 2)
    fibs[pos] = result
    return result

start = time.time()
for i in range(100):
    result = get_pos_fib(i)
    print(i, ' --- ', result)
end = time.time()
duration = end - start
print('All calculated in', duration, 'secs.' )
