from dash import Dash, html, dcc, Input, Output
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
    dbc.Col(children=[dbc.Select(id="dropdown-input",
            options=[
                {"label": "Events", "value": "events"},
                {"label": "Sports", "value": "sports"},
                {"label": "Countries", "value": "countries"},
                {"label": "Athletes", "value": "participants"},
            ],
            value="events",),
            ],
            width=4),
    dbc.Col(children=[
        html.Div([dbc.Label("Select the Paralympic Games type"),
                  dbc.Checklist(
                      id="checklist-input",
                      options=[
                          {"label": "Summer", "value": "summer"},
                          {"label": "Winter", "value": "winter"},
                      ],
                      value=["summer"],),   # Default selected value
                  ])],
            width={"size": 4, "offset": 2}),
])

row_three = dbc.Row([
    dbc.Col(children=[dcc.Graph(id="line-chart",
                                figure=line_fig)], width=6),
    dbc.Col(children=[], id="bar-chart", width=6),
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


# Add callbacks
@app.callback(
    Output(component_id='line-chart', component_property='figure'),
    Input(component_id='dropdown-input', component_property='value')
)
def update_line_chart(feature):
    figure = ch.line_chart(feature)
    return figure


@app.callback(
    Output(component_id='bar-chart', component_property='children'),
    Input(component_id='checklist-input', component_property='value')
)
def update_output_div(selected_values):
    figures = []
    for value in selected_values:
        fig = ch.bar_gender(value)
        # Assign id to be used to identify the charts
        id = f'bar-chart-{value}'
        element = dcc.Graph(figure=fig, id=id)
        figures.append(element)
    return figures


# Hovering or selecting a marker in the map should update the card relevant to that event
@app.callback(
    Output(component_id='card', component_property='children'),
    Input(component_id='map', component_property='hoverData')
)
def display_card(hover_data):
    text = hover_data['points'][0]['hovertext']
    if text is not None:
        return ch.create_card


# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5050)
