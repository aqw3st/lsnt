#implement vector ops
import math

class Vector():
  def __init__(self, vector):
    self.vector = vector
  
  def __repr__(self):
    return f"vector({self.vector})"

  def __add__(self, vec2):
    res_vec = []
    for i, j in zip(self.vector, vec2.vector):
      res_vec.append(i+j)
    return Vector(res_vec)

  def __mul__(self, vec2):
    res_vec = []
    for i, j in zip(self.vector, vec2.vector):
      res_vec.append(i*j)
    return sum(res_vec)

  def mag(self):
    return math.sqrt(sum([el**2 for el in self.vector]))

  def dot(self, vec2, angle = 0, eps=0.00001):
    cos_degree = math.cos(math.radians(angle))
    l1, l2 = Vector(self.vector).mag(), vec2.mag()
    return l1 * l2 * cos_degree
  

  def scmul(self, k):
    for i in range(len(self.vector)):
      self.vector[i] *= k
    return Vector(self.vector)

  
  # @staticmethod
  def angle(vec1, vec2):
    cos_degree = vec1 * vec2 / (vec1.mag() * vec2.mag())
    
    return cos_degree



vec1 = Vector([1,2,3])
vec2 = Vector([4,5,6])
# print(vec1+vec2)
# print(vec1*vec2)
# print(vec1.mag())
# print(vec1.dot(vec2))
# print(angle(vec1, vec2))
print(Vector.angle(vec1, vec2))