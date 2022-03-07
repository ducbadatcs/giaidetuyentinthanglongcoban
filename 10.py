if __name__ == "__main__":
    fi = open("BAI10.INP", "r")
    fo = open("BAI10.OUT", "w")
    s = fi.readline()
    l = len(s.split())
    s = s.replace(" ", "")
    k = len(set(s)) - 1 #ham readline doc ca ky tu \n
    fo.write(str(l) + "\n" + str(k))
    fi.close()
    fo.close()
