import time
import os
import pickle


choice1 = "1. Calendar"
choice2 = "2. Notes"
choice3 = "3. Events"
choice4 = "4. Tasks"
choice5 = "5. Exit"


def mainmenu():
	os.system("cls")
	print("\tMain Menu")
	print(f"{choice1}\n{choice2}\n{choice3}\n{choice4}\n{choice5}")
	choice = int(input("Enter your choice: "))
	return choice


def error():
	print("Please enter a valid choice.")


def calendar():
	os.system("cls")
	print("Enter the date to know your tasks and events of that day(if any)")
	ch = input("Enter the date(dd/mm/yy): ")
	try:
		f1 = open("events.dat","rb")
		ef = 0
		event = pickle.load(f1)
		while(True):
			#event = pickle.load(f1)
			for i in event:
				if i[1] == ch:
					print(f"EVENTS: \n{i[0]}\n\n")
					ef = 1
					break
			if ef == 0:
				print(f"No event for {ch}")
				break
			else:
				break
	except IOError:
		print("NO EVENTS FOUND")
	'''
	try:
		f1 = open("tasks.dat","rb")
		tf = 0
		task = pickle.load(f1)
		while(True):
			for i in task:
				if i[1] == ch:
					print(f"TASKS: \n{i[0]}\n\n")
					ef = 1
					break
			if ef == 0:
				print(f"No task for {ch}")
				break
			else:
				break
	except IOError:
		print("NO TASKS FOUND")
	'''

	while (True):
		exitinput = input("Type Exit to return to main menu: ")
		if exitinput.lower() == "exit":
			print("Exiting..")
			break
		else:
			print("Enter exit to leave..")


def notes():
	os.system("cls")
	choice1 = "1. Add a note"
	choice2 = "2. Edit a note"
	choice3 = "3. View your notes"
	choice4 = "4. Delete a note"
	choice5 = "5. Exit"

	def error1():
		print("Please enter a valid choice.")
	
	def menu():
		print(f"\n{choice1}\n{choice2}\n{choice3}\n{choice4}\n{choice5}")
		choice = int(input("Enter your choice: "))
		return choice
	
	note = []
	
	def addanote():
		try:
			f = open("notes.dat","wb")
			no_of_notes = int(input("How many notes do you want to enter: "))
			for i in range(no_of_notes):
				heading = input("Enter heading of the note: ")
				content = input("Enter the content of the note: ")
				data = [i+1,heading,content]
				note.append(data)
			f.seek(0)
			pickle.dump(note,f)
			f.close()
		except IOError:
			print("File not found")
	def viewyournotes():
		try:
			f = open("notes.dat","rb")
			ur_notes = pickle.load(f)
			os.system("cls")
			print("\nYOUR NOTES")
			for i in ur_notes:
				print("                    ")
				print(f"Note number: {i[0]}")
				print(f"Heading: {i[1]}")
				print(f"Content: {i[2]}")
			f.close()
		except IOError:
			print("File not found")

	def editanote():
		
		def editheading():
			try:
				f = open("notes.dat","rb+")
				head = pickle.load(f)
				print(head)
				note_found = 0
				heading_verification =  input("Enter the note Heading: ")
				for i in head:
					if i[1].lower() == heading_verification.lower():
						print(i)
						print(f"Current heading is: {i[1]}")
						i[1]= input("Enter new Headng: ")
						note_found = 1 
				if note_found == 0:
						print("Invalid note Heading")
				else:
					print("Done!!'")
					f.seek(0)
					pickle.dump(head,f)
				f.close()
			except IOError:
				print("File not found")


		def editcontent():
			try:
				f = open("notes.dat","rb+")
				content = pickle.load(f)
				print(content)
				note_found = 0
				heading_verification =  input("Enter the note Heading: ")
				for i in content:
					if i[1].lower() == heading_verification.lower():
						print(i)
						print(f"Current content is: {i[2]}")
						i[2]= input("Enter new content: ")
						note_found = 1 
				if note_found == 0:
					print("Invalid note Heading")
				else:
					print("Done!!")
					f.seek(0)
					pickle.dump(content,f)
				f.close()
			except IOError:
				print("File not found")

			#notesmain()
		
		while True:
			print("What do you want to update")
			option1 = "1. Edit the heading of the note"
			option2 = "2. Edit the content of a note"
			print(f"{option1}\n{option2}")
			chedit = int(input("enter your choice: "))
			if chedit > 2 or chedit < 0:
				print("\nPlease enter a valid choice\n")
				continue
			elif chedit == 1:
				editheading()
				break
			elif chedit == 2:
				editcontent()
				break
			else:
				break
	
	def deleteanote():
		try:
			f = open("notes.dat","rb+")
			delete = pickle.load(f)
			print(delete)
			note_verification = input("Enter the note heading of the note which you want to delete: ")
			note = []
			for i in delete:
				if i[1] == note_verification:
					continue
				else:
					note.append(i)
			f.seek(0)
			pickle.dump(note,f)
			f.close()
		except IOError:
			print("File not found")

	def notesmain():
		while(True):
			ch = menu()
			if ch > 5 or ch < 1:
				error()
				continue
			elif ch == 1:
				addanote()
			elif ch == 2:
				editanote()
			elif ch == 3:
				viewyournotes()
			elif ch == 4:
				deleteanote()
			elif ch == 5:
				break
	if __name__ == '__main__':
    			notesmain()

def events():
	os.system("cls")
	choice1 = "1. Add an event"
	choice2 = "2. View your events"
	choice3 = "3. Edit an event"
	choice4 = "4. Delete an event"
	choice5 = "5. Exit"
	def menu():
		print(f"{choice1}\n{choice2}\n{choice3}\n{choice4}\n{choice5}")
		ch = int(input("Enter your choice: "))
		return ch
	def error():
		print("Please enter a valid choice")
		time.sleep(1.5)
	event = []

	def add_a_event():
		try:
			f = open("events.dat","wb")
			no_of_events = int(input("How many events do you want to enter: "))
			for i in range(no_of_events):
				event1 = input("What is the event:")
				date = input("What is the date(dd/mm/yy): ")
				data = [event1, date]
				event.append(data)
			f.seek(0)
			pickle.dump(event,f)
			f.close()
		except IOError:
			print("File not found")
	def viewurevent():
		try:
			f = open("events.dat","rb")
			ur_events = pickle.load(f)
			os.system("cls")
			print("\nYOUR EVENTS")
			for i in ur_events:
				print("                    ")
				print(f"Date: {i[1]}")
				print(f"Event: {i[0]}")
			f.close()
		except IOError:
			print("File not found")
	def edit_an_event():
			
		def editevent():
			try:
				f = open("events.dat","rb+")
				content = pickle.load(f)
				print(content)
				note_found = 0
				date_verification =  input("Enter the date of the event(dd/mm/yy): ")
				for i in content:
					print(i)
					if i[1] == date_verification:
						print(i)
						print(f"Current event: {i[0]}")
						i[0]= input("Enter the new event: ")
						note_found = 1 
				if note_found == 0:
					print(f"No event for {date_verification}")
				else:
					print("Done!!")
					f.seek(0)
					pickle.dump(content,f)
				f.close()
			except IOError:
				print("File not found")
		def editdate():
			try:
				f = open("events.dat","rb+")
				content = pickle.load(f)
				print(content)
				note_found = 0
				date_verification =  input("Enter the date of the event(dd/mm/yy): ")
				for i in content:
					if i[1] == date_verification:
						print(i)
						print(f"Current date: {i[1]}")
						i[1]= input("Enter the new date: ")
						note_found = 1 
				if note_found == 0:
					print(f"No event for {date_verification}")
				else:
					print("Done!!")
					f.seek(0)
					pickle.dump(content,f)
				f.close()
			except IOError:
				print("File not found")
		while(True):
			print("What do you want to update?")
			option1 = "1. Edit an event"
			option2 = "2. Edit the date of an event"
			print(f"{option1}\n{option2}")
			chedit = int(input("enter your choice: "))
			if chedit > 2 or chedit < 0:
				print("\nPlease enter a valid choice\n")
				continue
			elif chedit == 1:
				editevent()
				break
			elif chedit == 2:
				editdate()
				break
			else:
				break
	def delete_an_event():
		try:
			f = open("events.dat","rb+")
			delete = pickle.load(f)
			print(delete)
			date_verification = input("Enter the date of which you want to delete the event: ")
			event = []
			for i in delete:
				if i[1] == date_verification:
					continue
				else:
					event.append(i)
			f.seek(0)
			pickle.dump(event,f)
			f.close()
		except IOError:
			print("File not found")

	def eventsmain():
		while(True):
			ch = menu()
			if ch > 5 or ch < 1:
				error()
				continue
			elif ch == 1:
				add_a_event()
			elif ch == 2:
				viewurevent()
			elif ch == 3:
				edit_an_event()
			elif ch == 4:
				delete_an_event()
			else:
				main()
				break
	if __name__ == '__main__':
    		eventsmain()

	
def tasks():
	os.system("cls")
	choice1 = "1. Add a task"
	choice2 = "2. View your tasks"
	choice3 = "3. Edit an tasks"
	choice4 = "4. Delete an task"
	choice5 = "5. Exit"
	def menu():
		print(f"{choice1}\n{choice2}\n{choice3}\n{choice4}\n{choice5}")
		ch = int(input("Enter your choice: "))
		return ch
	def error():
		print("Please enter a valid choice")
		time.sleep(1.5)
	tasks = []

	def add_a_task():
		try:
			f = open("tasks.dat","wb")
			no_of_events = int(input("How many tasks do you want to enter: "))
			for i in range(no_of_events):
				task = input("What is the task: ")
				date = input("What is the date(dd/mm/yy): ")
				data = [task, date]
				tasks.append(data)
			f.seek(0)
			pickle.dump(tasks,f)
			f.close()
		except IOError:
			print("File not found")
		
	def viewurtasks():
		try:
			f = open("tasks.dat","rb")
			ur_tasks = pickle.load(f)
			os.system("cls")
			print("\nYOUR TASKS")
			for i in ur_tasks:
				print("                    ")
				print(f"Date: {i[1]}")
				print(f"Task: {i[0]}")
			f.close()
		except IOError:
			print("File not found")

	def edit_a_task():
			
		def edittask():
			try:
				f = open("events.dat","rb+")
				task = pickle.load(f)
				print(task)
				note_found = 0
				date_verification =  input("Enter the date of the event(dd/mm/yy): ")
				for i in task:
					print(i)
					if i[1] == date_verification:
						print(i)
						print(f"Current task: {i[0]}")
						i[0]= input("Enter the new task: ")
						note_found = 1 
				if note_found == 0:
					print(f"No task(s) for {date_verification}")
				else:
					print("Done!!")
					f.seek(0)
					pickle.dump(task,f)
				f.close()
			except IOError:
				print("File not found")

		def editdate():
			try:
				f = open("tasks.dat","rb+")
				task = pickle.load(f)
				print(task)
				note_found = 0
				date_verification =  input("Enter the date of the task(dd/mm/yy): ")
				for i in task:
					if i[1] == date_verification:
						print(i)
						print(f"Current date: {i[1]}")
						i[1]= input("Enter the new date: ")
						note_found = 1 
				if note_found == 0:
					print(f"No task for {date_verification}")
				else:
					print("Done!!")
					f.seek(0)
					pickle.dump(task,f)
				f.close()
			except IOError:
				print("File not found")

		while(True):
			print("What do you want to update?")
			option1 = "1. Edit a task"
			option2 = "2. Edit the date of an task"
			print(f"{option1}\n{option2}")
			chedit = int(input("enter your choice: "))
			if chedit > 2 or chedit < 0:
				print("\nPlease enter a valid choice\n")
				continue
			elif chedit == 1:
				edittask()
				break
			elif chedit == 2:
				editdate()
				break
			else:
				break

	def delete_a_task():
		try:
			f = open("tasks.dat","rb+")
			delete = pickle.load(f)
			print(delete)
			date_verification = input("Enter the date of which you want to delete the task: ")
			tasks = []
			for i in delete:
				if i[1] == date_verification:
					continue
				else:
					tasks.append(i)
			f.seek(0)
			pickle.dump(tasks,f)
			f.close()
		except IOError:
			print("File not found")

	def tasksmain():
		while(True):
			ch = menu()
			if ch > 5 or ch < 1:
				error()
				continue
			elif ch == 1:
				add_a_task()
			elif ch == 2:
				viewurtasks()
			elif ch == 3:
				edit_a_task()
			elif ch == 4:
				delete_a_task()
			else:
				main()
				break
				break
	if __name__ == '__main__':
    		tasksmain()


def main():
	while(True):
		choice = mainmenu()
		if choice > 5 or choice < 1:
			error()
			time.sleep(1.5)
			continue
		elif choice == 1:
			calendar()
		elif choice == 2:
			notes()
		elif choice == 3:
			events()
		elif choice == 4:
			tasks()
		else:
			break 

if __name__=="__main__":
	main()