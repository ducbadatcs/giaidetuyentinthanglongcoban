if __name__ == "__main__":
    fi = open("BAI14.INP", "r")
    fo = open("BAI14.OUT", "w")
    k, m, n = map(int, fi.readline().split())
    s = ((n - k) // k + 1) + ((n - m) // m + 1) - ((n - k*m) // (k*m) + 1)
    fo.write(str(s))
    fi.close()
    fo.close()
