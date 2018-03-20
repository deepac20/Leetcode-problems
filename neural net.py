def nnet(n,w,b,minX,maxX):
    scount = 0
    nscount = 0
    id = maxX-minX+1
    x = minX
    while(id != 0):
        xtemp = x
        for i in range(n):
            y = w[i]*xtemp + b[i]
            xtemp= y
        if y % 2 == 0:
            nscount += 1
        else:
            scount += 1
        x += 1
        id -= 1
    print(str(nscount) + " " + str(scount))
    return 0
    
def main():
    t = eval(input())
    for j in range(t):
        w=[]
        b=[]
        n,minX,maxX = [int(x) for x in input().split()]
        for i in range(n):
            wtemp, btemp = map(int, input().split())
            w.append(wtemp) 
            b.append(btemp)
        nnet(n,w,b,minX,maxX)
    return 0

if __name__ == '__main__':
    main()