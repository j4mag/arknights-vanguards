import plotly.graph_objects as go
from vanguard_lib.lib.plotting import save_plot

def test_save_plot_no_title():
    fig=go.Figure(layout=go.Layout())
    save_plot(fig, tgt_dir="output")

def test_save_plot_with_title():
    fig=go.Figure(layout=go.Layout(title='test'))
    save_plot(fig, tgt_dir="output")
    