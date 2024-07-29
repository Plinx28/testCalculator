import pytest


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call':
        # Добавляем информацию о параметрах теста
        if 'parametrize' in item.keywords:
            parametrize_marks = [mark for mark in item.iter_markers(name="parametrize")]
            for mark in parametrize_marks:
                argnames = mark.args[0]
                argvalues = item.callspec.params
                param_info = ', '.join(f"{name}={argvalues[name]}" for name in argnames.split(','))
                report.sections.append(("Test Parameters", param_info))

        # Добавляем содержимое лога для теста test_log_file
        if report.nodeid == 'tests/test_webcalculator.py::test_log_file':
            log_content = item.config._metadata.get('Log Content', '')
            report.sections.append(("Log Content", log_content))


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_header(cells):
    cells.insert(2, "<th>Parameters</th>")


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_table_row(report, cells):
    parameters = next((v for k, v in report.sections if k == "Test Parameters"), "")
    cells.insert(2, f'<td>{parameters}</td>')
