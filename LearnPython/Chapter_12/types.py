from typing import List, Union, Tuple, Dict

numbers: List[int] = [1, 2, 3]
names: Tuple[str] = ("Ayush", "Anirudhra", "Aatif")
output: Union[str, int, float] 
product_info: Dict[str, Union[int, str, float]] = {
  "product_name": "laptop", 
  "price": 999.9, 
  "quantity": 5
}

n: int = 5
name: str = "Ayush"

def text(a: int, b: str) -> None: 
  print(f"{b} choosed {a}")
  return 

text(n, name)