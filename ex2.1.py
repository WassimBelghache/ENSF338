import sys
import math

def do_stuff():
    
    
    if len(sys.argv) < 4:
        print("Usage:  python script_name.py <a> <b> <c>")
        return
    # i)  The overall code computes the quadratic equation with values a,b, and c.
    # 
    # ii) The assumption that the correct number of command-line arguments was always provided caused an error.
    #     The code above ensures that the script is only executed if less than four (or three) command-line arguments are given.
    
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    c = float(sys.argv[3])
    
    d = b**2 - 4*a*c
    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2*a)
        root2 = (-b - math.sqrt(d)) / (2*a)
        print(f'The solutions are: {root1}, {root2}')
    elif d == 0:
        root = -b / (2*a)
        print(f'The solution is: {root}')
    else:
        print('There are no real solutions.')

do_stuff()

