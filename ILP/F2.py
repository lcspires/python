massa, altura = map(float, input().split())

IMC = massa / (altura*altura)

#print(f"IMC: {IMC:.2f}")

if IMC < 17:
    print("muito-abaixo-do-peso")
elif IMC >= 17 and IMC <= 18.49:
    print("abaixo-do-peso")
elif IMC >= 18.50 and IMC <= 24.99:
    print("peso-normal")
elif IMC >= 25 and IMC <= 29.99:
    print("acima-do-peso")
elif IMC >= 30 and IMC <= 34.99:
    print("obesidade-1")
elif IMC >= 35 and IMC <= 39.99:
    print("obesidade-2")
elif IMC >= 40:
    print("obesidade-3")
