def srt(lst):
    gap=len(lst)
    swaps=True
    while gap>1 or swaps:
        gap=max(1,int(gap/1.247))
        swaps=False
        for i in range(len(lst)-gap):
            j=i+gap
            if lst[i]>lst[j]:
                lst[i],lst[j]=lst[j],lst[i]
                swaps=True
    return lst
