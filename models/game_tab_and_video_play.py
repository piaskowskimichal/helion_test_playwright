from utils.pages_url import main_page
from playwright.sync_api import expect

class GameTabAndVideoPlay:
    def __init__(self,page):
        self.page=page

    def navigate(self):
        self.page.goto(main_page)   

    def confirm_cookies(self):
        confirm=self.page.locator('text=Rozumiem')   
        confirm.click()

    def game_tab_click(self):
        game_tab=self.page.locator('text=Gry').first   
        game_tab.click()

    def unity_tab_click(self):
        unity_tab=self.page.locator("[id=\"gry\\/unity\"]")
        unity_tab.click()

    def book_select_click(self):
        book_select=self.page.locator("text=Praktyczny kurs programowania C# w Unity. Kurs video. Poziom podstawowy >> nth=1")
        book_select.click()

    def play_video_click(self):
        play_video=self.page.locator('a:has-text("Play")').first
        expect(play_video).to_be_enabled()
        play_video.click() 