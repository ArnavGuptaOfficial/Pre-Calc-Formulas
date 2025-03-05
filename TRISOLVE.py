import math

def law_of_sines(a, A, b=None, B=None):
    if b:
        B = math.degrees(math.asin(b * math.sin(math.radians(A)) / a))
    elif B:
        b = a * math.sin(math.radians(B)) / math.sin(math.radians(A))
    return b, B

def law_of_cosines(a, b, C):
    C_rad = math.radians(C)
    return math.sqrt(a**2 + b**2 - 2*a*b*math.cos(C_rad))

def triangle_solver():
    print("Triangle Solver")
    print("1:AAS 2:ASA 3:SAS 4:SSA")
    print("5:SSS 6:AA with Area")
    case = int(input("Case(1-6): "))
    
    if case == 1:
        A = float(input("A(deg): "))
        B = float(input("B(deg): "))
        a = float(input("a: "))
        C = 180 - A - B
        b, _ = law_of_sines(a, A, B=B)
        c = law_of_cosines(a, b, C)
        print(f"C={C:.2f}, b={b:.2f}, c={c:.2f}")
    elif case == 2:
        A = float(input("A(deg): "))
        b = float(input("b: "))
        C = float(input("C(deg): "))
        B = 180 - A - C
        a, _ = law_of_sines(b, B, A=A)
        c = law_of_cosines(a, b, C)
        print(f"B={B:.2f}, a={a:.2f}, c={c:.2f}")
    elif case == 3:
        A = float(input("A(deg): "))
        b = float(input("b: "))
        c = float(input("c: "))
        a = law_of_cosines(b, c, A)
        B = math.degrees(math.asin(b * math.sin(math.radians(A)) / a))
        C = 180 - A - B
        print(f"a={a:.2f}, B={B:.2f}, C={C:.2f}")
    elif case == 4:
        a = float(input("a: "))
        b = float(input("b: "))
        A = float(input("A(deg): "))
        try:
            _, B = law_of_sines(a, A, b=b)
            C = 180 - A - B
            c = law_of_cosines(a, b, C)
            print(f"B={B:.2f}, C={C:.2f}, c={c:.2f}")
        except ValueError:
            print("No solution found.")
    elif case == 5:
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
        A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2*b*c)))
        B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2*a*c)))
        C = 180 - A - B
        print(f"A={A:.2f}, B={B:.2f}, C={C:.2f}")
    elif case == 6:
        A = float(input("A(deg): "))
        B = float(input("B(deg): "))
        a = float(input("a: "))
        C = 180 - A - B
        b, _ = law_of_sines(a, A, B=B)
        c, _ = law_of_sines(a, A, B=C)
        area = 0.5 * a * b * math.sin(math.radians(C))
        print(f"C={C:.2f}, b={b:.2f}, c={c:.2f}, Area={area:.2f}")
    else:
        print("Invalid case!")


