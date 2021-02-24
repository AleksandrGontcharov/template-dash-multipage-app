"""
This file contains the app_title and the theme.
"""

import dash
import dash_bootstrap_components as dbc

##############################################################
#                SET THE TITLE FOR THE APP
# Title of the app - appears as the Logo, and the title on the tab of the browser
##############################################################

app_title = "Aleksandr Gontcharov Multi-Page Web App"

##############################################################
#               SET THE THEME FOR THE APP
# Dark themes: CYBORG, DARKLY, SOLAR, SUPERHERO
# Light themes: CERULEAN, COSMO, FLATLY, JOURNAL, LITERA, MINTY,
#               PULSE, SANDSTONE, SKETCHY, SLATE, SPACELAB, UNITED
# Themes I like: COSMO, LUMEN, LUX, MATERIA,  YETI
##############################################################
external_stylesheets = [dbc.themes.LUX]

# Define the app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.config.suppress_callback_exceptions = True
app.title = app_title
