if __name__ == "__main__":
    fi = open("BAI17.INP", "r")
    fo = open("BAI17.OUT", "w")
    n = int(fi.readline())
    s = t = 0
    while n > 0:
        s += 1
        t += n % 10
        n //= 10
    fo.write(str(s) + "\n" + str(t))
    fi.close()
    fo.close()
