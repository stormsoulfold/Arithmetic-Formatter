def arithmetic_arranger(problems, show_answers=False):
    row = ""
    row1 = []
    row2 = []
    operator = []
    problemCount = 0
    numberCount = 0
    i = 0
    result = ""
    answer = 0
#Assign row1, row2, operator and handle errors
    for problem in problems:
        problemCount +=1
        for char in problem.strip(" "):
            
            if char == "+" or char == "-":
                row1.append(row)
                row = ""
                operator += char
                if numberCount > 4:
                    return 'Error: Numbers cannot be more than four digits.'
                numberCount = 0
            elif char.isdigit():
                row += char
                numberCount += 1
            elif char == "/" or char =="*" or char =="x":
                return "Error: Operator must be '+' or '-'."                
            elif char ==" ":
                pass
            else:    
                return 'Error: Numbers must only contain digits.'
        if numberCount > 4:
                    return 'Error: Numbers cannot be more than four digits.'
        numberCount = 0
        if problemCount > 5:
            return 'Error: Too many problems.'
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
    result += "\n"

    #Fourth Row
    i = 0
    for op in operator:
        if op == "+":
            answer += int(row1[i]) + int(row2[i])
        elif op == "-":
            answer += int(row1[i]) - int(row2[i])
        result +=  str(answer) + "       "
        answer = 0
        i += 1
    return result

print(arithmetic_arranger(["39 + 8", "1 + 71","9999 + 9999", "523 - 49"]))
