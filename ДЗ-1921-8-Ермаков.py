def f(a, b, m):
    if a == b:
        return m % 2 == 0
    if m == 0:
        return 0
    
    h = [
        f(a + 1, b, m - 1), 
        f(a + 3, b, m - 1), 
    ] if a < b else [
        f(a, b + 1, m - 1), 
        f(a, b + 3, m - 1), 
    ]

    return any(h) if (m - 1) % 2 == 0 else all(h)

t = [b for b in range(1, 24) if not f(13, b, 1) and f(13, b, 3)]

print("19)", min([b for b in range(1, 24) if f(13, b, 2)]))
print("20)", f"{t[0]} {t[1]}")
print("21)", [b for b in range(1, 24) if not f(13, b, 2) and f(13, b, 4)])
