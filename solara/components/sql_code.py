import ipyvue
import react_ipywidgets as react
import traitlets


class SqlCodeWidget(ipyvue.VueTemplate):
    template_file = (__file__, "sql_code.vue")

    label = traitlets.Unicode("").tag(sync=True)
    query = traitlets.Unicode(allow_none=True, default_value=None).tag(sync=True)
    tables = traitlets.Dict(allow_none=True, default_value=None).tag(sync=True)
    height = traitlets.Unicode("180px").tag(sync=True)


@react.component
def SqlCode(label="Query", query=None, tables=None, on_query=None, height="180px"):
    return SqlCodeWidget.element(label=label, query=query, tables=tables, on_query=on_query, height=height)