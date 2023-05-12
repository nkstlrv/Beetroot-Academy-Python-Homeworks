def lst_mult(mult_lst: list):
    m = 1
    for ad_item in mult_lst:
        m = m * ad_item
    return m


def lst_sub(sub_lst: list):
    s = sub_lst
    for s_ind, s_item in enumerate(s):
        if s_ind == len(s) - 1:
            break
        s[0] = s[0] - s[s_ind + 1]
    return s[0]


def lst_add(add_lst: list):
    a = 0
    for a_item in add_lst:
        a = a + a_item
    return a


def lst_div(div_lst: list):
    d = div_lst
    try:
        for d_ind, d_item in enumerate(d):
            if d_ind == len(d) - 1:
                break
            d[0] = d[0] / d[d_ind + 1]
        return d[0]
    except ZeroDivisionError:
        print("\n ERROR"
              "\n You can't divide by ZERO")


###################################################
# Functions test

if __name__ == "__main__":

    print("\n Addition test -->", lst_add([3, 5, 3]))
    print("\n Subtraction test -->", lst_sub([10, 3, 5]))
    print("\n Multiplication test -->", lst_mult([2, 2, 4]))
    print("\n Division test -->", lst_div([16, 1, 0]))
