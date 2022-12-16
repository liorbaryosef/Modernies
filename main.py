import number_theory_functions as ntf


def q2():
    n = 1000
    a = 456457 % n  # changed to a number Zar to n  as approved by Adi
    b = 7896543
    c = 74365753
    phi_n = 400
    # betha = b % phi_n
    # base = ntf.modular_exponent(a, betha, n)
    exponent = ntf.modular_exponent(b, c, phi_n)
    print(ntf.modular_exponent(a, exponent, n) // 100)
