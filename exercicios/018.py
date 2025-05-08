import math
angulo=float(input("Digite um angulo: "))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print("O angulo de {} tem o seno {:.2f}".format(angulo, seno))
print("O angulo de {} tem o cosseno {:.2f}".format(angulo, cos))
print("O angulo de {} tem a tangente {:.2f}".format(angulo, tan))