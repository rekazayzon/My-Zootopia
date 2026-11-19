import json


def load_data(file_path):
    """ Loads a JSON file and returns the parsed data."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal_obj):
    """Serializes a single animal dictionary into a HTML list item."""
    output = '<li class="cards__item">\n'

    name = animal_obj.get("name")
    if name:
        output += f'  <div class="card__title">{name}</div>\n'

    output += '  <div class="card__text">\n'
    output += '  <ul>\n'

    characteristics = animal_obj.get("characteristics", {})

    diet = characteristics.get("diet")

    if diet:
        output += f"    <li><strong>Diet:</strong> {diet}<br/>\n"

    locations = animal_obj.get("locations")
    if locations:
        output += f"    <li><strong>Location:</strong> {locations[0]}<br/>\n"

    animal_type = characteristics.get("type")
    if animal_type:
        output += f"    <li><strong>Type:</strong> {animal_type}<br/>\n"

    output += "  </ul>\n"
    output += "  </div>\n"
    output += "</li>\n"
    return output


def get_available_skin_types(animals_data):
  """Returns a sorted list of unique skin_type values from the dataset."""
  skin_types = set()
  for animal in animals_data:
    characteristics = animal.get("characteristics", {})
    skin_type = characteristics.get("skin_type")
    if skin_type:
      skin_types.add(skin_type)
    else:
      skin_types.add("Unknown")
  return sorted(skin_types)


def main():
    """Prompts user for a skin_type, filters animals, and generates animals.html."""
    animals_data = load_data('animals_data.json')

    available_skin_types = get_available_skin_types(animals_data)
    print("You may filter the animal data by skin type or view all the data. Available skin types: ")
    print("- Any (including Unknown)")
    for st in available_skin_types:
        print(f"- {st}")

    selected_skin_type = input("\nPlease enter a skin type from the list above (Or 'Any' for all): ").strip()

    output = ""
    for animal_obj in animals_data:
        characteristics = animal_obj.get("characteristics", {})
        animal_skin_type = characteristics.get("skin_type") or "Unknown"

        if (
            selected_skin_type.lower() == "any"
            or animal_skin_type.lower() == selected_skin_type.lower()
        ):
            output += serialize_animal(animal_obj)

    with open("animals_template.html", "r", encoding="utf-8") as template_file:
        template_content = template_file.read()

    new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w", encoding="utf-8") as output_file:
        output_file.write(new_html_content)

    print(f"\nWebsite successfully generated for skin type: {selected_skin_type}")

if __name__ == "__main__":
    main()
