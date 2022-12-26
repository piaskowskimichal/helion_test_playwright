import sys
sys.path.append('.')
from utils.pages_url import main_page
from models.game_tab_and_video_play import GameTabAndVideoPlay
from playwright.sync_api import Playwright,Page

def test_game_tab_and_video_play(page: Page):

    test_game_tab_and_video_play=GameTabAndVideoPlay(page)
    test_game_tab_and_video_play.navigate()
    test_game_tab_and_video_play.confirm_cookies()
    test_game_tab_and_video_play.game_tab_click()
    test_game_tab_and_video_play.unity_tab_click()
    test_game_tab_and_video_play.book_select_click()
    test_game_tab_and_video_play.play_video_click()
    


