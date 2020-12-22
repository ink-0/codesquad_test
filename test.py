#step-2 평면큐브  테스트코드
#U 테스트
def U(cube,type): # U 테스트
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

# 모든 함수 입력받았을 때 다 작동되는 지 테스트, 그러나 UUR처럼 연속된 입력에서는 오류 발생 확인
inp=0
while inp != 'Q':
    cmd = list(input('cube> '))
    for i in range(len(cmd)):
        inp=cmd.pop(0)
        print(inp)
        if inp == "U":
            cube = U(cube, 'left')
        elif inp == "U'":
            cube = U(cube, 'right')

        elif inp == "B":
            cube = B(cube, 'right')
        elif inp == "B'":
            cube = B(cube, 'left')

        elif inp == "R":
            cube = R(cube, 'up')
        elif inp == "R'":
            cube = R(cube, 'down')

        elif inp == "L":
            cube = L(cube, 'down')
        elif inp == "L'":
            cube = L(cube, 'up')

        if inp=='Q':
            print('bye~')
            break
        for i in cube:
            print(*i)
        print()