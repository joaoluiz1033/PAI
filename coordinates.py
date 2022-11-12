
def convert_to_coordinate(alg):
    if alg[0] == 'a':
        return int(alg[1])-1,0
    if alg[0] == 'b':
        return int(alg[1])-1,1
    if alg[0] == 'c':
        return int(alg[1])-1,2
    if alg[0] == 'd':
        return int(alg[1])-1,3
    if alg[0] == 'e':
        return int(alg[1])-1,4
    if alg[0] == 'f':
        return int(alg[1])-1,5
    if alg[0] == 'g':
        return int(alg[1])-1,6
    if alg[0] == 'h':
        return int(alg[1])-1,7
    else: 
        return 'pls insert valid coordinate'
    
    
if __name__ == "__main__":
    x,y = convert_to_coordinate('b8')
    print(x,y)