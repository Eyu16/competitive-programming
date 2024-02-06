if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    i = [x for x in range(x + 1)]
    j = [y for y in range(y + 1)]
    k = [z for z in range(z + 1)]
    print ([[a, b, c] for a in i for b in j for c in k if sum([a, b, c]) != n])
