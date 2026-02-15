from Pages.radio_buttons_page import RadioButtonsPage


def test_select_radio_buttons(driver):

    radio = RadioButtonsPage(driver)

    radio.go_to_radio_page()

    radio.select_blue_color()
    radio.select_tennis_sport()

    assert radio.is_blue_selected()
    assert radio.is_tennis_selected()
