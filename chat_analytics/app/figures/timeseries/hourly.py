import dash_core_components as dcc
import plotly.express as px
import dash_html_components as html

from chat_analytics.services.chat_analytics import get_weekly, get_hourly


def get_hourly_figure() -> dcc.Graph:
    return html.Div(
        dcc.Graph(
            id='hourly-graph'
        ),
        style={'width': '49%', 'display': 'inline-block'}
    )


def update_hourly(topic: str):
    df = get_hourly(topic)
    fig = px.scatter(df, x='hour', y='count', color="sender")
    fig.update_traces(mode='lines+markers')
    fig.update_layout(
        title=f"Hourly seasonality ({topic})",
        yaxis=dict(title="Avg", ticklen=5, zeroline=False, gridwidth=2),
    )
    return fig
