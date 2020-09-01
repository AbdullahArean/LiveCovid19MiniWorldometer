from bs4 import BeautifulSoup as soup
import urllib.request, urllib.parse, urllib.error
import re
import json
main_url = 'https://www.worldometers.info/coronavirus/country/'
main_url2 = 'https://www.worldometers.info/coronavirus/#countries'

continents = [ 'Europe', 'North America', 'Asia', 'South America', 'Africa', 'Oceania']


def word_to_alphabet_list(word):
		alpha_list=[]
		word=word.lower()
		for alpha in word:
			alpha_list.append(alpha)
		return alpha_list 
def match_number_checker(comparing_word,user_given_word):
	count=0
	n=0
	alpha_list= word_to_alphabet_list(comparing_word)
	word_list= word_to_alphabet_list(user_given_word)
	while n<len(alpha_list) and n<len(word_list):
		if alpha_list[n] == word_list[n]:
				count+=2
		if n+1< len(word_list):
			if alpha_list[n] == word_list[n+1]:
					count+=1
		if n+1< len(alpha_list):
			if alpha_list[n+1] == word_list[n]:
					count+=1
		if len(word_list)>=3:
			if alpha_list[:3]==word_list[:3]:
				count+=5
		n+=1

	return count
def output_refiner(usinp, valid_list):
	desout=None #our desired output which will match with district_name_key
	hmatch=None #highest match
	
	#start of loop, we iterate in between all the elements of Districtlist to find desired output in basis of highest match
	for item in valid_list: 
		match=match_number_checker(item, usinp)
		
		
		#initial_case
		if hmatch==None:
			hmatch= match
			desout= item
		#if more match found it will be our desired word
		
		if hmatch< match:
			hmatch= match
			desout=item
	return(desout)#returning our desired output
	
countries = ['us', 'russia', 'brazil', 'spain', 'uk', 'italy', 'france', 'germany', 'turkey', 'iran', 'india', 'peru', 'canada', 'saudi-arabia', 'mexico', 'chile', 'belgium', 'pakistan', 'netherlands', 'qatar', 'ecuador', 'belarus', 'sweden', 'switzerland', 'singapore', 'bangladesh', 'portugal', 'united-arab-emirates', 'ireland', 'indonesia', 'poland', 'ukraine', 'kuwait', 'south-africa', 'colombia', 'romania', 'israel', 'austria', 'japan', 'egypt', 'dominican-republic', 'philippines', 'denmark', 'south-korea', 'serbia', 'panama', 'argentina', 'afghanistan', 'czech-republic', 'norway', 'bahrain', 'algeria', 'kazakhstan', 'morocco', 'malaysia', 'australia', 'nigeria', 'oman', 'moldova', 'finland', 'ghana', 'armenia', 'bolivia', 'cameroon', 'luxembourg', 'iraq', 'azerbaijan', 'hungary', 'honduras', 'sudan', 'guinea', 'thailand', 'uzbekistan', 'senegal', 'greece', 'guatemala', 'bosnia-and-herzegovina', 'bulgaria', 'tajikistan', 'cote-d-ivoire', 'croatia', 'djibouti', 'cuba', 'macedonia', 'democratic-republic-of-the-congo', 'estonia', 'iceland', 'el-salvador', 'lithuania', 'somalia', 'gabon', 'new-zealand', 'slovakia', 'mayotte', 'slovenia', 'kyrgyzstan', 'maldives', 'kenya', 'guinea-bissau', 'china-hong-kong-sar', 'sri-lanka', 'tunisia', 'latvia', 'lebanon', 'albania', 'mali', 'niger', 'cyprus', 'costa-rica', 'equatorial-guinea', 'venezuela', 'zambia', 'paraguay', 'burkina-faso', 'andorra', 'uruguay', 'haiti', 'georgia', 'jordan', 'san-marino', 'malta', 'chad', 'sierra-leone', 'channel-islands', 'jamaica', 'tanzania', 'nepal', 'south-sudan', 'congo', 'reunion', 'taiwan', 'central-african-republic', 'ethiopia', 'state-of-palestine', 'madagascar', 'cabo-verde', 'togo', 'isle-of-man', 'mauritius', 'montenegro', 'viet-nam', 'rwanda', 'nicaragua', 'sao-tome-and-principe', 'french-guiana', 'liberia', 'swaziland', 'myanmar', 'yemen', 'martinique', 'faeroe-islands', 'mauritania', 'mozambique', 'uganda', 'guadeloupe', 'gibraltar', 'brunei-darussalam', 'mongolia', 'benin', 'guyana', 'bermuda', 'cambodia', 'cayman-islands', 'trinidad-and-tobago', 'aruba', 'bahamas', 'monaco', 'barbados', 'liechtenstein', 'sint-maarten', 'malawi', 'libya', 'french-polynesia', 'angola', 'syria', 'zimbabwe', 'china-macao-sar', 'burundi', 'saint-martin', 'eritrea', 'comoros', 'botswana', 'antigua-and-barbuda', 'gambia', 'timor-leste', 'grenada', 'bhutan', 'laos', 'namibia', 'belize', 'fiji', 'new-caledonia', 'saint-lucia', 'saint-vincent-and-the-grenadines', 'curacao', 'dominica', 'saint-kitts-and-nevis', 'falkland-islands-malvinas', 'turks-and-caicos-islands', 'holy-see', 'montserrat', 'suriname', 'greenland', 'seychelles', 'british-virgin-islands', 'papua-new-guinea', 'caribbean-netherlands', 'saint-barthelemy', 'western-sahara', 'anguilla', 'lesotho', 'saint-pierre-and-miquelon', 'china']
continents = [ 'Europe', 'North America', 'Asia', 'South America', 'Africa', 'Oceania']
District = [
    'Brahamanbaria', 'Barguna', 'Bogra', 'Chuadanga', 'Dhaka', 'Dinajpur',
    'Feni', 'Gaibandha', 'Gazipur', 'Habiganj', 'Jessore', 'Jhalokati',
    'Jhenaidah', 'Joypurhat', 'Kushtia', 'Lakshmipur', 'Madaripur', 'Magura',
    'Manikganj', 'Meherpur', 'Munshiganj', 'Naogaon', 'Narayanganj',
    'Narsingdi', 'Natore', 'Nawabganj', 'Nilphamari', 'Panchagarh', 'Rajbari',
    'Rangamati', 'Rangpur', 'Shariatpur', 'Sherpur', 'Sirajganj', 'Sylhet',
    'Bandarban', 'Comilla', 'Netrakona', 'Thakurgaon', 'Bagerhat',
    'Kishoreganj', 'Barisal', 'Chittagong', 'Bhola', 'Chandpur', "Cox's Bazar",
    'Faridpur', 'Gopalganj', 'Jamalpur', 'Khagrachhari', 'Khulna', 'Narail',
    'Kurigram', 'Maulvibazar', 'Lalmonirhat', 'Mymensingh', 'Noakhali',
    'Pabna', 'Tangail', 'Patuakhali', 'Pirojpur', 'Rajshahi', 'Satkhira',
	    'Sunamganj']




#this fuction make soup of the html code for navigaiting at ease
def url_address(url):
	#next 6 lines helps this code to pretend myself as a fake browser.....
	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

	#url = "https://www.worldometers.info/coronavirus/country/bangladesh/"
	headers = {
	    'User-Agent': user_agent,
	}

	request = urllib.request.Request(url, None,
	                                 headers)  #The assembled request
	response = urllib.request.urlopen(request)
	data = response.read()  # The data u need
	#6 lines ends here

	bsoup = soup(data, "html.parser")

	return bsoup
a="*"
print(a*100)
print("Welcome To Live Covid-19 Mini Worldometer")
print(a*100)
print("Gathering Data......")
info=url_address('https://www.worldometers.info/coronavirus/#country')
print("Data Successfully Gathered:)")
def worldreport():

	print("World Report")

	main_url = 'https://www.worldometers.info/coronavirus/#country'


#Getting Full world status


	container4 =info.findAll("div", {"class": "content-inner"})

	#Shows total cases ....
	level = 0
	for item in container4[0].findAll("span"):
		level += 1
		
		if level == 1:
			total_cases = item.text
		elif level == 2:
			total_deaths = item.text
			
		elif level == 3:
			total_recovered = item.text
		else:
			break
	
	print("Total cases:", total_cases)
	print("Total Deaths:", total_deaths)
	print("Total Recovered:", total_recovered)

	print("\n")
#End of whole world news

def connection(url):

	print(
	    "Data is being updated.....")  #Giving User hint that work is on the go
	#Accessing data from URL and opening it in a handle file in our device
	urlhandle = urllib.request.urlopen(url)

	#Retrieving data from URLAHANDLE and decoding it
	retrieved_data = urlhandle.read().decode()

	#Loading all the retrieved data in a JSON file to easily access
	#Another reason of loadng as JSON file is that data was in JSON format in API
	json_file = json.loads(retrieved_data)

	return json_file  #Returning Function value the JSON data retrieved from URL


#End of Connection Function

def continentreport(cname):
	print(a*100)
		#shows continent based cases......
	user_inp= output_refiner(cname,continents)
	print("Loading Data of",user_inp)
	

	container2 = info.findAll("tbody")

	continent_total_cases = list()
	continent_total_death = list()

	for item in container2[0].findAll(
		    "tr", {"class": "total_row_world row_continent"}):
		x = item.text
		total_case = re.findall(r'\S+\d', x)
		
		continent_total_cases.append(total_case[0])
		continent_total_death.append(total_case[2])
		
	index = continents.index(user_inp)
	print("Total cases in", user_inp, "is",
			      continent_total_cases[index])
	print("Total death cases in", user_inp, "is",
			      continent_total_death[index])
	print("\n")




def countryreport(iname):
	name= output_refiner(iname,countries)
	print("Gather COVID-19 status upadate of",name)
	print("Gathering Data")
	main_url_C= 'https://www.worldometers.info/coronavirus/country/'+ name
	infoc= url_address(main_url_C)
	print("Data Successfully Gathered")
	container4 = infoc.findAll("div" , {"class": "content-inner"})
	level = 0
	for item in container4[0].findAll("span"):
		level += 1
		if level == 1:
			total_cases = item.text
		elif level == 2:
			total_deaths = item.text
		elif level == 3:
			total_recovered = item.text
			break

			
	print("Total cases:", total_cases)
	print("Total Deaths:", total_deaths)
	print("Total Recovered:", total_recovered)
			
	print('\n')
	container3 = infoc.findAll("div", {"id": "news_block"})
	print("Updated data of last 7 days in",name, end='\n')
	for item in container3[0].findAll("li", {"class": "news_li"}):
		data = item.text
		for i in range(0, len(data), 1):
			if data[i] != '[':
				print(data[i], end='')
			else:
				break

		print(end='\n')
def districtrepot(iname):
	district_name = output_refiner(iname,District)

	#Government Provided Official district data provider API
	url_district_data = 'http://covid19tracker.gov.bd/api/district'
	#Displaying User the thing that search is on the go
	print("Searching For Data of", district_name, "District....")

	#Giving the URL in Function getting back the JSON file retrieved from the API
	json_district_data = connection(url_district_data)

	#Retrieving info of all the disrict
	many_districts_info = json_district_data["features"]

	#looping in all the district to find the desired district
	for one_district_info in many_districts_info:

		#Retrieving District name key to check if it is the desired district
		district_name_key = one_district_info["properties"]["key"]

		#If we founnd the desired district name in retrieved district name key, then we will print the data
		if district_name_key == district_name:

			#if condition fullfill we will get confirmed cases number
			district_confirmed_cases = one_district_info["properties"][
			    "confirmed"]

			#Giving confirmed case of desired district as  User Output
			print("Confirmed Cases in", district_name, "so far is",
			      district_confirmed_cases)
		#End of Condition

		else:  #if not found do the loop again
			continue
	#End of loop of finding desired district data


#End of district latest updater function
		
while True:
	print(a*100)
	print("Please Select From Program Menu")
	print("1. World COVID-19 Status update")
	print("2. Continent wise COVID-19 Status update")
	print("3. Country wise Status COVID-19 Update")
	print("4. District wise Data of Bangladesh")
	print("5. Exit")
	inp = int(input("Give input (1/2/3/4/5) to access COVID-19 status update accordingly\n"))

	if inp== 1:
		worldreport()

		
	elif inp==2:
		cont=input("Please Enter Continent Name, You can enter wrong or word, program will fix that :)\n")
		continentreport(cont)
	
	
	elif inp==3:
		b=input("Please Enter country Name, You can enter wrong or word, program will fix that :)\n")
		countryreport(b)

	elif inp==4:
		dis=input("Please Enter District Name of Bangladesh, You can enter wrong or word, program will fix that :)\n")
		districtrepot(dis)
	else:
		break

#last statement of program
print(a*60+'Thanks For Being With Us'+a*36+'Developed by : AIH Technologies'+a*20+' Coded by: AREAN '+a*20)
#finish of program "
		
