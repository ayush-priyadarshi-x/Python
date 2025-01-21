from typing import List
names: List[str] = ["Ayush", "Aatif", "Anirudhra", "Ronish", "Roshan", "Palak", "Nandani"]

for index, item in enumerate(names): 
    if (index + 1) in [3, 5, 7]: 
        print(item)
