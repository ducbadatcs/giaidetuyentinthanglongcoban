def soboi(k: int, n: int):
    s = ((n - k) // k + 1)
    if s <= 0:
        return 0
    return s

if __name__ == "__main__":
    fi = open("BAI18.INP", "r")
    fo = open("BAI18.OUT", "w")
    k = int(fi.readline())
    m = int(fi.readline())
    n = int(fi.readline())
    a = soboi(m, n) + soboi(k, n) - soboi(k*m, n)
    fo.write(str(a))
    fi.close()
    fo.close()
