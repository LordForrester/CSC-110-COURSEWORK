def big_diff(nums):
  highest = nums[0]
  lowest = nums[0]
  for val in nums:
      if val > highest:
          highest = val
      if val < lowest:
          lowest = val
  
  diff = highest - lowest

  return diff

def main():
    numList = [2, 5, 1, 9, 8, 4]

    print(big_diff(numList))

main()
    
