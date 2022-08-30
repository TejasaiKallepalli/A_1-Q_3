sisters_tuple=("charishmasai","Nikhitha","chandana") #Creating a tuple
print(sisters_tuple)
brothers_tuple=("Jeevan","Harsha","Sandy","Sreekanth") #Creating a tuple
print(brothers_tuple)
sibblings_tuple=sisters_tuple+brothers_tuple  #joining sister_tuple and brother_tuple using addition operator
print(sibblings_tuple)
print("No:- of sibblings :",+len(sibblings_tuple)) #finding the length of the tuple using len() method
sibblings_tuple+=("KNVD","Bala") #appending tuple with father name and mother name
print(sibblings_tuple)
family_members=sibblings_tuple #modifying sibblings_tuple to Family_members
print(family_members)