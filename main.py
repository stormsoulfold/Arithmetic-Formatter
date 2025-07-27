def arithmetic_arranger(problems, show_answers=False):
    row = ""
    row1 = []
    row2 = []
    operator = []
    i = 0
    result = ""
    #Assign row1, row2 and operator
    for problem in problems:
        for char in problem.strip(" "):
            if char == "+" or char == "-":
                row1.append(row)
                row = ""
                operator += char
            elif char.isdigit():
                row += char
        row2.append(row)
        row = ""

    #First Row
    space = "    "
    for n in row1:
        s = 0
        for char in n:
            s -= 1
        result += space[:s] + row1[i]
        i += 1 
        space = "          "
    i = 0
    result += "\n"

    #Second Row
    space = "  "
    for n in row2:
        s = 0
        for char in n:
            s -= 1
        result += operator[i] + space[:s] + " " + row2[i] + "    "
        i +=1
        space = "   "
    result += "\n"

    #Third Row
    i = 0
    for problem in problems:
        ma = max(int(row1[i]),int(row2[i]))
        for char in str(ma):
            result += "-"
        result += "--    "
        i += 1

    return result

print(arithmetic_arranger(["39 + 8", "1 + 71","9999 + 9999", "523 - 49"]))
