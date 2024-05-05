from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


# For Chrome
driver = webdriver.Chrome()

driver.get("https://fr.indeed.com/jobs?q=alternance+informatique&l=lyon+%2869%29&from=searchOnDesktopSerp&vjk=cd8964c8fb0cf9f4")
input("Appuyez sur Entrée pour fermer le navigateur...")

# xpath = f"//*[@id='mosaic-provider-jobcards']/ul/li[1]/div/div/div/div/div/table/tbody/tr/td/div/h2/a/span"

# element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, xpath)))
# print(element.job)

# items_count = len(driver.find_elements(By.XPATH, "//*[@id='mosaic-provider-jobcards']/ul/li"))
# print(items_count)
items = driver.find_elements(By.XPATH, "//*[@id='mosaic-provider-jobcards']/ul/li")
i=0
for item in items:
    i += 1
    xpath = f"//*[@id='mosaic-provider-jobcards']/ul/li[{i}]/div/div/div/div/div/table/tbody/tr/td/div/h2/a/span" # job title part
    target_div = item.find_element(By.XPATH, ".//div")  # Modifiez ce XPath selon le besoin spécifique
    class_attribute = target_div.get_attribute('class')
    if "mosaic-zone nonJobContent-desktop" == class_attribute:
        continue  # Passer à l'élément suivant si la classe n'est pas celle désirée
    job_element = driver.find_element(By.XPATH, xpath)
    print(job_element.text)  # Affiche le jobe trouvé
    xpath = f"//*[@id='mosaic-provider-jobcards']/ul/li[{i}]/div/div/div/div/div/table/tbody/tr/td/div[2]/div" # job title part
    Company_element = driver.find_element(By.XPATH, xpath)
    print(Company_element.text)  # Affiche le jobe trouvé
    xpath = f'//*[@id="mosaic-provider-jobcards"]/ul/li[1]/div/div/div/div/div/div[1]/div/div/span[3]' # job title part
    Company_element = driver.find_element(By.XPATH, xpath)
    print(Company_element.text)  # Affiche le jobe trouvé

