
def removeElement(self, nums, val) -> int:
    tmp = []
    for i in nums:
        if i == val:
            continue
        tmp.append(i)
    for j in range(len(tmp)):
        nums[j] = tmp[j]
    return len(tmp)
    
removeElement([1,1,2,3],1)