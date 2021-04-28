celcius = float(input('suhu celcius : '))

celcius_reamur = 4/5
celcius_fahrenheit = 9/5

reamur = celcius * celcius_reamur
fahrenheit = (celcius * celcius_fahrenheit) + 32
print('%0.1f derajat celcius sama dengan %0.1f derajat reamur' %(celcius, reamur))
print('%0.1f derajat celcius sama dengan %0.1f derajat fahrenheit' %(celcius, fahrenheit))