# texts for problems
title = "Practice Problems" # title of document

equationText = "Solve these equations." # text for solving equations
factorizeText = "Factor these equations." # text for factorizing an expression
drawGraphText = "Draw the graph of each function." # text for drawing the graph of a function
simplifyFracText = "Simplify each fraction." # text for simplifying a fraction

# LaTeX settings
language = "latvian" # language for LaTeX babel package

# necessary text
beginning = r"""
\documentclass[12pt,fleqn]{article}
\usepackage{amsmath,scalerel}
 
\setlength\parindent{0pt}
\setlength{\mathindent}{0pt}
\date{\today}

\begin{document}
"""
end = r"""
\end{document}
"""
# function for writing the tex document
def writeTex(problems):
    with open("problem_set.tex","w", encoding="utf-8") as file:
        file.write(beginning)
        file.write(problems)
        file.write(end)
