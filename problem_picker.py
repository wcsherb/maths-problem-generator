import random, sympy
import mathematics

x, y = sympy.symbols('x y')

# Instructions
equationText = "Solve these equations." # text for solving equations
factorizeText = "Factor these equations." # text for factorizing an expression
drawGraphText = "Draw the graph of each function." # text for drawing the graph of a function
simplifyFracText = "Simplify each fraction." # text for simplifying a fraction
sortFracText = "Write the fractions from least to greatest."

# write n problems of a set type
def generateProblems(n, type):
    """Returns a tuple of:
    - instructions
    - latex string for the problem set
    """

    # select function and accompanying text based on problem type
    match type:
        case "algebraic equation":
            problemText = equationText
            problemFunction = mathematics.algebraicEquation
        case "trigonometric equation":
            problemText = equationText
            problemFunction = mathematics.trigEqMix
        case "factorize":
            problemText = factorizeText
            problemFunction = mathematics.factorizeEx
        case "linear function":
            problemText = drawGraphText
            problemFunction = mathematics.linearFunc
        case "quadratic function":
            problemText = drawGraphText
            problemFunction = mathematics.quadraticFunc
        case "hyperbola function":
            problemText = drawGraphText
            problemFunction = mathematics.hyperbolaFunc
        case "trigonometric function":
            problemText = drawGraphText
            problemFunction = mathematics.trigFunc
        case "simplify fraction":
            problemText = simplifyFracText
            problemFunction = mathematics.simplifyFracEx
        case "improper fraction":
            problemText = simplifyFracText
            problemFunction = mathematics.improper_fraction
        case "mixed number":
            problemText = equationText + " " + simplifyFracText
            problemFunction = mathematics.mixed_number
        case "sort fractions":
            problemText = sortFracText
            problemFunction = mathematics.sort_fractions

    string = r"\section*{" + problemText + "}\n"
    string = string + r"\markboth{" + problemText + "}{}\n"
    string = string + r"\thispagestyle{plain}" + "\n"

    # write n number of problems
    for i in range(n):
        string = string + r"        \begin{equation}" + problemFunction() + r"\end{equation}" + "\n"
        string = string + r"        \vspace{4cm}" + "\n"
    
    string = string + r"\newpage" + "\n"

    return string
