# Getting Started

### What is Inform?

**Inform is a programming language** that looks like the English language, and lets you make interactive stories.

### How do you interact with stories?

You pretend to tell the main character (you) what to do.

<!-- inform-example: kitchen
title = "Great stories start in the kitchen"
kind = "standalone"
explanation = "The entire introductory story: a title and one room."
commands = ["jump", "walk north", "look at self"]
expect = ["You jump on the spot."]
-->
```inform7
"Great Stories Start in the Kitchen" by You

Your own kitchen is a room.
```

Using **just** those instructions, Inform can make a world like this.

Imagine you are typing the green words telling your character in the story what to do:

> #### Great Stories Start in the Kitchen
> An Interactive Fiction by You
> 
> ***kitchen***
>
> **\>`jump`**  
> You jump on the spot.  
> 
> **\>`walk north`**  
> You can't go that way 
> 
> **\>`look at self`**  
> As good-looking as ever  

Imagine the lines that look like these: 

> **\>`walk`**   

are commands you typed and then hit enter.

### How can I try making these interactive stories?

There's a program (also alled Inform) that you can install on a Windows, Mac, or Linux computer for free.  

Download the latest app for your computer: [Windows](https://github.com/DavidKinder/Windows-Inform7/releases/latest), [Mac](https://github.com/TobyLobster/Inform/releases/latest), or [Linux](https://flathub.org/en/apps/com.inform7.IDE). Open the downloaded file and follow the installation steps for your system.

Installation is a little different on each computer, and this guide is about writing stories, not installing software. for more detailed and official instructions, start with the official [*Writing with Inform* guide](https://ganelson.github.io/inform-website/book/WI_1_1.html), also included in the app once you install it.

### Do you want to get started learning how to make these worlds?

If you do let's start with this book's guide to [making places](../places/README.md).

If you still have more frequently asked questions, keep reading!

### How did this kind of thing start?

Way back in the 1980's, this used to be the most cutting edge way to make video games.  Graphics were just boxes jumping around
so if you wanted rich, beautiful worlds, you had to write about them.  Some people thought this was the way people would write
and read the novels of the future.

### Did people actually pay money for games like this?

Yeah!  The most successful game (Zork) by the most successful company (Infocom) made about $50 million (in today's dollars).

### Do people still make them?

People still make these kinds of games but now mostly call them Interactive Fiction.  It works the same though: you and the computer talk to each other using a written language.

### Are there pictures?

There can be but usually there aren't.  It's mostly about worlds described like fiction, using prose.

### Did you make Inform 7?

No.  

I wrote this guide to help people understand how to use it.  I'm a computer programmer, writer, and user of Inform 7 named Daniel Talsky.

When I was learning Inform 7 I had a hard time finding the answers to some important and simple concepts that would have helped me understand more quickly.

Inform 7 is primarily the work of a pretty amazing scholar named [Graham Nelson](https://en.wikipedia.org/wiki/Graham_Nelson).  He built it on top of older tools other cool people wrote.  Many other people have helped him of course, but in any case, not me.

I just really like Inform 7 and like to teach things.  Inform 7 is pretty unique as a programming language.  (No other programming language comes closer to using the English Language.)

### Only the English language?

You can make interactive stories in other languages but it's harder.  Writing the instructions in another language is even harder but it's a long term goal of the project.

### Are there 6 other Informs?

Yes.  

The 7th one still uses the 6th as it's base so 7 is really 6 + 7.

Inform 7 is the first one that makes such a solid attempt to let you write instructions in the English Language.

### Is Inform 7 Open Source?

Yes!

Inform 7 is open source: [its source code is on GitHub](https://github.com/ganelson/inform). The project welcomes pull requests for small fixes, such as typos or bugs. For larger changes to the language, start with the [Inform Evolution project](https://github.com/ganelson/inform-evolution), where proposals for new features are discussed.

