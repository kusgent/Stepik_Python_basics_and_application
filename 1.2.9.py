# https://stepik.org/lesson/24458/step/9?unit=6765

objects = [1, 2, 1, 2, 3]
ans = 0
l = []
for obj in objects:
    if id(obj) not in l:
        ans += 1
        l.append(id(obj))
print(ans)