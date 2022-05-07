#
#  file: worksheets.py
#
#  Generate practice arithmetic worksheets.  Python 3.
#
#  RTK, 17-Jul-2021
#  Last update:  19-Oct-2021
#
#  Public domain
#
################################################################

import sys
import os
import binascii
import random
from decimal import Decimal
from fractions import Fraction


################################################################
#  Worksheets
#
class Worksheets:
    """Create some worksheets"""

    #-----------------------------------------------------------
    #  Prelude
    #
    def Prelude(self):
        """What comes before"""

        return "\n".join([
                "\\documentclass[12pt]{article}",
                "\\usepackage{geometry}",
                "\\geometry{letterpaper,left=20mm,top=15mm}",
                "\\usepackage{array}",
                "\\newcount\\gpten % (global) power-of-ten -- tells which digit we are doing",
                "\\countdef\\rtot2 % running total -- remainder so far",
                "\\countdef\\LDscratch4 % scratch",
                "\\def\\longdiv#1#2{%",
                " \\vtop{\\normalbaselines \\offinterlineskip",
                "   \\setbox\\strutbox\\hbox{\\vrule height 2.1ex depth .5ex width0ex}%",
                "   \\def\\showdig{$\\underline{\\the\\LDscratch\\strut}$\\cr\\the\\rtot\\strut\\cr",
                "       \\noalign{\\kern-.2ex}}%",
                "   \\global\\rtot=#1\\relax",
                "   \\count0=\\rtot\\divide\\count0by#2\\edef\\quotient{\\the\\count0}%\\show\\quotient",
                "   % make list macro out of digits in quotient:",
                "   \\def\\temp##1{\\ifx##1\\temp\\else \\noexpand\\dodig ##1\\expandafter\\temp\\fi}%",
                "   \\edef\\routine{\\expandafter\\temp\\quotient\\temp}%",
                "   % process list to give power-of-ten:",
                "   \\def\\dodig##1{\\global\\multiply\\gpten by10 }\\global\\gpten=1 \\routine",
                "   % to display effect of one digit in quotient (zero ignored):",
                "   \\def\\dodig##1{\\global\\divide\\gpten by10",
                "      \\LDscratch =\\gpten",
                "      \\multiply\\LDscratch  by##1%",
                "      \\multiply\\LDscratch  by#2%",
                "      \\global\\advance\\rtot-\\LDscratch \\relax",
                "      \\ifnum\\LDscratch>0 \\showdig \\fi % must hide \\cr in a macro to skip it",
                "   }%",
                "   \\tabskip=0pt",
                "   \\halign{\\hfil##\\cr % \\halign for entire division problem",
                "     $\\quotient$\\strut\\cr",
                "     #2$\\,\\overline{\\vphantom{\\big)}%",
                "     \\hbox{\\smash{\\raise3.5\\fontdimen8\\textfont3\\hbox{$\\big)$}}}%",
                "     \\mkern2mu \\the\\rtot}$\\cr\\noalign{\\kern-.2ex}",
                "     \\routine \\cr % do each digit in quotient",
                "}}}",
                "\\begin{document}\n"])


    #-----------------------------------------------------------
    #  Postlude
    #
    def Postlude(self):
        """What comes after"""

        return "\\end{document}\n"


    #-----------------------------------------------------------
    #  Sub
    #
    def Sub(self):
        """Sub two positive integers"""

        A = random.randint(1,3999) + 1000
        B = random.randint(1,A)
        C = A-B

        ans  = "\\vspace{4mm}\n{\\large \\begin{tabular}{cr}\n"
        ans += ("    & \\verb|%d| \\\\" % A) + "\n"
        ans += ("$-$ & \\verb|%d| \\\\" % B) + "\n"
        ans += "\\hline\n"
        ans += "\\end{tabular}}\n\\vspace{29mm}\n"

        sol  = "{\\vspace{4mm}\n\\large \\begin{tabular}{cr}\n"
        sol += ("    & \\verb|%d| \\\\" % A) + "\n"
        sol += ("$-$ & \\verb|%d| \\\\" % B) + "\n"
        sol += "\\hline\n"
        sol += (" & \\verb|%d| \\\\" % C) + "\n"
        sol += "\\end{tabular}}\n\\vspace{23mm}\n"

        return sol, ans


    #-----------------------------------------------------------
    #  SubNice
    #
    def SubNice(self):
        """Sub two positive integers without borrowing"""
        
        A = ""
        for i in range(4):
            A += str(random.randint(1,9))
        b = random.randint(0,int(A[0]))
        if (b == 0):
            B = " "
        else:
            B = str(b)
        for i in range(3):
            B += str(random.randint(0,int(A[i+1])))
        A = int(A)
        B = int(B)
        C = A-B

        ans  = "\\vspace{4mm}\n{\\large \\begin{tabular}{cr}\n"
        ans += ("    & \\verb|%d| \\\\" % A) + "\n"
        ans += ("$-$ & \\verb|%d| \\\\" % B) + "\n"
        ans += "\\hline\n"
        ans += "\\end{tabular}}\n\\vspace{29mm}\n"

        sol  = "{\\vspace{4mm}\n\\large \\begin{tabular}{cr}\n"
        sol += ("    & \\verb|%d| \\\\" % A) + "\n"
        sol += ("$-$ & \\verb|%d| \\\\" % B) + "\n"
        sol += "\\hline\n"
        sol += (" & \\verb|%d| \\\\" % C) + "\n"
        sol += "\\end{tabular}}\n\\vspace{23mm}\n"

        return sol, ans


    #-----------------------------------------------------------
    #  Subm
    #
    def Subm(self):
        """Subtract two positive or negative integers"""

        A = random.randint(-999,999)
        B = random.randint(-999,999)
        C = A-B

        ans  = "\\vspace{4mm}\n{\\large \\begin{tabular}{cr}\n"
        ans += ("    & \\verb|%d| \\\\" % A) + "\n"
        ans += ("$-$ & \\verb|%d| \\\\" % B) + "\n"
        ans += "\\hline\n"
        ans += "\\end{tabular}}\n\\vspace{29mm}\n"

        sol  = "{\\vspace{4mm}\n\\large \\begin{tabular}{cr}\n"
        sol += ("    & \\verb|%d| \\\\" % A) + "\n"
        sol += ("$-$ & \\verb|%d| \\\\" % B) + "\n"
        sol += "\\hline\n"
        sol += (" & \\verb|%d| \\\\" % C) + "\n"
        sol += "\\end{tabular}}\n\\vspace{23mm}\n"

        return sol, ans


    #-----------------------------------------------------------
    #  Addm
    #
    def Addm(self):
        """Add two positive or negative integers"""

        A = random.randint(-999,999)
        B = random.randint(-999,999)
        C = A+B

        ans  = "\\vspace{4mm}\n{\\large \\begin{tabular}{cr}\n"
        ans += ("    & \\verb|%d| \\\\" % A) + "\n"
        ans += ("$+$ & \\verb|%d| \\\\" % B) + "\n"
        ans += "\\hline\n"
        ans += "\\end{tabular}}\n\\vspace{29mm}\n"

        sol  = "{\\vspace{4mm}\n\\large \\begin{tabular}{cr}\n"
        sol += ("    & \\verb|%d| \\\\" % A) + "\n"
        sol += ("$+$ & \\verb|%d| \\\\" % B) + "\n"
        sol += "\\hline\n"
        sol += (" & \\verb|%d| \\\\" % C) + "\n"
        sol += "\\end{tabular}}\n\\vspace{23mm}\n"

        return sol, ans


    #-----------------------------------------------------------
    #  Add2
    #
    def Add2(self):
        """Add two positive integers"""

        A = random.randint(1,3999) + 100
        B = random.randint(1,3999) + 100
        C = A+B

        ans  = "\\vspace{4mm}\n{\\large \\begin{tabular}{cr}\n"
        ans += ("    & \\verb|%d| \\\\" % A) + "\n"
        ans += ("$+$ & \\verb|%d| \\\\" % B) + "\n"
        ans += "\\hline\n"
        ans += "\\end{tabular}}\n\\vspace{29mm}\n"

        sol  = "{\\vspace{4mm}\n\\large \\begin{tabular}{cr}\n"
        sol += ("    & \\verb|%d| \\\\" % A) + "\n"
        sol += ("$+$ & \\verb|%d| \\\\" % B) + "\n"
        sol += "\\hline\n"
        sol += (" & \\verb|%d| \\\\" % C) + "\n"
        sol += "\\end{tabular}}\n\\vspace{23mm}\n"

        return sol, ans


    #-----------------------------------------------------------
    #  Add3
    #
    def Add3(self):
        """Add three positive integers"""

        A = random.randint(1,3999) + 100
        B = random.randint(1,3999) + 100
        C = random.randint(1,3999) + 100
        D = A+B+C

        ans  = "\\vspace{4mm}\n{\\large \\begin{tabular}{cr}\n"
        ans += ("    & \\verb|%d| \\\\" % A) + "\n"
        ans += ("    & \\verb|%d| \\\\" % B) + "\n"
        ans += ("$+$ & \\verb|%d| \\\\" % C) + "\n"
        ans += "\\hline\n"
        ans += "\\end{tabular}}\n\\vspace{26mm}\n"

        sol  = "\\vspace{4mm}\n{\\large \\begin{tabular}{cr}\n"
        sol += ("    & \\verb|%d| \\\\" % A) + "\n"
        sol += ("    & \\verb|%d| \\\\" % B) + "\n"
        sol += ("$+$ & \\verb|%d| \\\\" % C) + "\n"
        sol += "\\hline\n"
        sol += (" & \\verb|%d| \\\\" % D) + "\n"
        sol += "\\end{tabular}}\n\\vspace{20mm}\n"

        return sol, ans


    #-----------------------------------------------------------
    #  Add4
    #
    def Add4(self):
        """Add four positive integers"""

        A = random.randint(1,3999) + 100
        B = random.randint(1,3999) + 100
        C = random.randint(1,3999) + 100
        D = random.randint(1,3999) + 100
        E = A+B+C+D

        ans  = "\\vspace{4mm}\n{\\large \\begin{tabular}{cr}\n"
        ans += ("    & \\verb|%d| \\\\" % A) + "\n"
        ans += ("    & \\verb|%d| \\\\" % B) + "\n"
        ans += ("    & \\verb|%d| \\\\" % C) + "\n"
        ans += ("$+$ & \\verb|%d| \\\\" % D) + "\n"
        ans += "\\hline\n"
        ans += "\\end{tabular}}\n\\vspace{20mm}\n"

        sol  = "\\vspace{4mm}\n{\\large \\begin{tabular}{cr}\n"
        sol += ("    & \\verb|%d| \\\\" % A) + "\n"
        sol += ("    & \\verb|%d| \\\\" % B) + "\n"
        sol += ("    & \\verb|%d| \\\\" % C) + "\n"
        sol += ("$+$ & \\verb|%d| \\\\" % D) + "\n"
        sol += "\\hline\n"
        sol += (" & \\verb|%d| \\\\" % E) + "\n"
        sol += "\\end{tabular}}\n\\vspace{16mm}\n"

        return sol, ans


    #-----------------------------------------------------------
    #  Muls
    #
    def Muls(self):
        """Multi-digit times single-digit"""

        A = 9999 + random.randint(0,9998)
        B = random.randint(2,9)
        C = A*B

        ans  = "\\vspace{4mm}\n{\\large \\begin{tabular}{cr}\n"
        ans += ("          & \\verb|%d| \\\\" % A) + "\n"
        ans += ("$\\times$ & \\verb|%d| \\\\" % B) + "\n"
        ans += "\\hline\n"
        ans += "\\end{tabular}}\n\\vspace{20mm}\n"

        sol  = "\\vspace{4mm}\n{\\large \\begin{tabular}{cr}\n"
        sol += ("          & \\verb|%d| \\\\" % A) + "\n"
        sol += ("$\\times$ & \\verb|%d| \\\\" % B) + "\n"
        sol += "\\hline\n"
        sol += (" & \\verb|%d| \\\\" % C) + "\n"
        sol += "\\end{tabular}}\n\\vspace{16mm}\n"
        return sol, ans


    #-----------------------------------------------------------
    #  Mul1
    #
    def Mul1(self):
        """Single-digit multiplication, all digits"""

        A = random.randint(2,9)
        B = random.randint(2,9)
        C = random.randint(2,9)
        D = random.randint(2,9)
        E = random.randint(2,9)
        F = random.randint(2,9)
        G = random.randint(2,9)
        H = random.randint(2,9)

        ans  = "{\\large \\begin{tabular}{cc}\n"
        ans += "\\ & \\ \\\\\n"
        ans += "\\begin{tabular}{rr} & \\verb|%d| \\\\ $\\times$ & \\verb|%d| \\\\ \\hline & \\\\ \\end{tabular} \\\n" % (A,B)
        ans += "\\begin{tabular}{rr} & \\verb|%d| \\\\ $\\times$ & \\verb|%d| \\\\ \\hline & \\\\ \\end{tabular} \\\n" % (C,D)
        ans += "\\ & \\ \\\\\n"
        ans += "\\ & \\ \\\\\n"
        ans += "\\begin{tabular}{rr} & \\verb|%d| \\\\ $\\times$ & \\verb|%d| \\\\ \\hline & \\\\ \\end{tabular} \\\n" % (E,F)
        ans += "\\begin{tabular}{rr} & \\verb|%d| \\\\ $\\times$ & \\verb|%d| \\\\ \\hline & \\\\ \\end{tabular} \\\n" % (G,H)
        ans += "\\end{tabular}}\n"
        ans += "\\vspace{3mm}\n"

        sol  = "{\\large \\begin{tabular}{cc}\n"
        sol += "\\ & \\ \\\\\n"
        sol += "\\begin{tabular}{rr} & \\verb|%d| \\\\ $\\times$ & \\verb|%d| \\\\ \\hline & \\verb|%d| \\\\ \\end{tabular} \\\n" % (A,B,A*B)
        sol += "\\begin{tabular}{rr} & \\verb|%d| \\\\ $\\times$ & \\verb|%d| \\\\ \\hline & \\verb|%d| \\\\ \\end{tabular} \\\n" % (C,D,C*D)
        sol += "\\ & \\ \\\\\n"
        sol += "\\ & \\ \\\\\n"
        sol += "\\begin{tabular}{rr} & \\verb|%d| \\\\ $\\times$ & \\verb|%d| \\\\ \\hline & \\verb|%d| \\\\ \\end{tabular} \\\n" % (E,F,E*F)
        sol += "\\begin{tabular}{rr} & \\verb|%d| \\\\ $\\times$ & \\verb|%d| \\\\ \\hline & \\verb|%d| \\\\ \\end{tabular} \\\n" % (G,H,G*H)
        sol += "\\end{tabular}}\n"
        sol += "\\vspace{3mm}\n"

        return sol, ans


    #-----------------------------------------------------------
    #  Mul2
    #
    def Mul2(self):
        """Multiply two two-digit integers"""

        A0 = random.randint(0,9)
        A1 = random.randint(1,9)
        A = 10*A1 + A0
        B0 = random.randint(0,9)
        B1 = random.randint(1,9)
        B = 10*B1 + B0
        C = A*B0
        D = A*B1*10

        ans  = "\\vspace{4mm}\n{\\large \\begin{tabular}{cr}\n"
        ans += ("          & \\verb|%d| \\\\" % A) + "\n"
        ans += ("$\\times$ & \\verb|%d| \\\\" % B) + "\n"
        ans += "\\hline\n"
        ans += "\\end{tabular}}\n\\vspace{33mm}\n"

        sol  = "{\\vspace{4mm}\n\\large \\begin{tabular}{cr}\n"
        sol += ("          & \\verb|%d| \\\\" % A) + "\n"
        sol += ("$\\times$ & \\verb|%d| \\\\" % B) + "\n"
        sol += "\\hline\n"
        sol += ("         & \\verb|%d| \\\\" % C) + "\n"
        sol += ("+        & \\verb|%d| \\\\" % D) + "\n"
        sol += "\\hline\n"
        sol += (" & \\verb|%d| \\\\" % (A*B)) + "\n"
        sol += "\\end{tabular}}\n\\vspace{14mm}\n"

        return sol, ans


    #-----------------------------------------------------------
    #  Mul3
    #
    def Mul3(self):
        """Multiply two three-digit integers"""

        A0 = random.randint(0,9)
        A1 = random.randint(0,9)
        A2 = random.randint(1,9)
        A = 100*A2 + 10*A1 + A0
        B0 = random.randint(0,9)
        B1 = random.randint(0,9)
        B2 = random.randint(1,9)
        B = 100*B2 + 10*B1 + B0
        C = A*B0
        D = A*B1*10
        E = A*B2*100

        ans  = "\\vspace{4mm}\n{\\large \\begin{tabular}{cr}\n"
        ans += ("          & \\verb|%d| \\\\" % A) + "\n"
        ans += ("$\\times$ & \\verb|%d| \\\\" % B) + "\n"
        ans += "\\hline\n"
        ans += "\\end{tabular}}\n\\vspace{33mm}\n"

        sol  = "{\\vspace{4mm}\n\\large \\begin{tabular}{cr}\n"
        sol += ("          & \\verb|%d| \\\\" % A) + "\n"
        sol += ("$\\times$ & \\verb|%d| \\\\" % B) + "\n"
        sol += "\\hline\n"
        sol += ("         & \\verb|%d| \\\\" % C) + "\n"
        sol += ("         & \\verb|%d| \\\\" % D) + "\n"
        sol += ("+        & \\verb|%d| \\\\" % E) + "\n"
        sol += "\\hline\n"
        sol += (" & \\verb|%d| \\\\" % (A*B)) + "\n"
        sol += "\\end{tabular}}\n\\vspace{8mm}\n"

        return sol, ans


    #-----------------------------------------------------------
    #  Md
    #
    def Md(self, d):
        """Single-digit multiplication for digit d"""

        A = random.randint(2,9)
        B = random.randint(2,9)
        C = random.randint(2,9)
        D = random.randint(2,9)

        ans  = "{\\large \\begin{tabular}{cc}\n"
        ans += "\\ & \\ \\\\\n"
        ans += "\\begin{tabular}{rr} & \\verb|%d| \\\\ $\\times$ & \\verb|%d| \\\\ \\hline & \\\\ \\end{tabular} \\\n" % (A,d)
        ans += "\\begin{tabular}{rr} & \\verb|%d| \\\\ $\\times$ & \\verb|%d| \\\\ \\hline & \\\\ \\end{tabular} \\\n" % (B,d)
        ans += "\\ & \\ \\\\\n"
        ans += "\\ & \\ \\\\\n"
        ans += "\\begin{tabular}{rr} & \\verb|%d| \\\\ $\\times$ & \\verb|%d| \\\\ \\hline & \\\\ \\end{tabular} \\\n" % (C,d)
        ans += "\\begin{tabular}{rr} & \\verb|%d| \\\\ $\\times$ & \\verb|%d| \\\\ \\hline & \\\\ \\end{tabular} \\\n" % (D,d)
        ans += "\\end{tabular}}\n"
        ans += "\\vspace{3mm}\n"

        sol  = "{\\large \\begin{tabular}{cc}\n"
        sol += "\\ & \\ \\\\\n"
        sol += "\\begin{tabular}{rr} & \\verb|%d| \\\\ $\\times$ & \\verb|%d| \\\\ \\hline & \\verb|%d| \\\\ \\end{tabular} \\\n" % (A,d,A*d)
        sol += "\\begin{tabular}{rr} & \\verb|%d| \\\\ $\\times$ & \\verb|%d| \\\\ \\hline & \\verb|%d| \\\\ \\end{tabular} \\\n" % (B,d,B*d)
        sol += "\\ & \\ \\\\\n"
        sol += "\\ & \\ \\\\\n"
        sol += "\\begin{tabular}{rr} & \\verb|%d| \\\\ $\\times$ & \\verb|%d| \\\\ \\hline & \\verb|%d| \\\\ \\end{tabular} \\\n" % (C,d,C*d)
        sol += "\\begin{tabular}{rr} & \\verb|%d| \\\\ $\\times$ & \\verb|%d| \\\\ \\hline & \\verb|%d| \\\\ \\end{tabular} \\\n" % (D,d,D*d)
        sol += "\\end{tabular}}\n"
        sol += "\\vspace{3mm}\n"

        return sol, ans


    #-----------------------------------------------------------
    #  Dmult
    #
    def Dmult(self):
        """Multiply two decimal numbers"""

        A0 = random.randint(1,9)
        A1 = random.randint(0,9)
        A2 = random.randint(0,9)
        A3 = random.randint(0,9)
        a = random.randint(1,4)
        sA= +1 if (random.random() < 0.5) else -1
        A = 1000*A3 + 100*A2 + 10*A1 + A0
        fa= Decimal(sA*A)*Decimal(10)**Decimal(-a)
        
        B0 = random.randint(1,9)
        B1 = random.randint(1,9)
        b = random.randint(1,4)
        sB= +1 if (random.random() < 0.5) else -1
        B = 10*B1 + B0
        fb= Decimal(sB*B)*Decimal(10)**Decimal(-b)
        
        C = sA*A*sB*B
        fc = fa * fb
        
        D0 = A*B0
        D1 = A*B1*10

        ans  = "\\vspace{4mm}\n{\\large \\begin{tabular}{cr}\n"
        ans += ("          & \\verb|%s| \\\\" % fa) + "\n"
        ans += ("$\\times$ & \\verb|%s| \\\\" % fb) + "\n"
        ans += "\\hline\n"
        ans += "\\end{tabular}}\n\\vspace{33mm}\n"

        sol  = "{\\vspace{4mm}\n\\large \\begin{tabular}{cr}\n"
        sol += ("          & \\verb|%s| \\\\" % fa) + "\n"
        sol += ("$\\times$ & \\verb|%s| \\\\" % fb) + "\n"
        sol += "\\hline\n"
        sol += ("         & \\verb|%d| \\\\" % D0) + "\n"
        sol += ("         & \\verb|%d| \\\\" % D1) + "\n"
        sol += "\\hline\n"
        sol += (" & \\verb|%s| \\\\" % fc) + "\n"
        sol += "\\end{tabular}}\n\\vspace{8mm}\n"

        return sol, ans



    #-----------------------------------------------------------
    #  Div1
    #
    def Div1(self):
        """Single-digit division"""

        D = random.randint(1000,99999)
        d = random.randint(2,9)
        q = D//d
        r = D % d

        ans  = "{\\setlength\\tabcolsep{2pt} \\begin{tabular}{rcl}\n"
        ans += " & & \\\\"
        ans += " \\cline{2-3}\n"
        ans += ("\\verb|%d| & ) & \\verb|%d|" % (d,D)) + "\\\\ \n"
        ans += "\\end{tabular}}\n\\vspace{44mm}\n"

        sol = "{\\small\\quad\\longdiv{%d}{%d}}\\vspace{3mm}\n" % (D,d)

        return sol, ans


    #-----------------------------------------------------------
    #  Divm
    #
    def Divm(self):
        """Multi-digit division"""

        D = random.randint(1000,99999)
        d = random.randint(10,999)
        q = D//d
        r = D % d

        ans  = "{\\setlength\\tabcolsep{2pt} \\begin{tabular}{rcl}\n"
        ans += " & & \\\\"
        ans += " \\cline{2-3}\n"
        ans += ("\\verb|%d| & ) & \\verb|%d|" % (d,D)) + "\\\\ \n"
        ans += "\\end{tabular}}\n\\vspace{44mm}\n"

        sol = "{\\small\\quad\\longdiv{%d}{%d}}\\vspace{3mm}\n" % (D,d)

        return sol, ans


    #-----------------------------------------------------------
    #  Frac1
    #
    def Frac1(self):
        """Single-digit fractions"""
        
        z = [1,2,3,4,5,6,7,8,9]
        random.shuffle(z)
        A,C,_,_,_,_,_,_,_ = z
        z = [2,3,4,5,6,7,8,9]
        random.shuffle(z)
        B,D,_,_,_,_,_,_ = z
        op = ["+","-","\\times","\\div"][random.randint(0,3)]

        if (op == "+"):
            f = Fraction(A,B) + Fraction(C,D)    
        elif (op == "-"):
            f = Fraction(A,B) - Fraction(C,D)    
        elif (op == "\\times"):
            f = Fraction(A,B) * Fraction(C,D)    
        else:
            f = Fraction(A,B) / Fraction(C,D)    

        E,F = f.numerator, f.denominator

        ans  = "\\vspace{4mm}\n"
        ans += "$\\displaystyle\\frac{%d}{%d} %s \\frac{%d}{%d}$\n" % (A,B,op,C,D)
        ans += "\\vspace{6mm}\n"

        sol  = "\\vspace{4mm}\n"
        if (E > 0):
            if (F != 1):
                sol += "$\\displaystyle\\frac{%d}{%d} %s \\frac{%d}{%d} = \\frac{%d}{%d}$\n" % (A,B,op,C,D,E,F)
            else:
                sol += "$\\displaystyle\\frac{%d}{%d} %s \\frac{%d}{%d} = %d$\n" % (A,B,op,C,D,E)
        else:
            if (F != 1):
                sol += "$\\displaystyle\\frac{%d}{%d} %s \\frac{%d}{%d} = -\\frac{%d}{%d}$\n" % (A,B,op,C,D,abs(E),F)
            else:
                sol += "$\\displaystyle\\frac{%d}{%d} %s \\frac{%d}{%d} = %d$\n" % (A,B,op,C,D,E)
        sol += "\\vspace{6mm}\n"

        return sol, ans


    #-----------------------------------------------------------
    #  Pow
    #
    def Pow(self):
        """Multiplication and division with powers"""

        B = [2,3,4,5,6,7,8,9]
        random.shuffle(B)
        B = B[0]

        a = [2,3,4,5,6,7,8,9]
        random.shuffle(a)
        s = [-1,1,1,1,1,1,1,1]
        random.shuffle(s)
        a = a[0] * s[0]
        
        b = [2,3,4,5,6,7,8,9]
        random.shuffle(b)
        s = [-1,1]
        random.shuffle(s)
        b = b[0] * s[0]

        op = ["\\times", "\\div"]
        random.shuffle(op)
        op = op[0]

        ans  = "\\vspace{4mm}\n"
        ans += "$\\displaystyle %d^{%d} %s %d^{%d}$\n" % (B,a,op,B,b)
        ans += "\\vspace{6mm}\n"

        if (op == "\\times"):
            c = a+b
        else:
            c = a-b

        sol  = "\\vspace{4mm}\n"
        sol += "$\\displaystyle %d^{%d} %s %d^{%d} = %d^{%d}$\n" % (B,a,op,B,b,B,c)
        sol += "\\vspace{6mm}\n"

        return sol, ans


    #-----------------------------------------------------------
    #  Pct1
    #
    def Pct1(self):
        """Percent of a number"""

        p = random.randint(1,100)
        n = random.randint(10,1000)
        a = (p/100.0)*n

        ans = "\\vspace{2mm}\\verb|%d|\\%% of \\verb|%d|\n" % (p,n)
        sol = "\\verb|%d|\\%% of \\verb|%d| is \\verb|%0.6f|\n" % (p,n,a)

        return sol, ans


    #-----------------------------------------------------------
    #  Pct2
    #
    def Pct2(self):
        """Percent change"""

        A = random.randint(10,100)
        if (random.random() < 0.5):
            B = A - random.randint(1,A-1)
        else:
            B = A + random.randint(1,A-1)
        p = 100.0*(B-A)/A

        ans = "\\vspace{2mm}from \\verb|%d| to \\verb|%d|\n" % (A,B)
        sol = "(\\verb|%d|-\\verb|%d|)/\\verb|%d| = \\verb|%0.3f|\\%%\n" % (B,A,A,p)

        return sol, ans


    #-----------------------------------------------------------
    #  Problem
    #
    def Problem(self):
        """Return a problem"""

        #  this program grew organically, hence the lame nested-if structure
        if (self.op == "add2"):
            sol, ans = self.Add2()
        elif (self.op == "add3"):
            sol, ans = self.Add3()
        elif (self.op == "add4"):
            sol, ans = self.Add4()
        elif (self.op == "addm"):
            sol, ans = self.Addm()
        elif (self.op == "subm"):
            sol, ans = self.Subm()
        elif (self.op == "sub"):
            sol, ans = self.Sub()
        elif (self.op == "subnb"):
            sol, ans = self.SubNice()
        elif (self.op == "mul1"):
            sol, ans = self.Mul1()
        elif (self.op == "mul2"):
            sol, ans = self.Mul2()
        elif (self.op == "mul3"):
            sol, ans = self.Mul3()
        elif (self.op == "muls"):
            sol, ans = self.Muls()
        elif (self.op[:2] == "md"):
            sol, ans = self.Md(int(self.op[-1]))
        elif (self.op == "div1"):
            sol, ans = self.Div1()
        elif (self.op == "divm"):
            sol, ans = self.Divm()
        elif (self.op == "frac1"):
            sol, ans = self.Frac1()
        elif (self.op == "pow"):
            sol, ans = self.Pow()
        elif (self.op == "dmult"):
            sol, ans = self.Dmult()
        elif (self.op == "pct1"):
            sol, ans = self.Pct1()
        elif (self.op == "pct2"):
            sol, ans = self.Pct2()
        else:
            raise ValueError("Not implemented")

        return sol, ans


    #-----------------------------------------------------------
    #  BuildPage
    #
    def BuildPage(self):
        """Build a page for the given op"""

        sols = []

        header = "\\begin{tabular}{|>{\\centering\\arraybackslash}p{4cm}|>{\\centering\\arraybackslash}p{4cm}|>{\\centering\\arraybackslash}p{4cm}|>{\\centering\\arraybackslash}p{4cm}|}"
        top = "\\hline"
        bot = "\\\\ \\hline\n" 

        if (self.op in ["mul1","md2","md3","md4","md5","md6","md7","md8","md9"]):
            header = "\\begin{tabular}{>{\\centering\\arraybackslash}p{4cm}>{\\centering\\arraybackslash}p{4cm}>{\\centering\\arraybackslash}p{4cm}>{\\centering\\arraybackslash}p{4cm}}"
            top = ""
            bot = "\\\\ \n"
        
        ans = "\n".join([
            "\\begin{center}", header, top])+"\n"

        #  fit more problems per page
        M = 4
        if (self.op == "frac1") or (self.op == "pow"):
            M = 10
        if (self.op == "pct1") or (self.op == "pct2"):
            M = 20
        
        for i in range(M):
            sol, t = self.Problem()
            sols.append(sol)
            ans += t + "&\n" 
            sol, t = self.Problem()
            sols.append(sol)
            ans += t + "&\n" 
            sol, t = self.Problem()
            sols.append(sol)
            ans += t + "&\n" 
            sol, t = self.Problem()
            sols.append(sol)
            ans += t + bot
        ans += "\\end{tabular}\n\\end{center}\n"

        soln = "\n".join([
            "\\begin{center}", header, top])+"\n"
        k = 0
        for i in range(M):
            soln += sols[k] + "&\n"; k += 1 
            soln += sols[k] + "&\n"; k += 1 
            soln += sols[k] + "&\n"; k += 1 
            soln += sols[k] + bot; k += 1 
        soln += "\\end{tabular}\n\\end{center}\n"

        return soln, ans


    #-----------------------------------------------------------
    #  Create
    #
    def Create(self):
        """Do it"""

        #  Build the document
        self.ans = self.Prelude()
        self.soln= self.Prelude()

        for i in range(self.pages):
            soln, ans = self.BuildPage()
            self.ans += ans
            self.soln += soln
            if (i < (self.pages-1)):
                self.ans += "\\newpage\n"
                self.soln += "\\newpage\n"

        self.ans += self.Postlude()
        self.soln += self.Postlude()

        # LaTeX it
        with open(self.output+"_problems.tex","w") as f:
            f.write(self.ans)
        os.system("pdflatex %s_problems.tex" % self.output)
        with open(self.output+"_solutions.tex","w") as f:
            f.write(self.soln)
        os.system("pdflatex %s_solutions.tex" % self.output)


    #-----------------------------------------------------------
    #  __init__
    #
    def __init__(self, op, pages, output):
        """Constructor"""

        self.op = op
        self.pages = pages
        self.output = output


################################################################
#  main
#
def main():
    """Parse command line"""

    if (len(sys.argv) == 1):
        print()
        print("worksheets <op> <pages> <output>")
        print()
        print("  <op>      - the operation (see below)")
        print("  <pages>   - number of pages")
        print("  <output>  - output base name")
        print()
        print("  <op> is one of")
        print("    add2    - two digit integer addition")
        print("    add3    - three digit integer addition")
        print("    add4    - four digit integer addition")
        print("    addm    - mixed-sign addition")
        print("    subm    - mixed-sign addition")
        print("    sub     - multidigit integer subtraction with borrowing")
        print("    subnb   - multidigit integer subtraction without borrowing")
        print("    mul1    - random single-digit multiplication") 
        print("    mul2    - multiply two two-digit integers")
        print("    mul3    - multiply two three-digit integers")
        print("    muls    - single-digit multiplication")
        print("    div1    - single-digit long division")
        print("    divm    - multi-digit long division")
        print("    md?     - multiplication practice for digit ?")
        print("    reduce  - fractions to reduce to lowest terms")
        print("    frac1   - arithmetic with one-digit fractions")
        print("    pow     - multiplication and division with powers")
        print("    dmult   - multiplication of decimal numbers")
        print("    pct1    - percent of a number")
        print("    pct2    - percent change")
        print()
        return

    op = sys.argv[1]
    pages = int(sys.argv[2])
    output = sys.argv[3]

    #  set the seed from /dev/urandom
    random.seed(int(binascii.hexlify(os.urandom(4)),16))

    Worksheets(op, pages, output).Create()


if (__name__ == "__main__"):
    main()

