from pathlib import Path

import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from app import app

##############################################################
# Predefine styles
##############################################################

# defines a style to be applied to rows - padding between rows (vertical padding)
padding_style = dict(padding="0.5rem 0.5rem", height="auto")

# defines a style to be applied to cards to remove border (can be border = "none")
border_style = dict(padding="0rem 0rem", border="1")

# defines a style to be applied to cards to remove border (can be border = "none")
no_border_style = dict(padding="0rem 0rem", border="none")

##############################################################
# Load homepage content
##############################################################

# Using the newer Pathlib library to read the context of a text file :)
markdown_content = (Path(__file__).parent / 'home.md').read_text()

##############################################################
# Layout
##############################################################


layout = dbc.Container([
    dbc.Row([dbc.Col(
        dbc.Card(dbc.CardBody(html.Div([dcc.Markdown(markdown_content), ],
                                       className="h-tag",
                                       style={'marginTop': '1em',
                                              'marginBottom': '1em',
                                              'marginLeft': '1em',
                                              'marginRight': '1em'})),
                 style=border_style, body=True,), xl=12,)],
            style=padding_style,
            )
])

# layout = html.Div([dcc.Markdown(markdown_content),
#                    ],
#                   style={'lineHeight': '50px'})
