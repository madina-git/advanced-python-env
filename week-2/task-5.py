allowed = set("ABCEHKMOPTX Y".replace(" ", ""))
a = int(input())
for _ in range(a):
    plate = input().strip()

    if (
        len(plate) == 6 and #6 символов 
        plate[0] in allowed and #1 символ буква?
        plate[1:4].isdigit() and #2-5 символ цифра?
        plate[4] in allowed and # 5 символ буква?
        plate[5] in allowed # 6 символ буква?
    ):
        print("Yes") 
    else:
        print("No")
