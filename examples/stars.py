# inverted star pyramid example

def pyramid(rows=5):
    for i in range(rows, 0, -1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))

if __name__ == '__main__':
    pyramid(5)
