import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv(
    'https://raw.githubusercontent.com/'
    'plotly/datasets/master/'
    '1962_2006_walmart_store_openings.csv')

# df = pd.read_csv('./all_uscrn_data.txt', delim_whitespace=True, header=None, usecols = [0,1,3,4,5,6,7,8], names =['WBAN','YM','LON','LAT','MAX','MIN','MEAN','AVG',])

app.layout = html.Div([
    html.H1('Walmart Store Openings'),
    html.Div(id='text-content'),
    dcc.Graph(id='map', figure={
        'data': [{
            'lat': df['LAT'],
            'lon': df['LON'],
            'marker': {
                'color': df['YEAR'],
                'size': 8,
                'opacity': 0.6
            },
            'customdata': df['storenum'],
            'type': 'scattermapbox'
        }],
        'layout': {
            'mapbox': {
                'accesstoken': 'pk.eyJ1IjoiY2hyaWRkeXAiLCJhIjoiY2ozcGI1MTZ3MDBpcTJ3cXR4b3owdDQwaCJ9.8jpMunbKjdq1anXwU5gxIw'
            },
            'hovermode': 'closest',
            'margin': {'l': 0, 'r': 0, 'b': 0, 't': 0}
        }
    })
])


@app.callback(
    dash.dependencies.Output('text-content', 'children'),
    [dash.dependencies.Input('map', 'hoverData')])
def update_text(hoverData):
    s = df[df['storenum'] == hoverData['points'][0]['customdata']]
    return html.H3(
        'The {}, {} {} opened in {}'.format(
            s.iloc[0]['STRCITY'],
            s.iloc[0]['STRSTATE'],
            s.iloc[0]['type_store'],
            s.iloc[0]['YEAR']
        )
    )


if __name__ == '__main__':
    app.run_server(debug=True)



