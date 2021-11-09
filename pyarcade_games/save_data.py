"""
Saving Data To Local Module
"""
import os

def save_data(variable_name: str, value):
    """Save data to a local storage.

    Args:
        variable_name (str): [name of the variable to be saved.]
        value ([type]): [value type]
    Returns;
        None
    """
    if not os.path.exists("games_data"):
        os.makedirs("games_data")

    file_path = "games_data/saves.py"
    with open(file_path, "a+") as saves_data:
        if type(value) == str:
            saves_data.write(f"{variable_name} = '{value}'\n")
        else:
            saves_data.write(f"{variable_name} = {value}\n")


        


if __name__ == "__main__":
    save_data("test_data",5)
    save_data("maximum_lvl","i am a string")
    save_data("gravity_range",99)