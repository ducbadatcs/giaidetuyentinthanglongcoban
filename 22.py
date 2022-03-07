if __name__ == "__main__":
    fi = open("BAI22.INP", "r")
    fo = open("BAI22.OUT", "w")
    n = int(fi.readline())
    l = []
    i = 2
    while n > 1:
        while n % i == 0:
            l.append(i)
            n //= i
        i += 1
    #make frequency array since l is already sorted
    k = [0] * (l[-1] + 2)
    for i in l:
        k[i] += 1
    for i in range(len(k)):
        if k[i] > 0:
            fo.write(str(i) + " " + str(k[i]) + "\n")
    fi.close()
    fo.close()

