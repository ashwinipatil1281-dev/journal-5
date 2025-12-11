import sys

default_P = 1000.0
default_R = 5.0
default_T = 2.0

if len(sys.argv) == 4:
    P = float(sys.argv[1])
    R = float(sys.argv[2])
    T = float(sys.argv[3])
    source = "User Input"
else:
    P = default_P
    R = default_R
    T = default_T
    source = "Self-assigned"

si = (P * R * T) / 100

print(f"Principal: {P} ({source})")
print(f"Rate: {R} ({source})")
print(f"Time: {T} ({source})")
print("Simple Interest:", si)
