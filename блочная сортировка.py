#блочная сортировка
def block_sort(lst, n):
    blocks = []
    for i in range(n):
        blocks.append([])
    if len(lst) <= 1:
        return
    for element in lst:
        blocks[(n * (element - min(lst))) // (max(lst) - min(lst) + 1)].append(element)
    for block in blocks:
        block_sort(block, n)
    index = 0
    for block in blocks:
        for element in block:
            lst[index] = element
            index += 1

list1 = [15,24,4,2,8,5,10,7,21,11,9]
block_sort(list1,6)
print(list1)

