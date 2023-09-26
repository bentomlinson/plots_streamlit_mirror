from plotly.subplots import make_subplots
import plotly.graph_objects as go


def add_trace_to_fig(fig, df, col, secondary_y, mode, color):
    fig.add_trace(
        go.Scattergl(
            name=col,
            x=df.index,
            y=df[col],
            line={'width': 1},
            mode=mode,
            marker=dict(color=color)
        ),
            secondary_y=secondary_y,
    )
    return fig


def make_dynamic_plot(df, parameters_df, fig_params: dict):
    axis_map = {
        "Left": False,
        "Right": True,
    }
    plot_type_map = {
        "Line": "lines",
        "Scatter": "markers",
    }
    fig = make_subplots(rows=1, cols=1, specs=[[{'secondary_y': True}]])
    for _, row in parameters_df.iterrows():
        var = row["variable"]
        secondary_y = axis_map[row["axis"]]
        mode = plot_type_map[row["plot_type"]]
        color = row["color"]
        fig = add_trace_to_fig(fig, df, var, secondary_y, mode, color)
    
    # Update y-axes ranges   
    if "left_range" in fig_params.keys():
        fig.update_yaxes(range=fig_params["left_range"], secondary_y=False)
    if "right_range" in fig_params.keys():
        fig.update_yaxes(range=fig_params["right_range"], secondary_y=True)

    return fig
