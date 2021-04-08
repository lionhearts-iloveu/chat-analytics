import dash
import dash_html_components as html
from dash.dependencies import Input, Output

from chat_analytics.app.figures.pie.topics import get_topics_pies
from chat_analytics.app.figures.seasonal import get_weekly_n_hourly
from chat_analytics.app.figures.timeseries.hourly import update_hourly
from chat_analytics.app.figures.timeseries.trend import get_trend_figure, update_trend
from chat_analytics.app.figures.timeseries.weekly import update_weekly
from chat_analytics.app.menu.topic import get_topic_menu

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Chat Analytics'),
    get_topic_menu(),
    get_topics_pies(),
    get_trend_figure(),
    get_weekly_n_hourly(),
])


@app.callback(
    Output(component_id='weekly-graph', component_property='figure'),
    Output(component_id='hourly-graph', component_property='figure'),
    Output(component_id='trend-graph', component_property='figure'),
    Input(component_id='topic', component_property='value')
)
def callback_update_weekly(topic: str):
    return [update_weekly(topic), update_hourly(topic), update_trend(topic)]
