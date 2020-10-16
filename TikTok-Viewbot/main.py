import os

from selenium import webdriver, common

os.system('cls && title [TikTok Automated Viewbot]')
VIDEO_URL = input('[>] TikTok Video URL: ')

views_sent = 0
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])  # Disables logging


def beautify(arg):
    # Adds a "thousands separator" — for readability purposes.
    return format(arg, ',d').replace(',', '.')


driver = webdriver.Chrome(options=options)
driver.set_window_size(800, 660)
driver.get('https://vipto.de/')
print('[!] Solve the captcha...')
captcha = True

while captcha:
    # Attempts to select the "Views" option.
    try:
        driver.find_element_by_xpath(
            '/html/body/div[4]/div[1]/div[3]/div/div[4]/div/button'
        ).click()
    except (
        common.exceptions.NoSuchElementException,
        common.exceptions.ElementClickInterceptedException
    ):
        continue
    driver.set_window_position(-10000, 0)
    print('[!] Running...')
    captcha = False

# Pastes the URL into the "Enter URL" textbox.
driver.find_element_by_xpath(
    '/html/body/div[4]/div[4]/div/div/div/form/div/input'
).send_keys(VIDEO_URL)

while True:
    os.system(
        f'title [TikTok Automated Viewbot] - Views Sent: {beautify(views_sent)} ^| Sending...'
    )
    waiting = True

    while waiting:
        # Clicks the "Search" button.
        driver.find_element_by_xpath(
            '/html/body/div[4]/div[4]/div/div/div/form/div/div/button'
        ).click()
        os.system('TIMEOUT 2 >NUL')

        try:
            # Clicks the "Send Views" button.
            driver.find_element_by_xpath(
                '/html/body/div[4]/div[4]/div/div/div/div/div[1]/div/form/button'
            ).click()
        except (
            common.exceptions.NoSuchElementException,
            common.exceptions.ElementNotInteractableException
        ):
            continue
        else:
            views_sent += 1000
            os.system(f'title [TikTok Automated Viewbot] - Views Sent: {beautify(views_sent)}')
            waiting = False
