import dash_core_components as dcc
import plotly.express as px
import dash_html_components as html

from chat_analytics.services.chat_analytics import get_weekly


def get_weekly_figure() -> dcc.Graph:
    return html.Div(
        dcc.Graph(
            id='weekly-graph'
        ),
        style={'width': '49%', 'display': 'inline-block'}
    )


def update_weekly(topic: str):
    df = get_weekly(topic)
    fig = px.scatter(df, x='weekday', y='count', color="sender")
    fig.update_traces(mode='lines+markers')
    fig.update_layout(
        title=f"Weekly seasonality ({topic})",
        yaxis=dict(title="Avg", ticklen=5, zeroline=False, gridwidth=2),
        xaxis=dict(
            title="Date",
            ticklen=5,
            zeroline=False,
            gridwidth=2,
            tickvals=[i for i in range(len(df["weekday_str"].tolist()))],
            ticktext=df["weekday_str"].tolist()
        )
    )
    return fig
