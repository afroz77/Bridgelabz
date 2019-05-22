import sys as s
try:
    v = float(s.argv[1])
    t = float(s.argv[2])

    if t <= 50 and v <= 120 and v > 3:
        w = (35.74+0.6215*t)+(0.4275*t-35.75)*(v**0.16)
        print(round(w, 2))
    else:
        print("Enter Valid Value ")
except ValueError:
    print("Invalid Input ")