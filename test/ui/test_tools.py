import uuid

import pytest

from modules.ui.pages.book_store_facade import BookStoreFacade


@pytest.mark.ui
def test_book_adding_should_create_book_in_profile_list(test_user, test_book_name):
    book_store_facade = BookStoreFacade()
    random_user_name = str(uuid.uuid4())
    print(random_user_name)
    book_store_facade.register(test_user, random_user_name)
    book_store_facade.login(test_user, random_user_name)
    book_store_facade.add_book(test_book_name)
    book_store_facade.validate_book_and_delete_account(test_book_name)
    book_store_facade.close_driver()


@pytest.mark.ui
def test_book_delete():
    assert False


@pytest.mark.ui
def test_login_of_existing_user_should_not_pass():
    assert False


@pytest.mark.ui
def test_logout_should_make_impossible_to_add_book():
    assert False
