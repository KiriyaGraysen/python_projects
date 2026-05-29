hash = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    ]
    
def hashFunction(data):
    sum_of_chars = 0
    
    for char in data:
        sum_of_chars += ord(char)
        
    return sum_of_chars % 10
    
def addData(data, hashTable):
    index = hashFunction(data)
    hashTable[index].append(data)
    
def deleteData(data, hashTable):
    index = hashFunction(data)
    
    for i in range(len(hashTable[index])):
        if hashTable[index][i] == data:
            return hashTable[index].pop(i)
            
    return None

addData("Hailynn", hash)
addData("Stuart", hash)
print(hash)

deleteData("Stuart", hash)
print(hash)