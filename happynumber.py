def happynumber(num):
    def get(number):
        tot=0
        while number>0:
            rem=number%10
            tot=tot+(rem*rem)
            number=number//10
        return tot
    slow=num
    fast=get(num)
    while slow!=fast:
        slow=get(slow)
        fast=get(get(fast))
        if fast==1:
            return True
    return slow==True
num=19
print(happynumber(num))