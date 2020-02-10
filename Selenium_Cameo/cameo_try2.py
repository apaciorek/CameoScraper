from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import selenium.webdriver.support.ui as ui
from time import sleep
import re
import csv




driver = webdriver.Chrome()

actions = ActionChains(driver)

driver.get("https://www.cameo.com/c/featured")

# cam_talents = driver.find_elements_by_xpath('//div[@class="XPdBo9MAZefkKbmAjpa86"]')
# print(len(cam_talents))



# res = [ cam_talents[0], cam_talents[-1] ]  
  
# # printing result 
# print ("The first and last element of list are : " +  str(res)) 
# print(len(cam_talents))


# for talent in cam_talents:
#      # name = talent.find_element_by_xpath('.//a[@class="_3z47DGIMGOtJrGd4zWYwcE"]').text
#      pricetags = talent.find_elements_by_xpath('//span[@class="_1Vx1MsN7oW62rZaRzXTdpo"]')
#      for pricetag in cam_talents:
#          price = pricetag.find_element_by_xpath('./span').text
#      # print('Talent = {}'.format(name))

# for talent in cam_talents:
#      for pricetag in pricetags:
#          name = talent.find_element_by_xpath('.//a[@class="_3z47DGIMGOtJrGd4zWYwcE"]').text
#          price = pricetag.find_element_by_xpath('./span').text
#          print('Talent = {}'.format(name), 'Price = {}'.format(price))

# index = 1

# while index <= 3:
#     try:
#         print("Scraping Celebrity" + str(index))
#         index = index +1
#         talent_buttons = driver.find_elements_by_xpath('//div[@class="_3yEJGdKwGboMQH4nTumQvk"]')
#Actions newTab = new Actions(driver); 
# main_window = driver.current_window_handle   
# talent_buttons = driver.find_elements_by_xpath('//div[@class="_1lesImzbM1n7vM34r-I6Fz"]')
# print(len(talent_buttons))
# print(len(talent_buttons[:3]))
# print(talent_buttons[:3])
category_links = driver.find_elements_by_xpath('//a[@class="_2UVgbrIGQxRzzAieNCcwdQ"]')
category_urls = []
for link in category_links:
     category_url = link.get_attribute("href")
     category_urls.append(category_url)
#print(category_urls)

talent_urls = []

for url in category_urls:
     driver.get(url)
     sleep(2)
     talent_links = driver.find_elements_by_xpath('//div[@class="_3yEJGdKwGboMQH4nTumQvk"]')
     #talent_urls = []

     for link in talent_links:
         talent_url = link.find_element_by_tag_name('a').get_attribute("href")
         talent_urls.append(talent_url)

print(len(talent_urls))

csv_file = open('talent_data.csv', 'w', encoding='utf-8', newline='')
writer = csv.writer(csv_file)


for url in talent_urls:
     talent_dict = {}
     driver.get(url)
     sleep(1)
     try:
         talent_name = driver.find_element_by_xpath('//h1[@id="profile-bio-name"]').text
     except:
         print(f'Couldn\'t get name!')
         talent_name = "999"
     try:
         talent_price = driver.find_element_by_xpath('//a[@id="bookLink"]').text
     except:
         print(f'Couldn\'t get price!')
         talent_price = "999"
     try:
         talent_profession = driver.find_element_by_xpath('//span[@id="profile-bio-profession"]').text
     except:
         print(f'Couldn\'t get profession!')
         talent_profession = "999"
     try:
         times = driver.find_element_by_xpath('//p[@class="gvgJ2l-Qvsw_Lli17CHba"]')
         r_time = times.find_element_by_tag_name('b').text
         #response_time = driver.find_element_by_tag_name('b').text
     except:
         print(f'Couldn\'t get response time!')
         r_time = "999"
     try:
         review_info = driver.find_element_by_xpath('//div[@id="profile-ratings"]')
         num_reviews = review_info.find_element_by_tag_name('b').text
     except:
         print(f'Couldn\'t get reviews!')
         num_reviews = "999"
     try:
         talent_rating = driver.find_element_by_xpath('//h5[@class="_3f6X2oCJ0q5_HCpRbtxAsh"]').text
     except:
         print(f'Couldn\'t get rating!')
         talent_rating = "999"
     try:
         talent_classification = driver.find_elements_by_xpath('//a[@class="_2UVgbrIGQxRzzAieNCcwdQ"]')
         classifications = []
         for thing in talent_classification:
             classification = thing.get_attribute("href")
             classifications.append(classification)
     except: 
         print(f'Couldn\'t get categories!')
         classifications = "999"

     #classes = talent_classification.find_elements_by_tag_name('a').get_attribute("href")
     # try:
     #     print('Talent = {}'.format(talent_name),
     #        'Price = {}'.format(talent_price),
     #        'Profession: {}'.format(talent_profession),
     #        'Typically responds in {}'.format(r_time),
     #        'Number of Reviews = {}'.format(num_reviews),
     #        'Rating = {}'.format(talent_rating),
     #        'Classes = {}'.format(classifications))
     # except:
     #     continue

     talent_dict['Name'] = talent_name
     talent_dict['Price'] = talent_price
     talent_dict['Profession'] = talent_profession
     talent_dict['ResponseTime'] = r_time
     talent_dict['Reviews'] = num_reviews
     talent_dict['Rating'] = talent_rating
     talent_dict['Categories'] = classifications

     writer.writerow(talent_dict.values())
     
     #print('Talent URL = {}'.format(talent_url))


csv_file.close()
driver.close()

#print(talent_urls)






# # I have buttons to click on that take me to every celebrity's page
# for talent_button in talent_buttons[:4]:

#     # click the button and open the link in a new tab
#      actions.key_down(Keys.COMMAND).click(talent_button).key_up(Keys.COMMAND).perform()
#      #driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + Keys.TAB)

#      # focus the driver onto the newly opened tab
#      driver.switch_to.window(driver.window_handles[1])

#      # let the page load, retrieve information about the celebrity from the page      
#      sleep(2)
#      talent_name = driver.find_element_by_xpath('//h1[@id="profile-bio-name"]').text
#      print('Talent = {}'.format(talent_name))

#      # close the tab
#      driver.close()

#      #return back to window of all the celebrities
#      driver.switch_to.window(main_window)
     


#     #talent_dict = {}
#     #try:
       
#         price = talent.find_element_by_xpath('.//span[@class="_1Vx1MsN7oW62rZaRzXTdpo"]/span').text
    # except:
    #     continue

    #, 'Price = {}'.format(price))
  #  class="XPdBo9MAZefkKbmAjpa86"

# print(len(cam_talents))
# for talent in cam_talents: 
     
# print(len(pricetags))


# print('Price = {}'.format(price))





