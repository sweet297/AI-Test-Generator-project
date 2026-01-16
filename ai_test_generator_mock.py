"""
AI-Powered Test Generator - MOCK VERSION (No API Key Required)
Author: AYA MAHBOUB
Date: January 2026
Description: Demonstrates AI test generation using pre-built templates
"""

from datetime import datetime
import time

# ============================================================================
# MOCK AI: TEMPLATE-BASED TEST GENERATION
# ============================================================================

def generate_selenium_test_mock(test_description):
    """
    Simulates AI generation using intelligent templates
    This demonstrates the concept without requiring OpenAI API
    """
    
    print("\n" + "="*70)
    print("🤖 AI is generating your test code...")
    print("="*70)
    print(f"📝 Description: {test_description}")
    print("⏳ Processing with AI model...\n")
    
    # Simulate AI thinking time
    time.sleep(2)
    
    # Template selection based on keywords
    description_lower = test_description.lower()
    
    # Login test template
    if "login" in description_lower and "invalid" in description_lower:
        code_template = '''"""
AI-Generated Test: Invalid Login Validation
Generated from: "{description}"
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestInvalidLogin:
    """Test suite for login validation with invalid credentials"""
    
    def setup_method(self):
        """Initialize WebDriver before each test"""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
    
    def teardown_method(self):
        """Clean up after each test"""
        self.driver.quit()
    
    def test_login_with_invalid_credentials(self):
        """
        Test Case: Verify error message appears when logging in 
        with invalid username and password
        """
        # Navigate to login page
        self.driver.get("http://localhost:8080/login")
        
        # Locate and fill username field
        username_field = self.driver.find_element(By.ID, "username")
        username_field.clear()
        username_field.send_keys("invalid_user@example.com")
        
        # Locate and fill password field
        password_field = self.driver.find_element(By.ID, "password")
        password_field.clear()
        password_field.send_keys("wrongPassword123")
        
        # Click login button
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        
        # Wait for error message to appear
        error_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "error-message"))
        )
        
        # Verify error message is displayed
        assert error_message.is_displayed(), "Error message should be visible"
        
        # Verify error message contains expected text
        assert "Invalid credentials" in error_message.text.lower() or \\
               "incorrect username or password" in error_message.text.lower(), \\
               f"Unexpected error message: {error_message.text}"
        
        print("✓ Test Passed: Error message displayed correctly for invalid login")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
'''

        code = code_template.replace("{description}", test_description)
    
    # Empty form validation template
    elif "empty" in description_lower and "form" in description_lower:
        code_template = '''"""
AI-Generated Test: Empty Form Validation
Generated from: "{description}"
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
            
            assert error_element.is_displayed(), \\
                f"Validation error for {field} should be visible"
            
            assert "required" in error_element.text.lower() or \\
                   "cannot be empty" in error_element.text.lower(), \\
                   f"Unexpected validation message for {field}: {error_element.text}"
        
        print(f"✓ Test Passed: All {len(required_fields)} required field validations working")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
'''

        code = code_template.replace("{description}", test_description)
    
    # Search validation template
    elif "search" in description_lower and "empty" in description_lower:
        code_template = '''"""
AI-Generated Test: Empty Search Validation
Generated from: "{description}"
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSearchValidation:
    """Test suite for search functionality validation"""
    
    def setup_method(self):
        """Initialize WebDriver before each test"""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
    
    def teardown_method(self):
        """Clean up after each test"""
        self.driver.quit()
    
    def test_search_with_empty_term(self):
        """
        Test Case: Verify warning appears when clicking search 
        without entering a search term
        """
        # Navigate to search page
        self.driver.get("http://localhost:8080/search")
        
        # Leave search field empty and click search button
        search_button = self.driver.find_element(By.ID, "search-button")
        search_button.click()
        
        # Wait for warning message
        warning_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "warning-message"))
        )
        
        # Verify warning is displayed
        assert warning_message.is_displayed(), "Warning message should be visible"
        
        # Verify warning text
        expected_warnings = [
            "please enter a search term",
            "search field cannot be empty",
            "enter at least one character"
        ]
        
        warning_text = warning_message.text.lower()
        assert any(exp in warning_text for exp in expected_warnings), \\
               f"Unexpected warning message: {warning_message.text}"
        
        print("✓ Test Passed: Warning displayed for empty search")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
'''

        code = code_template.replace("{description}", test_description)
    
    # Shopping cart template
    elif "cart" in description_lower or "shopping" in description_lower:
        code_template = '''"""
AI-Generated Test: Shopping Cart Functionality
Generated from: "{description}"
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestShoppingCart:
    """Test suite for shopping cart functionality"""
    
    def setup_method(self):
        """Initialize WebDriver before each test"""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
    
    def teardown_method(self):
        """Clean up after each test"""
        self.driver.quit()
    
    def test_add_item_updates_cart_count(self):
        """
        Test Case: Verify cart count updates correctly when adding an item
        """
        # Navigate to product page
        self.driver.get("http://localhost:8080/products")
        
        # Get initial cart count
        cart_badge = self.driver.find_element(By.CLASS_NAME, "cart-count")
        initial_count = int(cart_badge.text) if cart_badge.text else 0
        
        # Find and click "Add to Cart" button for first product
        add_to_cart_btn = self.driver.find_element(
            By.XPATH, 
            "//button[contains(@class, 'add-to-cart')][1]"
        )
        add_to_cart_btn.click()
        
        # Wait for cart count to update
        WebDriverWait(self.driver, 10).until(
            lambda d: int(d.find_element(By.CLASS_NAME, "cart-count").text or 0) > initial_count
        )
        
        # Get updated cart count
        updated_count = int(cart_badge.text)
        
        # Verify count increased by 1
        assert updated_count == initial_count + 1, \\
               f"Cart count should increase by 1. Expected {initial_count + 1}, got {updated_count}"
        
        print(f"✓ Test Passed: Cart count updated from {initial_count} to {updated_count}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
'''

        code = code_template.replace("{description}", test_description)
    
    # Logout template
    elif "logout" in description_lower:
        code_template = '''"""
AI-Generated Test: Logout Functionality
Generated from: "{description}"
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLogout:
    """Test suite for logout functionality"""
    
    def setup_method(self):
        """Initialize WebDriver before each test"""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
    
    def teardown_method(self):
        """Clean up after each test"""
        self.driver.quit()
    
    def test_logout_clears_session_and_redirects(self):
        """
        Test Case: Verify logout clears session and redirects to homepage
        """
        # First, login to create a session
        self.driver.get("http://localhost:8080/login")
        
        username_field = self.driver.find_element(By.ID, "username")
        username_field.send_keys("testuser@example.com")
        
        password_field = self.driver.find_element(By.ID, "password")
        password_field.send_keys("password123")
        
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
        
        # Wait for successful login (dashboard appears)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "dashboard"))
        )
        
        # Click logout button
        logout_button = self.driver.find_element(By.ID, "logout-btn")
        logout_button.click()
        
        # Wait for redirect to homepage
        WebDriverWait(self.driver, 10).until(
            EC.url_to_be("http://localhost:8080/") or 
            EC.url_contains("/home")
        )
        
        # Verify user is redirected to homepage
        current_url = self.driver.current_url
        assert current_url.endswith("/") or "/home" in current_url, \\
               f"Should redirect to homepage, but got: {current_url}"
        
        # Verify session is cleared (try accessing protected page)
        self.driver.get("http://localhost:8080/dashboard")
        
        # Should redirect back to login
        WebDriverWait(self.driver, 10).until(
            EC.url_contains("/login")
        )
        
        assert "/login" in self.driver.current_url, \\
               "Session should be cleared, user should be redirected to login"
        
        print("✓ Test Passed: Logout successful, session cleared, redirected to homepage")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
'''

        code = code_template.replace("{description}", test_description)
    
    # Generic template for any other description
    else:
        code_template = '''"""
AI-Generated Test: Custom Test Scenario
Generated from: "{description}"
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestCustomScenario:
    """AI-generated test suite based on user description"""
    
    def setup_method(self):
        """Initialize WebDriver before each test"""
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
    
    def teardown_method(self):
        """Clean up after each test"""
        self.driver.quit()
    
    def test_custom_scenario(self):
        """
        Test Case: {description}
        
        This test was automatically generated by AI based on 
        the provided natural language description.
        """
        # Navigate to application
        self.driver.get("http://localhost:8080/")
        
        # AI would analyze the description and generate appropriate
        # Selenium commands here. For demonstration, this shows
        # the structure of a well-formed test.
        
        # Example: Find and interact with elements
        # element = self.driver.find_element(By.ID, "element-id")
        # element.click()
        
        # Example: Wait for conditions
        # WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((By.CLASS_NAME, "result"))
        # )
        
        # Example: Assertions
        # assert expected_condition, "Error message"
        
        print(f"✓ Test structure generated for: {description}")
        print("Note: Specific element locators would be determined by AI analysis")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
'''

        code = code_template.replace("{description}", test_description)
    
    return code


# ============================================================================
# SAVE GENERATED CODE TO FILE
# ============================================================================

def save_test_file(code, test_number):
    """Saves generated test code to a Python file"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"generated_test_{test_number}_{timestamp}.py"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write(code)
    
    print(f"💾 Saved to: {filename}")
    return filename


# ============================================================================
# DISPLAY MENU
# ============================================================================

def show_menu():
    """Display the main menu with example test scenarios"""
    
    print("\n" + "="*70)
    print("  🚀 AI-POWERED SELENIUM TEST GENERATOR (MOCK VERSION)")
    print("="*70)
    print("\n📋 PRE-DEFINED TEST EXAMPLES:")
    print("-" * 70)
    
    examples = [
        "Test that logging in with invalid username and password shows an error message",
        "Test that submitting an empty registration form displays validation errors for all required fields",
        "Test that clicking the search button without entering any search term shows a warning message",
        "Test that adding an item to the shopping cart updates the cart count correctly",
        "Test that clicking logout button clears the user session and redirects to homepage"
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n  {i}. {example}")
    
    print("\n" + "-"*70)
    print("  0. Enter your own custom test description")
    print("  Q. Quit program")
    print("="*70 + "\n")
    
    return examples


# ============================================================================
# MAIN PROGRAM
# ============================================================================

def main():
    """Main program loop"""
    
    print("\n" + "="*70)
    print("  ℹ️  DEMO MODE - Using Template-Based AI Simulation")
    print("="*70)
    print("This version demonstrates AI test generation without requiring")
    print("an OpenAI API key. It uses intelligent templates based on keywords.")
    print("="*70)
    
    test_count = 0
    
    while True:
        examples = show_menu()
        
        choice = input("👉 Enter your choice: ").strip()
        
        # Quit
        if choice.upper() == 'Q':
            print(f"\n👋 Goodbye! Generated {test_count} test(s).\n")
            break
        
        # Pre-defined examples
        elif choice.isdigit() and 1 <= int(choice) <= len(examples):
            test_description = examples[int(choice) - 1]
        
        # Custom description
        elif choice == '0':
            test_description = input("\n📝 Enter your test description: ").strip()
            if not test_description:
                print("❌ Description cannot be empty!")
                continue
        
        else:
            print("❌ Invalid choice! Please try again.\n")
            continue
        
        # Generate the test using mock AI
        test_count += 1
        generated_code = generate_selenium_test_mock(test_description)
        
        # Display result
        print("\n" + "="*70)
        print("✅ GENERATED TEST CODE:")
        print("="*70 + "\n")
        print(generated_code)
        print("\n" + "="*70)
        
        # Save to file
        filename = save_test_file(generated_code, test_count)
        print(f"✅ Test #{test_count} generated successfully!")
        print("="*70)
        
        # Continue?
        continue_choice = input("\n🔄 Generate another test? (Y/N): ").strip().upper()
        if continue_choice != 'Y':
            print(f"\n✅ Done! Generated {test_count} test(s). Check your project folder.\n")
            break


# ============================================================================
# RUN THE PROGRAM
# ============================================================================

if __name__ == "__main__":
    main()