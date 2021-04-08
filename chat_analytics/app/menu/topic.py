import dash_html_components as html
import dash_core_components as dcc

from chat_analytics.config.config import config


def get_topic_menu():
    return html.Div([
        html.Div(children='Topic'),
        dcc.Dropdown(
            id='topic',
            options=[{'label': topic.name, 'value': topic.name} for topic in config.topics],
            value=config.topics[0].name
        )
    ])