from vanguard_lib import app


def test_simulation():
    parameters = app.get_parameters(None)
    app.run(parameters)
