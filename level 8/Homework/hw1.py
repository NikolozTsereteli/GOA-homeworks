#1) მომხმარებელს შემოატანინეთ ორი რიცხვი, შემდეგ კი შეადარეთ ეს ორი რიცხვი ერთმენთს, მიღებული მნიშვნელობა შეინახეთ ცვლადში და შემდეგ დაბეჭდეთ მისი მონაცემთა ტიპი და მნიშვნელობა

num1 = int(input("How long do you sleep usually: "))
num2 = int(input("For how long can you hold your breath: "))
Truth = num1 > num2
Lie = num1 < num2
print(Truth)
print(Lie)
print(type(Truth))
print(type(Lie))
