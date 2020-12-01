n = int(input())
matrix = []
for i in range(n):
    a = input().strip()
    matrix.append(a)

    if 'm' in a:
        m_r = i
        m_c = a.index('m')
    if 'p' in a:
        p_r = i
        p_c = a.index('p')
    
r_diff = m_r - p_r
c_diff = m_c - p_c

while True:
    if r_diff != 0:
        if r_diff<0:
            r_diff += 1
            print('DOWN')
        elif r_diff>0:
            r_diff -= 1
            print('UP')
    if c_diff != 0:
        if c_diff<0:
            c_diff += 1
            print('RIGHT')
        elif c_diff>0:
            c_diff -= 1
            print('LEFT')
    if r_diff == 0 and c_diff == 0:
        break
        
        
        
        
'''
Sample input

3
---
-m-
p--

Sample output

DOWN
LEFT

'''
