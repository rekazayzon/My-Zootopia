import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r", encoding="utf-8") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')

# Step 4 - Serialization

output = ""

for animal in animals_data:
  # Open new card for each animal
  output += '<li class="cards__item">\n'

  name = animal.get("name")
  if name:
    output += f'  <div class="card__title">{name}</div>\n'

  # Open card text paragraph
  output += '  <p class="card__text">\n'

  characteristics = animal.get("characteristics", {})

  diet = characteristics.get("diet")

  if diet:
    output += f"    <strong>Diet:</strong> {diet}<br/>\n"

  locations = animal.get("locations")
  if locations:
    output += f"    <strong>Location:</strong> {locations[0]}<br/>\n"

  animal_type = characteristics.get("type")
  if animal_type:
    output += f"    <strong>Type:</strong> {animal_type}<br/>\n"
  # Close card text paragraph and card
  output += "  </p>\n"
  output += "</li>\n"

# reading html template
with open("animals_template.html", "r", encoding="utf-8") as template_file:
  template_content = template_file.read()

# replaces the placeholder for generated data
new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

# writing new html file
with open("animals.html", "w", encoding="utf-8") as output_file:
  output_file.write(new_html_content)
