N = 10**5
is_prime = [1]*N
# We know 0 and 1 are composites
is_prime[0] = 0
is_prime[1] = 0

def sieve():
    """
    We cross out all composites from 2 to sqrt(N)
    """
    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= N:
        # If we already crossed out this number, then continue
        if is_prime[i] == 0:
            i += 1
            continue

        j = 2*i
        while j < N:
            # Cross out this as it is composite
            is_prime[j] = 0
            # j is incremented by i, because we want to cover all multiples of i
            j += i

        i += 1

sieve()
def first_prime_forward(num):     
    for i in range(num,num**2):
      if i>1:
        if(is_prime[i]):
            return i

def first_prime_backward(num):     
    for i in range(num,0,-1):
      if i>1:
        if(is_prime[i]):
            return i
        
def solve(num):

    magic = int(num**(1/2))
    #print(magic)
    num1 = first_prime_forward(magic+1)
    num2 = first_prime_backward(magic)
    if(num1*num2 == num):
        #print(num1,num2)
        print(num)
    else:
        return solve(num-1)


t = int(input())
for i in range(t):
    n = int(input())
    print(f"Case #%i: "%(1+i),end=" ")
    solve(n)
