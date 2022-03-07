if __name__ == "__main__":
    fi = open("BAI8.INP", "r")
    fo = open("BAI8.OUT", "w")
    h, m, s = map(int, fi.readlines())
    s += 5
    if s > 60:
        s -= 60
        m += 1
    if m == 60:
        m = 0
        h += 1
    if h == 24:
        h = 0
    fo.write(str(h) + "\n" + str(m) + "\n" + str(s))
    fi.close()
    fo.close()

