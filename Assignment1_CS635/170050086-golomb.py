import math

def golomb(M,N):                
    q = math.floor(N/M)
    r = N%M
    res = ""
    for i in range(int(q)):
        res += "1"
    res += "0"
    if M == 1:
        return res
    b = math.floor(math.log(M,2))
    if r >= pow(2,b+1) - M:
        r = r + pow(2,b+1) - M
        r = bin(r).replace("0b", "")
        try:
            for i in range(int(b+1)-len(r)):
                res += "0"
        except:
            pass
    else:
        r = bin(r).replace("0b", "")
        try:
            for i in range(int(b)-len(r)):
                res += "0"
        except:
            pass
  
    res+=r
    return res


import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--parameter", help="enter parameter value")
parser.add_argument("-n", "--number", help="enter number to encoded")

args = parser.parse_args()

M = int(args.parameter)
N = int(args.number)
if M>0 and N>0:
    print(golomb(M,N))
else:
    print("invalid input")

