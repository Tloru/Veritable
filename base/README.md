# Welcome to Veritable
Well, if you're reading this, you probably just started a new Veritable project.
Congrats!
Now, what do you do from here?.
Don't worry, we've got your back.

![A Cute Doggo](/src/doggo.jpg)
> An image of a cute doggo.

## Getting Started
> This README was generated upon running the `$ veritable
init [project name]` command.

In your project directory, you'll see a few Veritable specific files and folders:

- The `.veritable` folder
- The `src` folder
- The `.veritableignore` file
- This `README.md` file

The `.veritable` folder is a hidden folder containing some of your project specific configuration files.
(You shouldn't have to edit any of these files directly - they can be edited through the `$ veritable configure FILE` command.
There is a list of a the commands and the arguments they take later on.)

The `src` folder contains all files (such as an image, etc.) you want to embed in a page.

The `.veritableingore` file is a `.gitignore`-style file that can be used to hide specific files and folders from the showing up on your project website.
By default, it's set to ignore the src folder and all hidden folders/files.

This `README.md` file is what you're reading right now.
It's intended to be used as a getting started guide and reference, so you can delete it after you're done reading it.

Let's talk about how Veritable turns your folders and files into a website.

## From Project to Site
When you initiate a folder, a `.veritable` folder is added to the project's base directory.
This is how the The Veritable Project source code tells whether or not the folder it's in a a Veritable project, so it's important to keep this folder around.

Let's see what the file structure of a finished Veritable project might look like:

```
+ Project Name
|-+ .veritable
| |-- [configuration files]
|
|-+ src
| |-- [static files, images, etc.]
|
|-- .veritableingore
|
|-- index.md
|
|-+ Blog
| |-- Dogs.md
| |-- Update.md
| |-- Hello.md
|
|-+ About
| |-- About.md
```

We've already talked about the `.veritable` and `src` folders, as well as the `.veritableingore` file.

Let's talk about the other files and folders in this Veritable project.

### The `index.md` file
This is the first file users will see when visiting your project's site.

When a folder only contains one non-hidden file, (in this case, the root `[Project Name]` folder containing the `index.md file`), Veritable will render this file instead of providing a list of all files in that directory.

> You can name a file `index.[extension]` to force this behavior if needed.
Note, however, that this might make other files in the same folder inaccessible.

### The `Blog` Folder
This folder contains a bunch of files.
When requested, it will show a list of all files it contains, in this case, the `Dogs.md` file, the `Update.md` file, and the `Hello.md` file.

When displaying these pages on the website, to the user, the extension will be stripped for clarity.

### The `About` folder
As mentioned before, when a folder only has one file, that file will be rendered. This is what we're doing with the `About` folder.  

Because we're using an `index` file, other files in this directory are not listed.

> Remember "*You can name a file `index.[extension]` to force this behavior if needed.
Note, however, that this might make other files in the same folder inaccessible.*"?

A way to get around this is to wrap files with a folder.
When you do this, the file will be visible as a section, and the user will be able to access it.

## Supported Files
So far, [Markdown](https://en.wikipedia.org/wiki/Markdown), and [RST](https://en.wikipedia.org/wiki/ReStructuredText)
files work as viable pages.
Any other file type will be displayed as plain text in a monospaced font.

> There are plans to add [HTML](https://en.wikipedia.org/wiki/HTML) and
[SMD](https://github.com/Structured-Markdown/structured_markdown) documents in the future. If you happen to implement this, please open a pull request. :)

## Accessing the `src` Folder
Let's say that we have a `doggo.md` file about dogs, and we want to display our own image of a doggo on that page (located in `/src/doggo.jpg`).

In markdown, we can use `![alt text](image url)` to display images.

To display the image of the doggo, we'd put something like

```
![A Image of a Cute Doggo](/src/doggo.jpg)
```

in the `doggo.md` file.

## Running Your Site
You're probably already doing this to read this file, but in case you aren't, you can use:

To start your site on your `localhost`, `cd` to your project folder and type:

```
$ veritable run
```

It should then show something like:

```
$ veritable run
Running on http://localhost:5000/...
```

Then open your favorite browser, and go to the `localhost` link.
Tada 🎉.

## Final Notes
That's about it for now.
Have fun with Veritable!

Sincerely,  
The Vertitable Project Authors

> **Now that you're done reading this, delete this file ('README.md'), and start your own project!**

### Commands
Oh, and here are all the veritable commands currently available:

| Command                          | Usage                                     |
| :------------------------------- | :---------------------------------------- |
| `veritable init [project path]`  | Start a new Veritable project in the CWD. |
| `veritable run`                  | Run your Veritable app.                   |
| `veritable configure [variable]` | Set a project variable, i.e. `AUTHOR`.    |

### Configuration Options
Here are all the project variables that can be configured through the `$ veritable configure [variable]` command.

| Name        | What it Does                                           |
| :---------: | :----------------------------------------------------- |
| AUTHOR      | The author of the veritable website you're working on. |
| DESCRIPTION | Some text describing your website.                     |
| NAME        | The name of your project                               |

### Definitions:
This is a list of most terms used within the veritable project source code.
(This isn't necessary know unless you're editing the source code yourself. )

Pages that can be displayed to the user:

- `endpoint`: a page, file, source, or folder.
- `page`: an endpoint that renders styled content.
- `raw`: an endpoint that renders the contents of a file.
- `source`: a literal file (such as an image) to be embedded in a page.
- `section`: an end_point that renders the contents of a directory.

System specific vocabulary:

- `web_path`: the path provided by the user.
- `path`: a system path.
- `folder`: a system folder.
- `file`: a system file.

What to call different people using the veritable project:

- user: a person using a Veritable website
- runner: a person making a Veritable project
- a Veritable Project author: a person working on The Veritable Project

the different uses of the word Veritable:

- a Veritable website: a veritable project rendered as a website through the veritable project.
- a Veritable project: series of folders/files created by a runner.
- The Veritable Project: the veritable project source code/tool.
