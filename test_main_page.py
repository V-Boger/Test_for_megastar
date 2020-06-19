from .pages.main_page import MainPage

def test_first(browser):
    link = "https://itmegastar.com/"
    page = MainPage(browser, link)  
    page.open()                      
    page.test1()          
def test_second(browser):
    link = "https://itmegastar.com/"
    page = MainPage(browser, link)   
    page.open()                     
    page.test2()          
		