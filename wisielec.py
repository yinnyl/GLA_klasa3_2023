password = "kanapka"

score = ("_" * len(password))
print(score)
guess = 1
tries = 6
all_letters = []

while guess <= 6:
    answer = input("Odgadnij literę: ")
    if answer in password:
        print("dobra litera")
        score = score[:password.index(answer)] + answer + score[password.index(answer)+1:]
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
        print("Liczba prób:", tries)
        print(all_letters)
        if tries == 0:
            print("Przegrałeś...")
    all_letters.append(answer.upper())
    if score == password:
        print("Zgadłeś!!!")
        break
