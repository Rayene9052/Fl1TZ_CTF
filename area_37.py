#!/usr/bin/env python3

def fun(x):
    product = x * 37
    product_str = str(product)
    rev = product_str[::-1]
    interleaved = "0".join(list(rev))
    value = int(interleaved)
    return value // 37

expected_hex = [
    "e8 6e 00 00",
    "8d eb 02 00",
    "0a 13 02 00",
    "fb 10 02 00",
    "dd 3d 01 00",
    "2c 15 02 00",
    "fb 10 02 00",
    "88 aa 01 00",
    "ac 4d 03 00",
    "dd 3d 01 00",
    "e4 3f 01 00",
    "8d eb 02 00",
    "fb 10 02 00",
    "fa 81 02 00",
    "50 b8 03 00",
    "e4 3f 01 00",
    "9f 7b 02 00",
    "8d eb 02 00",
    "ac 4d 03 00",
    "0c 12 02 00"
]

expected = []
for hex_str in expected_hex:
    b_val = bytes.fromhex(hex_str)
    value = int.from_bytes(b_val, "little")
    expected.append(value)

flag_chars = []
for exp in expected:
    found = None
    for x in range(32, 127):
        if fun(x) == exp:
            found = chr(x)
            break
    if found is None:
        flag_chars.append("?")
    else:
        flag_chars.append(found)

flag = "FL1TZ" + "".join(flag_chars) 
print("Flag:", flag)
