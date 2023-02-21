#default value argument function
def cal_total(p,r=3.5,t=2):
    i=p*r*t/100
    tt=p+i
    return tt

print(cal_total(10000))
print(cal_total(20000,5))
print(cal_total(30000,6,3))
print(cal_total(r=9,p=2000))

