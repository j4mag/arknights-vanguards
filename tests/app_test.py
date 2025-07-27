from vanguard_lib import app


def test_config_round_trip():
    config_file: str = "config/config.json"
    with open(config_file, encoding="utf-8") as f:
        config_text = f.read()
    parameters = app.get_parameters(config_file)
    config_text_2 = parameters.model_dump_json(indent=4, round_trip=True)

    assert config_text == config_text_2


def test_no_config():
    config_file: str = "config/config.json"
    parameters_no_input = app.get_parameters(None)
    with open(config_file, "w", encoding="utf-8") as f:
        f.write(parameters_no_input.model_dump_json(indent=4, round_trip=True))
    parameters_with_input = app.get_parameters(config_file)
    assert parameters_no_input == parameters_with_input


def test_main_config():
    app.main(("-c", "config/config.json"))


def test_main_no_config():
    app.main("")


def test_disabled_plots():
    parameters = app.Parameters(
        simulations=[
            app.SimulationParameters(
                operators=app.vanguards.ALL_OPERATOR_SKILLS,
                title="All Operators",
                t_step=0.1,
                t_end=240,
                dp_start=0,
                plot_dp_absolute=False,
                plot_dp_added=False,
                plot_dp_added_trend=False,
                plot_dp_relative=False,
            ),
        ]
    )
    app.run(parameters)
