import timeit

print("Выберите метод сортировки: 1-Быстрая сортировка;2-Сортировка расчёской;")
start_time = """
import qs
import comb

s=int(input())
nums=[34,6,2,4,8,5,21,32,12]
if s==1:
    print("Быстрая сортировка:",qs.quick_sort(nums))
if s==2:
    print("Сортировка расчёской",comb.srt(nums))
"""
end_time = timeit.timeit(start_time, number = 1)
print(end_time)
