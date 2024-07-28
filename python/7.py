import math

def area_of_triangle(a, b, c):


  s = (a + b + c) / 2
  area = math.sqrt(s * (s - a) * (s - b) * (s - c))
  return area

def main():
 


  a1 = float(input("Enter side a1: "))
  b1 = float(input("Enter side b1: "))
  c1 = float(input("Enter side c1: "))


  a2 = float(input("Enter side a2: "))
  b2 = float(input("Enter side b2: "))
  c2 = float(input("Enter side c2: "))

  
  area1 = area_of_triangle(a1, b1, c1)
  area2 = area_of_triangle(a2, b2, c2)


  total_area = area1 + area2

 
  percent1 = (area1 / total_area) * 100
  percent2 = (area2 / total_area) * 100

  print("Area of triangle 1:", area1)
  print("Area of triangle 2:", area2)
  print("Total area:", total_area)
  print("Triangle 1 contribution:", percent1, "%")
  print("Triangle 2 contribution:", percent2, "%")

if __name__ == "__main__":
  main()
