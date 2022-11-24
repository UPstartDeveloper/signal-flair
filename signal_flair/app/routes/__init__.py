from flask import current_app as app

__all__ = ["index"]


from .index import index
from .load_file import get_load_file, post_load_file
from .reports import reports, show_report

app.add_url_rule("/", view_func=index, methods=["GET", "POST"])
app.add_url_rule("/reports", view_func=reports, methods=["GET"])
app.add_url_rule("/show-report", view_func=show_report, methods=["GET"])
app.add_url_rule("/load-file", view_func=get_load_file, methods=["GET"])
app.add_url_rule("/load-file", view_func=post_load_file, methods=["POST"])
