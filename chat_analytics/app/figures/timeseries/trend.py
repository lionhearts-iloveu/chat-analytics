import dash_core_components as dcc
import plotly.express as px
import dash_html_components as html

from chat_analytics.services.chat_analytics import get_trend


def get_trend_figure() -> dcc.Graph:
    return html.Div(
        dcc.Graph(
            id='trend-graph'
        )
    )


def update_trend(topic: str):
    df = get_trend(topic)
    fig = px.scatter(df, x='date', y='count', color="sender")
    fig.update_traces(mode='lines+markers')
    fig.update_layout(
        title=f"Trend ({topic})",
        yaxis=dict(title="Sum", ticklen=5, zeroline=False, gridwidth=2),
    )
    return fig
