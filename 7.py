"""
Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A formula de conversão é: C = 5.0 * ( F - 32.0) / 9.0,sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.
"""

f = float(input())

c = 5 * (f - 32 ) / 9

print(c)