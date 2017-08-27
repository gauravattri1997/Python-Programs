r=int(input())
for i in range(0,r):
    l = int(input())
    st = input()
    st = st.replace(".","")
    le = len(st)
    if st=='':
        print('Valid')
    elif le%2==0 and st[0]=='H' and st[le-1]=='T' and 'HH' not in st and 'TT' not in st:
        print('Valid')
    else:
        print('Invalid')
