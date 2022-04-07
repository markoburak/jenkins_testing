id_selector = lambda id_: f"[id='{id_}']"
class_selector = lambda class_: f"[class='{class_}']"
link = lambda href_: f"//a[contains(@href, {href_})]"

general_selectors = {
    "main_screen": {
        "title": f"h1{class_selector('hero__title')}",
        "button": f"a{class_selector('getStarted_CALW')}"
    }
}
