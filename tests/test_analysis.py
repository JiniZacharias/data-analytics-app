from src.analysis import run_analysis

def test_run_analysis():
    results = run_analysis()
    assert 'mean' in results
    assert results['mean'] > 0

from selenium import webdriver

def test_homepage():
    driver = webdriver.Chrome()
    driver.get("http://localhost:5000")
    assert "Mean Value" in driver.page_source
    driver.quit()
