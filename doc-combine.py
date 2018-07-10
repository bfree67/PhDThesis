# -*- coding: utf-8 -*-
"""

A little utility to combine all 5 LaTex chapters into one document
that can be then easily copied into a single LaTex document for comparison
using Latexdiff.

10 Jul 2018


##################################
for original thesis use:
chapters = ["Chapter1_Intro-lt.tex", 
            "Chapter2_ProblemDescription-lt.tex", 
            "Chapter3_Methodology-lt.tex",
            "Chapter4_Results-lt.tex",
            "Chapter5_Conclusions-lt.tex"]
"""
import io
import datetime

chapters = ["Chapter1_Intro.tex", 
            "Chapter2_ProblemDescription.tex", 
            "Chapter3_Methodology.tex",
            "Chapter4_Results.tex",
            "Chapter5_Conclusions.tex"]

outputfile = "fileout" + datetime.datetime.today().strftime('%Y-%m-%d') + ".tex"

fulltext = ""

for chap in chapters:
    
    with io.open(chap, "r", encoding="utf8") as filein:
        text = filein.read()
        filein.close()
        
    fulltext += text

with io.open(outputfile, "w", encoding="utf8") as output:
    output.write(fulltext)

print("Combined file saved in: ", outputfile)