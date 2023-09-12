def mostCalories(data):
  
  biggestNum = 0
  whichElf = 0

  for i in data:
    for j in i:
      if biggestNum == 0 or biggestNum < int(j):
        biggestNum = int(j)
        whichElf = data.index(i) + 1

  return biggestNum, whichElf

def calorieByElf(list):
  # print("".join(data).split(" "))

  elfAndCalories = []
  linesCount = 0
  idx = 0
  
  for i in list:

    if i == "\n": # Empty line. Warning: there is also a line break for each line with numbers.
      linesCount += 1
    
    if linesCount != 1 and i != "\n":
      
      if idx > len(elfAndCalories) - 1:
        elfAndCalories.append([])
        
      elfAndCalories[idx].append(i[:-1])
      
    elif linesCount == 1:
      
      idx += 1
      linesCount = 0
      continue

  return elfAndCalories

with open ("exemplo1.txt", "r") as file:
  data = file.readlines()

  result = calorieByElf(data)
  num, elf = mostCalories(result)

  print(result)
  print(f"{elf}° elfo: {num} calorias.")

print("\n----------------------------------------\n")

with open ("exemplo2.txt", "r") as file:
  data = file.readlines()

  result = calorieByElf(data)
  num, elf = mostCalories(result)

  print(result)
  print(f"{elf}° elfo: {num} calorias.")