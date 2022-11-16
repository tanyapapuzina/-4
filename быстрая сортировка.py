def quick_sort(nums):
    if len(nums)<=1:
        return nums
    else:
        q=nums[len(nums)//2]
        l_nums=[]
        r_nums=[]
        middle=[q]
        for n in nums:
            if n < q:
                l_nums.append(n)
            elif n > q:
                r_nums.append(n)
            else:
                continue
        return quick_sort(l_nums) + middle + quick_sort(r_nums)
