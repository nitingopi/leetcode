def two_sum(nums:list[int], target:int) -> tuple[int,int] | None:
    map_dict: dict[int, int] = {}
    for i in range(len(nums)):
        if nums[i] in map_dict.keys():
            return  map_dict[nums[i]], i
        map_dict[target - nums[i]] = i

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
