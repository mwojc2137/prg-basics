facebook = True

twitter = False

instagram = True

good_influencer = False

if facebook == True:
    if twitter == True or instagram == True:
        good_influencer = True
elif twitter == True and instagram == True:
    good_influencer == True

if good_influencer == True:
    print("You are a good influencer!")
else:
    print("no.")

