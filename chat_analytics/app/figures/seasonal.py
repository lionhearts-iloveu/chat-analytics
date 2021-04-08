from chat_analytics.app.figures.timeseries.hourly import get_hourly_figure
from chat_analytics.app.figures.timeseries.weekly import get_weekly_figure
import dash_html_components as html


def get_weekly_n_hourly():
    return html.Div(
        [
            get_weekly_figure(),
            get_hourly_figure(),
        ],
        className='row'
    )
