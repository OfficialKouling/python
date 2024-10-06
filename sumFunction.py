def sum(array):
    total = 0
    for i in array:
        total += i
    return total

def manyElements(array):
    def calculateElements(array, index):
        try:
            array[index]
            return calculateElements(array, index+1)
        except IndexError:
            return index
    try:
        array[0]
    except IndexError:
        return "No elements found."
    
    return f"Number of elements: {calculateElements(array, 0)}"

userArray = [1,3,5]
print(sum(userArray)+2)
print(manyElements(userArray))