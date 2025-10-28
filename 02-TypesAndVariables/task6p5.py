###
# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone = input('Enter phone number: ')
print(phone)
if phone.isdigit() == False:
    print('Only use digits!')
if phone.isdigit() == True:
    if len(phone) == 9:
        print(f'Your phone number: {phone[0:3]}-{phone[3:6]}-{phone[6:9]}')
    if len(phone)!= 9:
        print('Phone number must have 9 digits')