from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

# Setup driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# 1- Se connecter au site : https://videotron.com/
driver.get("https://videotron.com/")
# Attendre 10 seconds quand le logo est disponible, ca veut dire l'url est ouverte
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "bf-logo")))
# 2- Trouver le nombre d’images sur le site et l’afficher dans la console de votre éditeur de code.
images = driver.find_elements(By.TAG_NAME, "img")
nb_images = len(images)
print("Nombre d'images sur le site :", nb_images)
print("==============")
# 3- Afficher la valeur de l’attribut « alt » des images du site dans la console.
for image in images:
    alt_text = image.get_attribute("alt")
    print("Attribut 'alt' de l'image :", alt_text)
print("==============")

# 4- Trouver le nombre de liens sur le site et l’afficher dans la console.
links = driver.find_elements(By.TAG_NAME, "a")
nb_links = len(links)
print("Nombre de liens sur le site :", nb_links)
print("==============")

# 5- Trouver le nombre de liens dans la section « footer » du site et l’afficher dans la console.
footer = driver.find_element(By.CLASS_NAME, "videotron-ui__main-footer")
footer_links = footer.find_elements(By.TAG_NAME, "a")
nb_footer_links = len(footer_links)
print("Nombre de liens dans la section 'footer' :", nb_footer_links)
print("==============")

# 6- Récupérer la valeur de l’attribut « hrf » de chaque lien dans la section « footer » du site et l’afficher dans la console.
for link in footer_links:
    href = link.get_attribute("href")
    print("Attribut 'href' du lien dans la section 'footer' :", href)

# Fermer le navigateur
driver.quit()