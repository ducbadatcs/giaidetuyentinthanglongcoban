if __name__ == "__main__":
    from math import gcd
    fi = open("BAI13.INP", "r")
    fo = open("BAI13.OUT", "w")
    a, b = map(int, fi.readline().split())
    k = gcd(a, b)
    a //= k
    b //= k
    fo.write(str(a) + " " + str(b))
    fi.close()
    fo.close()
    
