from playwright.sync_api import Page
import logging

logger = logging.getLogger(__name__)


class BasePage:
    """Base page class with common functionality for all page objects."""
    
    def __init__(self, page: Page):
        """Initialize the BasePage with a page object.
        
        Args:
            page (Page): The page object.
        
        Returns:
            None
        
        """
        self.page = page
    
    def navigate_to(self, url: str) -> None:
        """Navigate to the specified URL.
        
        Args:
            url (str): The URL to navigate to.
        
        Returns:
            None
        
        """
        logger.info(f"Navigating to: {url}")
        self.page.goto(url)
    
    def wait_for_page_load(self) -> None:
        """Wait for the page to finish loading.
        
        Returns:
            None
        
        """
        self.page.wait_for_load_state('networkidle')
        logger.info("Page load completed")
    
    def take_screenshot(self, filename: str) -> None:
        """Take a screenshot of the current page.
        
        Args:
            filename (str): The name of the screenshot file.
        
        Returns:
            None
        
        """
        screenshot_path = f"reports/screenshots/{filename}.png"
        self.page.screenshot(path=screenshot_path, full_page=True)
        logger.info(f"Screenshot saved: {screenshot_path}")
    
    def scroll_to_element(self, locator: str) -> None:
        """Scroll to a specific element.
        
        Args:
            locator (str): The CSS selector or XPath for the element.
        
        Returns:
            None
        
        """
        element = self.page.locator(locator)
        element.scroll_into_view_if_needed()
        logger.info(f"Scrolled to element: {locator}")
    
    def get_page_title(self) -> str:
        """Get the current page title.
        
        Returns:
            str: The title of the current page.
        
        """
        title = self.page.title()
        logger.info(f"Page title: {title}")
        return title
