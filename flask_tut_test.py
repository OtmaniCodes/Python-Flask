# import requests

# host =  'http://127.0.0.1:5000/'

# def get_data(id):
# 	url = host + f'video/{id}'
# 	try:
# 		response = requests.get(url)
# 		print(response.status_code)
# 		print(response.text)
# 	except(e):
# 		print(f'error: {e}') 
	

# def put_data(id):
# 	url = host + f'video/{id}'
# 	try:
# 		response = requests.put(url, {'name': 'video_01', 'views':22, 'likes':10})
# 		print(response.status_code)
# 		print(response.text)
# 	except(e):
# 		print(f'error: {e}') 
	

# def delete_data(id):
# 	url = host + f'video/{id}'
# 	try:
# 		response = requests.delete(url)
# 		print(response.status_code)
# 		print(response.text)
# 	except(e):
# 		print(f'error: {e}') 


# def post_data(id):
# 	url = host + f'video/{id}'
# 	response = requests.post(url)

# 	print(response.status_code)
# 	print(response.json)
# 	print(response.text)

# def update_data(id):
# 	url = host + f'video/{id}'
# 	response = requests.patch(url, {'likes':2929})

# 	print(response.status_code)
# 	print(response.json)
# 	print(response.text)

# # put_data(1) 
# get_data(1)
# get_data(4)
# update_data(1)
# update_data(7)

# # post_data()





import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.exists(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename, 'w') as file:
    pass

  # # Return the list of files in the new directory
  return os.listdir(os.getcwd())
  # return os.getcwd()

print(new_directory("PythonPrograms", "script.py"))


