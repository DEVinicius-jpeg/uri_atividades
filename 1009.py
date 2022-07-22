nomeVendedor = input()
salarioVendedor = float(input())
vendasVendedor = float(input())

calculoComissao = "%.2f"%(salarioVendedor + (vendasVendedor * 0.15 ))

print(f"TOTAL = R$ {calculoComissao}")