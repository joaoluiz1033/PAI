
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
    
if __name__ == "__main__":
    [x,y] = convert_to_coordinate('b5')
    print(x,y)    
    pos = reconvert_to_alg([x,y])
    print(pos)