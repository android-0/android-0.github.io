# SSG

Posted: Tue, 22-10-2025.

Suddenly I wanted to redesign my blog into one long page.
I made really simple static site generator in python.
This is the first time I used uv.
I write blog posts in markdown and place them inside md directory.
For all files in md directory, if there is no corresponding html file in tmp directory
or it is newer, I will convert it using markdown library to html and place it in tmp directory.
Then I join all html files inside tmp directory into single HTML.
