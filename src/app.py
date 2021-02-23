"""
This file 
"""

import dash
import dash_bootstrap_components as dbc

###########################################
# Set these parameters at the top
###########################################

# The title of the App
app_title = "My Multi-Page Web App"  # Title of the app - appears as the Logo, and the title on the tab of the browser
# Set the theme of the app CERULEAN, COSMO, CYBORG, DARKLY, FLATLY, JOURNAL, LITERA, LUMEN, LUX, MATERIA, MINTY, PULSE, SANDSTONE, SIMPLEX, SKETCHY, SLATE, SOLAR, SPACELAB, SUPERHERO, UNITED, YETI
external_stylesheets = [dbc.themes.YETI]
###########################################

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# The title of the app that appears on the browser tab
app.config.suppress_callback_exceptions = True
app.title = app_title


