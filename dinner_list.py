dinner_list = ['ed', 'julz', 'mom']
message = f"Invitation to dinner list\n {dinner_list[0].title()},\n {dinner_list[1].title()},\n {dinner_list[2].title()}"
print(message)
j = 'julz'
dinner_list.remove(j)
dinner_list.insert(1, 'carissa')
message1 = f"Invitation to dinner updates {dinner_list[0].title()}, {dinner_list[1].title()}, {dinner_list[2].title()}\n\nThose who cannot attend: {j[0].title()}{j[1]}{j[2]}{j[3]}."
print(message1)
print("\nIndividual invitations")
dinner_invite1 = f"Invitation to dinner {dinner_list[0].title()}"

dinner_invite2 = f"Invitation to dinner {dinner_list[1].title()}"

dinner_invite3 = f"Invitation to dinner {dinner_list[2].title()}"

print(dinner_invite1)
print(dinner_invite2)
print(dinner_invite3)

dinner_list.insert(0, 'mike')
dinner_list.append('orie')
dinner_list.insert(4, 'paul')
print(dinner_list)

dinner_invite4 = f"Invitation to dinner {dinner_list[3].title()}"

dinner_invite5 = f"Invitation to dinner {dinner_list[4].title()}"

dinner_invite6 = f"Invitation to dinner {dinner_list[5].title()}"


message2 = f"\nInvitation to dinner updates, I have recieved updates that the table is bigger and i invited\n {dinner_list[3].title()},\n {dinner_list[4].title()},\n and {dinner_list[5].title()}\n Those currently attending\n {dinner_list[0].title()},\n {dinner_list[1].title()},\n {dinner_list[2].title()}\n {dinner_list[3].title()},\n {dinner_list[4].title()},\n {dinner_list[5].title()}."
print(message2)


message_cancel = f"\nInvitation to dinner updates, I have recieved updates that the table has been over bidded\n and i can only take two people, whom i decided will be filled by original 2\n of my 3 original guests. I do deeply apologize \n {dinner_list[0].title()}."
print(message_cancel)
dinner_list.pop(0)
print(dinner_list)
message_cancel1 = f"\nInvitation to dinner updates, I have recieved updates that the table has been over bidded\n and i can only take two people, whom i decided will be filled by original 2\n of my 3 original guests. I do deeply apologize \n {dinner_list[1].title()}."
print(message_cancel1)
dinner_list.pop(1)
print(dinner_list)
message_cancel = f"\nInvitation to dinner updates, I have recieved updates that the table has been over bidded\n and i can only take two people, whom i decided will be filled by original 2\n of my 3 original guests. I do deeply apologize \n {dinner_list[2].title()}."
print(message_cancel)
dinner_list.pop(2)
print(dinner_list)
message_cancel = f"\nInvitation to dinner updates, I have recieved updates that the table has been over bidded\n and i can only take two people, whom i decided will be filled by original 2\n of my 3 original guests. I do deeply apologize \n {dinner_list[2].title()}."
print(message_cancel)
dinner_list.pop(2)
print(dinner_list)
message_final = f"\nInvitation to dinner updates, I have recieved updates that the table has been over bidded\n and i can only take two people, whom i decided will be filled by original 2\n of my 3 original guests. \n {dinner_list[0].title()}, you made the cut."
print(message_final)
message_final = f"\nInvitation to dinner updates, I have recieved updates that the table has been over bidded\n and i can only take two people, whom i decided will be filled by original 2\n of my 3 original guests. \n {dinner_list[1].title()}, you made the cut."
print(message_final)
print(dinner_list)
del dinner_list[0]
del dinner_list[0]
print(dinner_list)