"""Helper functions for plotting scripts."""
import pandas as pd
import plotly.graph_objects as go


def import_df(file_path):
    TIMESTAMP_LABEL = "timestamp"
    TIMESTAMP_FORMAT = "%d-%m-%Y %H:%M"

    df = pd.read_csv(file_path, header=1)
    df.drop(0, axis=0, inplace=True)
    df[TIMESTAMP_LABEL] = pd.to_datetime(df[TIMESTAMP_LABEL], format=TIMESTAMP_FORMAT)
    df.set_index(TIMESTAMP_LABEL, inplace=True)
    df = df.apply(pd.to_numeric)
    return df


def add_range_slider(fig):
    # Work from copy
    fig = go.Figure(fig)
    # Update layout with range slider
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list(
                    [
                        dict(count=1, label="1m", step="month", stepmode="backward"),
                        dict(count=6, label="6m", step="month", stepmode="backward"),
                        # dict(count=1, label="YTD", step="year", stepmode="todate"),
                        # dict(count=1, label="1y", step="year", stepmode="backward"),
                        dict(step="all"),
                    ]
                )
            ),
            rangeslider=dict(visible=True),
            type="date",
        ),
        height=600,
    )
    return fig
