import tkinter as tk
from tkinter import scrolledtext
from random import randint, random
from math import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from cmath import sin as csin
from cmath import cos as ccos
from cmath import pi as cpi
from cmath import e as ce
from cmath import phase
from cmath import sqrt as csqrt
from cmath import log as clog
from cmath import log10 as clog10
from sympy import *

root = tk.Tk()
root.title("Calculator")
root.iconbitmap("C:/My files/Coding/programming_main/New projects _py/Calculator/icon.ico")
root.geometry("300x300")
root.config(bg="#0E96CC")

Output = tk.Entry(root, bg="white", fg="black", width=40, justify=tk.RIGHT)
Hints = tk.Label(root, bg="white", fg="black", text="Hint : ")
Trigomode = tk.Label(root, bg="#C468BE", fg="black", text="Trigo Calculations are in rad")
welcometxt = tk.Label(root, bg=root.cget('bg'), fg="black", text="Welcome , choose a mode in the Mode menu")

# Pads :

numberpad = tk.Frame(root, bg="#0E96CC", width=150, height=300)
scientificpad = tk.Frame(root, bg="#C468BE")
arithmeticpad = tk.Frame(root, bg="#D49E22")
functionspad = tk.Frame(root, bg="#333B80")
complexpad = tk.Frame(root, bg="#81FF61")
equationpad = tk.Frame(root, bg="#F6FF00")

# Normal mode :


def insert_Number(i):
    Output.insert(tk.END, str(i))


def insert_0():
    Output.insert(tk.END, "0")


def insert_comma():
    Output.insert(tk.END, ".")


def insert_add():
    Output.insert(tk.END, "+")


def insert_minus():
    Output.insert(tk.END, "-")


def insert_mutiply():
    Output.insert(tk.END, "*")


def insert_divide():
    Output.insert(tk.END, "/")


def insert_oppar():
    Output.insert(tk.END, "(")


def insert_clopar():
    Output.insert(tk.END, ")")


def insert_c():
    Output.delete(0, tk.END)


def insert_back():
    current = Output.get()
    Output.delete(0, tk.END)
    Output.insert(tk.END, current[:-1])


def insert_equal():
    expression = Output.get()
    try:
        result = eval(expression)
        Output.delete(0, tk.END)
        Output.insert(tk.END, result)
    except Exception as e:
        Output.delete(0, tk.END)
        Output.insert(tk.END, f"Error: {str(e)}")


input1 = tk.Button(numberpad, text="1", bg="white", fg="black", padx=10, pady=10, command=lambda: insert_Number(1))
input2 = tk.Button(numberpad, text="2", bg="white", fg="black", padx=10, pady=10, command=lambda: insert_Number(2))
input3 = tk.Button(numberpad, text="3", bg="white", fg="black", padx=10, pady=10, command=lambda: insert_Number(3))
input4 = tk.Button(numberpad, text="4", bg="white", fg="black", padx=10, pady=10, command=lambda: insert_Number(4))
input5 = tk.Button(numberpad, text="5", bg="white", fg="black", padx=10, pady=10, command=lambda: insert_Number(5))
input6 = tk.Button(numberpad, text="6", bg="white", fg="black", padx=10, pady=10, command=lambda: insert_Number(6))
input7 = tk.Button(numberpad, text="7", bg="white", fg="black", padx=10, pady=10, command=lambda: insert_Number(7))
input8 = tk.Button(numberpad, text="8", bg="white", fg="black", padx=10, pady=10, command=lambda: insert_Number(8))
input9 = tk.Button(numberpad, text="9", bg="white", fg="black", padx=10, pady=10, command=lambda: insert_Number(9))
input0 = tk.Button(numberpad, text="0", bg="white", fg="black", padx=10, pady=10, command=insert_0)
inputc = tk.Button(numberpad, text="C", bg="white", fg="black", padx=10, pady=10, command=insert_c)
inputcomma = tk.Button(numberpad, text=".", bg="white", fg="black", padx=10, pady=10, command=insert_comma)
inputadd = tk.Button(numberpad, text="+", bg="white", fg="black", padx=10, pady=10, command=insert_add)
inputminus = tk.Button(numberpad, text="-", bg="white", fg="black", padx=10, pady=10, command=insert_minus)
inputmutiply = tk.Button(numberpad, text="*", bg="white", fg="black", padx=10, pady=10, command=insert_mutiply)
inputdivide = tk.Button(numberpad, text="/", bg="white", fg="black", padx=10, pady=10, command=insert_divide)
inputequal = tk.Button(numberpad, text="=", bg="white", fg="black", padx=10, pady=10, command=insert_equal)
inputback = tk.Button(numberpad, text="<-", bg="white", fg="black", padx=8, pady=9, command=insert_back)
inputoppar = tk.Button(numberpad, text="(", bg="white", fg="black", padx=10, pady=10, command=insert_oppar)
inputclopar = tk.Button(numberpad, text=")", bg="white", fg="black", padx=10, pady=10, command=insert_clopar)

inputoppar.grid(row=1, column=1)
inputclopar.grid(row=1, column=2)
inputc.grid(row=1, column=3)
inputback.grid(row=1, column=4)
input7.grid(row=2, column=1)
input8.grid(row=2, column=2)
input9.grid(row=2, column=3)
inputadd.grid(row=2, column=4)
input4.grid(row=3, column=1)
input5.grid(row=3, column=2)
input6.grid(row=3, column=3)
inputminus.grid(row=3, column=4)
input1.grid(row=4, column=1)
input2.grid(row=4, column=2)
input3.grid(row=4, column=3)
inputmutiply.grid(row=4, column=4)
inputcomma.grid(row=5, column=1)
input0.grid(row=5, column=2)
inputequal.grid(row=5, column=3)
inputdivide.grid(row=5, column=4)

# Scientific mode :


def insert_sin():
    Output.insert(tk.END, "sin(")


def insert_cos():
    Output.insert(tk.END, "cos(")


def insert_tan():
    Output.insert(tk.END, "tan(")


def insert_asin():
    Output.insert(tk.END, "asin(")


def insert_acos():
    Output.insert(tk.END, "acos(")


def insert_atan():
    Output.insert(tk.END, "atan(")


def insert_ln():
    Output.insert(tk.END, "log(")


def insert_exp():
    Output.insert(tk.END, "exp(")


def insert_log10():
    Output.insert(tk.END, "log10(")


def insert_exp10():
    Output.insert(tk.END, "(10**")


def insert_log():
    Output.insert(tk.END, "log(")
    Hints.config(text="Hint : log(x,base) refering to log_(base)(x)")


def insert_pow():
    Output.insert(tk.END, "**")


def insert_randint():
    Output.insert(tk.END, "randint(")
    Hints.config(text="Hint : randint(StartValue,EndValue")


def randbin():
    return randint(0, 1)


def insert_randbin():
    Output.insert(tk.END, "randbin()")


def randfloat():
    return round(random(), 3)


def insert_randfloat():
    Output.insert(tk.END, "randfloat()")
    Hints.config(text="Hint : randomly a float with 3 digits after coma")


def randdice():
    return randint(1, 6)


def insert_randdice():
    Output.insert(tk.END, "randdice()")


def insert_abs():
    Output.insert(tk.END, "abs(")


def insert_virgule():
    Output.insert(tk.END, ",")


def insert_pi():
    Output.insert(tk.END, "pi")


def insert_e():
    Output.insert(tk.END, "e")


def insert_sqrt():
    Output.insert(tk.END, "sqrt(")


def rt(x, n):
    return x**(1 / n)


def insert_nrt():
    Output.insert(tk.END, "rt(")
    Hints.config(text="Hint : rt(x,n) for n_root(x)")


def insert_convrad():
    Output.insert(tk.END, "radians(")


def insert_convdeg():
    Output.insert(tk.END, "degrees(")


inputsin = tk.Button(scientificpad, text="sin", bg="white", fg="black", padx=10, pady=10, command=insert_sin)
inputcos = tk.Button(scientificpad, text="cos", bg="white", fg="black", padx=10, pady=10, command=insert_cos)
inputtan = tk.Button(scientificpad, text="tan", bg="white", fg="black", padx=10, pady=10, command=insert_tan)
inputasin = tk.Button(scientificpad, text="asin", bg="white", fg="black", padx=10, pady=10, command=insert_asin)
inputacos = tk.Button(scientificpad, text="acos", bg="white", fg="black", padx=10, pady=10, command=insert_acos)
inputatan = tk.Button(scientificpad, text="atan", bg="white", fg="black", padx=10, pady=10, command=insert_atan)
inputln = tk.Button(scientificpad, text="ln", bg="white", fg="black", padx=10, pady=10, command=insert_ln)
inputexp = tk.Button(scientificpad, text="e^", bg="white", fg="black", padx=10, pady=10, command=insert_exp)
inputlog10 = tk.Button(scientificpad, text="log_10", bg="white", fg="black", padx=10, pady=10, command=insert_log10)
inputexp10 = tk.Button(scientificpad, text="10^", bg="white", fg="black", padx=10, pady=10, command=insert_exp10)
inputlog = tk.Button(scientificpad, text="log", bg="white", fg="black", padx=10, pady=10, command=insert_log)
inputpow = tk.Button(scientificpad, text="^", bg="white", fg="black", padx=10, pady=10, command=insert_pow)
inputrandint = tk.Button(scientificpad, text="randint", bg="white",
                         fg="black", padx=10, pady=10, command=insert_randint)
inputrandbin = tk.Button(scientificpad, text="rand 0/1", bg="white",
                         fg="black", padx=10, pady=10, command=insert_randbin)
inputrandfloat = tk.Button(scientificpad, text="rand 0.", bg="white", fg="black",
                           padx=10, pady=10, command=insert_randfloat)
inputranddice = tk.Button(scientificpad, text="diceroll", bg="white",
                          fg="black", padx=10, pady=10, command=insert_randdice)
inputabs = tk.Button(scientificpad, text="abs", bg="white", fg="black", padx=10, pady=10, command=insert_abs)
inputvirgule = tk.Button(scientificpad, text=",", bg="white", fg="black", padx=10, pady=10, command=insert_virgule)
inputpi = tk.Button(scientificpad, text="π", bg="white", fg="black", padx=10, pady=10, command=insert_pi)
inpute = tk.Button(scientificpad, text="e", bg="white", fg="black", padx=10, pady=10, command=insert_e)
inputsqrt = tk.Button(scientificpad, text="sqrt", bg="white", fg="black", padx=10, pady=10, command=insert_sqrt)
inputnrt = tk.Button(scientificpad, text="n-root", bg="white", fg="black", padx=10, pady=10, command=insert_nrt)
inputconvrad = tk.Button(scientificpad, text="->RAD", bg="white", fg="black", padx=10, pady=10, command=insert_convrad)
inputconvdeg = tk.Button(scientificpad, text="->DEG", bg="white", fg="black", padx=10, pady=10, command=insert_convdeg)

inputsin.grid(row=1, column=1)
inputcos.grid(row=2, column=1)
inputtan.grid(row=3, column=1)
inputasin.grid(row=1, column=2)
inputacos.grid(row=2, column=2)
inputatan.grid(row=3, column=2)
inputln.grid(row=4, column=1)
inputexp.grid(row=4, column=2)
inputlog10.grid(row=5, column=1)
inputexp10.grid(row=5, column=2)
inputlog.grid(row=6, column=1)
inputpow.grid(row=6, column=2)
inputrandint.grid(row=1, column=3)
inputrandbin.grid(row=1, column=4)
inputranddice.grid(row=2, column=3)
inputrandfloat.grid(row=2, column=4)
inputsqrt.grid(row=3, column=3)
inputnrt.grid(row=3, column=4)
inputabs.grid(row=4, column=3)
inputvirgule.grid(row=4, column=4)
inputpi.grid(row=5, column=3)
inpute.grid(row=5, column=4)
inputconvrad.grid(row=6, column=3)
inputconvdeg.grid(row=6, column=4)

# Arithmetic mode :


def insert_gcd():
    Output.insert(tk.END, "gcd(")


def insert_lcm():
    Output.insert(tk.END, "lcm(")


def insert_div():
    Output.insert(tk.END, "//")


def insert_mod():
    Output.insert(tk.END, "%")


def list_PrimeFactors(n):
    A = 2
    L = []
    while n != 1:
        if n % A == 0:
            L.append(A)
            n = n // A
        else:
            A += 1
    S = ""
    for i in range(len(L)):
        S += str(L[i]) + " * "
    S = S[:len(S) - 2]
    return S


def insert_primefactors():
    Output.insert(tk.END, "list_PrimeFactors(")
    Hints.config(text="Hint : gives prime factors in form of factors without powers")


def isprime(n):
    A = 0
    for i in range(1, n + 1):
        if n % i == 0:
            A += 1
    if A == 2:
        return 1
    else:
        return 0


def insert_primecheck():
    Output.insert(tk.END, "isprime(")
    Hints.config(text="Hint : returns 1 if prime else 0")


def list_Divisors(n):
    L = []
    for i in range(1, n + 1):
        if n % i == 0:
            L.append(i)
    S = ""
    for i in range(len(L)):
        S += str(L[i]) + " , "
    S = S[:len(S) - 2]
    return S


def insert_divisors():
    Output.insert(tk.END, "list_Divisors(")
    Hints.config(text="Hint : gives divisors in form ..,..,..,..")


def list_multiples(n, x):
    L = []
    i = 1
    while n < x:
        L.append(n * i)
        i += 1
        n += n * i
    S = ""
    for i in range(len(L)):
        S += str(L[i]) + " , "
    S = S[:len(S) - 2]
    return S


def insert_multiples():
    Output.insert(tk.END, "list_Multiples(")
    Hints.config(text="Hint : list_Multiples(n,x) gives multiples of n less than x in form ..,..,..,..")


def Factorial(x):
    P = 1
    for i in range(1, x + 1):
        P *= i
    return P


def insert_fact():
    Output.insert(tk.END, "Factorial(")


def P(n, p):
    return ((Factorial(n)) / Factorial(n - p))


def C(n, p):
    return ((Factorial(n)) / (Factorial(p)) * (Factorial(n - p)))


def insert_perm():
    Output.insert(tk.END, "P(")
    Hints.config(text="P(n,p)")


def insert_comb():
    Output.insert(tk.END, "C(")
    Hints.config(text="C(n,p)")


def Divisors_Count(n):
    A = 0
    for i in range(1, n + 1):
        if n % i == 0:
            A += 1
    return A


def insert_divcnt():
    Output.insert(tk.END, "Divisors_Count(")


def isperfect(n):
    S = 0
    for i in range(1, n + 1):
        if n % i == 0:
            S = S + i
    if S == n:
        return 1
    else:
        return 0


def insert_prfctncheck():
    Output.insert(tk.END, "isperfect(")
    Hints.config(text="Hint : returns 1 if perfect else 0")


def Fibonaci(n):
    L = [0, 1]
    while len(L) < n:
        next_number = L[-1] + L[-2]
        L.append(next_number)
    S = ""
    for i in range(len(L)):
        S += str(L[i]) + " , "
    S = S[:len(S) - 2]
    return S


def insert_fib():
    Output.insert(tk.END, "Fibonacci(")
    Hints.config(text="Hint : gives the first n elements of the Fibonacci sequence in form ..,..,..,..")


inputgcd = tk.Button(arithmeticpad, text="gcd", bg="white", fg="black", padx=10, pady=10, command=insert_gcd)
inputlcm = tk.Button(arithmeticpad, text="lcm", bg="white", fg="black", padx=10, pady=10, command=insert_lcm)
inputdiv = tk.Button(arithmeticpad, text="div", bg="white", fg="black", padx=10, pady=10, command=insert_div)
inputmod = tk.Button(arithmeticpad, text="mod", bg="white", fg="black", padx=10, pady=10, command=insert_mod)
inputprimefactors = tk.Button(arithmeticpad, text="Prime factors", bg="white",
                              fg="black", padx=10, pady=10, command=insert_primefactors)
inputprimecheck = tk.Button(arithmeticpad, text="Prime check", bg="white",
                            fg="black", padx=10, pady=10, command=insert_primecheck)
inputdivisors = tk.Button(arithmeticpad, text="divisors", bg="white",
                          fg="black", padx=10, pady=10, command=insert_divisors)
inputmultiples = tk.Button(arithmeticpad, text="multiples", bg="white",
                           fg="black", padx=10, pady=10, command=insert_multiples)
inputfact = tk.Button(arithmeticpad, text="!", bg="white", fg="black", padx=10, pady=10, command=insert_fact)
inputperm = tk.Button(arithmeticpad, text="P", bg="white", fg="black", padx=10, pady=10, command=insert_perm)
inputcomb = tk.Button(arithmeticpad, text="C", bg="white", fg="black", padx=10, pady=10, command=insert_comb)
inputvirg = tk.Button(arithmeticpad, text=",", bg="white", fg="black", padx=10, pady=10, command=insert_virgule)
inputdivcnt = tk.Button(arithmeticpad, text="Divisors Count", bg="white",
                        fg="black", padx=10, pady=10, command=insert_divcnt)
inputprfctncheck = tk.Button(arithmeticpad, text="Perfect Number Check", bg="white",
                             fg="black", padx=10, pady=10, command=insert_prfctncheck)
inputfib = tk.Button(arithmeticpad, text="Fibonacci Sequence", bg="white",
                     fg="black", padx=10, pady=10, command=insert_fib)


inputgcd.grid(row=1, column=1)
inputlcm.grid(row=2, column=1)
inputdiv.grid(row=1, column=2)
inputmod.grid(row=2, column=2)
inputprimefactors.grid(row=3, column=1, columnspan=2)
inputdivisors.grid(row=1, column=3)
inputmultiples.grid(row=2, column=3)
inputprimecheck.grid(row=3, column=3)
inputfact.grid(row=4, column=2)
inputperm.grid(row=4, column=3)
inputcomb.grid(row=4, column=4)
inputvirg.grid(row=4, column=1)
inputdivcnt.grid(row=1, column=4)
inputprfctncheck.grid(row=2, column=4)
inputfib.grid(row=3, column=4)

# Functions mode :


def insert_inf():
    Output.insert(tk.END, "inf")


def insert_x():
    Output.insert(tk.END, "x")


def insert_graph():
    graphwindow = tk.Toplevel(root)
    graphwindow.iconbitmap("icon.ico")
    graphwindow.config(bg=root.cget('bg'))
    graphwindow.title("Graphical Calculator")

    frame = tk.Frame(graphwindow)
    frame.config(bg=functionspad.cget('bg'))
    frame.pack(padx=10, pady=10)

    global entry_expression, error_label

    titleexp = tk.Label(frame, text="f(x)=")
    titleexp.pack()

    entry_expression = tk.Entry(frame, width=30)
    entry_expression.pack(pady=5)

    error_label = tk.Label(frame, fg="red")
    error_label.pack()

    graph_button = tk.Button(frame, text="Graph", command=Graph)
    graph_button.pack(pady=5)


def Graph():
    expression = entry_expression.get()
    try:
        def f(x):
            return eval(expression)

        x = np.linspace(-10, 10, 1000)
        y = f(x)

        plt.plot(x, y)
        plt.xlabel("x")
        plt.ylabel("f(x)")
        plt.title("Graph of f(x)")
        plt.grid(True)
        plt.show()

    except Exception as e:
        error_label.config(text=f"Error: {str(e)}")


def insert_diff():
    diffwindow = tk.Toplevel(root)
    diffwindow.iconbitmap("C:/My files/Coding/programming_main/New projects _py/Calculator/icon.ico")
    diffwindow.config(bg=root.cget('bg'))
    diffwindow.title("Derivative Calculator")

    frame = tk.Frame(diffwindow)
    frame.config(bg=functionspad.cget('bg'))
    frame.pack(padx=10, pady=10)

    global entry_expressiondiff, derivative_label, error_labeldiff

    titleexp = tk.Label(frame, text="f(x)=")
    titleexp.pack()

    entry_expressiondiff = tk.Entry(frame, width=30)
    entry_expressiondiff.pack(pady=5)

    derivative_label = tk.Label(frame, text="", fg="green")
    derivative_label.pack(pady=5)

    error_labeldiff = tk.Label(frame, fg="red")
    error_labeldiff.pack()

    derivative_button = tk.Button(frame, text="Calculate Derivative", command=get_derivative)
    derivative_button.pack(pady=5)


def get_derivative():
    expression = entry_expressiondiff.get()
    x = symbols('x')

    try:
        f_x = simplify(expression)
        f_prime_x = diff(f_x, x)
        f_prime_x=simplify(f_prime_x)
        derivative_label.config(text=f"f'(x) = {f_prime_x}")
        error_labeldiff.config(text="")
    except Exception as e:
        derivative_label.config(text="")
        error_labeldiff.config(text=f"Error: {str(e)}")


def get_integral():
    expression = entry_expressioninteg.get()
    x = symbols('x')

    try:
        f_x = sympify(expression)
        integral = integrate(f_x, x)
        integral=simplify(integral)
        integral_label.config(text=f"The indefinite integral of f(x) is: {integral} + C")
        error_labelinteg.config(text="")
    except Exception as e:
        integral_label.config(text="")
        error_labelinteg.config(text=f"Error: {str(e)}")


def insert_integ():
    integwindow = tk.Toplevel(root)
    integwindow.iconbitmap("C:/My files/Coding/programming_main/New projects _py/Calculator/icon.ico")
    integwindow.config(bg=root.cget('bg'))
    integwindow.title("Indefinite Integral Calculator")

    frame = tk.Frame(integwindow)
    frame.config(bg=functionspad.cget('bg'))
    frame.pack(padx=10, pady=10)

    global entry_expressioninteg, integral_label, error_labelinteg

    titleexp = tk.Label(frame, text="f(x)=")
    titleexp.pack()

    entry_expressioninteg = tk.Entry(frame, width=30)
    entry_expressioninteg.pack(pady=5)

    integral_label = tk.Label(frame, text="", fg="green")
    integral_label.pack(pady=5)

    error_labelinteg = tk.Label(frame, fg="red")
    error_labelinteg.pack()

    integral_button = tk.Button(frame, text="Calculate Indefinite Integral", command=get_integral)
    integral_button.pack(pady=5)


def get_limit():
    expression = entry_expressionlim.get()
    a_value = entry_a.get()
    x = symbols('x')

    try:
        f_x = sympify(expression)
        limit_value = limit(f_x, x, a_value)
        limit_value=sympify(limit_value)
        limit_labellim.config(text=f"lim f(x) as x -> {a_value} = {limit_value}")
        error_labellim.config(text="")
    except Exception as e:
        limit_label.config(text="")
        error_labellim.config(text=f"Error: {str(e)}")


def insert_lim():
    limwindow = tk.Toplevel(root)
    limwindow.iconbitmap("C:/My files/Coding/programming_main/New projects _py/Calculator/icon.ico")
    limwindow.config(bg=root.cget('bg'))
    limwindow.title("Limit Calculator")

    frame = tk.Frame(limwindow)
    frame.config(bg=functionspad.cget('bg'))
    frame.pack(padx=10, pady=10)

    global entry_expressionlim, entry_a, limit_labellim, error_labellim

    titleexp = tk.Label(frame, text="f(x)=")
    titleexp.pack()

    entry_expressionlim = tk.Entry(frame, width=30)
    entry_expressionlim .pack(pady=5)

    aexp = tk.Label(frame, text="a=")
    aexp.pack()

    entry_a = tk.Entry(frame, width=10)
    entry_a.pack(pady=5)

    limit_labellim = tk.Label(frame, text="", fg="green")
    limit_labellim .pack(pady=5)

    error_labellim = tk.Label(frame, fg="red")
    error_labellim .pack()

    limit_button = tk.Button(frame, text="Calculate Limit", command=get_limit)
    limit_button.pack(pady=5)


def generate_table():
    expression = entry_expressiontab.get()
    start_x = float(entry_start_x.get())
    end_x = float(entry_end_x.get())
    step_size = float(entry_step_size.get())

    x = symbols('x')
    try:
        f_x = sympify(expression)
        table_text.delete("1.0", tk.END)  # Clear previous table content

        table_text.insert(tk.END, f"{'x':<10}{'f(x)':<10}\n")
        table_text.insert(tk.END, "-" * 20 + "\n")

        current_x = start_x
        table_data = []
        while current_x <= end_x:
            f_x_value = f_x.subs(x, current_x)
            table_text.insert(tk.END, f"{current_x:<10.4f}{f_x_value:<10.4f}\n")
            table_data.append([current_x, f_x_value])
            current_x += step_size

        error_labeltab.config(text="")
        return table_data
    except Exception as e:
        table_text.delete("1.0", tk.END)
        error_labeltab.config(text=f"Error: {str(e)}")
        return None


def save_to_excel():
    table_data = generate_table()
    if table_data:
        df = pd.DataFrame(table_data, columns=["x", "f(x)"])
        df.to_excel("table_of_values.xlsx", index=False)
        save_label.config(text="Table saved to table_of_values.xlsx")
    else:
        save_label.config(text="Error: Cannot save table. Check input.")


def insert_tab():
    tabwindow = tk.Toplevel(root)
    tabwindow.iconbitmap("icon.ico")
    tabwindow.config(bg=root.cget('bg'))
    tabwindow.title("Table of Values Calculator")
    warnlabel = tk.Label(tabwindow, text="Warning : still under work , can't work on values <=0")
    warnlabel.pack(padx=10, pady=10)
    frame = tk.Frame(tabwindow)
    frame.config(bg=functionspad.cget('bg'))
    frame.pack(padx=10, pady=10)

    global entry_expressiontab, entry_start_x, entry_end_x, entry_step_size, table_text, error_labeltab, save_button, save_label

    label_expressiontab = tk.Label(frame, text="f(x) expression:")
    label_expressiontab.pack()
    entry_expressiontab = tk.Entry(frame, width=30)
    entry_expressiontab.pack(pady=5)

    label_start_x = tk.Label(frame, text="Start x:")
    label_start_x.pack()
    entry_start_x = tk.Entry(frame, width=10)
    entry_start_x.pack(pady=5)

    label_end_x = tk.Label(frame, text="End x:")
    label_end_x.pack()
    entry_end_x = tk.Entry(frame, width=10)
    entry_end_x.pack(pady=5)

    label_step_size = tk.Label(frame, text="Step size:")
    label_step_size.pack()
    entry_step_size = tk.Entry(frame, width=10)
    entry_step_size.pack(pady=5)

    table_text = scrolledtext.ScrolledText(frame, width=30, height=10)
    table_text.pack()

    error_labeltab = tk.Label(frame, fg="red")
    error_labeltab.pack()

    table_button = tk.Button(frame, text="Generate Table", command=generate_table)
    table_button.pack(pady=5)

    save_button = tk.Button(frame, text="Save to Excel", command=save_to_excel)
    save_button.pack(pady=5)

    save_label = tk.Label(frame, fg="blue")
    save_label.pack()


inputinf = tk.Button(functionspad, text="∞", bg="white", fg="black", padx=10, pady=10, command=insert_inf)
inputx = tk.Button(functionspad, text="x", bg="white", fg="black", padx=10, pady=10, command=insert_x)
inputgraph = tk.Button(functionspad, text="Graph", bg="white", fg="black", padx=10, pady=10, command=insert_graph)
inputdiff = tk.Button(functionspad, text="d/dx", bg="white", fg="black", padx=10, pady=10, command=insert_diff)
inputinteg = tk.Button(functionspad, text="∫", bg="white", fg="black", padx=10, pady=10, command=insert_integ)
inputlim = tk.Button(functionspad, text="lim", bg="white", fg="black", padx=10, pady=10, command=insert_lim)
inputtab = tk.Button(functionspad, text="Table of values", bg="white",
                     fg="black", padx=10, pady=10, command=insert_tab)

inputinf.grid(row=1, column=1)
inputx.grid(row=1, column=2)
inputgraph.grid(row=1, column=3)
inputtab.grid(row=1, column=4)
inputdiff.grid(row=2, column=1)
inputinteg.grid(row=2, column=2)
inputlim.grid(row=2, column=3)

# Complex Mode :


def insert_i():
    Output.insert(tk.END, "j")


def insert_cpi():
    Output.insert(tk.END, "cpi")


def insert_ce():
    Output.insert(tk.END, "ce")


def magnitude(z):
    return abs(z)


def insert_mag():
    Output.insert(tk.END, "magnitude(")


def insert_ph():
    Output.insert(tk.END, "phase(")


def conj(z):
    return z.conjugate()


def insert_conj():
    Output.insert(tk.END, "conj(")


def insert_csqrt():
    Output.insert(tk.END, "csqrt(")


def insert_cln():
    Output.insert(tk.END, "clog(")


def insert_clog10():
    Output.insert(tk.END, "clog10(")


def insert_csin():
    Output.insert(tk.END, "csin(")


def insert_ccos():
    Output.insert(tk.END, "ccos(")


inputi = tk.Button(complexpad, text="i", bg="white", fg="black", padx=10, pady=10, command=insert_i)
inputcpi = tk.Button(complexpad, text="π", bg="white", fg="black", padx=10, pady=10, command=insert_cpi)
inputce = tk.Button(complexpad, text="e", bg="white", fg="black", padx=10, pady=10, command=insert_ce)
inputv = tk.Button(complexpad, text=",", bg="white", fg="black", padx=10, pady=10, command=insert_virgule)
inputmag = tk.Button(complexpad, text="Magnitude", bg="white", fg="black", padx=10, pady=10, command=insert_mag)
inputph = tk.Button(complexpad, text="Phase", bg="white", fg="black", padx=10, pady=10, command=insert_ph)
inputconj = tk.Button(complexpad, text="Conjugate", bg="white", fg="black", padx=10, pady=10, command=insert_conj)
inputcsqrt = tk.Button(complexpad, text="sqrt", bg="white", fg="black", padx=10, pady=10, command=insert_csqrt)
inputcln = tk.Button(complexpad, text="ln", bg="white", fg="black", padx=10, pady=10, command=insert_cln)
inputclog10 = tk.Button(complexpad, text="log_10", bg="white", fg="black", padx=10, pady=10, command=insert_clog10)
inputcsin = tk.Button(complexpad, text="sin", bg="white", fg="black", padx=10, pady=10, command=insert_csin)
inputccos = tk.Button(complexpad, text="cos", bg="white", fg="black", padx=10, pady=10, command=insert_ccos)


inputi.grid(row=1, column=1)
inputcpi.grid(row=2, column=1)
inputce.grid(row=3, column=1)
inputv.grid(row=4, column=1)
inputmag.grid(row=1, column=2)
inputph.grid(row=2, column=2)
inputconj.grid(row=3, column=2)
inputcsqrt.grid(row=1, column=3)
inputcln.grid(row=2, column=3)
inputclog10.grid(row=3, column=3)
inputcsin.grid(row=1, column=4)
inputccos.grid(row=2, column=4)

# Equations :


def solvearith():
    a = int(aentry.get())
    b = int(bentry.get())
    c = int(centry.get())
    try:
        d = gcd(a, b)
        val_p = [0, 1]
        val_r = [a, b]
        val_q = ["(x)"]
        p = 1
        val_q.append(a // b)
        while val_r[p] != 0:
            p = p + 1
            val_p.append(p)
            val_r.append((val_r[p - 2]) % (val_r[p - 1]))
            if val_r[p] != 0:
                val_q.append((val_r[p - 1]) // (val_r[p]))
            else:
                val_q.append("(x)")

        val_u = [1, 0]
        val_v = [0, 1]
        for i in range(2, p + 1):
            val_u.append((val_u[i - 2]) - (val_q[i - 1]) * (val_u[i - 1]))
            val_v.append((val_v[i - 2]) - (val_q[i - 1]) * (val_v[i - 1]))
        n = p + 1
        if c == 1:
            Aff = "Solutions for the equation are:"
            Aff = Aff + "\n" + (f"u = {val_u[n-2]} + k * {val_u[n-1]}")
            Aff = Aff + "\n" + (f"v = {val_v[n-2]} + k * {val_v[n-1]}")
            solutions_out.insert(tk.END, Aff)
        else:
            if c % d == 0:
                Aff = "Solutions for the equation are:"
                Aff = Aff + "\n" + (f"u = {(val_u[n-2])*c} + k * {(val_u[n-1])*c}")
                Aff = Aff + "\n" + (f"v = {(val_v[n-2])*c} + k * {(val_v[n-1])*c}")
                solutions_out.insert(tk.END, Aff)
            else:
                solutions_out.insert(tk.END, "The equation admits no solutions")
    except Exception as e:
        solutions_out.delete("1.0", tk.END)
        solutions_out.insert(tk.END, f"Error: {str(e)}")


def arithcalc():
    arithwindow = tk.Toplevel(root)
    arithwindow.iconbitmap("icon.ico")
    arithwindow.title("Diophantine solver using the Bezout-Euclide method")
    arithwindow.config(bg=root.cget('bg'))

    frame = tk.Frame(arithwindow)
    frame.config(bg=equationpad.cget('bg'))
    frame.pack(padx=10, pady=10)

    alabel = tk.Label(frame, text="a")
    ulabel = tk.Label(frame, text="u")
    pluslabel = tk.Label(frame, text="+")
    blabel = tk.Label(frame, text="b")
    vlabel = tk.Label(frame, text="v")
    eqlabel = tk.Label(frame, text="=")
    clabel = tk.Label(frame, text="c")

    global aentry, bentry, centry, solutions_out

    aentry = tk.Entry(frame, width=5)
    bentry = tk.Entry(frame, width=5)
    centry = tk.Entry(frame, width=5)

    alabel.grid(row=1, column=1)
    ulabel.grid(row=1, column=2)
    pluslabel.grid(row=1, column=3)
    blabel.grid(row=1, column=4)
    vlabel.grid(row=1, column=5)
    eqlabel.grid(row=1, column=6)
    clabel.grid(row=1, column=7)
    aentry.grid(row=2, column=1)
    bentry.grid(row=2, column=4)
    centry.grid(row=2, column=7)

    solvebut = tk.Button(frame, text="Solve", command=solvearith)
    solvebut.grid(row=3, column=4, padx=5, pady=5)

    solutions_out = tk.Text(frame, width=50, height=5)
    solutions_out.grid(row=4, column=1, columnspan=7)


def solve_equation():
    equation_str = entry_equation.get()
    x = symbols('x')
    try:
        equation = Eq(sympify(equation_str), 0)
        solutions = solve(equation, x)
        solution_text.delete("1.0", tk.END)  # Clear previous solutions
        if len(solutions) == 0:
            solution_text.insert(tk.END, "No real solutions found.")
        else:
            for idx, sol in enumerate(solutions):
                solution_text.insert(tk.END, f"Solution {idx + 1}: x = {sol}\n")
    except Exception as e:
        solution_text.delete("1.0", tk.END)
        solution_text.insert(tk.END, f"Error: {str(e)}")


def floatsolver():
    floateq = tk.Toplevel(root)
    floateq.iconbitmap("icon.ico")
    floateq.config(bg=root.cget('bg'))
    floateq.title("Equations with float variables Solver")

    frame = tk.Frame(floateq)
    frame.config(bg=equationpad.cget('bg'))
    frame.pack(padx=10, pady=10)

    global entry_equation, solution_text

    label_equation = tk.Label(frame, text="Enter the equation:")
    label_equation.pack()
    entry_equation = tk.Entry(frame, width=30)
    entry_equation.pack(pady=5)

    solve_button = tk.Button(frame, text="Solve Equation", command=solve_equation)
    solve_button.pack(pady=5)

    solution_text = tk.Text(frame, width=40, height=10)
    solution_text.pack()


def solve_complex_equation():
    z = symbols('z')
    equation_str = entry_equationc.get()
    try:
        equation = Eq(sympify(equation_str), 0)
        solutions = solveset(equation, z, domain=S.Complexes)

        solution_textc.delete("1.0", tk.END)  # Clear previous solutions

        if len(solutions) == 0:
            solution_textc.insert(tk.END, "No complex solutions found.")
        else:
            for sol in solutions:
                solution_textc.insert(tk.END, f"z = {sol}\n")

    except Exception as e:
        solution_textc.delete("1.0", tk.END)
        solution_textc.insert(tk.END, f"Error: {str(e)}")


def complexsolver():
    ceqsolve = tk.Toplevel(root)
    ceqsolve.iconbitmap("icon.ico")
    ceqsolve.config(bg=root.cget('bg'))
    ceqsolve.title("Complex Equation Solver")

    frame = tk.Frame(ceqsolve)
    frame.config(bg=equationpad.cget('bg'))
    frame.pack(padx=10, pady=10)

    global entry_equationc, solution_textc

    label_equationc = tk.Label(frame, text="Enter the complex equation:")
    label_equationc.pack()
    entry_equationc = tk.Entry(frame, width=30)
    entry_equationc.pack(pady=5)

    solve_buttonc = tk.Button(frame, text="Solve Complex Equation", command=solve_complex_equation)
    solve_buttonc.pack(pady=5)

    solution_textc = tk.Text(frame, width=40, height=10)
    solution_textc.pack()


def solve_linear_system():
    try:
        a1 = float(entry_a1.get())
        b1 = float(entry_b1.get())
        c1 = float(entry_c1.get())

        a2 = float(entry_a2.get())
        b2 = float(entry_b2.get())
        c2 = float(entry_c2.get())

        if a2 * b1 - b2 * a1 == 0:
            solution_textsys.delete("1.0", tk.END)
            solution_textsys.insert(tk.END, "Error: Denominator is zero. Cannot solve the system.")
            return

        x = (b1 * c2 - b2 * c1) / (a2 * b1 - b2 * a1)
        y = c1 / b1 - (a1 * x) / b1

        solution_textsys.delete("1.0", tk.END)
        solution_textsys.insert(tk.END, f"x = {x}\n")
        solution_textsys.insert(tk.END, f"y = {y}\n")

    except Exception as e:
        solution_textsys.delete("1.0", tk.END)
        solution_textsys.insert(tk.END, f"Error: {str(e)}")


def syssolver():
    syswindow = tk.Toplevel(root)
    syswindow.iconbitmap("icon.ico")
    syswindow.config(bg=root.cget('bg'))
    syswindow.title("Solution of Linear System")

    indice1 = tk.Label(syswindow, text="{a1x+b1y=c1")
    indice1.pack(padx=10)

    indice2 = tk.Label(syswindow, text="{a2x+b2y=c2")
    indice2.pack(padx=10)

    frame = tk.Frame(syswindow)
    frame.config(bg=equationpad.cget('bg'))
    frame.pack(padx=10, pady=10)

    global entry_a1, entry_b1, entry_c1, entry_a2, entry_b2, entry_c2, solution_textsys

    label_a1 = tk.Label(frame, text="Enter a1:")
    label_a1.grid(row=0, column=0, padx=5)
    entry_a1 = tk.Entry(frame, width=10)
    entry_a1.grid(row=0, column=1, padx=5)

    label_b1 = tk.Label(frame, text="Enter b1:")
    label_b1.grid(row=0, column=2, padx=5)
    entry_b1 = tk.Entry(frame, width=10)
    entry_b1.grid(row=0, column=3, padx=5)

    label_c1 = tk.Label(frame, text="Enter c1:")
    label_c1.grid(row=0, column=4, padx=5)
    entry_c1 = tk.Entry(frame, width=10)
    entry_c1.grid(row=0, column=5, padx=5)

    label_a2 = tk.Label(frame, text="Enter a2:")
    label_a2.grid(row=1, column=0, padx=5)
    entry_a2 = tk.Entry(frame, width=10)
    entry_a2.grid(row=1, column=1, padx=5)

    label_b2 = tk.Label(frame, text="Enter b2:")
    label_b2.grid(row=1, column=2, padx=5)
    entry_b2 = tk.Entry(frame, width=10)
    entry_b2.grid(row=1, column=3, padx=5)

    label_c2 = tk.Label(frame, text="Enter c2:")
    label_c2.grid(row=1, column=4, padx=5)
    entry_c2 = tk.Entry(frame, width=10)
    entry_c2.grid(row=1, column=5, padx=5)

    solve_button = tk.Button(frame, text="Solve Linear System", command=solve_linear_system)
    solve_button.grid(row=2, columnspan=6, pady=10)

    solution_textsys = tk.Text(frame, width=40, height=5)
    solution_textsys.grid(row=3, columnspan=6, padx=5)


floateq = tk.Button(equationpad, text="x ∈ ℝ", bg="white", fg="black", padx=10, pady=10, command=floatsolver)
complexeq = tk.Button(equationpad, text="z ∈ ℂ", bg="white", fg="black", padx=10, pady=10, command=complexsolver)
aritheq = tk.Button(equationpad, text="au+bv=c", bg="white", fg="black", padx=10, pady=10, command=arithcalc)
syseq = tk.Button(equationpad, text="(x,y) systems", bg="white", fg="black", padx=10, pady=10, command=syssolver)

floateq.grid(row=1, column=1)
complexeq.grid(row=1, column=2)
aritheq.grid(row=2, column=1)
syseq.grid(row=2, column=2)

# Menus :


def close():
    root.destroy()


def randomcolorcode():
    L = []
    for i in range(0, 10):
        L.append(str(i))
    for i in range(0, 6):
        L.append(chr(ord("a") + i))
    Code = "#"
    for i in range(6):
        Code += L[randint(0, 15)]
    return Code


def randombgset():
    root.config(bg=randomcolorcode())


def setbgred():
    root.config(bg="red")


def setbggreen():
    root.config(bg="green")


def setbgyellow():
    root.config(bg="yellow")


def setbgwhite():
    root.config(bg="white")


def setbgblack():
    root.config(bg="black")


def setbgorange():
    root.config(bg="orange")


def setbgblue():
    root.config(bg="blue")


def setbgcyan():
    root.config(bg="cyan")


def normal():
    root.geometry("300x300")
    scientificpad.grid_forget()
    Trigomode.grid_forget()
    arithmeticpad.grid_forget()
    functionspad.grid_forget()
    complexpad.grid_forget()
    Hints.config(text="Hints : ")
    Output.grid(row=1, column=1, pady=5)
    Hints.grid(row=1, column=2, padx=5, pady=5)
    numberpad.grid(row=3, column=1, pady=5)
    welcometxt.grid_forget()
    equationpad.grid_forget()
    aboutframe.grid_forget()


def scientific():
    root.geometry("520x330")
    arithmeticpad.grid_forget()
    scientificpad.grid(row=3, column=2, pady=5)
    Trigomode.grid(row=2, column=1)
    functionspad.grid_forget()
    functionspad.grid_forget()
    complexpad.grid_forget()
    Hints.config(text="Hints : ")
    Output.grid(row=1, column=1, pady=5)
    Hints.grid(row=1, column=2, padx=5, pady=5)
    numberpad.grid(row=3, column=1, pady=5)
    welcometxt.grid_forget()
    equationpad.grid_forget()
    aboutframe.grid_forget()


def arithmetic():
    root.geometry("600x330")
    arithmeticpad.grid(row=3, column=2, pady=5)
    scientificpad.grid_forget()
    Trigomode.grid_forget()
    functionspad.grid_forget()
    complexpad.grid_forget()
    Hints.config(text="Hints : ")
    Output.grid(row=1, column=1, pady=5)
    Hints.grid(row=1, column=2, padx=5, pady=5)
    numberpad.grid(row=3, column=1, pady=5)
    welcometxt.grid_forget()
    equationpad.grid_forget()
    aboutframe.grid_forget()


def function():
    root.geometry("540x430")
    arithmeticpad.grid_forget()
    scientificpad.grid(row=3, column=2, pady=5)
    Trigomode.grid(row=2, column=1)
    functionspad.grid(row=4, column=1, columnspan=2, pady=5)
    complexpad.grid_forget()
    Hints.config(text="Hints : Beta version , if u find some bugs report them")
    Output.grid(row=1, column=1, pady=5)
    Hints.grid(row=1, column=2, padx=5, pady=5)
    numberpad.grid(row=3, column=1, pady=5)
    welcometxt.grid_forget()
    equationpad.grid_forget()
    aboutframe.grid_forget()


def complex():
    root.geometry("520x330")
    arithmeticpad.grid_forget()
    scientificpad.grid_forget()
    Trigomode.grid_forget()
    functionspad.grid_forget()
    complexpad.grid(row=3, column=2, pady=5)
    Hints.config(text="Hints : ")
    Output.grid(row=1, column=1, pady=5)
    Hints.grid(row=1, column=2, padx=5, pady=5)
    numberpad.grid(row=3, column=1, pady=5)
    welcometxt.grid_forget()
    equationpad.grid_forget()
    aboutframe.grid_forget()


def equation():
    root.geometry("290x230")
    welcometxt.grid_forget()
    numberpad.grid_forget()
    Hints.grid(row=1, column=1, padx=5, pady=5)
    Hints.config(text="Hints : Beta version , if u find some bugs report them")
    Output.grid_forget()
    arithmeticpad.grid_forget()
    scientificpad.grid_forget()
    Trigomode.grid_forget()
    functionspad.grid_forget()
    complexpad.grid_forget()
    equationpad.grid(row=2, column=1, padx=5, pady=5)
    aboutframe.grid_forget()


aboutframe = tk.Frame(root)

Name = tk.Label(aboutframe, text=("Professor Xenon"), fg="#0E96CC", font=("Arial", 20))
image = tk.PhotoImage(file="C:/My files/Coding/programming_main/New projects _py/Calculator/Me.png")
infos = tk.Label(aboutframe, font=("Arial", 10))
infos.config(text="Real name: Med Amin Haffouz \nEmail:aminhfz01@gmail.com")

Name.grid(row=1, column=1, columnspan=2)
image_label = tk.Label(aboutframe, image=image)
image_label.grid(row=2, column=1)
infos.grid(row=2, column=2)


def about():
    root.geometry("500x470")
    welcometxt.grid_forget()
    numberpad.grid_forget()
    Hints.grid_forget()
    Output.grid_forget()
    arithmeticpad.grid_forget()
    scientificpad.grid_forget()
    Trigomode.grid_forget()
    functionspad.grid_forget()
    complexpad.grid_forget()
    equationpad.grid_forget()
    aboutframe.grid(row=1, column=1, pady=5, padx=5)


menu = tk.Menu(root)

modesetting = tk.Menu(menu)
menu.add_cascade(label="Mode", menu=modesetting)
modesetting.add_command(label="Normal Mode", command=normal)
modesetting.add_command(label="Scientific Mode", command=scientific)
modesetting.add_command(label="Arithmetic Mode", command=arithmetic)
modesetting.add_command(label="Complex Mode", command=complex)
modesetting.add_command(label="Function Mode", command=function)
modesetting.add_command(label="Equation Mode", command=equation)

bgsetting = tk.Menu(menu)
menu.add_cascade(label="Set Background", menu=bgsetting)
bgsetting.add_command(label="Red", command=setbgred)
bgsetting.add_command(label="Green", command=setbggreen)
bgsetting.add_command(label="Yellow", command=setbgyellow)
bgsetting.add_command(label="White", command=setbgwhite)
bgsetting.add_command(label="Black", command=setbgblack)
bgsetting.add_command(label="Orange", command=setbgorange)
bgsetting.add_command(label="Blue", command=setbgblue)
bgsetting.add_command(label="Cyan", command=setbgcyan)
bgsetting.add_command(label="Random", command=randombgset)

menu.add_command(label="About", command=about)
menu.add_command(label="Exit", command=close)

root.config(menu=menu)

welcometxt.grid(row=1, column=1)

root.mainloop()
