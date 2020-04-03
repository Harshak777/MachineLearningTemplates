inp = int(input())
s = 'abcdefghijklmnopqrstuvwxyz'
li = list(s)
ml = []
if inp >=1 and inp <=26:
    i = inp
    k = i-1
    print(k,li[k])
    o=k
    while o >=0:
        st = ''
        for l in range(k):
            if l >= o and l <=k:
                st+=str(li[l])
            else:
                st+='-'
            st+='-'
        l = k
        st +=li[k]
        st2 = ''
        for l in range(k):
            if l >= o and l <=k:
                st2 =str(li[l])+st2
            else:
                st2 ='-'+st2
            st2 ='-'+st2
        print(st+st2)
        ml.append(st+st2)
        o -=1
    i = len(ml)-2
    while i>=0:
        print(ml[i])
        i -=1