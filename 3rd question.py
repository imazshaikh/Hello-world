import json

x = {
  "name": "Imaz",
  "age": 23,
  "married": True,
  "divorced": False,
  "children": ("Saksi","Raj"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))
