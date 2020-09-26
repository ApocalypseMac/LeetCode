# Query C(n, r) mod p in O(1) time after (linear) preprocessing

'''
1. basic idea (ref: https://www.geeksforgeeks.org/queries-of-ncrp-in-o1-time-complexity/)
C(n, r) = n! / (r! * (n-r)!)
C(n, r) \equiv n! * (r!)^-1 * ((n-r)!)^-1 mod p (-1 denotes modular inverse)
Thus we can calculate k! mod p and (k!)^-1 mod p in advance

2. calculate inverse factorial
n! = n * (n-1)!
(n!)^-1 \equiv n^-1 * ((n-1)!)^-1 mod p
Induction from 1 to N

3. calculate inverse number (ref: https://www.geeksforgeeks.org/modular-multiplicative-inverse-1-n/)
Method: Extended Euclidean Algorithm
Recursive call 
invn[a] = invn[p%a] * (p - p // a) % p
'''

p = 10 ** 9 + 7 # a large prime number
N = 10 ** 6 + 1 # max preprocessing length

# initialize
fac = [0] * N # n! mod p
inv = [1] * N # (n!)^-1 mod p

def init(p, N):
    fac[0] = 1
    for i in range(2, N): # after this, inv[:] == invn[:] (except 0)
        inv[i] = inv[p%i] * (p - p // i) % p
    for i in range(1, N):
        fac[i] = i * fac[i-1] % p
        inv[i] = inv[i] * inv[i-1] % p # invn[i] * inv[i-1] % p
    return

init(p, N)

def comb(a, b):
    if a < 0 or b < 0 or a < b:
        return 0
    return fac[a] * inv[b] * inv[a-b] % p

# test
print(comb(4, 2))
print(comb(15, 4))
print(comb(20, 3))




