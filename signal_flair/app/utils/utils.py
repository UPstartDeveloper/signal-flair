from flask import session


def set_session_var(var_name: str, value: str) -> None:
    """
    Used to configure error messages to the user
    in the current session.
    """
    session[var_name] = value
    session[var_name + "_old"] = True


def check_session_var(var_name):
    """
    Used to display error messages to the user
    in the current session.
    """
    if var_name in session:
        if var_name + "_old" in session:
            del session[var_name + "_old"]
        else:
            del session[var_name]


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
