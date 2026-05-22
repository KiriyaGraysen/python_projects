def logic():
    n = int(input("\nHow many data are there in the dataset?: "))
    
    x = []
    for i in range(n):
        x.append(float(input(f"Data {i + 1}: ")))
    
    x.sort()
    
    median = 0
    if len(x) % 2 == 0:
        median = (x[len(x) // 2 - 1] + x[len(x) // 2]) / 2
        
    elif len(x) % 2 == 1:
        median = x[len(x) // 2]
        
    print(f"Median: {median}")