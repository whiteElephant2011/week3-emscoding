import time


heights_string = input("Please enter the heights (space-separated): ")
heights = list(map(int, heights_string.split()))

print(f"loading request...")

start_time = time.time()

waterstored = 0
maxL = 0
maxR = 0
minmax = 0

for idx in range(len(heights)):
  for L in range(idx+1):
    if heights[L] > maxL:
      maxL = heights[L]
  for R in range(idx+1, len(heights)):
    if heights[R] > maxR:
      maxR = heights[R]
  minmax = min(maxL, maxR)
  if minmax > heights[idx]:
    waterstored += minmax - heights[idx]
  maxL = 0
  maxR = 0

print(f"The total amount of water that can be stored is {waterstored}.")


end_time = time.time()
elapsed_time = end_time - start_time

rounded_time = round(elapsed_time, 5)

print("This took {} seconds to calculate.".format(rounded_time))
print()
time.sleep(3)
print("water was said in a british accent")






