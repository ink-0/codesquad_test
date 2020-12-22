#step-2 평면큐브  테스트코드
#U 테스트
def U(cube,type):
    if type=='right':
        print('U에서 right 호출')
    elif type=='left':
        print('U에서 left 호출')
    return cube

cube = [ ['R','R','W'],['G','C','W'],['G','B','B'] ]
for i in cube:
    print(*i)
print()

U(cube,'right') # right호출 테스트
U(cube,'left') # left호출 테스트