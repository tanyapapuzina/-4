#Пирамидальная сортировка
def  a(lst, i, n):
    i_left = 2 * i + 1
    i_right = 2 * i + 2
    i_largest = i
    if i_left <= n and lst[i_left] > lst[i_largest]:
        i_largest = i_left
    if i_right <= n and lst[i_right] > lst[i_largest]:
        i_largest = i_right

    if i_largest == i:
        return
    else:
        lst[i_largest], lst[i] = lst[i], lst[i_largest]
        a(lst,i_largest,n)

def prmd(lst):
    middle = len(lst) // 2
    for index in reversed(range(0, middle + 1)):
        a(lst, index, len(lst) - 1)

def prmd_sort(lst):
    prmd(lst)
    for index in reversed(range(0, len(lst))):
        lst[0], lst[index] = lst[index], lst[0]
        a(lst, 0, index - 1)

lst = [30,27,19,20,21,17,4,6,3,7,18,8,1,2]
prmd_sort(lst)
print(lst)
