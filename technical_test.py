lines = [1,8,6,2,5,4,8,3,7]

def getMaxArea(lines):
    maxArea = 0
    area = 0
    maxheight = 0
    
    length = len(lines)
    for i in range(length):
        area = (i+1) * lines[i]
        
        if area > maxArea:
            maxArea = area

    
print(getMaxArea(lines))