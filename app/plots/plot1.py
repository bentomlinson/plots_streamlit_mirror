import plotly.graph_objects as go
from plotly.subplots import make_subplots


def plot_wind_speed_vs_9999(df):
    # Select columns which contain WdSpdHor_Avg and rename them as height
    df = df.copy()
    df = df.filter(regex='WdSpdHor_Avg')
    df.columns = df.columns.str.extract('(\d+)', expand=False).astype(int)
    # Get boolean mask of values which are in [9998, 9999]
    error_mask = df.isin([9998, 9999])

    # Get booelan mask of values which are not in [9998, 9999] and higher than 100
    # This is the mask of values which are not errors and higher than 100
    nan_mask = (~error_mask) & (df > 100)

    # Replace value in either mask to be nan
    df = df.mask(error_mask | nan_mask)

    df2 = error_mask.copy()
    # df2 = df2.astype(int)
    df2.columns = df2.columns.astype(str) + " m"  # Do we want continuous or discrete values?

    df3 = nan_mask.copy()
    # df2 = df2.astype(int)
    df3.columns = df3.columns.astype(str) + " m" 

    # Plot
    error_colors = [
        (0, "rgba(255, 255, 255, 0)"),
        (1, "rgba(245, 168, 39, 1)"),
    ]
    nan_colors = [
        (0, "rgba(255, 255, 255, 0)"),
        (1, "rgba(255, 0, 0, 1)"),
    ]

    fig = make_subplots(rows=1, cols=1, specs=[[{'secondary_y': True}]])
    for col in df.columns:
        fig.add_trace(
            go.Scattergl(
                name=col,
                x=df.index.to_pydatetime(),
                y=df[col],
                line={'width': 1},
            ),
                secondary_y=False,
        )
    fig.add_trace(
        go.Heatmap(
            x=df2.index.to_pydatetime(),
            y=df2.columns,
            z=df2.astype(int).T.values,
            coloraxis='coloraxis1',
            hoverinfo = 'skip',
        ),
            secondary_y=True,
    )
    fig.add_trace(
        go.Heatmap(
            x=df3.index.to_pydatetime(),
            y=df3.columns,
            z=df3.astype(int).T.values,
            coloraxis='coloraxis2',
            hoverinfo = 'skip',
        ),
            secondary_y=True,
    )
    fig.update_layout(
        coloraxis1 = {"colorscale": error_colors},
        coloraxis2 = {"colorscale": nan_colors},
    )
    fig.update_coloraxes(showscale=False)

    return fig
