import uuid
import pathlib
import slugify
import numpy as np
import plotly.graph_objects as go

from . import api
from . import simulation


def ceil_to(x: float, to: float) -> float:
    return np.ceil(x / to) * to


def floor_to(x: float, to: float) -> float:
    return np.floor(x / to) * to


PLOT_RANGE = [0, 120]


def plot_dp_absolute(results: list[api.SimulationResult], title: str = "") -> go.Figure:
    baseline = simulation.simulate(
        api.SimulationSetup(
            name="Natural DP Generation",
            operator=None,
            time_step=results[0].setup.time_step,
            time_end=results[0].setup.time_end,
            dp_start=results[0].setup.dp_start,
        )
    )
    fig = go.Figure(
        layout=go.Layout(
            xaxis=go.layout.XAxis(
                title="Time [s]",
                range=PLOT_RANGE,
            ),
            yaxis=go.layout.YAxis(
                title="DP",
                range=[
                    0,
                    ceil_to(
                        max(
                            max(result.dp[result.t <= PLOT_RANGE[1]])
                            for result in results
                        ),
                        20,
                    ),
                ],
            ),
            title=(title + "<br>" if title else "")
            + f"DP Generation<br>initial DP={baseline.setup.dp_start:.0f}",
            hoverlabel=go.layout.Hoverlabel(namelength=-1),
            legend=go.layout.Legend(groupclick="toggleitem"),
        ),
        data=[
            go.Scatter(
                x=baseline.t,
                y=baseline.dp,
                name=baseline.name,
            )
        ]
        + [
            go.Scatter(
                x=result.t,
                y=result.dp,
                name=result.setup.operator.skill.name,
                legendgroup=result.setup.operator.name,
                legendgrouptitle_text=result.setup.operator.name,
                line=go.scatter.Line(color=result.setup.color, dash="solid"),
                hovertemplate=f"(%{{x}}, %{{y:.2f}})<extra>{result.setup.operator.name}"
                f"<br>{result.setup.operator.skill.name}</extra>",
            )
            for result in results
            if result.setup.operator is not None
        ],
    )
    return fig


def plot_dp_added(results: list[api.SimulationResult], title: str = "") -> go.Figure:
    baseline = simulation.simulate(
        api.SimulationSetup(
            name="Natural DP Generation",
            operator=None,
            time_step=results[0].setup.time_step,
            time_end=results[0].setup.time_end,
            dp_start=results[0].setup.dp_start,
        )
    )
    fig = go.Figure(
        layout=go.Layout(
            xaxis=go.layout.XAxis(
                title="Time [s]",
                range=PLOT_RANGE,
            ),
            yaxis=go.layout.YAxis(
                title="DP vs Baseline",
                range=[
                    floor_to(
                        min(
                            min((result.dp - baseline.dp)[result.t <= PLOT_RANGE[1]])
                            for result in results
                        ),
                        20,
                    ),
                    ceil_to(
                        max(
                            max((result.dp - baseline.dp)[result.t <= PLOT_RANGE[1]])
                            for result in results
                        ),
                        20,
                    ),
                ],
            ),
            title=(title + "<br>" if title else "")
            + f"DP Generation Delta vs {baseline.name}"
            f"<br>initial DP={baseline.setup.dp_start:.0f}",
            hoverlabel=go.layout.Hoverlabel(namelength=-1),
            legend=go.layout.Legend(groupclick="toggleitem"),
        ),
        data=[
            go.Scatter(
                x=result.t,
                y=result.dp - baseline.dp,
                name=result.setup.operator.skill.name,
                legendgroup=result.setup.operator.name,
                legendgrouptitle_text=result.setup.operator.name,
                line=go.scatter.Line(color=result.setup.color, dash="solid"),
                hovertemplate=f"(%{{x}}, %{{y:.2f}})<extra>{result.setup.operator.name}"
                f"<br>{result.setup.operator.skill.name}</extra>",
            )
            for result in results
            if result.setup.operator is not None
        ],
    )
    return fig


def window(width: int) -> np.ndarray[float]:
    return np.ones(int(width)) / width


def plot_dp_added_trend(
    results: list[api.SimulationResult], title: str = ""
) -> go.Figure:
    baseline = simulation.simulate(
        api.SimulationSetup(
            name="Natural DP Generation",
            operator=None,
            time_step=results[0].setup.time_step,
            time_end=results[0].setup.time_end,
            dp_start=results[0].setup.dp_start,
        )
    )
    means = [
        (
            result,
            np.convolve(  # very gross moving average, where the period is the operator's cycle time
                result.dp - baseline.dp,
                window(
                    int(
                        (
                            result.setup.operator.skill.sp_cost
                            + result.setup.operator.skill.duration
                        )
                        // result.setup.time_step
                    )
                ),
                "same",
            ),
        )
        for result in results
        if result.setup.operator is not None
    ]

    fig = go.Figure(
        layout=go.Layout(
            xaxis=go.layout.XAxis(
                title="Time [s]",
                range=PLOT_RANGE,
            ),
            yaxis=go.layout.YAxis(
                title="DP vs Baseline",
                range=[
                    floor_to(
                        min(
                            min((result.dp - baseline.dp)[result.t <= PLOT_RANGE[1]])
                            for result in results
                        ),
                        20,
                    ),
                    ceil_to(
                        max(
                            max((result.dp - baseline.dp)[result.t <= PLOT_RANGE[1]])
                            for result in results
                        ),
                        20,
                    ),
                ],
            ),
            title=(title + "<br>" if title else "")
            + f"DP Generation Delta vs {baseline.name} (w/ Trendlines)"
            f"<br>initial DP={baseline.setup.dp_start:.0f}",
            hoverlabel=go.layout.Hoverlabel(namelength=-1),
            # legend=go.layout.Legend(groupclick='toggleitem'), # breaks because of showlegend=False trend lines
        ),
        data=sum(
            [
                [
                    go.Scatter(
                        x=result.t,
                        y=result.dp - baseline.dp,
                        name=result.setup.operator.skill.name,
                        legendgroup=result.setup.name,
                        legendgrouptitle_text=result.setup.name,
                        line=go.scatter.Line(color=result.setup.color, dash="solid"),
                        hovertemplate=f"(%{{x}}, %{{y:.2f}})<extra>{result.setup.operator.name}"
                        f"<br>{result.setup.operator.skill.name}</extra>",
                    ),
                    go.Scatter(
                        x=result.t,
                        y=mean,
                        name=result.setup.operator.skill.name + " (Trend)",
                        legendgroup=result.setup.name,
                        legendgrouptitle_text=result.setup.name,
                        line=go.scatter.Line(color=result.setup.color, dash="dash"),
                        hovertemplate=f"(%{{x}}, %{{y:.2f}})<extra>{result.setup.operator.name}"
                        f"<br>{result.setup.operator.skill.name} (Trend)</extra>",
                        showlegend=False,
                    ),
                ]
                for (result, mean) in means
            ],
            start=[],
        ),
    )
    return fig


def plot_dp_relative(results: list[api.SimulationResult], title: str = "") -> go.Figure:
    baseline = results[0]
    fig = go.Figure(
        layout=go.Layout(
            xaxis=go.layout.XAxis(
                title="Time [s]",
                range=PLOT_RANGE,
            ),
            yaxis=go.layout.YAxis(
                title="DP vs Baseline",
                range=[
                    floor_to(
                        min(
                            min((result.dp - baseline.dp)[result.t <= PLOT_RANGE[1]])
                            for result in results
                        ),
                        10,
                    ),
                    ceil_to(
                        max(
                            max((result.dp - baseline.dp)[result.t <= PLOT_RANGE[1]])
                            for result in results
                        ),
                        10,
                    ),
                ],
            ),
            title=(title + "<br>" if title else "")
            + f"DP Generation Delta vs {baseline.name}"
            f"<br>initial DP={baseline.setup.dp_start:.0f}",
            hoverlabel=go.layout.Hoverlabel(namelength=-1),
            legend=go.layout.Legend(groupclick="toggleitem"),
        ),
        data=[
            go.Scatter(
                x=result.t,
                y=result.dp - baseline.dp,
                name=result.setup.operator.skill.name,
                legendgroup=result.setup.operator.name,
                legendgrouptitle_text=result.setup.operator.name,
                line=go.scatter.Line(color=result.setup.color, dash="solid"),
                hovertemplate=f"(%{{x}}, %{{y:.2f}})<extra>{result.setup.operator.name}"
                f"<br>{result.setup.operator.skill.name}</extra>",
            )
            for result in results
            if result.setup.operator is not None
        ],
    )
    return fig


def save_plot(
    fig: go.Figure,
    tgt_dir: pathlib.Path | str = "outputs",
    show: bool = False,
    mkdir: bool = False,
):
    tgt_dir = pathlib.Path(tgt_dir)
    if mkdir:
        tgt_dir.mkdir(exist_ok=True)

    title = fig.layout.title.text
    if not title:
        title = uuid.uuid1()

    title = slugify.slugify(str(title)) + ".html"
    output_path = tgt_dir / title
    output_path.unlink(missing_ok=True)
    fig.write_html(output_path)

    if show:
        fig.show()
