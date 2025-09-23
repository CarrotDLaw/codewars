# 541c8630095125aba6000c00

def digital_root(n):
    while n >= 10:
        sum = 0
        temp = n
        
        while temp > 0:
            sum += temp % 10
            temp //= 10
            
        n = sum
            
    return n
