import random
chance = int(input("남은 기회를 입력해 주세요. \n"))
while chance:
    chance -= 1
    chance_name = input("기회의 이름을 입력해 주세요. \n")
    possibility = int(input("붙을 확률을 입력해 주세요. %단위 \n"))
    result = random.choices([True, False], weights=[possibility, 100-possibility])
    if result[0]:
        print(chance_name + " 합격..!")
    else:
        print(chance_name + " 불합격..ㅠ")
