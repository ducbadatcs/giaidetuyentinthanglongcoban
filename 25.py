if __name__ == "__main__":
    fi = open("BAI25.INP", "r")
    fo = open("BAI25.OUT", "w")
    h, m, s = map(int, fi.readline().split())
    s += 5
    if s >= 60:
        s -= 60
        m += 1
    if m == 60:
        m = 0
        h += 1
    if h == 24:
        h = 0
    fo.write(str(h) + ":" + str(m) + ":" + str(s))
    fi.close()
    fo.close()
