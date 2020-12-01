n = int(input())
r, c = map(int, input().strip().split())
matrix = []
for i in range(n):
    a = input().strip()
    matrix.append(a)

    if 'p' in a:
        r_diff = r -i
        c_diff = c - a.index('p')

while True:
    if r_diff != 0:
        if r_diff<0:
            r_diff += 1
            print('DOWN')
        elif r_diff>0:
            r_diff -= 1
            print('UP')
        break
    if c_diff != 0:
        if c_diff<0:
            c_diff += 1
            print('RIGHT')
        elif c_diff>0:
            c_diff -= 1
            print('LEFT')
        break
        
        
        
'''
Sample Input

5
2 3
-----
-----
p--m-
-----
-----

Sample Output

LEFT

'''
