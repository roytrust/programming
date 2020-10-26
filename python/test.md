### Pytest
* Exclude: ` @pytest.mark.slow; pytest "not slow" `
* pytest.ini: Prevent mistakes: ` addopts = --strict; markers = slow `
* list markers: `pytest --markers`
* html report: `pytest --html=report.html`
* doctest: `pytest --doctest-modules`

### Unittest
* python -m unittest test.py -k some -v
* `@unittest.skip('WIP'); assertRaises`
