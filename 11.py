if __name__ == "__main__":
    fi = open("BAI11.INP", "r")
    fo = open("BAI11.OUT", "w")
    ng, th, na = map(int, fi.readline().split())
    if th == 2:
        if na % 400 == 0 or (na % 4 == 0 and na % 100 != 0):
            if ng == 29:
                ng = 1
                th = 3
            else:
                ng += 1
        else:
            if ng == 28:
                ng = 1
                th = 3
            else:
                ng += 1
    elif th == 12:
        if ng == 31:
            ng = th = 1
            na += 1
        else:
            ng += 1
    elif th in [1, 3, 5, 7, 8, 10]:
        if ng == 31:
            ng = 1
            th += 1
        else:
            ng += 1
    else:
        if ng == 30:
            ng = 1
            th += 1
        else:
            ng += 1
    fo.write(str(ng) + " " + str(th) + " " + str(na))
    fi.close()
    fo.close()






