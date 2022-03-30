def loop_over_list():
    numbers = [1,2,3,4,5,6]
    result = []
    
    for item in numbers:
        item += 1
        result.append(item)
        
    
    
    return result

print(loop_over_list())