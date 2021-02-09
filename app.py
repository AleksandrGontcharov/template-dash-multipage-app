"""
The index of the web app that links all the individual pages.
This script defines the navigation on the top bar of the web app.
The requirement is to add .py files into the pages folder.
There should always be a home.py + (other optional pages) and the link to
home is set to "/"

"""
import dash
import dash_bootstrap_components as dbc

###########################################
# Set these parameters at the top
###########################################

# The title of the App
app_title = "MLAS Multi-Page Web App"  # Title of the app - appears as the Logo, and the title on the tab of the browser
# Set the theme of the app CERULEAN, COSMO, CYBORG, DARKLY, FLATLY, JOURNAL, LITERA, LUMEN, LUX, MATERIA, MINTY, PULSE, SANDSTONE, SIMPLEX, SKETCHY, SLATE, SOLAR, SPACELAB, SUPERHERO, UNITED, YETI
external_stylesheets = [dbc.themes.YETI]
###########################################

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# The title of the app that appears on the browser tab
app.config.suppress_callback_exceptions = True
app.title = app_title