

#_*_coding: UTF-8_*_
# from prettytable import PrettyTable
# pt = PrettyTable()
#
# pt.field_names=[i for i in range(1,10)]
#
# mulp=[["{b}x{a}={c}".format(a=a,b=b,c=a*b) if a>=b else "" for b in range(1,10)] for a in range(1,10)]
# map(pt.add_row,mulp)
#
# print(pt)



for a in range(1,10):
    d = []
    for b in range(1,10):
        if b <= a:
            c = '%d*%d=%d'%(a,b,a*b)
            d.append(c)
    print(d)
