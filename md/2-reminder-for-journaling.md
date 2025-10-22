# Reminder for Journaling

Posted: Sun, 14-07-2024.
Edited: Mon, 13-10-2025.

I keep forgeting to write my journal. My solution is to create a program that checks and reminds
me if I haven't filled my journal whenever I open a terminal.

I only use txt file on vim for journaling. Nothing fancy. I don't like note taking app like
obsidian and notion, because too many buttons and many features that I will never use.
I use a subset of markdown syntax for organizing my journal:

```
# Journal

## 2024

### 07-11-24
- Some interesting events.
- Today I learned ....

### 06-11-24
- Finished chapter 1 of "insert book name"
- Tried installing new OS.
```

So, here is the code:
[journalreminder.c](https://codeberg.org/jonesangga/dotfiles/src/branch/main/utils/journalreminder.c)

First, it checks the last modified date of a given filename argument, in this case my journal.txt file.
And subtract that to today's date. Then it prints a message if the date difference is not zero.

To run that everytime I open a terminal I added the following line to my `.bashrc` file:

```
~/.dotfiles/utils/journalreminder ~/Meta/journal.txt
```

One of its limitation is if I forgot to write journal for, say 5 days, and now I write it but
only for today's date, it will not show the message again. Though that also what I intended:
if I forget to write for one day, the reason might be there is nothing interesting to
write that day.
