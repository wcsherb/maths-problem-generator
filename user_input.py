from problem_picker import generateProblems
from tex_generator import writeTex
import os

file_names = ["math_practice_1", "math_practice_2"]

for file_name in file_names:

  # generate the problems
  problems = generateProblems(2, "linear function") + generateProblems(4, "algebraic equation") + generateProblems(2, "trigonometric equation")
  problems = generateProblems(6, "improper fraction") + generateProblems(6, "mixed number") + generateProblems(6, "sort fractions")
  
  # put it into LaTeX file
  writeTex(problems, f"{file_name}.tex")
  
  # generate pdf and delete all auxillary files
  os.system(f"pdflatex {file_name}.tex")
  os.remove(f"{file_name}.log")
  os.remove(f"{file_name}.aux")
