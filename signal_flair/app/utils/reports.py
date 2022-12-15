from pandas_profiling import ProfileReport
from os.path import dirname, abspath

import matplotlib


def get_save_path():
    """Used to list/display past reports."""
    return dirname(dirname(abspath(__file__))) + "/views/reports/"


def generate_pandas_prof_report(df, title):
    """
    Generate a new report, and save to disk.

    Parameters:
        df(pd.DataFrame): data parsed from the user-uploaded file
        report_config(dict): assumed to contain 3 key-value pairs:
            1) "report-title" (str) - should be submitted through the
            form on the "/load-file" route
            2) "column-to-analyze" - if doing outlier detection, this is
            expected to be the case-sensitive name of one of the numerical
            columns in the uploaded CSV

    Returns: str: the title of the report (signals that execution was successful)
    """
    matplotlib.use("agg")
    profile = ProfileReport(df, title=title, explorative=False)

    output_path = get_save_path()
    output_path = output_path + title + ".html"

    profile.to_file(output_path)
