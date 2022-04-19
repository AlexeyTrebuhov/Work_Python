# 6.7.	Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

import os
os.system("cls")

a = (True, False)

print ('Out \n')

for x in a:
    for y in a:
        for z in a:
            c = not (x or y or z ) 
            d = not x and not y and not z
            if c == d:
                print ('True')
            else:
                print ('False')
print ('\n')