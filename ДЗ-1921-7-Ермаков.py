def f(a, b, m):
    if a + b >= 231:
        return m % 2 == 0
    if m == 0:
        return 0
    
    h = [
        f(a + 2, b, m - 1), 
        f(a, b + 2, m - 1),  
        f(a * 2, b, m - 1), 
        f(a, b * 2, m - 1)
    ]

    return any(h) if (m - 1) % 2 == 0 else all(h)


t = [b for b in range(1, 214) if not f(17, b, 1) and f(17, b, 3)]

print("Нужна помощь с 19:")
print("19)", *[b for b in range(1, 214) if f(17, b, 2)])
print("20)", f"{min(t)} {max(t)}")
print("21)", min([b for b in range(1, 214) if not f(17, b, 2) and f(17, b, 4)]))
