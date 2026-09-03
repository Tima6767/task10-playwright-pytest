import allure

def attach_screenshot(page, name):
    try:
        screenshot = page.screenshot()
        allure.attach(
            screenshot,
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
    except Exception as e:
        print(f"WARNING: Failed to attach screenshot '{name}': {e}")