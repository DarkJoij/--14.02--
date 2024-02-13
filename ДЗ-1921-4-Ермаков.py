def f(s, m):
    if 45 <= s <= 112:
        return m % 2 == 0
    if s > 112:
        return m % 2 != 0
    if m == 0: 
        return 0

    h = [f(s + 2, m - 1), f(s * 3, m - 1)]

    return any(h) if (m - 1) % 2 == 0 else all(h)


to = [s for s in range(1, 45) if not f(s, 2) and f(s, 4)]

print("19)", min([s for s in range(1, 45) if f(s, 2)]))
print("20)", len([s for s in range(1, 45) if not f(s, 1) and f(s, 3)]))
print(f"21) {min(to)}, {max(to)}")
