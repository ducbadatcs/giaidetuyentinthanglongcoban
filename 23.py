if __name__ == "__main__":
    fi = open("BAI23.INP", "r")
    fo = open("BAI23.OUT", "w")
    from math import ceil
    n = int(fi.readline())
    if n < 3:
        fo.write("9")
    else:
        #[3, 4, 5, 6, 7, 8]
        #[1, 1, 2, 2, 3, 3]
        s = 9 * 10 ** ((n-1) // 2)
        fo.write(str(s))
    fi.close()
    fo.close()
