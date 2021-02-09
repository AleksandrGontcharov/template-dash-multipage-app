import dash_html_components as html
import dash_bootstrap_components as dbc
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
        "Demonstration of a callback with Input from Text Box",
        className="card-title",
        style=dict(textAlign="center"),
    ),
    html.H6(
        "Type something in the text box and press predict",
        className="card-subtitle",
        style=dict(textAlign="center"),
    ),
]


##############################################################
# Row 2 Content
##############################################################

row_2_1_textbox = [
    dbc.Input(id="id-text-box", placeholder="Type something...", type="text"),
]

row_2_2_button = [
    dbc.Button("Predict", color="primary", id="id-button", type="text"),
]

row_2_3_output = [
    html.H4(id="id-result", style={"vertical-align": "middle"}),
]


##############################################################
# Callbacks
##############################################################


@app.callback(
    Output(component_id="id-result", component_property="children"),
    [Input(component_id="id-button", component_property="n_clicks")],
    State(component_id="id-text-box", component_property="value"),
)
def predict(n, input_value):
    # if not clicked yet then n = 0
    if n is None:
        return ""
    # else n > 0, then it has been clicked
    else:
        #
        if input_value == None:
            return "You typed 0 characters."
        else:
            if len(input_value) == 1:
                return f"You typed {len(input_value)} character."
            else:
                return f"You typed {len(input_value)} characters."


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
                        style=border_style,
                        body=False,
                    ),
                    xl=5,
                ),
                dbc.Col(
                    dbc.Card(
                        dbc.CardBody(row_2_2_button),
                        className="card align-items-center",
                        style=border_style,
                        body=True,
                    ),
                    xl=2,
                    align="center",
                ),
                dbc.Col(
                    dbc.Card(
                        row_2_3_output,
                        className="card align-items-center",
                        style=no_border_style,
                        body=True,
                    ),
                    xl=5,
                    align="center",
                ),
            ],
            style=padding_style,
            # align="center",
        ),
    ]
)
