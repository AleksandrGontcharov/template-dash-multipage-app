import dash_html_components as html
import dash_bootstrap_components as dbc

from app import app

##############################################################
# Predefine styles
##############################################################

# defines a style to be applied to rows - padding between rows (vertical padding)
padding_style = dict(padding="0.5rem 0rem", height="auto")

# defines a style to be applied to cards to remove border (can be border = "none")
border_style = dict(padding="0.5rem 0rem", border="1")

# defines a style to be applied to cards to remove border (can be border = "none")
no_border_style = dict(padding="0.5rem 0rem", border="none")


##############################################################
# Row 1 Content
##############################################################

row_1_content = [html.H4("Row 1 - Full Row",
                         className="card-title",
                         style=dict(textAlign="center"),
                         ),
                 html.H6("Keep borders, then remove them wherever needed with borderstyle",
                         className="card-subtitle",
                         style=dict(textAlign="center"),
                         ),
                 ]

##############################################################
# Row 2 Content
##############################################################

row_2_col_1 = [html.H4("Row 2 Col 1",
                       className="card-title",
                       style=dict(textAlign="center"),
                       ),
               html.H6("This column is 4/12",
                       className="card-subtitle",
                       style=dict(textAlign="center"),
                       ),
               ]

row_2_col_2 = [html.H4("Image Centered In Card",
                       className="card-title",
                       style=dict(textAlign="center"),
                       ),
               html.H6("This column is 8/12",
                       className="card-subtitle",
                       style=dict(textAlign="center"),
                       ),
               html.Img(src="https://i.redd.it/dwvrl8kddng31.png",
                        style={
                            "maxWidth": "20%",
                            "maxHeight": "20%",
                        },
                        ),
               ]


##############################################################
# Row 3 Content
##############################################################

row_3_col_1 = [html.H5("Row 3 - Vertically Centered Row",
                       className="card-title",
                       style=dict(textAlign="center"),
                       ),
               html.H6("This column is 6/12",
                       className="card-subtitle",
                       style=dict(textAlign="center"),
                       ),
               ]

row_3_col_2 = [html.H4("Image Centered In Card",
                       className="card-title",
                       style=dict(textAlign="center"),
                       ),
               html.H6("This column is 6/12",
                       className="card-subtitle",
                       style=dict(textAlign="center"),
                       ),
               html.Img(src="https://i.redd.it/dwvrl8kddng31.png",
                        style={
                            "maxWidth": "20%",
                            "maxHeight": "20%",
                        },
                        ),
               ]

##############################################################
# Row 4 Content
##############################################################
row_4_col_1 = [html.H4("Row 4 - Add Cardbody",
                       className="card-title",
                       style=dict(textAlign="center"),
                       ),
               html.H6("Content in a card with cardbody adds extra padding",
                       className="card-subtitle",
                       style=dict(textAlign="center"),
                       ),
               ]

row_4_col_2 = [html.H4("Row 4 - Without Cardbody",
                       className="card-title",
                       style=dict(textAlign="center"),
                       ),
               html.H6("The columns in this row are also vertically centered",
                       className="card-subtitle",
                       style=dict(textAlign="center"),
                       ),
               ]

##############################################################
# Row 5 Content
##############################################################
row_5_deck = [dbc.Card([html.H4("Item 1 in Deck",
                                className="card-title",
                                style=dict(textAlign="center"),
                                ),
                        ]
                       ),
              dbc.Card([dbc.CardBody(html.H4(
                  "Item 2 in Deck with CardBody",
                  className="card-title",
                  style=dict(textAlign="center"),
              ),)]),
              dbc.Card([html.H4("Item 3 has no border",
                                className="card-title",
                                style=dict(textAlign="center"),
                                ),
                        ],
                       style=no_border_style,
                       ),
              ]


##############################################################
# Callbacks
##############################################################

# No callbacks in this file

##############################################################
# Layout
##############################################################

layout = dbc.Container([
    # Row 1
    dbc.Row(
        [dbc.Col(dbc.Card(row_1_content, style=border_style), xl=12)],
        style=padding_style,
    ),
    # Row 2
    dbc.Row([
        dbc.Col(dbc.Card(
            row_2_col_1,
            style=border_style,
            body=False,),
            xl=4,),
        dbc.Col(dbc.Card(
            row_2_col_2,
            className="card align-items-center",
            style=border_style,
            body=True,),
            xl=8,
            align="center",
        ), ],
        style=padding_style,
        #  align="center",
    ),
    # Row 3
    dbc.Row([
            dbc.Col(dbc.Card(
                    row_3_col_1,
                    style=border_style,
                    body=False,
                    ),
                    xl=6,
                    ),
            dbc.Col(
                dbc.Card(
                    row_3_col_2,
                    className="card align-items-center",
                    style=border_style,
                    body=True,
                ),
                xl=6,
                align="center",
            ),
            ],
            style=padding_style,
            align="center",
            ),
    # Row 4
    dbc.Row([
            dbc.Col(dbc.Card(
                    dbc.CardBody(row_4_col_1),
                    style=border_style,
                    body=True,
                    ),
                    xl=6,
                    ),
            dbc.Col(
                dbc.Card(
                    row_4_col_2,
                    className="card align-items-center",
                    style=border_style,
                    body=True,
                ),
                xl=6,
                # align="center",
            ),
            ],
            style=padding_style,
            align="center",
            ),
    # Row 5
    dbc.Row([
            dbc.Col(dbc.Card(
                dbc.CardDeck(row_5_deck), style=border_style),
                xl=12,
            )
            ],
            style=padding_style,
            ),
]
)
