# 0x14. JavaScript - Web scraping

## Resources

#### Read or watch:

* [Working with JSON data](https://intranet.alxswe.com/rltoken/ONv-sSv-FA87Mc5rMZmO6A)
* [The workflow of accessing the attributes of a simply-created JSON object by Jimmy Tran from Cohort 1 - San Francisco](https://intranet.alxswe.com/rltoken/zm0h7FqpQCZZpPZqxxwLxA)
* [request module](https://intranet.alxswe.com/rltoken/goymbxGy-cTc5ZdKBTUcTQ)
* [Modern JS](https://intranet.alxswe.com/rltoken/j2PStAUtVPdXKwrrFxpt0g)

## Learning Objectives

### General

* Why JavaScript programming is amazing
* How to manipulate JSON data
* How to use request and fetch API
* How to read and write a file using fs module

## Tasks

## 0. Readme

- Write a script that reads and prints the content of a file.

### Requirements:

The first argument is the file path
The content of the file must be read in <code>utf-8</code>
If an error occurred during the reading, print the error object

Mode: mandatory

File/s: [0-readme.js](./0-readme.js)
<hr>

## 1. Write me

- Write a script that writes a string to a file.

### Requirements:

The first argument is the file path
The second argument is the string to write
The content of the file must be written in <code>utf-8</code>
If an error occurred during while writing, print the error object

Mode: mandatory

File/s: [1-writeme.js](./1-writeme.js)
<hr>

## 2. Status code

- Write a script that display the status code of a GET request.

### Requirements:

The first argument is the URL to request (<code>GET</code>)
The status code must be printed like this: <code>code: &lt;status
code&gt;</code>
You must use the module <code>request</code>

Mode: mandatory

File/s: [2-statuscode.js](./2-statuscode.js)
<hr>

## 3. Star wars movie title

- Write a script that prints the title of a Star Wars movie where the episode
	number matches a given integer.

### Requirements:

The first argument is the movie ID
You must use
the <a href="/rltoken/HwLU2L7tJ4TEjzfTBc7zTA" title="Star wars API" target="_blank">
Star wars API</a> with the
endpoint <code>https://swapi-api.alx-tools.com/api/films/:id</code>
You must use the module <code>request</code>

Mode: mandatory

File/s: [3-starwars_title.js](./3-starwars_title.js)
<hr>

## 4. Star wars Wedge Antilles

- Write a script that prints the number of movies where the character “Wedge
	Antilles” is present.

### Requirements:

The first argument is the API URL of
the <a href="/rltoken/HwLU2L7tJ4TEjzfTBc7zTA" title="Star wars API" target="_blank">
Star wars API</a>: <code>https://swapi-api.alx-tools.com/api/films/</code>
Wedge Antilles is character ID <code>18</code> - your script <strong>
must</strong> use this ID for filtering the result of the API
You must use the module <code>request</code>

Mode: mandatory

File/s: [4-starwars_count.js](./4-starwars_count.js)
<hr>

## 5. Loripsum

- Write a script that gets the contents of a webpage and stores it in a file.

### Requirements:

The first argument is the URL to request
The second argument the file path to store the body response
The file must be UTF-8 encoded
You must use the module <code>request</code>

Mode: mandatory

File/s: [5-request_store.js](./5-request_store.js)
<hr>

## 6. How many completed?

- Write a script that computes the number of tasks completed by user id.

### Requirements:

The first argument is the API
URL: <code>https://jsonplaceholder.typicode.com/todos</code>
Only print users with completed task
You must use the module <code>request</code>

Mode: mandatory

File/s: [6-completed_tasks.js](./6-completed_tasks.js)
<hr>

## 7. Who was playing in this movie?

- Write a script that prints all characters of a Star Wars movie:

### Requirements:

The first argument is the Movie ID - example: <code>3</code> = “Return of the
Jedi”
Display one character name by line
You must use
the <a href="/rltoken/HwLU2L7tJ4TEjzfTBc7zTA" title="Star wars API" target="_blank">
Star wars API</a>
You must use the module <code>request</code>

Mode: #advanced

File/s: [100-starwars_characters.js](./100-starwars_characters.js)
<hr>

## 8. Right order

- Write a script that prints all characters of a Star Wars movie:

### Requirements:

The first argument is the Movie ID - example: <code>3</code> = “Return of the
Jedi”
Display one character name by line <strong>in the same order of the list
“characters” in the <code>/films/</code> response</strong>
You must use
the <a href="/rltoken/HwLU2L7tJ4TEjzfTBc7zTA" title="Star wars API" target="_blank">
Star wars API</a>
You must use the module <code>request</code>

Mode: #advanced

File/s: [101-starwars_characters.js](./101-starwars_characters.js)
<hr>
