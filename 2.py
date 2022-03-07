if __name__ == "__main__":
    fi = open("BAI2.INP", "r")
    fo = open("BAI2.OUT", "w")
    s = fi.readline() + '1'
    t = 0
    k = []
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            t += 1
        else:
            k.append(t+1)
            t = 0
    fo.write(str(max(k)))
    fi.close()
    fo.close()
