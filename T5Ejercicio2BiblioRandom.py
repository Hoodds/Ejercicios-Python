# -*- coding: utf-8 -*-
# Calcular (IMC = peso (kg)/ [estatura (m)]2)
import random
estatura=round(random.uniform(1.0, 2.1), 2)
peso=round(random.uniform(50, 150), 2)
imc=round(peso/estatura**2, 2)
print("El IMC de alguien que pesa ",peso," kilos y mide ",estatura," metros es ",imc )