import plotly.graph_objects as go
from plotly.subplots import make_subplots


def add_current_data(
    fig, df, flag_df, nan_df, row, col, cbar_loc, colorscale="Viridis"
):
    fig.add_trace(
        go.Heatmap(
            x=df.index.to_pydatetime(),
            y=df.columns,
            z=df.T.values,
            colorscale=colorscale,
            colorbar=dict(len=0.5, y=cbar_loc),
        ),
        row=row,
        col=col,
    )
    fig.add_trace(
        go.Heatmap(
            x=flag_df.index.to_pydatetime(),
            y=flag_df.columns,
            z=flag_df.T.values,
            coloraxis="coloraxis1",
            hoverinfo="skip",
        ),
        row=row,
        col=col,
    )
    fig.add_trace(
        go.Heatmap(
            x=nan_df.index.to_pydatetime(),
            y=nan_df.columns,
            z=nan_df.T.values,
            coloraxis="coloraxis2",
            hoverinfo="skip",
        ),
        row=row,
        col=col,
    )
    return fig


def plot_adcp(df):
    df = df.copy()

    # Select columns which contain ADCP and rename them as height
    df = df.filter(regex="ADCP")

    vc_df = df.filter(regex="_vc_")
    vc_df.columns = vc_df.columns.str.extract("(\d+)", expand=False).astype(int)
    vc_nan_df = vc_df.isnull().astype(int).copy()
    vc_flag_df = (vc_df > 100).astype(int).copy()
    vc_df = vc_df[vc_df <= 100]

    dc_df = df.filter(regex="_dc_")
    dc_df.columns = dc_df.columns.str.extract("(\d+)", expand=False).astype(int)
    dc_nan_df = dc_df.isnull().astype(int).copy()
    dc_flag_df = (dc_df > 360).astype(int).copy()
    dc_df = dc_df[dc_df <= 360]

    # Plot
    nan_colors = [
        (0, "rgba(255, 255, 255, 0)"),
        (1, "rgba(245, 168, 39, 1)"),
    ]
    flag_colors = [
        (0, "rgba(255, 255, 255, 0)"),
        (1, "rgba(255, 0, 0, 1)"),
    ]
    colorscale = "Viridis"
    colorscale = "haline"

    fig = make_subplots(rows=2, cols=1)
    fig = add_current_data(
        fig, vc_df, vc_flag_df, vc_nan_df, 1, 1, 0.79, colorscale=colorscale
    )
    fig = add_current_data(
        fig, dc_df, dc_flag_df, dc_nan_df, 2, 1, 0.21, colorscale=colorscale
    )
    fig.update_layout(
        coloraxis1={"colorscale": flag_colors, "showscale": False},
        coloraxis2={"colorscale": nan_colors, "showscale": False},
    )
    fig.update_yaxes(autorange="reversed")
    return fig
