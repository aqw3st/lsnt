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
    assert Vector(self.vector).shape() == Vector(vec2).shape(), 'Vectors dimensions don`t match'
    res_vec = []
    for i, j in zip(self.vector, vec2.vector):
      res_vec.append(i*j)
    return res_vec

  def shape(self):
    if len(self.vector) == 0: return (0, )
    if isinstance(self.vector[0], int): return (len(self.vector), )
    else: return len(self.vector), len(self.vector[0])

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

  @staticmethod
  def angle(vec1, vec2, degree = False):
    rad = math.acos(vec1 * vec2 / (vec1.mag() * vec2.mag()))
    if degree == True:
      return rad * (180/math.pi)
    return rad

  @staticmethod
  def cross_product(vec1, vec2, degree = 0):
    assert vec1.shape() == (3,), f"""Only (3,) vectors allowed, but {vec1} is {vec1.shape()}"""
    assert vec2.shape() == (3,), f"""Only (3,) vectors allowed, but {vec2} is {vec2.shape()}"""
    raise ValueError("Not implemented yet") 

vec1 = Vector([1,2,3,10])
vec2 = Vector([4,5,6,8])
# print(vec1.shape())
# print(Vector.cross_product(vec1, vec2))
print(vec1+vec2)
print(vec1*vec2)
# print(vec1.mag())
# print(vec1.dot(vec2))
# print(Vector.angle(vec1, vec2, degree = True))