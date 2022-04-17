import fire


def save_model(model, out_folder: str):
    """
    Serialise the model to an output folder 
    """
    pass


def evaluate_model(model, test_data):
    """
    Evaluate your model against the test data.
    """
    pass


def split_data(data):
    """
    Generate data splits
    """
    pass


def load_data(in_folder: str):
    """
    Load the csv file and join them in a format you can use
    """
    pass


def train(in_folder: str, out_folder: str) -> None:
    """
    Consume the data from the input folder to generate the model 
    and serialise it to the out_folder
    """
    pass
  

if __name__ == '__main__':
  fire.Fire(train)
