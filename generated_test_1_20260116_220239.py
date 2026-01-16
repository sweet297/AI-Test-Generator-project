"""
AI-Generated Test: Empty Form Validation
Generated from: "Test that submitting an empty registration form displays validation errors for all required fields"
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestEmptyFormValidation:
    """Test suite for form validation with empty fields"""
    
    def setup_method(self):
        """Initialize WebDriver before each test"""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
    
    def teardown_method(self):
        """Clean up after each test"""
        self.driver.quit()
    
    def test_submit_empty_registration_form(self):
        """
        Test Case: Verify validation errors appear when submitting
        an empty registration form
        """
        # Navigate to registration page
        self.driver.get("http://localhost:8080/register")
        
        # Click submit without filling any fields
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_button.click()
        
        # Wait for validation errors to appear
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "validation-error"))
        )
        
        # Check for required field errors
        required_fields = ["username", "email", "password", "confirm-password"]
        
        for field in required_fields:
            error_element = self.driver.find_element(
                By.XPATH, 
                f"//input[@name='{field}']/following-sibling::span[@class='validation-error']"
            )
            
            assert error_element.is_displayed(), \
                f"Validation error for {field} should be visible"
            
            assert "required" in error_element.text.lower() or \
                   "cannot be empty" in error_element.text.lower(), \
                   f"Unexpected validation message for {field}: {error_element.text}"
        
        print(f"✓ Test Passed: All {len(required_fields)} required field validations working")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
