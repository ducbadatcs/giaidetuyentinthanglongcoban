if __name__ == "__main__":
    fi = open("BAI16.INP", "r")
    fo = open("BAI16.OUT", "w")
    n = int(fi.readline())
    s = bin(n)[2:]
    fo.write(s + "\n")
    k = int("0b" + "".join(sorted(s, reverse = True)), 2)
    fo.write(str(k))
    fi.close()
    fo.close()



