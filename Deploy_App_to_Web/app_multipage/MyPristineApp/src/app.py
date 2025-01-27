import dash
import pages_plugin
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, plugins=[pages_plugin],
           external_stylesheets=[dbc.themes.BOOTSTRAP])

# Declare server for Heroku deployment. Needed for Procfile.
server = app.server

navbar = dbc.NavbarSimple(
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem(page["name"], href=page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
        nav=True,
        label="More Pages",
    ),
    brand="Multi Page App Plugin Demo MyPristineApp",
    color="primary",
    dark=True,
    className="mb-2",
)

app.layout = dbc.Container(
    [navbar, pages_plugin.page_container],
    className="dbc",
    fluid=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)
