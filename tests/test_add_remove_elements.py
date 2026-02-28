"""Tests for the Add/Remove Elements page."""
import pytest
from playwright.sync_api import expect

class TestSlowResourcesPage:
    """Tests for status banner visibility on the Add/Remove Elements page."""

    @pytest.fixture(autouse=True)
    def setup_pages(self, home_page, page, add_remove_elements_page, base_url):
        """Set up page objects and base URL as class attributes."""
        self.page = page
        self.home_page = home_page
        self.add_remove_elements_page = add_remove_elements_page
        self.base_url = base_url

    @pytest.fixture
    def navigate_to_add_remove_elements(self):
        """Fixture to navigate to the Add/Remove Elements page."""
        self.home_page.goto_home_page(self.base_url)
        self.home_page.click_add_remove_element_card()

    def test_add_one_element(self, navigate_to_add_remove_elements):
        """Test adding a single element creates exactly one delete button."""
        self.add_remove_elements_page.click_add_element_button()
        count = self.add_remove_elements_page.get_delete_buttons_count()
        assert count == 1, f"Expected 1 delete button, but found {count}"

    def test_initial_state(self, navigate_to_add_remove_elements):
        """Test that no delete buttons are present initially."""
        count = self.add_remove_elements_page.get_delete_buttons_count()
        assert count == 0, f"Expected 0 delete buttons initially, but found {count}"

    def test_add_multiple_elements(self, navigate_to_add_remove_elements):
        """Test adding multiple elements creates one new delete button per click."""
        num_clicks = 5
        for i in range(num_clicks):
            self.add_remove_elements_page.click_add_element_button()
            count = self.add_remove_elements_page.get_delete_buttons_count()
            expected = i + 1
            assert count == expected, f"After {expected} clicks, expected {expected} delete buttons, but found {count}"

    def test_button_visibility_after_adding_one(self, navigate_to_add_remove_elements):
        """Test that Add Element and Delete buttons are visible after adding one element."""
        # Add one element
        self.add_remove_elements_page.click_add_element_button()
        
        # Check Add Element button is visible
        add_button = self.add_remove_elements_page.get_add_element_button()
        expect(add_button).to_be_visible()
        
        # Check Delete button is visible
        delete_button = self.add_remove_elements_page.get_delete_button(1)
        expect(delete_button).to_be_visible()

    def test_button_text(self, navigate_to_add_remove_elements):
        """Test that newly created elements display the correct 'Element N' text."""
        num_elements = 3
        for i in range(num_elements):
            self.add_remove_elements_page.click_add_element_button()
            # Check the text of the newly added element
            added_element = self.add_remove_elements_page.get_added_element(i + 1)
            expect(added_element).to_have_text(f"Element {i + 1}")

    def test_remove_single_element(self, navigate_to_add_remove_elements):
        """Test removing a single element removes only that button."""
        # Add 3 elements
        for _ in range(3):
            self.add_remove_elements_page.click_add_element_button()
        initial_count = self.add_remove_elements_page.get_delete_buttons_count()
        assert initial_count == 3, f"Expected 3 delete buttons after adding, but found {initial_count}"
        
        # Remove the first element
        self.add_remove_elements_page.click_delete_button(1)
        final_count = self.add_remove_elements_page.get_delete_buttons_count()
        assert final_count == 2, f"Expected 2 delete buttons after removing one, but found {final_count}"

    def test_remove_multiple_elements(self, navigate_to_add_remove_elements):
        """Test removing multiple elements updates the list correctly."""
        # Add 5 elements
        for _ in range(5):
            self.add_remove_elements_page.click_add_element_button()
        initial_count = self.add_remove_elements_page.get_delete_buttons_count()
        assert initial_count == 5, f"Expected 5 delete buttons after adding, but found {initial_count}"
        
        # Remove the 1st and 3rd element (now 2nd and 4th after first removal)
        self.add_remove_elements_page.click_delete_button(1)
        self.add_remove_elements_page.click_delete_button(2)
        final_count = self.add_remove_elements_page.get_delete_buttons_count()
        assert final_count == 3, f"Expected 3 delete buttons after removing two, but found {final_count}"

    def test_add_after_removing_all(self, navigate_to_add_remove_elements):
        """Test that adding elements works after deleting all."""
        # Add 3 elements
        for _ in range(3):
            self.add_remove_elements_page.click_add_element_button()
        initial_count = self.add_remove_elements_page.get_delete_buttons_count()
        assert initial_count == 3, f"Expected 3 delete buttons after adding, but found {initial_count}"
        
        # Remove all elements
        while self.add_remove_elements_page.get_delete_buttons_count() > 0:
            self.add_remove_elements_page.click_delete_button(1)
        zero_count = self.add_remove_elements_page.get_delete_buttons_count()
        assert zero_count == 0, f"Expected 0 delete buttons after removing all, but found {zero_count}"
        
        # Add one more element
        self.add_remove_elements_page.click_add_element_button()
        final_count = self.add_remove_elements_page.get_delete_buttons_count()
        assert final_count == 1, f"Expected 1 delete button after adding one, but found {final_count}"
