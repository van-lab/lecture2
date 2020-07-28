i = 28
print(f"i is {i}")
f = 2.8
print(f"f is {f}")
b = True
print(f"b is {b}")
n = None
print(f"n is {n}")
    
x = 28
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
print("Sequences")
name = "alice"
print (name[0], name[1])
print("tuple type")
coord = (10.0, 20.0)
print (coord[0], coord[1])
print("list type")
names = ["alice", "bob", "charlie"]
print (names[0], names[1])

print("loop")
for i in range(5):
    print(i)
for name in names:
    print(name)
print("set type, item in set unique")
s = set()
s.add(1)
s.add(2)
s.add(3)
print(s)
print("dictionary type key:value")
ages = {"alice":22, "bob":27}
ages["charlie"] = 30
ages["alice"] += 1
print(ages)
