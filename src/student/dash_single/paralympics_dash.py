from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

import charts as ch

# Variable that defines the meta tag for the viewport
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]

# Variable that contains the external_stylesheet to use, in this case
# Bootstrap styling from dash bootstrap components (dbc)
external_stylesheets = [dbc.themes.BOOTSTRAP]

# Pass the stylesheet and meta_tag variables to the Dash app constructor
app = Dash(__name__, external_stylesheets=external_stylesheets,
           meta_tags=meta_tags)

# Figures
line_fig = ch.line_chart("sports")
bar_fig = ch.bar_gender("summer")
map = ch.scatter_geo()
card = ch.create_card('Barcelona 1992')

# Create the 12 column layout for the Paralympics app
row_one = dbc.Row([
    dbc.Col([html.H1('Paralympics Data Analytics'),
             html.P('''Lorem ipsum dolor sit amet, consectetur adipiscing elit,
                    Oraesent congue luctus elit nec gravida.''')]),
])

row_two = dbc.Row([
    dbc.Col(children=[dbc.Select(options=[
        {"label": "Events", "value": "events"},
        {"label": "Sports", "value": "sports"},
        {"label": "Countries", "value": "countries"},
        {"label": "Athletes", "value": "participants"},
        ],
        value="events",
        id="dropdown-input",),
        ],
        width=4),
    dbc.Col(children=[
        html.Div([dbc.Label("Select the Paralympic Games type"),
                  dbc.Checklist(
                    options=[
                        {"label": "Summer", "value": "summer"},
                        {"label": "Winter", "value": "winter"},
                    ],
                    value=["summer"],
                    id="checklist-input",),])
                    ], width={"size": 4, "offset": 2}),
    # 2 'empty' columns between this and the previous column
])

row_three = dbc.Row([
    dbc.Col(children=[dcc.Graph(id="line-chart",
                                figure=line_fig)], width=6),
    dbc.Col(children=[dcc.Graph(id="bar-chart", figure=bar_fig)], width=6),
])

row_four = dbc.Row([
    dbc.Col(children=[dcc.Graph(id="map",
                                figure=map)], width=8),
    dbc.Col(children=[dbc.Card(children=[card], id='card')], width=4),
])

# Wrap the layout in a Bootstrap container
app.layout = dbc.Container([
    # Add the HTML layout components in here
    row_one,
    row_two,
    row_three,
    row_four,
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5050)
