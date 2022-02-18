import sympy
from termcolor import colored

print("Exceptions to (n^2 - 2)/2 prime rule:")
print(" ")

n = 0

def print_factors(x):
    factors = []
    for i in range(1, x + 1):
       if x % i == 0:
           if i != 1 and i != x:
            factors.append(i)

    return(factors)


max = input(colored("How high should the program go? ", 'blue'))
global fct
fct = input(colored("Display factors? (No increases speed) [y/n] " , "green"))
n = input("start from (default=2): ")
log = input("Optional: log file name (leave blank for no logging): ")

try:
    instart = int(n)
    if instart < 2:
        n = 2
    elif instart >= 2:
        n = instart
except ValueError:
    n = 2

print(colored("Finding exceptions: ", "yellow"))
if int(max)<341:
    print(colored("No exceptions exist under 341", "red"))

if int(max)>99999:
    print("This may take a while...")



while n<=int(max):
    prime = sympy.isprime(n)
    sq = 2**n
    sq2 = sq-2
    divv = sq2%n
    # print(f"{n}  -  {sq2}  -  {divv}")

    if divv == 0 and prime == False:
        if fct.lower() == "yes" or fct.lower() == "y":
            fctrs = print_factors(n)
            print(colored(f"{n} ", "red"), "-", colored(f" factors: {fctrs}", "green"))
            if log != "" and log != " ":
                with open(f"{log}.txt", 'a') as f:
                    f.write(f"\n{n}")
        else:
            print(colored(f"{n} ", "red"))
            if log != "" and log != " ":
                with open(f"{log}.txt", 'a') as f:
                    f.write(f"\n{n}")

    n+=1
