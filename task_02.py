
def coincidence(list=None,a=None,b=None):
    if list == None or a == None or b == None:
        return []
    spisak=[]
    for i in range(len(list)):
            if isinstance(list[i],(int,float)) and not isinstance(list[i], bool):
                if a <= list[i] < b:
                    spisak.append(list[i])
    return spisak
print(coincidence([1, 2 , 3, 4, 5],3,6))
print(coincidence())
print(coincidence([True, None, 1, 'foo',4, 2, 2.5],1, 4))