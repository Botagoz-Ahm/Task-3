n = input()
number=0
for i in range(len(n)):
    if n[i]=='f':
        number+=1
        if number==2:
            print(i)

if number==1:
    print('-1')
elif 'f' not in n:
    print('-2')
