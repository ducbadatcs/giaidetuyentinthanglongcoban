if __name__ == "__main__":
    fi = open("BAI9.INP", "r")
    fo = open("BAI9.OUT", "w")
    st = fi.readline().lower()
    s = fi.readline().replace(" ", "").lower()
    a = []
    for i in s:
        d = 0
        for j in st:
            if i == j:
                d += 1
        a.append(d)
    a = a[:-1]
    fo.write(str(min(a)))
    fi.close()
    fo.close()
