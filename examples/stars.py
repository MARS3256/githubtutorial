# inverted star pyramid example

def pyramid(rows=7):
    """Create an inverted star pyramid."""
    for i in range(rows, 0, -1):
        print(' ' * (rows - i) + '*' * (2 * i - 1))

if __name__ == '__main__':
    pyramid(7)
