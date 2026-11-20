import random
from sympy import sin, cos, symbols, Rational, latex, expand, sqrt, pi, expand, simplify, UnevaluatedExpr

x, y = symbols('x y')

# change the sign of the number w 50% probability
def sign(n):
    a=random.randrange(2)

    if a == 1:
        n = - 1 * n

    return n

# turn expression into equation
def equify(string):
    return string + " = 0"

############################### ELEMENTARY SCHOOL #####################

def improper_fraction():
  
  # Experiencing this bug
  # https://github.com/python/cpython/issues/95303
  # Avoiding random.randint()
  
  denom_list = [2, 3, 4, 5, 6, 7, 8]
  denom = random.sample(denom_list, 1)
  denom = denom[0]
  
  whole_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  whole_number = random.sample(whole_list, 1)
  whole_number = whole_number[0]
  
  numerator_base = whole_number * denom
  extra_list = list(range(1,denom))
  num_extra = random.sample(extra_list, 1)
  num_extra = num_extra[0]
  numerator = numerator_base + num_extra
  
  ex = r"\frac{" + str(numerator) + "}{" + str(denom) + "}"
  
  return ex


def mixed_number():
  
  same_denom = [True, False]
  same_denom = random.sample(same_denom, 1)
  same_denom = same_denom[0]
  
  whole_urn = [2, 3, 4, 5, 6, 7, 8, 9, 10]
  whole_a = random.sample(whole_urn, 1)
  whole_a = whole_a[0]
  whole_urn = list(range(1,whole_a))
  whole_b = random.sample(whole_urn, 1)
  whole_b = whole_b[0]
  whole_list = [whole_a, whole_b]
  # Larger whole number should come first
  whole_list.sort()
  whole_1 = whole_list[1]
  whole_2 = whole_list[0]
  
  if same_denom:
    denom_list = [2, 3, 4, 5, 6, 7, 8]
    denom = random.sample(denom_list, 1)
    denom_1 = denom_2 = denom[0]
    
    num_urn = list(range(1,denom_1))
    num_a = random.sample(num_urn, 1)
    num_b = random.sample(num_urn, 1)
    num_list = [num_a[0], num_b[0]]
    num_list.sort()
    # Smaller denominator comes first to force borrowing from whole number
    num_1 = num_list[0]
    num_2 = num_list[1]
  else:
    denom_a_list = [2, 3, 4, 5]
    denom_a = random.sample(denom_a_list, 1)
    denom_a = denom_a[0]
    
    multiplier = random.sample(denom_a_list, 1)
    multiplier = multiplier[0]
    denom_b = denom_a * multiplier
    
    num_a_urn = list(range(1, denom_a))
    num_a = random.sample(num_a_urn, 1)
    num_a = num_a[0]
    num_b_urn = list(range(1, denom_b))
    num_b = random.sample(num_b_urn, 1)
    num_b = num_b[0]
    
    num_dict = {"a": num_a, "b": num_b}
    denom_dict = {"a": denom_a, "b": denom_b}
    frac_dict = {"a": num_a / denom_a, "b": num_b / denom_b}
    
    # Fractions should be in descending order to force borrowing
    sorted_dict = dict(sorted(frac_dict.items(), key=lambda item: item[1]))
    key_list = [k for k, v in sorted_dict.items()]
    
    key_1 = key_list[0]
    key_2 = key_list[1]
    
    num_1 = num_dict[key_1]
    num_2 = num_dict[key_2]
    denom_1 = denom_dict[key_1]
    denom_2 = denom_dict[key_2]
    
  ex_1 = str(whole_1) + r"\frac{" + str(num_1) + "}{" + str(denom_1) + "}"
  ex_2 = str(whole_2) + r"\frac{" + str(num_2) + "}{" + str(denom_2) + "}"
  
  return ex_1 + " - " + ex_2
  
############################### TOPIC 0 ###############################
# problems that are taught in middle school

# common factor / kopīgais reizinātājs
def commonFacEx():
    # generate random non zero coefficients a and b; n and m - powers of x
    a = sign(random.randrange(1,10))
    b = sign(random.randrange(1,4))
    n = random.randrange(1,4)
    m = random.randrange(1,4)
    
    # generate the expression analytically
    ex = expand(a * x ** n * (x ** m + b ** m))
    return ex

# grouping / grupēšanas paņēmiens
def groupingEx():
    # random small coefficients
    a = sign(random.randrange(1,4))
    b = sign(random.randrange(1,4))
    c = sign(random.randrange(1,4))
    # generate random DIFFERENT powers of x
    n = random.randrange(1,5)
    m = random.randrange(1,5)
    while n == m:
        m = random.randrange(1,3)

    ex = expand((a * x ** n + b) * (x ** m + c))
    return ex

# linear function
def linearFunc():
    a = sign(random.randrange(11))
    b = sign(random.randrange(1,6))
    c = sign(random.randrange(6))
    k = random.randrange(2)

    # choose form y = kx + b or Ax + Bx + C based on k
    if k == 0:
        ex = "y = " + latex(Rational(a,b) * x + c)
    else:
        ex = latex(a * x + b * y + c) + " = 0"

    return ex

# graph for quadratic function y = ax^2 + bx + c
def quadraticFunc():
    k = random.randrange(1,4) # this is for denominator for a
    a = sign(random.randrange(1,6))
    b = sign(random.randrange(6))
    c = sign(random.randrange(6))
    return "y = " + latex(Rational(a, k) * x ** 2 + b * x + c)

############################### END ###############################

############################### TOPIC 1: VECTORS ###############################
############################### END ###############################

############################### TOPIC 2: LINEAR FUNCTION ###############################
############################### END ###############################

############################### TOPIC 3: COMBINATORICS AND GRAPHS ###############################
############################### END ###############################

############################### TOPIC 4: STATISTICS ###############################
############################### END ###############################

############################### TOPIC 5: EQUATIONS, ALGEBRAIC FRACTIONS AND THEIR GRAPHS ###############################°

# for formula a^3 +/- b^3
def cubeEx():
    # generate two relatively small non zero coefficients for my equations
    a = sign(random.randrange(1,4))
    b = sign(random.randrange(1,5))

    ex = expand((a * x) ** 3 + b ** 3)
    return ex

# randomly pick one of the three factorizable expression types
def factorizeEx():
    k = random.randrange(3)

    match k:
        case 0:
            return latex(commonFacEx())
        case 1:
            return latex(cubeEx())
        case 2:
            return latex(groupingEx())

# equation of the form ax^4 + bx^2 + c = 0
def substitution():
    # generate the twoo roots
    a = sign(random.randrange(9))
    b = sign(random.randrange(9))

    return latex(expand((x ** 2 - a) * (x ** 2 - b)))

# simple edge case where students would use graphs to solve the equation
def graphEq():
    a = sign(random.randrange(4))
    b = sign(random.randrange(10))

    # pick the type of edge case - sqrt(x), x^3 or x^4
    k = random.randrange(3)
    match k:
        case 0:
            ex = x ** 3
        case 1:
            ex = sqrt(x)
        case 2:
            ex = x ** 4

    return latex(ex) + " = " + latex(a * x + b)

# call random type of equation
def algebraicEquation():
    k = random.randrange(3)

    match k:
        case 0:
            return equify(factorizeEx())
        case 1:
            return equify(substitution())
        case 2:
            return graphEq()

# graph for algebraic fractions (hyperbola)
def hyperbolaFunc():
    k = sign(random.randrange(1,13))
    a = random.randrange(1,3)
    b = sign(random.randrange(6))
    c = sign(random.randrange(6))
    ex = "y = " + latex(k / (a * x - b) + c)
    return ex

# generate one factor of an expression to be factorized
def polynomialEx():
    k = random.randrange(7)

    match k:
        case 0:
            ex = sign(random.randrange(2,9))
        case 1:
            ex = x ** random.randrange(1,5)
        case 2:
            a = sign(random.randrange(1,5))
            ex = x ** 2 - x * a + a ** 2
        case 3:
           a = sign(random.randrange(1,5))
           ex = x ** 2 + a
    if k > 3:
        ex = sign(1) * x - sign(random.randrange(7))

    return ex

# generate a fraction in such a way that it can be simplified
def simplifyFracEx():
    ex = polynomialEx()
    return latex(UnevaluatedExpr(simplify(ex * polynomialEx()) / simplify(ex * polynomialEx())))


############################### END ###############################

############################### TOPIC 6: EQUATIONS WITH FRACTIONS ###############################
############################### END ###############################

############################### TOPIC 7: SIN AND COS FUNCTIONS ###############################

# pick a root from 0, 1/2, sqrt(2)/2, sqrt(3)/2 and 1 
def trigRoot():
    k = random.randrange(7)
    if k < 3:
        return 0
    elif k == 3:
        return sign(Rational(1,2))
    elif k == 4:
        return sign(sqrt(2)/2)
    elif k == 5:
        return sign(sqrt(3)/2)
    elif k == 6:
        return sign(1)

# typical radian value generator
def trigValue():
    k = random.randrange(5)
    match k:
        case 0:
            return 0
        case 1:
            return sign(pi)/2
        case 2:
            return sign(pi)/3
        case 3:
            return sign(pi)/4
        case 4:
            return sign(pi)/6

# pick a trig function between sin and cos
def trigSinCos(y):
    k = random.randrange(2)
    match k:
        case 0:
            return sin(y)
        case 1:
            return cos(y)

# generate a sin or cos function with deformations
def trigFunc():  
    a = random.randrange(1,4)
    b = random.randrange(1,4)
    c = trigValue()

    # expression inside sin or cos
    ex = "y = " + latex(a * trigSinCos(b * x - c) + trigRoot())
    return ex
############################### END ###############################

############################### TOPIC 8: TRIGONOMETRIC EXPRESSIONS AND EQUATIONS ###############################

# trigonometric equation in normal(?) format
def basicTrigEq():
    eq = latex(trigSinCos(x)) + " = " + latex((trigRoot()))
    return eq

# generic trigonometric equation w multiple steps
def trigEq():
    a = random.randrange(1,4)
    b = random.randrange(1,4)
    c = trigValue()

    # expression inside sin or cos
    eq = latex(a * trigSinCos(b * x - c)) + " = " + latex(trigRoot() * a)
    return eq

# trigonometric equations to be solved by substitution (or sometimes factorization)
def trigSubs():
    # get two roots for quadratic equation
    a = trigRoot()
    b = trigRoot()

    # get the trig function

    eq = equify(latex(expand((x - a)*(x - b)).subs(x,trigSinCos(x))))
    return eq

# randomly pick a type of trig equation
def trigEqMix():
    k = random.randrange(3)
    match k:
        case 0:
            return basicTrigEq()
        case 1:
            return trigSubs()
        case 2:
            return trigEq()
############################### END ###############################
