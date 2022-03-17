a = 204  # people on the plane
b = 15
c = 0
g = 6
k = 34
l = a / 68
m = 2

n = 1  # Sections on the plane
q = 1  # Number of aisles
s = 2  # Movement speed accouting for accordion effect
# v = 0
# w = a
# z = 3  # man num carry on


def calc():
    return 5*q*n*k + (g / q)*(2+s+b+s*n*k)+a*s*q*(((q-1) / 2)*c + l)

print(calc() / 60)