# Welcome to Veritable
Well, if you're reading this, you probably just started a new Veritable website.
Congrats!
Now, what do you do from here?.
Don't worry, we've got your back.

![A Cute Doggo](src/doggo.jpg)
> An image of a cute doggo.

## Getting Started
> This README was generated upon running the `$ veritable
new [project name]` command.

In this directory, you should see 2 (well, 3) folders:

- the `root` folder,
- the `src` folder,
- (and the `.veritable` folder - this is where we do all the engine stuff, so you shouldn't have to worry about it).

Let's focus on the `root` and `src` folders first.

### The `root` Folder
The root folder contains all visible content or *articles* you want the users to see.

If you're making a simple blogging website, here's what your project structure might look like:

```
- root
|-+ Blog
| |-- dogs.md
| |-- update.md
| |-- hello.md
|
|-+ About
| |-- about.md
```
> A tree diagram of an example structure contained within the `root` folder.

Folders are the equivalent of site sections - think of them like a navbar.
This site only has sections nested one layer deep, but in theory, you could nest sections forever.

This blog has two sections, a `Blog` section, and an `About` section.
When a section contains only one file (the `About` section, for instance), that file will be displayed when that section is clicked.
However, if a section contains more than 1 page, when clicked a list overview of all accessible files will appear.

A file endpoint in the above source tree is the equivalent of a *page*, *article*, or *post*.
In the `Blog` section, we see three posts - `dogs.md`, `update.md`, and `hello.md`.

So far,
[Markdown](https://en.wikipedia.org/wiki/Markdown),
[HTML](https://en.wikipedia.org/wiki/HTML),
[SMD](https://github.com/Structured-Markdown/structured_markdown),
[Text](https://en.wikipedia.org/wiki/Text_file), and
[RST](https://en.wikipedia.org/wiki/ReStructuredText)
files work as viable pages.
Any other file type will be displayed as plain text in a monospaced font.

Anyway, let's see what `dog.md` might look like:

```
# Dogs Are Awesome!
As you already *probably* know, dogs are the **best** animals on earth. The end.
```
> A post about dogs.

That's pretty cool.

Let's recap.
The `root` folder contains all files (i.e pages, posts, etc.) that are directly visible to the user through the site.
Pages are organized into sections using folders - if a section only contains one page, that page will be displayed instead of an overview of all the pages that that section contains.
A page can be written in a myriad of Markup Languages, including Markdown and HTML.


Let's say you want to insert your own image into the `dog.md` post.
How would you do that?

Enter the `src` folder.

### The `src` Folder
The `src` folder should contain files (such as images) used by your project that you don't want to show directly on your website.

All resources under the `src` can be accessed by using the `/src/[file]` URL.
If you check the `src` folder right now, you'll see a cute pic of a doggo.

Let's try to put this image into the `dog.md` post we previewed earlier.

```
# Dogs Are Awesome!
As you already *probably* know, dogs are the **best** animals on earth.
Need proof?
Just take a good look at this picture:

![an awesome doggo](/src/doggo.jpg)
> A picture of a beautiful doggo.
```
> Extending the post to include the doggo pic.

See that?
On like 6, we use standard Markdown format to display the doggo image in the src folder. Of course, this is just scratching the surface of what's possible, but you get the idea.

Recap: You can use the src folder to store 'hidden' files that you can reference throughout your posts.

## Running Your Site
To start your site on your `localhost`, `cd` to your project folder and type:

```
$ veritable run
```

It should then show something like:

```
$ veritable run
Running on http://localhost:5000/...
```

Then open your favorite browser, and go to the localhost link.
Tada.

## Final Notes
That's about it for now.
Have fun with Veritable!

Sincerely,  
Me (The Vertitable Developer)

**Now that you're done reading this, delete this file ('README.md'), and start your own project!**

Oh, and here are all the veritable commands currently available:

| Command                             | Usage                                       |
| :---------------------------------- | :------------------------------------------ |
| `veritable new [project name]`      | Start a new Veritable project in the CWD.   |
| `veritable run`                     | Run your Veritable app.                     |
| `veritable bind [variable] [value]` | Set a project variable, i.e. `site author`. |
