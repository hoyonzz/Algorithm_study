a, b, c = map(int, input().split())

def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

gcd1 = gcd(a, b)
lcm1 = a*b // gcd1
gcd2 = gcd(lcm1, c)
lcm2 = lcm1*c // gcd2

print(lcm2)


