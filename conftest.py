import pytest


BLOCKED_RESOURCE_PARTS = (
    "doubleclick.net",
    "google-analytics.com",
    "googleads",
    "googlesyndication",
    "googletagmanager.com",
    "fonts.googleapis.com",
)


@pytest.fixture(autouse=True)
def block_unstable_external_resources(page):
    page.route(
        "**/*",
        lambda route: (
            route.abort()
            if any(part in route.request.url for part in BLOCKED_RESOURCE_PARTS)
            else route.continue_()
        ),
    )
