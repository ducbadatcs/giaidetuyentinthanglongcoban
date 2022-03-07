if __name__ == "__main__":
    fi = open("BAI19.INP", "r")
    fo = open("BAI19.OUT", "w")
    n = int(fi.readline())
    t = 1
    s = 1
    for i in range(1, n+1):
        t *= i
        s += 1/t
    fo.write(str(s))
    fi.close()
    fo.close()

