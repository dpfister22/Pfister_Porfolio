#!/usr/bin/env python3

import argparse
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

### README ###
# This script is used to replace broken images in google sheets that are used for the 
# Avrae discord bot for Dungeons and Dragons Character Sheets. A while back the images
# hosted on Imgur were deleted and resulted in a 404. This Selenium script will open
# a Firefox window and loop through the find and replace function to replace the 
# broken images with the new working ones. You will need to first set your sheet up to
# allow edit permissions to anyone with the link, this can be disabled after running 
# the script. If you would like to test this first create a copy of your sheet or use
# a copy of a genaric one I have.
#
# Test Link: https://docs.google.com/spreadsheets/d/1i1DDNa_LzHpxVHmJmv2bMQKEhdctZqMRUaL3SkKQT1g/edit?usp=drivesdk
##############

# Image Links that need to be changed:
#
# pDLyws9 > G8kk6zf
# 7QK0Di3 > 6avJSbK
# 0vzBUBN > OlUFGxq
# akCBwzl > u3YeDks
# 3HoNe7T > r6YjQVe
# uqb7XDQ > VUGDDJt
# ENNiwCO > AaGmGAX
# 10n7w9L > 2e2hhyX
# 4O5N38g > u9a6TBA
# jBL9ubu > 0VlrXCA
# chPdnlb > GFrq6pf
# xskFwrF > sMN3tei
# tw87e8J > k6zj6md
# t9i010d > pxrdqMy
# Sq1W5Ei > wJZp2Dm
# 1yaxTYB > IxRRFOd
# Ru9ghsV > RzcHHl9
#

driver = webdriver.Firefox()
action = ActionChains(driver)

# Setting up argparse for different options
parser = argparse.ArgumentParser()
parser.add_argument(
    "-s",
    "--sheet",
    dest="sheet_link",
    help="Link for a single sheet in GSheets",
    required=True,
)
args = parser.parse_args()

# List of functions to fill out what imgur urls to find
imgur_find = [
    "action.send_keys('p').key_down(Keys.SHIFT).send_keys('dl').key_up(Keys.SHIFT).send_keys('yws9.png').perform()",
    "action.send_keys('7').key_down(Keys.SHIFT).send_keys('qk').key_up(Keys.SHIFT).send_keys('0').key_down(Keys.SHIFT).send_keys('d').key_up(Keys.SHIFT).send_keys('i3.png').perform()",
    "action.send_keys('0vz').key_down(Keys.SHIFT).send_keys('bubn').key_up(Keys.SHIFT).send_keys('.png').perform()",
    "action.send_keys('ak').key_down(Keys.SHIFT).send_keys('cb').key_up(Keys.SHIFT).send_keys('wzl.png').perform()",
    "action.send_keys('3').key_down(Keys.SHIFT).send_keys('h').key_up(Keys.SHIFT).send_keys('o').key_down(Keys.SHIFT).send_keys('n').key_up(Keys.SHIFT).send_keys('e7').key_down(Keys.SHIFT).send_keys('t').key_up(Keys.SHIFT).send_keys('.png').perform()",
    "action.send_keys('uqb7').key_down(Keys.SHIFT).send_keys('xdq').key_up(Keys.SHIFT).send_keys('.png').perform()",
    "action.key_down(Keys.SHIFT).send_keys('enn').key_up(Keys.SHIFT).send_keys('iw').key_down(Keys.SHIFT).send_keys('co').key_up(Keys.SHIFT).send_keys('.png').perform()",
    "action.send_keys('10n7w9').key_down(Keys.SHIFT).send_keys('l').key_up(Keys.SHIFT).send_keys('.png').perform()",
    "action.send_keys('4').key_down(Keys.SHIFT).send_keys('o').key_up(Keys.SHIFT).send_keys('5').key_down(Keys.SHIFT).send_keys('n').key_up(Keys.SHIFT).send_keys('38g.png').perform()",
    "action.send_keys('j').key_down(Keys.SHIFT).send_keys('bl').key_up(Keys.SHIFT).send_keys('9ubu.png').perform()",
    "action.send_keys('ch').key_down(Keys.SHIFT).send_keys('p').key_up(Keys.SHIFT).send_keys('dnlb.png').perform()",
    "action.send_keys('xsk').key_down(Keys.SHIFT).send_keys('f').key_up(Keys.SHIFT).send_keys('wr').key_down(Keys.SHIFT).send_keys('f').key_up(Keys.SHIFT).send_keys('.png').perform()",
    "action.send_keys('tw87e8').key_down(Keys.SHIFT).send_keys('j').key_up(Keys.SHIFT).send_keys('.png').perform()",
    "action.send_keys('t9i010d.png').perform()",
    "action.key_down(Keys.SHIFT).send_keys('s').key_up(Keys.SHIFT).send_keys('q1').key_down(Keys.SHIFT).send_keys('w').key_up(Keys.SHIFT).send_keys('5').key_down(Keys.SHIFT).send_keys('e').key_up(Keys.SHIFT).send_keys('i.png').perform()",
    "action.send_keys('1yax').key_down(Keys.SHIFT).send_keys('TYB').key_up(Keys.SHIFT).send_keys('.png').perform()",
    "action.key_down(Keys.SHIFT).send_keys('r').key_up(Keys.SHIFT).send_keys('u9ghs').key_down(Keys.SHIFT).send_keys('v').key_up(Keys.SHIFT).send_keys('.png').perform()",
]

# List of functions to fill out what imgur urls to replace
imgur_replace = [
    "action.key_down(Keys.SHIFT).send_keys('g').key_up(Keys.SHIFT).send_keys('8kk6zf.png').perform()",
    "action.send_keys('6av').key_down(Keys.SHIFT).send_keys('js').key_up(Keys.SHIFT).send_keys('b').key_down(Keys.SHIFT).send_keys('k').key_up(Keys.SHIFT).send_keys('.png').perform()",
    "action.key_down(Keys.SHIFT).send_keys('o').key_up(Keys.SHIFT).send_keys('l').key_down(Keys.SHIFT).send_keys('ufg').key_up(Keys.SHIFT).send_keys('xq.png').perform()",
    "action.send_keys('u3').key_down(Keys.SHIFT).send_keys('y').key_up(Keys.SHIFT).send_keys('e').key_down(Keys.SHIFT).send_keys('d').key_up(Keys.SHIFT).send_keys('ks.png').perform()",
    "action.send_keys('r6').key_down(Keys.SHIFT).send_keys('y').key_up(Keys.SHIFT).send_keys('j').key_down(Keys.SHIFT).send_keys('qv').key_up(Keys.SHIFT).send_keys('e.png').perform()",
    "action.key_down(Keys.SHIFT).send_keys('vugddj').key_up(Keys.SHIFT).send_keys('t.png').perform()",
    "action.key_down(Keys.SHIFT).send_keys('a').key_up(Keys.SHIFT).send_keys('a').key_down(Keys.SHIFT).send_keys('g').key_up(Keys.SHIFT).send_keys('m').key_down(Keys.SHIFT).send_keys('gax').key_up(Keys.SHIFT).send_keys('.png').perform()",
    "action.send_keys('2e2hhy').key_down(Keys.SHIFT).send_keys('x').key_up(Keys.SHIFT).send_keys('.png').perform()",
    "action.send_keys('u9a6').key_down(Keys.SHIFT).send_keys('tba').key_up(Keys.SHIFT).send_keys('.png').perform()",
    "action.send_keys('0').key_down(Keys.SHIFT).send_keys('v').key_up(Keys.SHIFT).send_keys('lr').key_down(Keys.SHIFT).send_keys('xca').key_up(Keys.SHIFT).send_keys('.png').perform()",
    "action.key_down(Keys.SHIFT).send_keys('gf').key_up(Keys.SHIFT).send_keys('rq6pf.png').perform()",
    "action.send_keys('s').key_down(Keys.SHIFT).send_keys('mn').key_up(Keys.SHIFT).send_keys('3tei.png').perform()",
    "action.send_keys('k6zj6md.png').perform()",
    "action.send_keys('pxrdq').key_down(Keys.SHIFT).send_keys('m').key_up(Keys.SHIFT).send_keys('y.png').perform()",
    "action.send_keys('w').key_down(Keys.SHIFT).send_keys('jz').key_up(Keys.SHIFT).send_keys('p2').key_down(Keys.SHIFT).send_keys('d').key_up(Keys.SHIFT).send_keys('m.png').perform()",
    "action.key_down(Keys.SHIFT).send_keys('i').key_up(Keys.SHIFT).send_keys('x').key_down(Keys.SHIFT).send_keys('rrfo').key_up(Keys.SHIFT).send_keys('d.png').perform()",
    "action.key_down(Keys.SHIFT).send_keys('r').key_up(Keys.SHIFT).send_keys('zc').key_down(Keys.SHIFT).send_keys('hh').key_up(Keys.SHIFT).send_keys('l9.png').perform()",
]


def open_browser(driver):
    driver.get(args.sheet_link)
    assert "Google Sheets" in driver.title
    time.sleep(5)


def find_and_replace(driver, action):
    for f, r in zip(imgur_find, imgur_replace):
        action = ActionChains(driver)
        action.key_down(Keys.CONTROL).send_keys("h").key_up(Keys.CONTROL).perform()
        time.sleep(2)
        # Instering info find box
        eval(f), print("Pasting Find Value") and time.sleep(1)
        action.send_keys(Keys.TAB).perform()
        # Instering into replace box
        eval(r), print("Pasting Replace Value") and time.sleep(1)
        # Click correct option boxes
        print("\nSelecting Options")
        driver.find_element(
            By.CSS_SELECTOR, "div.waffle-find-replace-option:nth-child(4)"
        ).click()
        driver.find_element(
            By.CSS_SELECTOR, "div.waffle-find-replace-option:nth-child(5)"
        ).click()
        driver.find_element(By.NAME, "findNext").click(), print("Finding") 
            and time.sleep(1)
        driver.find_element(By.NAME, "replaceAll").click(), print("Replacing") 
            and time.sleep(3)
        # Confirming actions
        driver.find_element(
            By.XPATH, '//button[@class="goog-buttonset-default goog-buttonset-action"]'
        ).click(), time.sleep(2)
        driver.find_element(By.NAME, "done").click()
    driver.close()
    print("\ncomplete")


def main():
    open_browser(driver)
    find_and_replace(driver, action)


if __name__ == "__main__":
    main()
