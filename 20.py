if __name__ == "__main__":
    fi = open("BAI20.INP", "r")
    fo = open("BAI20.OUT", "w")
    #doc 3 so tren cung 1 dong
    a, b, c = map(float, fi.readline().split())
    if a <= 0 or b <= 0 or c <= 0:
        fo.write(f"{a}, {b}, {c} khong phai la 3 canh cua 1 tam giac")
    if a + b <= c or a + c <= b or b + c <= a:
        fo.write(f"{a}, {b}, {c} khong phai la 3 canh cua 1 tam giac")
    else:
        vuong = a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a
        tu = a*a + b*b < c*c or a*a + c*c < b*b or b*b + c*c < a*a
        deu = a == b == c
        can = (a == b or b == c or a == c) and not deu
        if vuong and can:
            fo.write(f"{a}, {b}, {c} la 3 canh cua 1 tam giac vuong can")
        elif tu and can:
            fo.write(f"{a}, {b}, {c} la 3 canh cua 1 tam giac tu can")
        elif vuong:
            fo.write(f"{a}, {b}, {c} la 3 canh cua 1 tam giac vuong")
        elif tu:
            fo.write(f"{a}, {b}, {c} la 3 canh cua 1 tam giac tu")
        elif deu:
            fo.write(f"{a}, {b}, {c} la 3 canh cua 1 tam giac deu")
        elif can:
            fo.write(f"{a}, {b}, {c} la 3 canh cua 1 tam giac can")
        else:
            fo.write(f"{a}, {b}, {c} la 3 canh cua 1 tam giac thuong")
    fi.close()
    fo.close()
