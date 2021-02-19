"""
The index of the web app that links all the individual pages.
This script defines the navigation on the top bar of the web dash app.
The requirement is to add .py files into the pages folder.
There should always be a home.py + (other optional pages) and the link to
home is set to "/"

"""

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

# import all pages in the app
from app import app
from app import app_title
from pages import *
from pages.__init__ import __all__ as list_of_pages

###########################################
# Set these parameters at the top
###########################################
# Navbar Color
navbar_color = "primary"  # can be one of many keywords (primary, light, dark, warning, secondary, success, danger, info, white) or a hex code
###########################################


def create_navbar_links(list_of_pages):
    """
    Generate a list of navbar page links. The output
    of this function is used in the navbar
    """
    navbar_links = []
    for page in list_of_pages:

        if page != "home":
            # Capitalize the page title and remove underscores
            page_title = page.replace("_", " ").title()
            navbar_links.append(
                dbc.NavItem(dbc.NavLink(page_title, href="/" + page, className="ml-2"))
            )

    return navbar_links


navbar = dbc.NavbarSimple(
    children=create_navbar_links(list_of_pages),
    brand=app_title,
    brand_href="/",
    color=navbar_color,
    dark=True,
)


def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

# embedding the navigation bar
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), navbar, html.Div(id="page-content")]
)


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def display_page(pathname):
    try:
        return globals()[pathname[1:]].layout
    except:
        # This loads the "/" url, which is hardcoded to link to home.py
        return home.layout


if __name__ == "__main__":
    app.run_server(host='127.0.0.1', port=8080, debug=True)

    
