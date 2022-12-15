from seleniumbase import BaseCase
import cv2
import time
import chromedriver_binary


class ComponentsTest(BaseCase):
    def test_basic(self):
        # open the app and take a screenshot
        self.open("http://localhost:8501")
        time.sleep(10)
        self.save_screenshot("current-screenshot.png")