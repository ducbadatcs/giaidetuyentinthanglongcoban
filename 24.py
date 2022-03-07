def opnum(n):
    s = str(n)
    return s == s[::-1]

if __name__ == "__main__":
    fi = open("BAI24.INP", "r")
    fo = open("BAI24.OUT", "w")
    l = list(fi.readlines())
    for i in l:
        t = 0
        l, r = map(int, i.split())
        for j in range(l, r+1):
            if opnum(j):
                t += 1
        fo.write(str(t) + "\n")
    fi.close()
    fo.close()


