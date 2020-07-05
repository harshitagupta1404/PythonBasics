''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    t=int(input())
    for i in range(t):
        n=int(input())
        p1=list(map(int,input().split()))
        p2=list(map(int,input().split()))
        power1=sorted(p1)
        power2=sorted(p2)
        #print(n,power1,power2)
        ctr1=0
        for i in range(n):
            if power1[i]>power2[i]:
                ctr1=ctr1+1
            else:
                j=1
                while i+j<len(power1) and power1[i+j]<=power2[i]:
                    #print("in while")
                    if i+j>=len(power1):
                        break
                    j=j+1
                    #print("in while j ",j,end=" ")
                if i+j>=n:
                        break
                power1[i],power1[i+j]=power1[i+j],power1[i]
                ctr1=ctr1+1
                #print("j",j,end=" ")
                if i+j+1==n:
                    break
            #print("i,ctr",i,ctr)
        print(ctr1)
    """    pow1=sorted(p1)
        pow2=sorted(p2)
        ctr2=0
        for i in range(n):
            if pow2[i]>pow1[i]:
                ctr2=ctr2+1
            else:
                j=1
                while i+j<n and pow2[i+j]<=pow1[i]:
                    #print("in while")
                    if i+j>=n:
                        break
                    j=j+1
                    #print("in while j ",j,end=" ")
                if i+j>=len(pow1):
                        break
                pow2[i],pow2[i+j]=pow2[i+j],pow2[i]
                ctr2=ctr2+1
                #print("j",j,end=" ")
                if i+j+1==n:
                    break
            #print("i,ctr",i,ctr)
        print(max(ctr1,ctr2))"""


main()


