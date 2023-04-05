### [Pytest](https://realpython.com/pytest-python-testing/)
* log config: `-v -o log_cli=true --log-cli-level=DEBUG --capture=tee-sys`
* **Fixtures** for handling test dependencies, state, and reusable functionality
* **Marks** for categorizing tests and limiting access to external resources
* **Parametrization** for reducing duplicated code between tests
* **Durations** to identify your slowest tests
* **Plugins** for integrating with other frameworks and testing tools

* Exclude: ` @pytest.mark.slow; pytest "not slow" `
* Set up parameters: `@pytest.fixture(name="argv")`
* pytest.ini: Prevent mistakes: ` addopts = --strict; markers = slow `
* [list markers](https://docs.pytest.org/en/stable/mark.htm): `pytest --markers`
* [@pytest.fixture](https://docs.pytest.org/en/stable/fixture.html). tmpdir. cleanup - yield
* html report: `pytest --html=report.html`
* doctest: `pytest --doctest-modules`. -o doctest_optionflags=. Permanently has ELLIPSIS. --doctest_glob=
* Parameterized tests
* [Assertions about expected exceptions](https://docs.pytest.org/en/stable/assert.html#assertions-about-expected-exceptions)
* [Tutorial](https://www.tutorialspoint.com/pytest/index.htm)

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

## Debug
* [most recently raised exception](https://wil.yegelwel.com/pdb-pm/): `import pdb; pdb.pm()`. u - up. 
* 
