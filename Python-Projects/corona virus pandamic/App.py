""" import dash_html_components as html """
import dash
from dash import dcc,html
from dash.dependencies import Input,Output
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go

""" Note :- href is link so write it in a inverted commas. Ans replace '=' equal to sign into ':' colon """
external_stylesheets = [

    {
        'href': "https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" ,
        'rel': "stylesheet" ,
        'integrity': "sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" ,
        'crossorigin': "anonymous"
    }
]

patients = pd.read_csv('state_wise_daily data file IHHPET.csv')
total = patients.shape[0]
active = patients[patients['Status']=='Confirmed'].shape[0]
recovered = patients[patients['Status']=='Recovered'].shape[0]
deaths = patients[patients['Status']=='Deceased'].shape[0]

options=[
    {'label':'All','value':'All'},
    {'label':'Hospitalized','value':'Hospitalized'},
    {'label': 'Recovered', 'value': 'Recovered'},
    {'label': 'Deceased', 'value': 'Deceased'},
]

options1=[
    {'label':'All','value':'All'},
    {'label':'Mask','value':'Mask'},
    {'label':'Sanitizer','value':'Sanitizer'},
    {'label':'Oxygen','value':'Oxygen'},
]

options2=[
    {'label':'All','value':'Status'},
    {'label':'Red Zone','value':'Red Zone'},
    {'label':'Blue Zone','value':'Blue Zone'},
    {'label':'Green Zone','value':'Green Zone'},
    {'label':'Orange Zone','value':'Orange Zone'},
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Corona Virus Pandemic', style = {'color': '#fff', 'text-align': 'center'}),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Cases", className='text-light'),
                    html.H4(total, className='text-light')
                ],className='card-body')
            ],className='card bg-danger')
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Active Cases   ", className='text-light'),
                    html.H4(active, className='text-light')
                ],className='card-body')
            ],className='card bg-info')
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Recovered Cases", className='text-light'),
                    html.H4(recovered,className='text-light')
                ],className='card-body')
            ],className='card bg-warning')
        ],className='col-md-3'),
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Deaths", className='text-light'),
                    html.H4(deaths, className='text-light')
                ],className='card-body')
            ],className='card bg-success')
        ],className='col-md-3')
    ], className='row'),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id = 'plot-graph', options = options1, value = 'All'),
                    dcc.Graph(id='graph')
                ],className='card-body')
            ],className='card bg-success')
        ], className='col-md-6'),
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id = 'my_dropdown', options = options2, value = 'Status'),
                    dcc.Graph(id = 'the_graph')
                ], className='card-body')
            ],className='card bg-info')
        ], className='col-md-6')
    ], className='row'),
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id = 'picker', options = options, value = 'All' ),
                    dcc.Graph(id = 'bar')
                ],className = 'card-body')
            ], className = 'card')
        ], className = 'col-md-12')
    ], className='row')
], className='Container')

""" whenever we use '@' it means it is a decorator function 
Note:- To call the function that is 'bar' function write inside dcc. Below code for calling 'bar' function """
@app.callback(Output('bar', 'figure'),[Input('picker', 'value')])
# create Function
def update_graph(selected_type):

    if selected_type =='All':
        fig = go.Figure(data=[go.Bar(x=patients['State'],y=patients['Total'])
                              ])
        # return{'data':[go.Bar(x=patients['State'],y=patients['Total'])],
        # 'layout':go.Layout(title='State Total Count',plot_bgcolor='orange')
        # }
    elif selected_type =='Hospitalized':
        fig = go.Figure(data=[go.Bar(x=patients['State'],y=patients['Hospitalized'])
                              ])
        #return{'data':[go.Bar(x=patients['State'],y=patients['Hospitalized'])],
               #'layout':go.Layout(title='State Total Count',plot_bgcolor='orange')
              # }
    elif selected_type =='Recovered':
        #return{'data':[go.Bar(x=patients['State'],y=patients['Recovered'])],
        fig = go.Figure(data=[go.Bar(x=patients['State'],y=patients['Recovered'])
                              ])
               #'layout':go.Layout(title='State Total Count',plot_bgcolor='orange')

    elif selected_type =='Deceased':

        fig = go.Figure(data=[go.Bar(x=patients['State'],y=patients['Deceased'])
                              ])
              #'layout':go.Layout(title='State Total Count',plot_bgcolor='orange')

    else:
        fig = go.Figure()
    fig.update_layout( title='State Total Count', plot_bgcolor='orange'
    )
    return fig

""" Note:- To call the function that is 'graph' function write inside dcc. Below code for calling 'graph' function """
@app.callback(Output('graph', 'figure'),[Input('plot-graph', 'value')])
# create function
def generate_graph(selected_type):

    if selected_type == 'All':
        return{'data':[go.Line(x=patients['Status'],y=patients['Total'])],
               'layout':go.Layout(title='Commodities Total Count',plot_bgcolor='pink')}

    if selected_type == 'Mask':
        return{'data':[go.Line(x=patients['Status'],y=patients['Mask'])],
               'layout':go.Layout(title='Commodities Total Count',plot_bgcolor='pink')}

    if selected_type == 'Sanitizer':
        return{'data':[go.Line(x=patients['Status'],y=patients['Sanitizer'])],
               'layout':go.Layout(title='Commodities Total Count',plot_bgcolor='pink')}

    if selected_type == 'Oxygen':
        return{'data':[go.Line(x=patients['Status'],y=patients['Oxygen'])],
               'layout':go.Layout(title='Commodities Total Count',plot_bgcolor='pink')}

    return {'data': [], 'layout':go.Layout(title='Loading...')}

""" Note:- To call the function that is 'graph' function write inside dcc. Below code for calling 'graph' function """
@app.callback(Output('the_graph','figure'),[Input('my_dropdown', 'value')])
# create Function
def generate_graph(my_dropdown):
   piechart = px.pie(data_frame=patients, names = my_dropdown, hole=0.3)
   return piechart







""" for host
    Note:- The above code provide local host with the help of flask """
if __name__ == '__main__':
    app.run(debug=True,use_reloader=False)