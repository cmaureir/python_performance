import time

N = 1000

t_start = time.perf_counter_ns()
class Persona1:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad
  # def __repr__(self) ¿quizás?

for _ in range(N):
    p = Persona1("Cristian", 34)
t_end = time.perf_counter_ns()
print("Persona1", (t_end-t_start)/10**9)

t_start = time.perf_counter_ns()

from dataclasses import dataclass

@dataclass
class Persona2:
  nombre: str
  edad: int

for _ in range(N):
    p = Persona2("Cristian", 34)

t_end = time.perf_counter_ns()
print("Persona2", (t_end-t_start)/10**9)


t_start = time.perf_counter_ns()
from collections import namedtuple

Persona3 = namedtuple("Persona3", ["nombre", "edad"])
for _ in range(N):
    p = Persona3("Cristian", 34)
t_end = time.perf_counter_ns()
print("Persona3", (t_end-t_start)/10**9)

t_start = time.perf_counter_ns()
import typing

class Persona4(typing.NamedTuple):
  nombre: str
  edad: int

for _ in range(N):
    p = Persona4("Cristian", 34)
t_end = time.perf_counter_ns()
print("Persona4", (t_end-t_start)/10**9)
