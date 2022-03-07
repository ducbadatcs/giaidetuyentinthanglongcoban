if __name__ == "__main__":
    fi = open("BAI6.INP", "r")
    fo = open("BAI6.OUT", "w")
    s = fi.readline()
    fo.write("".join(sorted(s)))
    fi.close()
    fo.close()
    
