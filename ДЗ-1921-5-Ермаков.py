def f(a, b, m, _19 = False):
    if a + b >= 45:
        return m % 2 == 0
    if m == 0:
        return 0
    
    h = [
        f(a + 1, b, m - 1), 
        f(a, b + 1, m - 1),  
        f(a * 3, b, m - 1), 
        f(a, b * 3, m - 1)
    ]

    return any(h) if ((m - 1) % 2 == 0) or _19 else all(h)


print("19)", min([b for b in range(1, 41) if f(4, b, 2, True)]))
print("20)", [b for b in range(1, 41) if not f(4, b, 1) and f(4, b, 3)])
print("21)", *[b for b in range(1, 41) if not f(4, b, 2) and f(4, b, 4)])
