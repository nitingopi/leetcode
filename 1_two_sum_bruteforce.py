def two_sum(nums:list[int], target:int) -> tuple[int,int] | None:
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]+nums[j] == target:
                return i,j

nums = [2, 7, 11, 15]
target = 9
ans = two_sum(nums,target)
print(f"{ans=}")
nums = [3, 2, 4]
target = 6
ans = two_sum(nums,target)
print(f"{ans=}")
nums = [3, 3]
target = 6
ans = two_sum(nums,target)
print(f"{ans=}")
