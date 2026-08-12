पूरा code याद रखने का तरीका

पहले GCD:

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
  

फिर LCM:

def lcm(a, b):
    return (a * b) // gcd(a, b)

GCD और LCM का connection
GCD → Recursion से निकालो
             ↓
LCM → GCD की मदद से निकालो

Interview में याद रखो ⭐⭐⭐

GCD(a,b) = gcd(b, a%b)
LCM(a,b) = (a*b) / GCD(a,b)

Python में integer result के लिए // use करना अच्छा रहता है:

(a * b) // gcd(a, b)


def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)


def lcm(a, b):
    return (a * b) // gcd(a, b)


print(lcm(12, 18))
