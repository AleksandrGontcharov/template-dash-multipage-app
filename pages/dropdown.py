import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

from app import app

##############################################################
# Predefine styles
##############################################################

padding_style = dict(
    padding="0.5rem 0rem", height="auto"
)  # defines a style to be applied to rows - padding between rows (vertical padding)

border_style = dict(
    padding="0.5rem 0rem", border="1"
)  # defines a style to be applied to cards to remove border (can be border = "none")

no_border_style = dict(
    padding="0.5rem 0rem", border="none"  # border = "none"
)  # defines a style to be applied to cards to remove border (can be border = "none")


##############################################################
# Row 1 Content
##############################################################

row_1_content = [
    html.H4(
        "Demonstration of a callback with Input from a DropDown",
        className="card-title",
        style=dict(textAlign="center"),
    ),
    html.H6(
        "Pick an Item from the dropdown",
        className="card-subtitle",
        style=dict(textAlign="center"),
    ),
]


##############################################################
# Row 2 Content
##############################################################

row_2_1_textbox = [
    dcc.Dropdown(
        id="id-dropdown",
        options=[
            {"label": "New York City", "value": "NYC"},
            {"label": "Montreal", "value": "MTL"},
            {"label": "San Francisco", "value": "SF"},
        ],
        value="NYC",
    )
]

row_2_2_output = [
    html.H2(id="id-output-from-dropdown", style={"vertical-align": "middle"}),
]


##############################################################
# Callbacks
##############################################################


@app.callback(
    Output(component_id="id-output-from-dropdown", component_property="children"),
    Input(component_id="id-dropdown", component_property="value"),
)
def update_output_div(dropdown_item):
    return dropdown_item


##############################################################
# Layout
##############################################################

layout = dbc.Container(
    [
        # Row 1
        dbc.Row(
            [dbc.Col(dbc.Card(row_1_content, style=border_style), xl=12)],
            style=padding_style,
        ),
        # Row 3
        dbc.Row(
            [
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(row_2_1_textbox),
                        style=no_border_style,
                        body=False,
                    ),
                    xl=6,
                ),
                dbc.Col(
                    dbc.Card(
                        row_2_2_output,
                        className="card align-items-center",
                        style=no_border_style,
                        body=True,
                    ),
                    xl=6,
                    align="center",
                ),
            ],
            style=padding_style,
            align="center",
        ),
    ]
)
