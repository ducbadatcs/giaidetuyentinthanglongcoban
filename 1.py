def sumdigits(n: int) -> int:
    t = 0
    while n > 0:
        t += n%10
        n //= 10
    return t

if __name__ == '__main__':
    fi = open("BAI1.INP", "r")
    fo = open("BAI1.OUT", "w")
    n = int(fi.readline())
    a = [int(i) for i in fi.readline().split()]
    m, idx = a[0], 0
    for i in range(n):
        if sumdigits(a[i]) > sumdigits(m):
            m = a[i]
            idx = i
    fo.write(str(m))
    fi.close()
    fo.close()
