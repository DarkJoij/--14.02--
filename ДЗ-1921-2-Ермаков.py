def f(a, b, m, _19 = False):
    if a + b >= 51:
        return m % 2 == 0
    if m == 0:
        return 0
    
    h = [
        f(a + 2, b, m - 1), 
        f(a, b + 2, m - 1), 
        f(a + 3, b, m - 1), 
        f(a, b + 3, m - 1), 
        f(a * 2, b, m - 1), 
        f(a, b * 2, m - 1), 
    ]

    return any(h) if ((m - 1) % 2 == 0) or _19 else all(h)


print("19)", min([b for b in range(1, 46) if f(5, b, 2, True)]))
print("20)", [b for b in range(1, 46) if not f(5, b, 1) and f(5, b, 3)])
print("21)", *[b for b in range(1, 46) if not f(5, b, 2) and f(5, b, 4)])
