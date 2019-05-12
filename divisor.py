def sample_code(N):

    print('Prime factor')
    fct = factorize(N)
    print(fct,num(fct))

    print('divisor')
    for div in divisorize(fct):
        print(div,num(div))


def divisorize(fct):
    b,e = fct.pop()
    pre_div = divisorize(fct) if fct else [[]]
    suf_div = [[(b,k)] for k in range(e + 1)]
    return [pre + suf for pre in pre_div for suf in suf_div]

def factorize(N):
    fct = []
    b,e = 2, 0
    while b * b <= N:
        while N % b == 0:
            N = N // b
            e = e + 1
            if e > 0:
                fct.append((b,e))
            b,e = b + 1,0
        if N > 1:
            fct.append((N,1))
        return fct

def num(fct):
    a = 1
    for base, exponent in fct:
        a = a * base ** exponent
    return a

N = int(input())
sample_code(N)