import datetime
import json

class ENote:
    def __init__(self):
        self.notes = []
        self.note_file = "enote_notes.json"
        self.log_file = "enote_log.txt"
        self.load_notes()

    def generate_note(self):
        title = input("Enter the title of the note: ")
        description = input("Enter the description of the note: ")
        author = input("Enter your name: ")
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        note = {
            "Date and Time": current_time,
            "Title": title,
            "Description": description,
            "Author": author
        }
        self.notes.append(note)
        self.save_notes()
        self._log_transaction("Generated a new note")
        print("Note generated successfully.")

    def view_notes(self):
        if not self.notes:
            print("No notes available.")
            return
        for index, note in enumerate(self.notes, 1):
            print(f"Note {index}:")
            for key, value in note.items():
                print(f"{key}: {value}")
            print()

    def exit_program(self):
        print("Exiting E-Note program. Thank you!")
        self._log_transaction("Exited the program")
        exit()

    def save_notes(self):
        with open(self.note_file, "w") as file:
            json.dump(self.notes, file)

    def load_notes(self):
        try:
            with open(self.note_file, "r") as file:
                self.notes = json.load(file)
        except FileNotFoundError:
            # If file not found, initialize an empty list of notes
            self.notes = []

    def _log_transaction(self, message):
        with open(self.log_file, "a") as file:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log_entry = f"[{current_time}] {message}\n"
            file.write(log_entry)

def main():
    e_note = ENote()

    while True:
        print("\nE-Note Program")
        print("1. Generate Note")
        print("2. View Notes")
        print("3. Exit Program")
        choice = input("Enter your choice: ")

        if choice == "1":
            e_note.generate_note()
        elif choice == "2":
            e_note.view_notes()
        elif choice == "3":
            e_note.exit_program()
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
