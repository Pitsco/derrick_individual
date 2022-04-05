# OOP
class Triangular:
    def __init__(self):
        self.triSeq = [0, 1]
    def __call__(self, n):
        if n < len(self.triSeq):
            return self.triSeq[n]
        else:
            # Compute the requested Factorial number
            triangularNumber = self(n-1)+n 
          
          # two recursive calls to self (__call__(self, n))
            self.triSeq.append(triangularNumber) # builds list, with most nested of the calculations 1st
        return self.triSeq[n]
      
tri_of = Triangular() # object instantiation and run __init__ method

# Imperative
def triangular_number(n):
    return n * (n + 1) / 2

def trian():
  n1 = int(input("Enter a number: "))
  n2 = int(input("Enter another number: "))
  
  print("Imperative: The {n1} Term of Triangular Number Sequence is: ")
  print(int(triangular_number(n1)))

  
  print("Imperative: The {n2} Term of Triangular Number Sequence is: ")
  print(int(triangular_number(n2)))
  
print("===================================================================")
  
print("OOP: The {n1} term of Triangular Number Sequence is: ")
print(tri_of(n1))
  
print("OOP: The {n2} term of Triangular Number Sequence is: ")
print(tri_of(n2))

if __name__ == "__main__":
    trian()