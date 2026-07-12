def test_hydranav_importable():
    import hydranav

    assert hydranav is not None


def test_hydranav_version():
    import hydranav

    assert hydranav.__version__ == "0.1.0"
