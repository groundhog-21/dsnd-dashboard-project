import pickle
from pathlib import Path

# Using the Path object, create a `project_root` variable
# set to the absolute path for the root of this project directory
# YOUR CODE HERE
project_root = Path(__file__).resolve().parent.parent


# Using the `project_root` variable
# create a `model_path` variable
# that points to the file `model.pkl`
# inside the assets directory
# YOUR CODE HERE
model_path = project_root / 'assets' / 'model.pkl'


def load_model():
    with model_path.open('rb') as file:
        model = pickle.load(file)

    return model
