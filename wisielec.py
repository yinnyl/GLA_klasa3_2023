password = "wisielec"
score = list(password)

for i in range(len(password)):
    score[i] = "_"

print(score)
guess = 1
tries = 6
all_letters = []

while guess <= 6:
    answer = input("Odgadnij literę: ")
    if answer in password:
        print("dobra litera")
        for i in range(len(password)):
            if password[i] == answer:
                score[i] = answer
        print(score)
        print("Liczba prób:",tries)
        print(all_letters)
        if answer.upper() in all_letters:
            print("ta litera już była")
            print("Liczba prób:", tries)
            all_letters.remove(answer.upper())
    else:
        print("zła litera")
        guess += 1
        tries -= 1
        print(score)
        print("Liczba prób:", tries)
        print(all_letters)
        if tries == 0:
            print("Przegrałeś...")
    all_letters.append(answer.upper())
    if ''.join(score) == password:
        print("Zgadłeś!!!")
        print(password)
        break
