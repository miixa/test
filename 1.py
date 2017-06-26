y = [[55,69022],[53,83029]]
x = [[37,92688],[39,2271]]

y1 = [[53,83029],[55,69022]]
x1 = [[39,2271],[37,92688]]

def xy(a):
    up_down = a[0][0] - a[1][0]
    if up_down > 0 :
        a[0].insert(2,0)
        a[1].insert(1,99999)
        counter = a[0][0]
        start = a[0][0]
        end = a[1][0]
        i = 0
        while counter >= end :
            if counter == start:
              i += 1
              counter -= 1
              continue
            if counter == end:
                break
            a.insert(i,[counter,99999,0])
            counter -= 1
            i += 1

    if up_down < 0 :
        a[0].insert(2,99999)
        a[1].insert(1,0)
        counter = a[0][0]
        start = a[0][0]
        end = a[1][0]
        i = 0
        while counter <= end :
            if counter == start:
                i += 1
                counter += 1
                continue
            if counter == end:
                break
            a.insert(i,[counter,0,99999])
            counter += 1
            i += 1
    return (a)

a1 = []
j = 1
for a in xy(y):
    i = a[1]
    while i > a[2]:
        a1.insert(j,[a[0],i,a[2]])
        i -= 100
        j += 1
#print(a1)

a2 = []
j = 1
for a in xy(x):
    i = a[1]
    while i < a[2]:
        a2.insert(j,[a[0],i,a[2]])
        i += 100
        j += 1
#print(a2[1000])

b1=[1,2,3,4,5]
b2=[6,7,8,9,0]
a1 = len(b1)
a2 = len(b2)
a3 = a1 - a2
for
