import customtkinter
import os
from time import sleep

count = []


def pw_checker():
	item_1 = count[0]
	item_2 = count[1]
	item_3 = count[2]
	item_4 = count[3]
	item_5 = count[4]
	item_6 = count[5]

	main_password = '143232'
	status = False

	if item_1 == '1':
		if item_2 == '4':
			if item_3 == '3':
				if item_4 == '2':
					if item_5 == '3':
						if item_6 == '2':
							status = True
							print('\nPassword correct')
							customtkinter.CTkLabel(root, text='The password is correct', text_color='green').pack(pady=70)

							

							os.system('pinfield/main.py')


	if status == True:
		pass
	else:
		print("\nThe password isn't correct!")
		root.destroy()
							


# this is the function called when the customtkinter.CTkButton is clicked
def btn_one():


	count.append('1')

	leng = len(count)

	if leng == 6:
		pw_checker()
	else:
		print('1')
		root.update()

	label_code = customtkinter.CTkLabel(root, text=count).place(x=136, y=40)

	


# this is the function called when the customtkinter.CTkButton is clicked
def btn_two():

	count.append('2')

	leng = len(count)

	if leng == 6:
		pw_checker()
	else:
		print('2')
		root.update()

	label_code = customtkinter.CTkLabel(root, text=count).place(x=136, y=40)




# this is the function called when the customtkinter.CTkButton is clicked
def btn_three():
	count.append('3')

	leng = len(count)

	if leng == 6:
		pw_checker()
	else:
		print('3')
		root.update()

	label_code = customtkinter.CTkLabel(root, text=count).place(x=136, y=40)


# this is the function called when the customtkinter.CTkButton is clicked
def btn_four():
	count.append('4')

	leng = len(count)

	if leng == 6:
		pw_checker()
	else:
		print('4')
		root.update()

	label_code = customtkinter.CTkLabel(root, text=count).place(x=136, y=40)


# this is the function called when the customtkinter.CTkButton is clicked
def btn_five():
	count.append('5')

	leng = len(count)

	if leng == 6:
		pw_checker()
	else:
		print('5')
		root.update()

	label_code = customtkinter.CTkLabel(root, text=count).place(x=136, y=40)


# this is the function called when the customtkinter.CTkButton is clicked
def btn_six():
	count.append('6')

	leng = len(count)

	if leng == 6:
		pw_checker()
	else:
		print('6')
		root.update()

	label_code = customtkinter.CTkLabel(root, text=count).place(x=136, y=40)



root = customtkinter.CTk()

# This is the section of code which creates the main window
root.geometry('325x343')
root.title('Auth')



# This is the section of code which creates a customtkinter.CTkButton
customtkinter.CTkButton(root, text='1', command=btn_one, width=50).place(x=37, y=163)


# This is the section of code which creates a customtkinter.CTkButton
customtkinter.CTkButton(root, text='2', command=btn_two, width=50).place(x=102, y=163)


# This is the section of code which creates a customtkinter.CTkButton
customtkinter.CTkButton(root, text='3', command=btn_three, width=50).place(x=169, y=164)


# This is the section of code which creates a customtkinter.CTkButton
customtkinter.CTkButton(root, text='4', command=btn_four, width=50).place(x=237, y=164)


# This is the section of code which creates a customtkinter.CTkButton
customtkinter.CTkButton(root, text='5', command=btn_five, width=50).place(x=102, y=230)


# This is the section of code which creates a customtkinter.CTkButton
customtkinter.CTkButton(root, text='6', command=btn_six, width=50).place(x=169, y=229)







root.mainloop()
