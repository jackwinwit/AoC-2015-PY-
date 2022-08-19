with open("Day2/data.txt", "r") as file:
    for item in file:
        if item[1] == "x":
            length = item[0]
        elif item[2] == "x":
            length = item[0] + item[1]
        elif item[3] == "x":
            width = item[2]

        

