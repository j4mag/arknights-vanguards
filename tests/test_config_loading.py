from vanguard_lib import app


def test_config_round_trip():
    config_file: str = "config/config.json"

    with open(config_file) as f:
        config_text = f.read()

    parameters = app.get_parameters(config_file)
    config_text_2 = parameters.model_dump_json(indent=4, round_trip=True)

    assert config_text == config_text_2
