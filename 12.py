if __name__ == "__main__":
    from math import gcd
    fi = open("BAI12.INP", "r")
    fo = open("BAI12.OUT", "w")
    a, b = map(int, fi.readline().split())
    k = gcd(a, b)
    a //= k
    b //=k
    if a % b != 0:
        c = a // b
        d = a - b * c
        fo.write(str(c) + " " + str(d) + " " + str(b))
    else:
        fo.write(str(a // b))
        fi.close()
        fo.close()
