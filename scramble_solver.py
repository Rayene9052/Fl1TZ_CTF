def func1(s):
    r1 = []
    for i2, c3 in enumerate(s):
        a4 = ord(c3)
        if (i2 + 1) % 2 == 1:
            s5 = a4 << 4
            n6 = chr(s5 % 256)  # keep within valid character range
        else:
            s7 = a4 >> a4
            n6 = chr(s7 % 256)
        r1.append(n6)
    t8 = ''.join(r1)
    return t8

def func2(s):
    l = len(s)
    k = [(l * i) % 256 for i in (1, 3, 7, 9, 13)]
    return ''.join(chr((ord(c) + k[i % 5]) % 256) for i, c in enumerate(s))

def func3(input):
    return input[::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1]

def func4(s):
    h = len(s) // 2
    a = s[:h][::-1]
    b = s[h:][::-1]
    r = []
    for x, y in zip(a, b):
        r.extend([x, y])
    if len(s) % 2:
        r.append(s[h])
    return ''.join(chr(ord(c) ^ 0xaa) for c in r)

def func5(input):
    return input[::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1]

def func6(s):
    y = []
    for i in s:
        a = ord(i)
        b = (a * 17 + 123) & 255
        c = (a // 2 + b // 2) & 255
        y.append(chr(c))
    return ''.join(y)

def func7(input):
    return input[::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1][::-1]

def func8(s):
    l = [-31, 103, -7, 119, 76, 47, -38, -25, 106, -35, 179, 11, 45, 76, -4, 71, 87, 68, 20, 102, 19, 38, 28, 83, 92, 46, 21, 117]
    e = []
    for i in range(len(l)):
        e.append(chr((ord(s[i]) - l[i]) % 256))
    return ''.join(e)

# Input string
s = "babatilifonolloumouhounnhehe"

# Run through each function in order
s = func1(s)
s = func2(s)
s = func3(s)
s = func4(s)
s = func5(s)
s = func6(s)
s = func7(s)
s = func8(s)

print("Final Output:", s)
