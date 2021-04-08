import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from chat_analytics.config.config import config
from chat_analytics.services.chat_analytics import get_weekly, get_count_per_topic, get_senders

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


def get_pie(sender=None):
    df = get_count_per_topic(sender)
    fig = px.pie(df, values='count', names='topic', title='Together' if sender is None else sender)
    return fig


def get_pies():
    l = [
        html.Div(
            dcc.Graph(
                id='pie-graph-all',
                figure=get_pie()
            ),
            className='four columns'
        ),
    ]
    for sender in get_senders():
        l.append(
            html.Div(
                dcc.Graph(
                    id=f'pie-graph-{sender}',
                    figure=get_pie(sender)
                ),
                className='four columns'
            )
        )
    return l


app.layout = html.Div(children=[
    html.H1(children='Chat Analytics'),
    html.Div([
        html.Div(children='''
            Topic
        '''),
        dcc.Dropdown(
            id='topic',
            options=[{'label': topic.name, 'value': topic.name} for topic in config.topics],
            value=config.topics[0].name
        )
    ]),
    dcc.Graph(
        id='weekly-graph'
    ),
    html.Div(
        get_pies(),
        className='row'
    )
])


@app.callback(
    Output(component_id='weekly-graph', component_property='figure'),
    Input(component_id='topic', component_property='value')
)
def update_weekly(topic: str):
    df = get_weekly(topic)
    fig = px.scatter(df, x='weekday', y='count', color="sender")
    fig.update_traces(mode='lines+markers')
    return fig
