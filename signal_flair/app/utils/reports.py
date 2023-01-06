import decimal
from os.path import dirname, abspath

import matplotlib
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport


# non-interactive backend, so we don't crash the browser
matplotlib.use("agg")


def parse_report_title(title: str, fpath: str) -> str:
    """
    In case user has not titled their report, 
    provide one based on the name of their
    provided CSV module.
    """
    fpath, title = fpath.replace("\\", "/"), ""
    input_title = title
    if input_title:
        title = title["report-title"]
    else:
        title = fpath.split("/")[-1].split(".")[-2]

    return title


def get_save_path():
    """Used to list/display past reports."""
    return dirname(dirname(abspath(__file__))) + "/views/reports/"


def generate_pandas_prof_report(
    df: pd.DataFrame, report_config: dict, fpath: str
) -> str:
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
    # unpack the params needed to configure the report
    title = parse_report_title(report_config["report-title"], fpath)

    column_to_analyze = report_config["column-to-analyze"]
    # prevent errors in parsing strings that represent numbers with commas
    if df[column_to_analyze].dtype == np.dtype("object"):
        df = df.assign(
            column_to_analyze=df[column_to_analyze].apply(
                lambda duration_str: float(
                    decimal.Decimal(duration_str.replace(",", ""))
                )
            )
        )

    # make the report
    output_path = get_save_path()
    output_path = output_path + title + ".html"

    # regular exploratory data stats + analysis
    eda_profile = ProfileReport(df, title=title, explorative=True)
    eda_profile.to_file(output_path)

    return title
