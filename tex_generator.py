
# function for writing the tex document
def writeTex(problems, file_name):
    
    # Beginning and ending text
    beginning = r"""
    \documentclass[12pt, fleqn, leqno]{article}
    \usepackage{amsmath, fancyhdr}
    \pagestyle{fancy}
    \fancyhf{}
    \setlength{\headheight}{14.5pt}
    \addtolength{\topmargin}{-2.5pt}
    \lhead{\leftmark}
    
    \begin{document}
    """
    
    end = r"""
    \end{document}
    """
    with open(file_name,"w", encoding="utf-8") as file:
        file.write(beginning)
        file.write(problems)
        file.write(end)
