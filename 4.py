if __name__ == "__main__":
    fi = open("BAI4.INP", "r")
    fo = open("BAI4.OUT", "w")
    a, b, c = map(int, fi.readline().split())
    fo.write(str(c - (a%c + b%c)%c))
    fi.close()
    fo.close()
