from time import sleep
try:
    from selenium import webdriver
except ImportError as error:
    print(str(error) + ", Check next link: https://selenium-python.readthedocs.io/installation.html")



def selenium_automation():
    randomtodo = "https://randomtodolistgenerator.herokuapp.com/library"
    todoist = "https://todoist.com/users/showlogin"

    driver = webdriver.Firefox()
    driver.get(randomtodo)

    # Find all containers with task
    containers = driver.find_elements_by_xpath(".//*[@class='card-body']")
    task_list = []
    for tasks in containers:
        task = tasks.find_element_by_xpath(
            './/div[@class="flexbox task-title"]')
        task_list.append(str(task.text).split('\n')[0])

    if len(task_list) == 6:
        task_list.pop()

    sleep(1)

    driver.get(todoist)

    # Find login input's
    username = driver.find_element_by_id("email")
    password = driver.find_element_by_id("password")

    # Set email and password
    username.send_keys("selenium-test@mozej.com")
    password.send_keys("password")

    # Click button
    btn = driver.find_element_by_xpath(
        "//*[@class='submit_btn ist_button ist_button_red sel_login']")
    btn.click()

    # Wait until page load
    sleep(5)

    # Try to remove alert timezone
    try:
        time_zone = driver.find_element_by_xpath(
            "//*[@class='timezone_link timezone_link_block']")
        time_zone.click()
    except:
        pass

    # Click btn add task
    new_task = driver.find_element_by_xpath(
        ".//*[@class='plus_add_button']")
    new_task.click()

    # For very task in task_list add new task
    for post_task in task_list:

        # repeat n times
        write = driver.find_element_by_xpath(
            ".//*[@class='notranslate public-DraftEditor-content']")
        write.send_keys(post_task)

        bnt_add_task = driver.find_element_by_xpath(
            ".//*[@class='ist_button ist_button_red']")
        sleep(.5)
        bnt_add_task.click()

    # driver.quit()


selenium_automation()
