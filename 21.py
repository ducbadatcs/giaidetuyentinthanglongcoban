if __name__ == "__main__":
    fi = open("BAI21.INP", "r")
    fo = open("BAI21.OUT", "w")
    n = float(fi.readline())
    for i in range(11):
        fo.write(f"Nam thu {i} co {n} dong\n")
        n *= 1.07
    fi.close()
    fo.close()
