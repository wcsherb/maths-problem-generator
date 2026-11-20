from problem_picker import generateProblems
from tex_generator import writeTex
import os

# generate the problems
problems = generateProblems(2, "linear function") + generateProblems(4, "algebraic equation") + generateProblems(2, "trigonometric equation")
problems = generateProblems(6, "improper fraction") + generateProblems(6, "mixed number")

# put it into LaTeX file
writeTex(problems)

# generate pdf and delete all auxillary files
os.system("pdflatex problem_set.tex")
os.remove("problem_set.log")
os.remove("problem_set.aux")
