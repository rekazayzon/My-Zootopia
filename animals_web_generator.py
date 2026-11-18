import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r", encoding="utf-8") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

# Step 1 - Print Data From File

output = ""

for animal in animals_data:
  name = animal.get("name")
  if name:
    output += f"Name: {name}\n"
  # !!! handling potentially empty characteristics field by defining it as an empty dict
  characteristics = animal.get("characteristics", {})

  diet = characteristics.get("diet")

  if diet:
    output += f"Diet: {diet}\n"

  locations = animal.get("locations")
  if locations:
    output += f"Location: {locations[0]}\n"

  animal_type = characteristics.get("type")
  if animal_type:
    output += f"Type: {animal_type}\n"

  output += "\n"

# reading html template
with open("animals_template.html", "r", encoding="utf-8") as template_file:
  template_content = template_file.read()

# replaces the placeholder for generated data
new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

# writing new html file
with open("animals.html", "w", encoding="utf-8") as output_file:
  output_file.write(new_html_content)
