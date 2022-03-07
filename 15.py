if __name__ == "__main__":
    fi = open("BAI15.INP", "r")
    fo = open("BAI15.OUT", "w")
    n = int(fi.readline())
    l = list(map(int, fi.readline().split()))
    a = b = l[0]
    for i in range(n):
        if l[i] < a:
            a = l[i]
        elif l[i] > b:
            b = l[i]
        else:
            continue
    fo.write(str(a + b))
    fi.close()
    fo.close()
