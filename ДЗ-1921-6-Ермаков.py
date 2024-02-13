def f(a, b, m):
    if a + b <= 20:
        return m % 2 == 0
    if m == 0:
        return 0
    
    h = [
        f(a - 1, b, m - 1), 
        f((a + 1) // 2, b, m - 1),  
        f(a, b - 1, m - 1), 
        f(a, (b + 1) // 2, m - 1),  
    ]

    return any(h) if (m - 1) % 2 == 0 else all(h)


t = [b for b in range(11,1000) if not f(10, b, 1) and f(10, b, 3)]

print("19)", *[b for b in range(11,1000) if f(10, b, 2)])
print("20)", f"{min(t)} {max(t)}")
print("21)", *[b for b in range(11,1000) if not f(10, b, 2) and f(10, b, 4)])
