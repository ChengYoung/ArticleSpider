
number = [4,5,0,45,21,65,8,10]

for item in number:
    try:
        result = 20 / item
    except:
        while(item<10):
            item = item + 1
            result = 20 /item
            if item != 0 :
                break
    print(result)