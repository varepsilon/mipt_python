def inc(x):
    print(type(x))
    if x == 0:
        return 0
    x += 1
    return x

if __name__ == '__main__':
    print('Hello, world!')
    print(inc(2))
    someList = [1, 2]
    someList += [3, 4]
    print(someList)