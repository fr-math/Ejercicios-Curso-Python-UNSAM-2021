#%%
# Ejercicio 3.6 
for n in range(10):
    print(n, end=' ')
for n in range(10,0,-1):
    print(n, end=' ')
for n in range(0,10,2):
    print(n, end=' ')
#%%
# Ejercicio 3.7
data = [4, 9, 1, 25, 16, 100, 49]
min(data)
max(data)
sum(data)

for x in data:
    print(x)
for n,x in enumerate(data):
    print(n,x)
for n in range(len(data)):
    print(data[n])