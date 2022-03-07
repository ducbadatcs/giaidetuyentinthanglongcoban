if __name__ == "__main__":
    fi = open('BAI7.INP', "r")
    fo = open("BAI7.OUT", "w")
    m = int(fi.readline())
    t = 0
    n = 1
    while t <= m:
        t += (-1)**(n+1) * n * (n+1)
        n += 1
    fo.write(str(n-1))
    fi.close()
    fo.close()
