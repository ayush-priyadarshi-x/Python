with open("pythonLInes.txt") as f: 
    contentArray = f.readlines()
    for line, contentLine in enumerate(contentArray, start=1): 
        if("python".upper() in contentLine.upper()): 
            print(f"The lines contains python : {line}")
            continue
    else: 
        print("Lines is finished. ")
        