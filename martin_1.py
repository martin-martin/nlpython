# Problem: Try to cap elements in the list. 

hiking = ["devil's den", "old lady", "north rim", "where angel's fly"]
print(hiking)
hiking.append("martin's trail")
#print(hiking)
#import string
#hiking_capped = ", ".join(hiking)
#string.capwords(hiking_capped)
#print(string.capwords(hiking_capped))



#for trail in hiking:
	#cap_trail = trail.title()
	#if "Devil'S Den" in cap_trail:
			#cap_trail = "Devil's Den"
	
	#print(cap_trail)
hiking_string = ", ".join(hiking)
capped_hiking = hiking_string.title()
print (capped_hiking.replace('S', 's'))


	




	