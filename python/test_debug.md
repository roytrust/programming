### Debug
* [most recently raised exception](https://wil.yegelwel.com/pdb-pm/): `import pdb; pdb.pm()`. u - up. 
* 

### Mock
* [Understanding the Python Mock Object Library](https://realpython.com/python-mock-library/)
* Mock, fake import package: `from unittest import mock; sys.modules['a.b']=mock.MagicMock()`
* Replace a package: `sys.modules['B'] = __import__('mock_B')`

### [Pytest](https://realpython.com/pytest-python-testing/)
* https://pytest-with-eric.com
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

### [Profiling](https://realpython.com/python-profiling/)
* Timers: time, timeit. Deterministic profilers: profile, cProfile, line_profiler. Statistical profilers: Pyinstrument, linux perf.
* time: `perf_counter(); process_time(); monotonic()`
* timeit: `timeit("code", number=interations, globals=globals()); python -m timeit -s "$SETUP_CODE" -r 100 "code"`
* [cProfile/profile](https://docs.python.org/3/library/profile.html#what-is-deterministic-profiling): `import cProfile; cProfile.run()`
* [Pyinstrument](https://pyinstrument.readthedocs.io/en/latest/)
* [Linux perf](https://realpython.com/python-profiling/#perf-count-hardware-and-system-events-on-linux):
  `perf record -g -F 999 "$HOME/python-custom-build/bin/python3" -X perf profile_perf.py;`  
  `perf report; perf report --hierarchy --sort comm,dso,sample`
* `sys.setprofile(); sys.settrace()`

### More
* Unittest
  * python -m unittest test.py -k some -v
  * `@unittest.skip('WIP'); assertRaises`
* doctest
  * Directives. Handling output that varies using a wildcard: `#doctest +ELLIPSIS; 0x... `. Traceback: ` +IGNORE_EXCEPTION_DETAIL`. -o for global options and directives
  * Send random numbers: `random.seed(1234)`
* Test doubles
  * mock. stub. fake: StringIO. Spy, make sure interactive betweem 2 objects. Monkey patching
  * http://xunitpatterns.com

