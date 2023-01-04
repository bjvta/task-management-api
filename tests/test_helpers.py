


from datetime import datetime
from src.helpers import CreateBugNameHelper


def test_create_bug_name():
    title = 'This is the title'
    day = datetime.now().day
    month = datetime.now().month
    result = CreateBugNameHelper(title).call()
    expected_result = f"bug-This-{day}{month}"
    assert result == expected_result
