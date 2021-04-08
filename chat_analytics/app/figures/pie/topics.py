import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

from chat_analytics.services.chat_analytics import get_count_per_topic, get_senders


def get_pie(sender=None):
    df = get_count_per_topic(sender)
    fig = px.pie(df, values='count', names='topic', title='Together' if sender is None else sender)
    return fig


def get_topics_pies() -> html.Div:
    children = [
        html.Div(
            dcc.Graph(
                id='pie-graph-all',
                figure=get_pie()
            ),
            className='four columns'
        ),
    ]
    for sender in get_senders():
        children.append(
            html.Div(
                dcc.Graph(
                    id=f'pie-graph-{sender}',
                    figure=get_pie(sender)
                ),
                className='four columns'
            )
        )
    return html.Div(
        children,
        className='row'
    )
