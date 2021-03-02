class Student:
  def __init__(self, scores = []):
    self.scores = scores

  def avg(self):
    return round(sum(self.scores) / len(self.scores))



# instance / objects
Sarkash = Student(scores = (1,2,3,4,5,56,32))
Tina = Student(scores = [45,23,67,12])
Luna = Student(scores = {45,32,12,87})

print(Sarkash.avg())
print(Tina.avg())
print(Luna.avg())