import time
from selenium import webdriver
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# Functional testing for IMDb.com, contains the following tests:
# Search Functionality: Search for actor, movie and validate data
# User Authentication: Create new user, Login and Log out process testing
# Watchlist Functionality testing: Login, search for movie, add to watchlist and validate
# Rating Functionality testing: Login, search for movie, rate it, go to my ratings page and validate data
# Social Sharing: Verify the functionality of sharing content on social media platforms

# setup and teardown (fixture)
@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print("test completed")


# Search functionality (search for actor, movie and validate data)
def test_search(test_setup):
    driver.get("https://imdb.com")
    searchbar = driver.find_element_by_xpath("//input[@id='suggestion-search']")
    # search for Ryan Reynolds and press enter
    searchbar.send_keys("Ryan Reynolds", Keys.RETURN)
    time.sleep(3)
    first_result = driver.find_element_by_xpath("//*[@id='__next']/main/div[2]/div[3]/section/div/div[1]/section[2]/div[2]/ul/li[1]").text
    assert "Ryan Reynolds" in first_result and "Actor" in first_result
    # search again, now for "Finding Nemo"
    second_searchbar = driver.find_element_by_xpath("//input[@id='suggestion-search']")
    second_searchbar.send_keys("Finding Nemo", Keys.RETURN)
    time.sleep(3)
    first_result_2 = driver.find_element_by_xpath("//*[@id='__next']/main/div[2]/div[3]/section/div/div[1]/section[2]/div[2]/ul/li[1]").text
    assert "Finding Nemo" in first_result_2 and "2003" in first_result_2

# Create new user process testing
def test_new_user(test_setup):
    driver.get("https://imdb.com")
    # click on sign in button
    signin_button = driver.find_element_by_xpath("//*[@id='imdbHeader']/div[2]/div[5]/a/span")
    signin_button.click()
    time.sleep(2)
    # click on create new account
    create_new_btn = driver.find_element_by_xpath("//*[@id='signin-options']/div/div[2]/a")
    create_new_btn.click()
    time.sleep(2)
    # insert data to fields
    name_field = driver.find_element_by_xpath("//*[@id='ap_customer_name']")
    name_field.send_keys("Tester")
    email_field = driver.find_element_by_xpath("//*[@id='ap_email']")
    email_field.send_keys("favan78084@shaflyn.com")
    password_field = driver.find_element_by_xpath("//*[@id='ap_password']")
    password_field.send_keys("tester2020")
    password_field_2 = driver.find_element_by_xpath("//*[@id='ap_password_check']")
    password_field_2.send_keys("tester2020")
    create_account_btn = driver.find_element_by_xpath("//*[@id='continue']")
    create_account_btn.click()
    time.sleep(5)

# Login process testing
def test_login(test_setup):
    driver.get("https://imdb.com")
    # click on sign in button
    signin_button = driver.find_element_by_xpath("//*[@id='imdbHeader']/div[2]/div[5]/a/span")
    signin_button.click()
    time.sleep(2)
    # click on create new account
    create_new_btn = driver.find_element_by_xpath("//*[@id='signin-options']/div/div[2]/a")
    create_new_btn.click()
    time.sleep(2)
    # click on "already have an account"
    already_btn = driver.find_element_by_xpath("//*[@id='ap_register_form']/div/div/div[6]/a")
    already_btn.click()
    time.sleep(2)
    # insert data to fields
    email_field = driver.find_element_by_xpath("//*[@id='ap_email']")
    email_field.send_keys("favan78084@shaflyn.com")
    password_field = driver.find_element_by_xpath("//*[@id='ap_password']")
    password_field.send_keys("tester2020")
    # click sign in button
    submit_btn = driver.find_element_by_xpath("//*[@id='signInSubmit']")
    submit_btn.click()
    time.sleep(3)
    # Sign Out Process Testing -
    # click on User dropdown menu
    user_menu = driver.find_element_by_xpath("//*[@id='imdbHeader']/div[2]/div[5]/div/label[2]")
    user_menu.click()
    time.sleep(2)
    # click on sign out button
    signout_btn = driver.find_element_by_xpath("//*[@id='navUserMenu-contents']/ul/a[6]/span")
    signout_btn.click()
    time.sleep(10)

# Watchlist functionality testing (login, search for movie, add to watchlist and validate it's been added)
def test_watchlist(test_setup):
    driver.get("https://imdb.com")
    # click on sign in button
    signin_button = driver.find_element_by_xpath("//*[@id='imdbHeader']/div[2]/div[5]/a/span")
    signin_button.click()
    time.sleep(2)
    # click on create new account
    create_new_btn = driver.find_element_by_xpath("//*[@id='signin-options']/div/div[2]/a")
    create_new_btn.click()
    time.sleep(2)
    # click on "already have an account"
    already_btn = driver.find_element_by_xpath("//*[@id='ap_register_form']/div/div/div[6]/a")
    already_btn.click()
    time.sleep(2)
    # insert data to fields
    email_field = driver.find_element_by_xpath("//*[@id='ap_email']")
    email_field.send_keys("favan78084@shaflyn.com")
    password_field = driver.find_element_by_xpath("//*[@id='ap_password']")
    password_field.send_keys("tester2020")
    # click sign in button
    submit_btn = driver.find_element_by_xpath("//*[@id='signInSubmit']")
    submit_btn.click()
    time.sleep(3)
    # after login process complete, begin watchlist testing
    searchbar = driver.find_element_by_xpath("//input[@id='suggestion-search']")
    # search for Finding Nemo and press enter
    searchbar.send_keys("Finding Nemo", Keys.RETURN)
    time.sleep(3)
    first_result = driver.find_element_by_xpath("//*[@id='__next']/main/div[2]/div[3]/section/div/div[1]/section[2]/div[2]/ul/li[1]")
    first_result.click()
    time.sleep(4)
    # add movie to watch list by clicking on the plus icon
    plus_icon = driver.find_element_by_xpath("//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[3]/div[1]/div[1]/div/div[2]")
    plus_icon.click()
    time.sleep(1)
    # move to watchlist page and check if our movie has been added
    watchlist_btn = driver.find_element_by_xpath("//*[@id='imdbHeader']/div[2]/div[4]/a/span")
    watchlist_btn.click()
    time.sleep(5)
    first_div = driver.find_element_by_xpath("//*[@id='page-1']/div/div/div[2]")
    assert "Finding Nemo" in first_div.text

# Rating functionality testing
def test_rating(test_setup):
    driver.get("https://imdb.com")
    # click on sign in button
    signin_button = driver.find_element_by_xpath("//*[@id='imdbHeader']/div[2]/div[5]/a/span")
    signin_button.click()
    time.sleep(2)
    # click on create new account
    create_new_btn = driver.find_element_by_xpath("//*[@id='signin-options']/div/div[2]/a")
    create_new_btn.click()
    time.sleep(2)
    # click on "already have an account"
    already_btn = driver.find_element_by_xpath("//*[@id='ap_register_form']/div/div/div[6]/a")
    already_btn.click()
    time.sleep(2)
    # insert data to fields
    email_field = driver.find_element_by_xpath("//*[@id='ap_email']")
    email_field.send_keys("favan78084@shaflyn.com")
    password_field = driver.find_element_by_xpath("//*[@id='ap_password']")
    password_field.send_keys("tester2020")
    # click sign in button
    submit_btn = driver.find_element_by_xpath("//*[@id='signInSubmit']")
    submit_btn.click()
    time.sleep(3)
    # after login process complete, begin watchlist testing
    searchbar = driver.find_element_by_xpath("//input[@id='suggestion-search']")
    # search for Finding Nemo and press enter
    searchbar.send_keys("Finding Nemo", Keys.RETURN)
    time.sleep(3)
    first_result = driver.find_element_by_xpath("//*[@id='__next']/main/div[2]/div[3]/section/div/div[1]/section[2]/div[2]/ul/li[1]")
    first_result.click()
    time.sleep(4)
    # click on rating button and rate the movie (10 stars for Nemo)
    rating_btn = driver.find_element_by_xpath("//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[2]/button/span/div/div[2]/div")
    rating_btn.click()
    time.sleep(5)
    # Locate the element (button with text "Rate 10")
    rate_10_button = driver.find_element_by_xpath("//button[@aria-label='Rate 10']")
    # Initialize ActionChains
    action = ActionChains(driver)
    # Move to the rate_10_button and hover
    action.move_to_element(rate_10_button).perform()
    time.sleep(2)
    action.click(rate_10_button).perform()
    time.sleep(1)
    # click Rate button
    rate_btn = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div[2]/button")
    rate_btn.click()
    time.sleep(2)
    # go to my ratings page and see if my rating is there and correct
    user_drop_menu = driver.find_element_by_xpath("//span[@class='imdb-header__account-toggle--logged-in imdb-header__accountmenu-toggle navbar__user-name navbar__user-menu-toggle__name navbar__user-menu-toggle--desktop']")
    user_drop_menu.click()
    time.sleep(2)
    my_ratings_page = driver.find_element_by_xpath("//span[normalize-space()='Your ratings']")
    my_ratings_page.click()
    time.sleep(3)
    rating_results = driver.find_element_by_class_name("ipl-rating-star__rating")
    our_movie = driver.find_element_by_xpath("//*[@id='ratings-container']/div[1]/div[2]/h3/a")
    assert "10" in rating_results.text and "Finding Nemo" in our_movie.text

# Social Sharing: Verify the functionality of sharing content on social media platforms
def test_social(test_setup):
    driver.get("https://imdb.com")
    # search for a movie (Finding Nemo)
    search_bar = driver.find_element_by_xpath("//input[@id='suggestion-search']")
    search_bar.send_keys("Finding Nemo", Keys.ENTER)
    # click on the movie title (first result)
    first_result = driver.find_element_by_xpath("//section[2]//div[2]//ul[1]//li[1]//div[2]//div[1]//a[1]")
    first_result.click()
    # click on Share button
    share_button = driver.find_element_by_xpath("//button[@title='Share on social media']//*[name()='svg']")
    share_button.click()
    time.sleep(5)
    # Test Facebook button link
    facebook_btn = driver.find_element_by_xpath("//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[1]/div/div[2]/div[2]/div/div/div/ul/a[1]")
    assert facebook_btn.get_attribute("href") == "https://www.facebook.com/sharer.php?u=https%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt0266543%2F%3Fref_%3Dext_shr_fb"
    # Test Twitter button link
    twitter_btn = driver.find_element_by_xpath("//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[1]/div/div[2]/div[2]/div/div/div/ul/a[2]")
    assert twitter_btn.get_attribute("href") == "https://twitter.com/intent/tweet?text=Check%20out%20this%20link%20on%20IMDb!%20-%20https%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt0266543%2F%3Fref_%3Dext_shr_tw"
    # Test Email button link
    email_btn = driver.find_element_by_xpath("//*[@id='__next']/main/div/section[1]/section/div[3]/section/section/div[1]/div/div[2]/div[2]/div/div/div/ul/a[3]")
    assert email_btn.get_attribute("href") == "mailto:?subject=Check%20out%20this%20link%20on%20IMDb!&body=Check%20out%20this%20link%20on%20IMDb!%20-%20https%3A%2F%2Fwww.imdb.com%2Ftitle%2Ftt0266543%2F%3Fref_%3Dext_shr_em"