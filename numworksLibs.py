import main
import math

def RepresentsFloat(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def clean_num(reduced_num):
    culprit = '.0'
    reduced_num_str = str(reduced_num)
    if reduced_num_str.endswith(culprit):
        reduced_num_clean = reduced_num_str[:-(len(culprit))]
        reduced_num = int(reduced_num_clean)
    return reduced_num

def clean_den(reduced_den):
    culprit = '.0'
    reduced_den_str = str(reduced_den)
    if reduced_den_str.endswith(culprit):
        reduced_den_clean = reduced_den_str[:-(len(culprit))]
        reduced_den = int(reduced_den_clean)
    return reduced_den

def drop_one_denom(reduced_num):
    return(str(reduced_num))

def simplify_fraction(numer, denom):
    if denom == 0:
        return "Division by 0 - result undefined"

    # Remove greatest common divisor:
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    # Note that reduced_den > 0 as documented in the gcd function.

    if common_divisor == 1:
        reduced_num = clean_num(reduced_num)
        reduced_den = clean_den(reduced_den)

        if reduced_den == 1:
            answer = drop_one_denom(reduced_num)
            return answer
        else:
            return(str(reduced_num)+"/"+str(reduced_den))
    else:
        # Bunch of nonsense to make sure denominator is negative if possible
        if (reduced_den > denom):
            if (reduced_den * reduced_num < 0):
                return(str(-reduced_num)+"/"+str(-reduced_den))
            else:
                return(str(reduced_num)+"/"+str(reduced_den))
        else:
            reduced_num = clean_num(reduced_num)
            reduced_den = clean_den(reduced_den)
            if reduced_den == 1:
                testsVar = drop_one_denom(reduced_num)
                return testsVar
            else:
                return(str(reduced_num)+"/"+str(reduced_den))

def simplify_fraction_quadratic(numer, denom):
    if denom == 0:
        return "Division by 0 - result undefined"

    # Remove greatest common divisor:
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    # Note that reduced_den > 0 as documented in the gcd function.

    if common_divisor == 1:
        return (numer, denom)
    else:
        # Bunch of nonsense to make sure denominator is negative if possible
        if (reduced_den > denom):
            if (reduced_den * reduced_num < 0):
                return(-reduced_num, -reduced_den)
            else:
                return (reduced_num, reduced_den)
        else:
            return (reduced_num, reduced_den)

def quadratic_function(a,b,c):
    if (b**2-4*a*c >= 0):
        x1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
        x2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
        # Added a "-" to these next 2 values because they would be moved to the other side of the equation
        mult1 = -x1 * a
        mult2 = -x2 * a
        (num1,den1) = simplify_fraction_quadratic(a,mult1)
        (num2,den2) = simplify_fraction_quadratic(a,mult2)
        if ((num1 > a) or (num2 > a)):
            # simplify fraction will make too large of num and denom to try to make a sqrt work
            return("No factorization")
        else:
            # Getting ready to make the print look nice
            if (den1 > 0):
                sign1 = "+"
            else:
                sign1 = ""
            if (den2 > 0):
                sign2 = "+"
            else:
                sign2 = ""
            return("({}x{}{})({}x{}{})".format(int(num1),sign1,int(den1),int(num2),sign2,int(den2)))
    else:
        # if the part under the sqrt is negative, you have a solution with i
        return("Solutions are imaginary")

def solve_linear_func(func_name, m, x, b):
    mx = (int(m)*int(x))
    y = int(mx) + int(b)
    return(func_name+"("+str(x)+")= "+str(y))

def find_domain_range_equation(equation):
    if 'x' or 'X' in equation:
        return('Infinite domain and range')

def find_domain_range_ordered(xs, ys):
    sd = ", "
    sr = ", "
    xsu = []
    ysu = []
    for i in xs:
        if i not in xsu:
            xsu.append(i)
    for i in ys:
        if i not in ysu:
            ysu.append(i)
    sd = sd.join(xsu)
    domainstr = "Domain: "+sd
    sr = sr.join(ysu)
    rangestr = "Range: "+sr
    return(domainstr+"\n"+rangestr)

def get_ordered_pair(ordered_pair_num, xs, ys):
    x = 0
    y = 0
    while (x is not None and y is not None):
        x = input("x for point #"+str(ordered_pair_num)+"(sbm): ")
        if (x == ""):
            print("Got empty, quitting...")
            main.page1()
        elif (x != ""):
            if (x == "sbm"):
                if ((xs == []) or (ys == [])):
                    print("Submission can't be empty")
                    get_ordered_pair(ordered_pair_num, xs, ys)
                answer = find_domain_range_ordered(xs, ys)
                x = None
                y = None
                break
            elif (RepresentsFloat(x)):
                print("Loading...")
            elif (any(c.isalpha() for c in x)):
                print("Must be a number!")
                get_ordered_pair(ordered_pair_num, xs, ys)
        y = input("y for point #"+str(ordered_pair_num)+": ")
        if (y == ""):
            print("y cannot be empty")
            get_ordered_pair(ordered_pair_num, xs, ys)
        elif (y != ""):
            if (RepresentsFloat(y)):
                print("loading...")
                ordered_pair_num += 1
            elif (any(c.isalpha() for c in x)):
                print("Must be a number!")
                get_ordered_pair(ordered_pair_num, xs, ys)
        xs += x
        ys += y
    return answer

def solve_pythagorean(solve_var):
    if solve_var == "a":
        b = input("What is your b?\n")
        c = input("What is your c?\n")
        cb2 = float(c)**2 - float(b)**2
        a = round(math.sqrt(cb2), 2)
        return a
    elif solve_var == "b":
        a = input("What is your a?\n")
        c = input("What is your c?\n")
        ca2 = float(c)**2 - float(a)**2
        b = round(math.sqrt(ca2), 2)
        return b
    elif solve_var == "c":
        a = input("What is your a?\n")
        b = input("What is your b?\n")
        ab2 = float(a)**2 + float(b)**2
        c = round(math.sqrt(ab2), 2)
        return c
    else:
        print("Invalid Variable")