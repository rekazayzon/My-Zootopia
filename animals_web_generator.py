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


def main():
    """Reads animal data, generates HTML content, and writes it to animals.html."""
    animals_data = load_data('animals_data.json')

    output = ""
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)

    with open("animals_template.html", "r", encoding="utf-8") as template_file:
        template_content = template_file.read()

    new_html_content = template_content.replace("__REPLACE_ANIMALS_INFO__", output)

    with open("animals.html", "w", encoding="utf-8") as output_file:
        output_file.write(new_html_content)


if __name__ == "__main__":
    main()
