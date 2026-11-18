import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r", encoding="utf-8") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

# Step 1 - Print Data From File
for animal in animals_data:
  name = animal.get("name")
  if name:
    print(f"Name: {name}")
  # !!! handling potentially empty characteristics field by defining it as an empty dict
  characteristics = animal.get("characteristics", {})

  diet = characteristics.get("diet")

  if diet:
    print(f"Diet: {diet}")

  locations = animal.get("locations")
  if locations:
    print(f"Location: {locations[0]}")

  animal_type = characteristics.get("type")
  if animal_type:
    print(f"Type: {animal_type}")

  print()
