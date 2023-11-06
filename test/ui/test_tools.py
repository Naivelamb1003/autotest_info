import pytest

from modules.ui.pages.enroll_facade import EnrollFacade


@pytest.mark.ui
def test_enroll(test_user):
    enrol_facade = EnrollFacade()
    enrol_facade.enroll(test_user, "Test message")
