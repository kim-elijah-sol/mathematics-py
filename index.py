from sympy import Derivative, symbols

x = symbols('x')
fx = 4*(x**4)+3*x

f_prime = Derivative(fx, x).doit()
print(f"fx의 도함수 {f_prime}")

value_in_3 = f_prime.subs({ x: 3 })
print(f"x=3에서의 기울기 : {value_in_3}")

f_prime_prime = Derivative(f_prime, x).doit()
print(f"fx의 2계도함수 {f_prime_prime}")