def searchBinary(startPosition, lastPosition):
    if (startPosition>lastPosition):
        _temp = startPosition
        startPosition = lastPosition
        lastPosition = _temp
    x = startPosition
    myList = []
    while(x<=lastPosition):
        myList.append(x)
        x = x+1 
    # print(myList)
    low = startPosition
    high = lastPosition
    while(low<=high):
        mid = (low + high) // 2
        print(mid)
        userHowMany = int(input("It's bigger or smaller? "))
        if(userHowMany == 1):
            low = mid
        elif(userHowMany == 2):
            high = mid
        else:
            print(f"Your number is: {mid}")
            break
if __name__ == "__main__":
    startPosition = int(input("Give me a start position: "))
    lastPosition = int(input("Give me a finish position: "))
    searchBinary(startPosition, lastPosition)
