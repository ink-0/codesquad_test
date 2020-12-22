#step-2 평면큐브  테스트코드
#U 테스트
def U(cube,type): # U 테스트
    if type=='right':
        cube[0].insert(0,cube[0].pop()) # right 알고리즘 적용
    elif type=='left':
        cube[0].append(cube[0].pop(0)) # left 알고리즘 적용
    return cube

# B,R,L 함수생성
def B(cube, type):
    print('B')
    return cube

def R(cube, type):
    print('R')
    return cube

def L(cube, type):
    print('L')
    return cube

cube = [ ['R','R','W'],['G','C','W'],['G','B','B'] ]
for i in cube:
    print(*i)
print()

print(U(cube,'right')) # U -> R 테스트
print(U(cube,'left')) # U -> L 테스트

# B,R,L 함수 작동확인
print(R(cube,'type'))
print(L(cube,'type'))
print(B(cube,'type'))