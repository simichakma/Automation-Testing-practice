from Pages.infinite_scroll_page import InfiniteScrollPage


def test_infinite_scroll(driver):

    page = InfiniteScrollPage(driver)
    page.go_to_page()

    # simple step scroll
    page.scroll_down_steps(steps=10, pause=1)

    # OR smarter scroll-until-end
    # page.scroll_to_bottom_smart()
