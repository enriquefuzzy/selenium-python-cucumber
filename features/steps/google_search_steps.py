from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# Chrome WebDriver is created/torn down before/after each scenario in features/environment.py
@given('the user is on Google')
def step_given_user_on_google(context):
    context.driver.get("https://www.google.com")

@when('the user searches for "{search_term}"')
def step_when_user_searches(context, search_term):
    # Locate the search input field and enter the search term
    search_input = context.driver.find_element(By.CSS_SELECTOR, "[name=q]")
    search_input.send_keys(search_term)
    search_input.submit()

@then('Dog results are displayed')
def step_then_dog_results_displayed(context):
    # Verify that the search results contain the word "Dog"
    search_results = WebDriverWait(context.driver, timeout=10).until(lambda d: d.find_element(By.XPATH,"//div[@data-attrid='title'][contains(text(), 'Dog')]"))
    search_results = context.driver.find_element(By.XPATH, "//div[@data-attrid='title'][contains(text(), 'Dog')]")
    assert search_results.text == 'Dog', "Dog results are not displayed"

@then('Cat results are displayed')
def step_then_dog_results_displayed(context):
    # Verify that the search results contain the word "Cat"
    search_results = WebDriverWait(context.driver, timeout=10).until(lambda d: d.find_element(By.CSS_SELECTOR,"[data-attrid=title]"))
    search_results = context.driver.find_element(By.CSS_SELECTOR, "[data-attrid=title]")
    assert search_results.text == 'Cat', "Cat results are not displayed"
