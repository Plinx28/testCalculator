import pytest


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == 'call':
        if hasattr(item, 'callspec'):
            param_info = ', '.join(f"{name}={value}" for name, value in item.callspec.params.items())
            report.sections.append(("Test Parameters", param_info))


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, "<th>Parameters</th>")


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    parameters = next((v for k, v in report.sections if k == "Test Parameters"), "")
    cells.insert(2, f'<td>{parameters}</td>')
