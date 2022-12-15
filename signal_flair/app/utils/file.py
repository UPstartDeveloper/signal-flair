import pandas as pd


def get_file_extension(fpath):
    """Returns the extension of a given file.

    Parameters
    ----------
    fpath: str
        Path of a file
    Returns
    -------
    str:
        extension of the given file
        the text after the last dot
    """
    return str(fpath).split(".")[-1]


def retrieve_dataset_from_file(fpath: str, nrows=None) -> pd.DataFrame:
    """Validates the uploaded file path, then parses it or throws an exception."""
    ext = get_file_extension(fpath)

    if ext == "csv":
        return pd.read_csv(fpath, sep=None, engine="python", nrows=nrows)
    elif ext in ["xls", "xlsx"]:
        return pd.read_excel(fpath, nrows=nrows)
    else:
        raise ValueError("Extension must be either a .csv, .xls, or .xlsx.")


def retrieve_dataset_from_upload(storage) -> pd.DataFrame:
    """Validates the uploaded file buffer, then parses it or throws an exception."""
    fpath = storage.filename
    ext = get_file_extension(fpath)

    if ext == "csv":
        return pd.read_csv(storage.stream)
    else:
        raise ValueError("Please upload a .csv file.")
