# Object-Oriented-Programming-
Object-Oriented Programming exercises

Python Development Portfolio Summary
I have been working on a series of Python projects to strengthen my software development skills. My recent work focuses on three core areas: Graphical User Interface (GUI) design, advanced Object-Oriented Programming (OOP) principles, and Database Management integration.

Here is a breakdown of what I have implemented in these files:

1. Desktop GUI Development (tkinter)

main3.py, main4.py, & main5.py: I built interactive desktop applications using the tkinter library. I progressed from simple window generation to utilizing class-based structures for UI components. I successfully implemented event-driven programming by binding button clicks to pop-up message boxes (showinfo). In the more advanced iterations, I utilized Frame widgets to cleanly separate layouts into left and right panels, demonstrating control over application structure and widget geometry.

2. Object-Oriented Programming & Abstraction (abc module)

main6.py & main7.py: I focused on system architecture by creating abstract base classes for vehicles (Arac). I defined abstract methods like hızlan() (accelerate) and yavasla() (decelerate) to enforce a strict contract for subclasses. I then implemented these behaviors dynamically in concrete classes like Otomobil (Car) and Motor (Motorcycle), where the acceleration logic differs based on attributes like cylinder volume.

main8.py: I applied the template method pattern to document processing. I created an abstract Belge (Document) class that dictates the exact workflow for processing a file (belge_ac, veri_oku, veri_isle, belge_kaydet). I then began extending this framework to support specific formats like PDF and Word.

3. Database Management Systems (SQLite)

main.py & main1.py: I developed a comprehensive Library Management System. I designed distinct classes for Kitap (Book), Uye (Member), and Kutuphane (Library). In the finalized version, I integrated an SQLite database to handle persistent storage. I wrote SQL queries to create tables, insert new book records, delete items, update borrowing statuses, and fetch complete library inventories. I also implemented user-specific logic, allowing members to borrow/return books and maintain personalized favorite lists.

main2.py: I built a streamlined employee management script. I structured an Employee class that directly interfaces with an SQLite database to create staff tables, execute INSERT queries for new hires (tracking ID, Department, and Position), and run SELECT queries to retrieve and display the active personnel roster.
