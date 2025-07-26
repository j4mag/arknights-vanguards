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
