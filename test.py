#step-2 평면큐브  테스트코드
#U 테스트
def U(cube,type):
    if type=='right':
        cube[0].insert(0,cube[0].pop()) # right 알고리즘 적용
    elif type=='left':
        cube[0].append(cube[0].pop(0)) # left 알고리즘 적용
    return cube


# B,R,L 함수에 큐브변경 알고리즘 적용
def B(cube, type):
    if type=='left':
        cube[2].append(cube[2].pop(0))
    elif type=='right':
        cube[2].insert(0,cube[2].pop())
    return cube
def R(cube, type):
    if type=='up':
        temp=cube[0][2]
        cube[0][2]=cube[1][2]
        cube[1][2]=cube[2][2]
        cube[2][2]=temp
    elif type=='down':
        temp=cube[2][2]
        cube[2][2]=cube[1][2]
        cube[1][2]=cube[0][2]
        cube[0][2]=temp
    return cube
def L(cube, type):
    if type=='up':
        temp=cube[0][0]
        cube[0][0]=cube[1][0]
        cube[1][0]=cube[2][0]
        cube[2][0]=temp
    elif type=='down':
        temp=cube[2][2]
        cube[2][0]=cube[1][0]
        cube[1][0]=cube[0][0]
        cube[0][0]=temp
    return cube

cube = [ ['R','R','W'],['G','C','W'],['G','B','B'] ]
for i in cube:
    print(*i)
print()

# while문 속에서 무한히 작동되는 지 테스트, Q입력하면 종료되는가 테스트
inp=0
while inp != 'Q':
    inp = input('cube> ')
    if inp=='U':
        U(cube,'left')

    elif inp=="U'":
        U(cube,'right')

    if inp=='Q':
        print('bye~')
        break
    for i in cube:
        print(*i)
    print()