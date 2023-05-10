from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Edge(service=EdgeService(executable_path="F:/django-apps/tdd/"))

driver.get('http://localhost:8000')

assert 'Django' in driver.title
