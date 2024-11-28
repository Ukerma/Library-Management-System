<h1>📚 Library Management System (LMS)</h1>
<p>
   This project implements a simple Library Management System (LMS) that allows users to manage books through a command-line interface. Users can list available books, add new books, and remove existing ones. The data is persistently stored in a file named <code>books.txt</code>.
</p>
<p>
   This project was developed as part of the <strong>Akbank Python Bootcamp: Yeni Nesil Proje Kampı</strong>.
</p>

<h2>🛠️ Features</h2>
<ul>
   <li> List all books in the library with details such as title, author, release year, and number of pages.</li>
   <li> Add a new book by providing the title, author, release year, and number of pages.</li>
   <li> Remove a book from the library by specifying its title.</li>
   <li> Persistent data storage in a file (<code>books.txt</code>).</li>
   <li> User-friendly menu interface with input validation.</li>
</ul>

<h2>⚙️ Technologies Used</h2>
<ul>
   <li> <strong>Language:</strong> Python</li>
   <li> <strong>Concepts:</strong>
      <ul>
         <li> File handling for data storage and manipulation.</li>
         <li> Object-oriented programming (OOP) for managing library operations.</li>
         <li> Command-line interface for user interaction.</li>
      </ul>
   </li>
</ul>

<h2>🚀 How to Use</h2>
<ol>
   <li> Clone or download the repository to your local machine.</li>
   <li> Run the program using a Python interpreter:
      <pre><code>python main.py</code></pre>
   </li>
   <li> Follow the menu options:
      <ul>
         <li><strong>1:</strong> List all books.</li>
         <li><strong>2:</strong> Add a new book.</li>
         <li><strong>3:</strong> Remove a book.</li>
         <li><strong>q:</strong> Exit the program.</li>
      </ul>
   </li>
</ol>

<h2>💡 Example Output</h2>
<pre>
╔═══════╣ LMS MENU ╠═══════╗
║    » 1- List Books       ║
║    » 2- Add Book         ║
║    » 3- Remove Book      ║
║    » q- Exit             ║
╚══════════════════════════╝

» Enter your choice (1/2/3/q): 1
» Book Name: The Catcher in the Rye, Author: J.D. Salinger, Release Date: 1951, Number of Pages: 277

» Enter your choice (1/2/3/q): 2
» Enter book title: 1984
» Enter book author: George Orwell
» Enter release year: 1949
» Enter number of pages: 328
» Book added successfully.

» Enter your choice (1/2/3/q): 3
» Enter the title of the book to remove: 1984
» Book '1984' removed successfully.
</pre>

<h2>👨‍💻 Author</h2>
<p>
   This project was developed by <strong>Umut Kerim ACAR (ukerma)</strong> as part of the <strong>Akbank Python Bootcamp: Yeni Nesil Proje Kampı</strong>.
</p>
