if __name__ == "__main__":
    fi = open("BAI5.INP", "r")
    fo = open("BAI5.OUT", "w")
    n, k = map(int, fi.readline().split())
    l = [k]
    for i in range(n-2):
        a, b = map(int, fi.readline().split())
        l.append(l[-1] - a + b)
    fo.write(str(max(l)))
    fi.close()
    fo.close()
