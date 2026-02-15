from Pages.autocomplete_page import AutocompletePage


def test_autocomplete_submit(driver):

    page = AutocompletePage(driver)
    page.go_to_page()

    page.select_country("Bangladesh")
    page.submit_form()

    assert "bangladesh" in page.get_result().lower()
