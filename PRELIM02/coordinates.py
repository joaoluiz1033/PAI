
def convert_to_coordinate(alg):
    if alg[0] == 'a':
        return [0,int(alg[1])-1]
    if alg[0] == 'b':
        return [1,int(alg[1])-1]
    if alg[0] == 'c':
        return [2,int(alg[1])-1]
    if alg[0] == 'd':
        return [3,int(alg[1])-1]
    if alg[0] == 'e':
        return [4,int(alg[1])-1]
    if alg[0] == 'f':
        return [5,int(alg[1])-1]
    if alg[0] == 'g':
        return [6,int(alg[1])-1]
    if alg[0] == 'h':
        return [7,int(alg[1])-1]
    else: 
        return 'pls insert valid coordinate'

def reconvert_to_alg(coord):
    if coord[0] == 0:
        return f"a{coord[1]+1}"
    if coord[0] == 1:
        return f"b{coord[1]+1}"
    if coord[0] == 2:
        return f"c{coord[1]+1}"
    if coord[0] == 3:
        return f"d{coord[1]+1}"
    if coord[0] == 4:
        return f"e{coord[1]+1}"
    if coord[0] == 5:
        return f"f{coord[1]+1}"
    if coord[0] == 6:
        return f"g{coord[1]+1}"
    if coord[0] == 7:
        return f"h{coord[1]+1}"
    
def get_one_to_other(alg1,alg2):
#this function takes the positions to go from 1 to 2 (without taking \
    #point 1 to account)    
#alg1 ==  first coordinates
#alg2 == second coordinates
    l = []
    
    coord1 = convert_to_coordinate(alg1)
    coord2 = convert_to_coordinate(alg2)
    
    x1 = coord1[0]
    y1 = coord1[1]
    
    x2 = coord2[0]
    y2 = coord2[1]
    
    if abs(x1-x2) == abs(y1-y2):
        incx = 1
        incy = 1
        if x1 > x2:
            incx = -1
        if y1 > y2:
            incy = -1
        x_pos = x1
        y_pos = y1
        while x_pos != x2 and y_pos != y2:
            x_pos += incx
            y_pos += incy
            l.append(reconvert_to_alg([x_pos,y_pos]))
    elif x1 == x2 or y1 == y2:
        if x1 == x2:
            incy = 1
            if y1 > y2:
                incy = -1
            y_pos = y1
            while y_pos != y2:
                y_pos += incy
                l.append(reconvert_to_alg([x1,y_pos]))
        else:
            incx = 1
            if x1 > x2:
                incx = -1
            x_pos = x1
            while x_pos != x2:
                x_pos += incx
                l.append(reconvert_to_alg([x_pos,y1]))
            
    else:
        l.append(alg2)
    #check straight return list
    #else knight return position 
    return l
    
if __name__ == "__main__":
    [x,y] = convert_to_coordinate('d2')
       
    pos = reconvert_to_alg([x,y])
    