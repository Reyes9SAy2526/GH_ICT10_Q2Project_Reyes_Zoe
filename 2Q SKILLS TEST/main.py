# Element Database
from pyscript import display, document

def nonmetal_elements(e):

    document.getElementById('results').innerHTML = ''
    user_input = document.getElementById('input1').value.strip().capitalize()

    elements = {
        'H': {'name': 'Hydrogen', 'number': 1, 'mass': 1.008},
        'C': {'name': 'Carbon', 'number': 6, 'mass': 12.011},
        'N': {'name': 'Nitrogen', 'number': 7, 'mass': 14.001},
        'O': {'name': 'Oxygen', 'number': 8, 'mass': 16.000},
        'F': {'name': 'Fluorine', 'number': 9, 'mass': 19.000},
        'P': {'name': 'Phosphorus', 'number': 15, 'mass': 30.974},
        'S': {'name': 'Sulfur', 'number': 16, 'mass': 32.06},
        'Cl': {'name': 'Chlorine', 'number': 17, 'mass': 35.45},
        'Se': {'name': 'Selenium', 'number': 34, 'mass': 78.971},
        'Br': {'name': 'Bromine', 'number': 35, 'mass': 79.904},
        'I': {'name': 'Iodine', 'number': 53, 'mass': 126.90},
        'He': {'name': 'Helium', 'number': 2, 'mass': 4.0026},
        'Ne': {'name': 'Neon', 'number': 10, 'mass': 20.180},
        'Ar': {'name': 'Argon', 'number': 18, 'mass': 39.948},
        'Kr': {'name': 'Krypton', 'number': 36, 'mass': 83.798},
        'Xe': {'name': 'Xenon', 'number': 54, 'mass': 131.29},
        'Rn': {'name': 'Radon', 'number': 86, 'mass': 222}
    }

    element = elements.get(user_input, 'Not Found')
    elements_checker = user_input in elements

    display_message = (
        f"Sorry, no {user_input} in the non-metals list.",
        f"Element Symbol: {user_input} | Element Name: {element['name']} | Atomic Number: {element['number']} | Atomic Mass: {element['mass']}"
    )

    display(display_message[elements_checker], target='results')
