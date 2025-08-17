# star pyramid example

def pyramid(rows=7):
    for i in range(1, rows+1):
        print(' '*(rows-i) + '*'*(2*i-1))

if __name__ == '__main__':
    pyramid(5)
