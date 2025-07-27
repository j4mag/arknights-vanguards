import plotly.graph_objects as go
from vanguard_lib import plotting


def test_save_plot_no_title():
    fig = go.Figure(layout=go.Layout())
    plotting.save_plot(fig, tgt_dir="output")


def test_save_plot_with_title():
    fig = go.Figure(layout=go.Layout(title="test"))
    plotting.save_plot(fig, tgt_dir="output")
