def search(L,e):
    '''Assume que L é uma lista em ordem crescente'''
    def bsearch(L,e,low,high):
        if high==low:
            return L[low]==e
        mid=(low+high)//2
        if L[mid]==e:
            return True
        elif L[mid]>e:
            if low==mid:
                return False
            else:
                return bsearch(L,e,low,mid-1)
        else:
            return bsearch(L,e,mid+1,high)
    if len(L)==0:
        return False
    else:
        return bsearch(L,e,0,len(L)-1)

L=[1,2,3,4,5,6,7,8,9]
