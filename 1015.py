x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
distancia ="%.4f"%(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (0.5))

print(distancia)