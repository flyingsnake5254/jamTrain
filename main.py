prompt = "請輸入指令: 1.英翻中 2.中翻英 3.離開 \n"

dic = {
    "bird": "鳥", "cat": "貓",
    "dog": "狗", "fish": "魚",
    "mouse": "老鼠", "rabbit": "兔子",
    "cow": "母牛", "horse": "馬",
    "pig": "豬", "sheep": "綿羊"
}


def getKey(value):
    global dic
    keys = dic.keys()
    for k in keys:
        if dic[k] == value:
            return k
    return None


def fun1():
    global dic
    inputCmd = input("請輸入英文單字: ")
    if inputCmd in dic.keys():
        print(inputCmd + " => " + dic[inputCmd] + "\n")
    else:
        print("查無此單字" + "\n")


def fun2():
    global dic
    inputCmd = input("請輸入中文單字: ")
    if inputCmd in dic.values():
        print(inputCmd + " => " + getKey(inputCmd) + "\n")
    else:
        print("查無此單字" + "\n")


while True:
    try:
        cmd = input(prompt)
        if cmd == "1":
            fun1()
        elif cmd == "2":
            fun2()
        elif cmd == "3":
            print()
            break
        else:
            print("請輸入正確的指令!")
            print()
    except:
        break