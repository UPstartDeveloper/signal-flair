from flask import render_template, session, request, redirect, url_for

from ..utils import file, utils, reports


def get_load_file():
    """Renders the form to upload CSV modules."""
    utils.check_session_var("error")
    return render_template("data-sources/load-file.html", session=session)


def post_load_file():
    """
    Process the uploaded CSV, then show the report
    OR redirect and show errors if there's a problem.
    """
    file_data = request.files
    form_data = request.form

    if "file-upload" not in file_data:
        return redirect(url_for("get_load_file"))

    storage = file_data["file-upload"]

    # 1. check extension
    fpath = storage.filename
    ext = file.get_file_extension(fpath)
    valid_ext = ["csv", "xlsx", "xls"]

    if ext not in valid_ext:
        utils.set_session_var(
            "error", "Sorry, file must be a CSV or Excel spreadsheet."
        )
        return redirect(url_for("get_load_file"))

    # 2. load the file into a pd.DataFrame
    try:
        data_df = file.retrieve_dataset_from_upload(storage)
    except Exception as _:  # most likely will be a TypeError
        utils.set_session_var("error", "Sorry, an unexpected error occurred.")
        return redirect(url_for("get_load_file"))

    # 3. Generate pandas-profiling report
    title = reports.generate_pandas_prof_report(data_df, form_data, fpath)

    # if successful, route the user to a specific report (from the list)
    return redirect(url_for("reports_list", name=title + ".html"))
