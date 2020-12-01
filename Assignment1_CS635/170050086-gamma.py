import math

def gamma(N):
    b = int(math.floor(math.log(N,2)))
    r = N - pow(2,b)
    length = ""
    for i in range(b):
        length+="1"
    length+="0"
    # offset = bin(r).replace("0b","")
    offset = bin(N).replace("0b","")[1:]
    return length,offset

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--number", help="enter number to encoded")
args = parser.parse_args()
N = int(args.number)
if N>1:
    l,o = gamma(N)
    print(l + "," + o)