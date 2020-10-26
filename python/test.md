### Pytest
* Exclude: ` @pytest.mark.slow; pytest "not slow" `
* pytest.ini: Prevent mistakes: ` addopts = --strict; markers = slow `
* list markers: `pytest --markers`
* html report: `pytest --html=report.html`
* doctest: `pytest --doctest-modules`. -o doctest_optionflags=. Permanently has ELLIPSIS. --doctest_glob=
* Parameterized tests

### Unittest
* python -m unittest test.py -k some -v
* `@unittest.skip('WIP'); assertRaises`

### doctest
* Directives. Handling output that varies using a wildcard: `#doctest +ELLIPSIS; 0x... `. Traceback: ` +IGNORE_EXCEPTION_DETAIL`. -o for global options and directives
* Send random numbers: `random.seed(1234)`

### Test doubles
* mock. stub. fake: StringIO. Spy, make sure interactive betweem 2 objects. Monkey patching
* http://xunitpatterns.com

### coverage
* branch
* trends

