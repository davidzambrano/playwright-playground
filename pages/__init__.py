"""Page objects package."""

from .add_remove_elements_page import AddRemoveElementsPage
from .base_page import BasePage
from .basic_auth_page import BasicAuthPage
from .home_page import HomePage
from .slow_resources_page import SlowResourcesPage

__all__ = [
    "BasePage",
    "HomePage",
    "SlowResourcesPage",
    "AddRemoveElementsPage",
    "BasicAuthPage",
]
