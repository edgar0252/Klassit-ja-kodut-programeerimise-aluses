import sys
sys.argv = ["x"] + input("Tehe: ").split()
if len(sys.argv) != 4:
    print("usage: ./solution.py a_number (an_operator +-*/%^) a_number")
else:
    try:
        a_number = int(sys.argv[1])
        tegevus = sys.argv[2]
        b_number = int(sys.argv[3])

        if tegevus == "+":
            print(a_number + b_number)
        elif tegevus == "-":
            print(a_number - b_number)
        elif tegevus == "*":
            print(a_number * b_number)
        elif tegevus == "/":
            print(a_number / b_number)
        elif tegevus == "%":
            print(a_number % b_number)
        elif tegevus == "^":
            print(a_number ** b_number)
        else:
            print("input error")
    except (ValueError, ZeroDivisionError):
        print("input error")



