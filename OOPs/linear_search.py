pos=-1
def search(lst,n):

    for i in range(len(lst)):
        if lst[i]==n:
            globals()['pos']=i
            return True

    '''i=0

    while i< len(lst):
        if lst[i]==n:
            globals()['pos']=i
            return True
        i+=1
'''


lst=[2,14,15,36,46,76,87]
n=int(input('Enter Num to search:'))


if search(lst,n):
    print('Found',pos+1)
else:
    print('Not found')
    
print('Msg from GIT hub')
