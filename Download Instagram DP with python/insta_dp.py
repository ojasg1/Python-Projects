'''Download Instagram Display picture with python '''


import instaloader

#create an instance
test = instaloader.Instaloader()

#fetch the account details
acc = input('Enter the Account Username: ')

#download the profile pic
test.download_profile(acc, profile_pic_only = True) 
