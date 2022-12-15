from flask import current_app as app

__all__ = ["index"]

from . import (
    index,
    load_file,
    reports,
)


# Give a path for all the routes
app.add_url_rule("/", view_func=index.home, methods=["GET", "POST"])
app.add_url_rule("/reports", view_func=reports.reports_list, methods=["GET"])
app.add_url_rule("/show-report", view_func=reports.show_report, methods=["GET"])
app.add_url_rule("/load-file", view_func=load_file.get_load_file, methods=["GET"])
app.add_url_rule("/load-file", view_func=load_file.post_load_file, methods=["POST"])
