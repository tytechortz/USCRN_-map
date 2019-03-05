import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


df = pd.read_csv('./all_uscrn_data.txt', delim_whitespace=True, header=None, usecols = [0,1,3,4,5,6,7,8], names =['WBAN','YM','LON','LAT','MAX','MIN','MEAN','AVG',])

sites = df.drop_duplicates(subset=['WBAN','LON', 'LAT'])

app.layout = html.Div([
    html.H1('USCRN Sites'),
    html.Div(id='text-content'),
    dcc.Graph(id='map', figure={
        'data': [{
            'lat': sites['LAT'],
            'lon': sites['LON'],
            'marker': {
                'color': 'red',
                'size': 4,
                'opacity': 0.6
            },
            'customdata': df['WBAN'],
            'type': 'scattermapbox'
        }],
        'layout': {
            'mapbox': {
                'accesstoken': 'pk.eyJ1IjoidHl0ZWNob3J0eiIsImEiOiJjanN1emtuc2cwMXNhNDNuejdrMnN2aHYyIn0.kY0fOoozCTY-4IUzcLx22w',
                'zoom':5,
                'hovermode': 'closest',
                'margin': {'l': 0, 'r': 0, 'b': 0, 't': 0},
            },
        }
    })
])


if __name__ == '__main__':
    app.run_server(debug=True)



