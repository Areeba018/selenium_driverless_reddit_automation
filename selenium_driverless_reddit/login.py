import asyncio
from selenium_driverless import webdriver
import random
import time
import traceback

# Helper functions
def random_sleep(min_seconds=2, max_seconds=5):
    sleep_time = random.uniform(min_seconds, max_seconds)
    time.sleep(sleep_time)

async def reddit_login(driver, user):
    try:
        await driver.maximize_window()
        await driver.get("https://www.reddit.com/login/", wait_load=True, timeout=120)
        print("Reddit website opened successfully.")


        # Enter the username
        username_field = await driver.find_element("xpath", "//*[@id='login-username']", timeout=20)
        if not username_field:
            print("Username field not found. Exiting.")
            return False
        
        await username_field.click()  # Await click coroutine
        await username_field.send_keys(user.get('username'))  # Await send_keys coroutine
        print("Username entered.")
        random_sleep()

        # Wait for the password field to appear
        password_field = await driver.find_element("xpath", "//*[@id='login-password']", timeout=20)
        if not password_field:
            print("Password field not found. Exiting.")
            return False

        await password_field.click()  # Await click coroutine
        await password_field.send_keys(user.get('password'))  # Await send_keys coroutine
        print("Password entered.")
        random_sleep()

        # Click the login button using the correct XPath
        login_button = await driver.find_element("xpath", "//div[@slot='primaryButton']//button[@class='login w-100 button-large button-brand' and text()='Log In']", timeout=30)
        if not login_button:
         print("Login button not found. Exiting.")
         return False
        await driver.execute_script("arguments[0].click();", login_button)
        print("Login button clicked.")


        # Wait and check the current URL
        await asyncio.sleep(5)  # Allow time for the redirect
        current_url = await driver.current_url  # Use await to get the URL value

        if not current_url:
            print("Failed to fetch current URL. Exiting.")
            return False

        print(f"Current URL after login: {current_url}")  # Debug log
        if "signin" in current_url:
            print("Login failed.")
            return False

        print("Login successful.")
        return True

    except Exception as e:
        print(f"Error during login: {e}")
        traceback.print_exc() 
        return False
