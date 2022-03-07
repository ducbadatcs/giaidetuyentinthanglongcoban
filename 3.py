if __name__ == "__main__":
    fi = open("BAI3.INP", "r")
    fo = open("BAI3.OUT", "w")
    n = int(fi.readline())
    while True:
        if str(n) == str(n)[::-1]:
            break
        else:
            n -= 1
    fo.write(str(n))
    fi.close()
    fo.close()
