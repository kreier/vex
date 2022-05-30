import timeit

def for_loop(n=100_000_000):
    s = 0
    for i in range(n):
        s += 1
    return s

def while_loop(n=100_000_000):
    i = 0
    #s = 0
    while i < n:
        #s += 1
        i += 1
    s = i
    return s

def main():
    print('Program started')
    print('while loop \t\t', timeit.timeit(while_loop, number=1))
    print('for loop \t\t', timeit.timeit(for_loop, number=1))

if __name__ == '__main__':
    main()
