# mcblog-platform
A simple, lightweight blog platform in Python/Django

# About
mcblog-platform is an open-source, lightweight, multi-user weblog, built to load fast on any device connected to the internet, and be screen adaptive. You can see it alive and test it [here](https://mcblg.pythonanywhere.com/), and read more about it on its top [post](https://mcblg.pythonanywhere.com/post/14/).

Some of mcblog's speed and security features:

+ Depends only on HTML/CSS - no JavaScript inside.
+ Uses lightweight [UIkit](https://github.com/uikit/uikit) HTML/CSS libraries - no Bootstrap.
+ Uses fast, open-source webfont service [Brick](https://github.com/alfredxing/brick) - no Google fonts.
+ Adapts the size of the font to the size of the screen.
+ Allows multiple users, but restricts publish, edit and delete actions to the authenticated author of each post.
+ Allows comments, but subjects them to approval by the author of the post.

# How to use
The easiest way to use mcblog's code is to make a fork of this repository to a repository of your own, because in most cases you will need it to be there to deploy onto a public server so you may use it online.

If you intend to do only small changes on the template (HTML) and the static (CSS) - the name of the blog, the color scheme and/or the main font - you may want to edit the files directly on your repository.

Otherwise, if you know how to program in Python/Django and intend to change also some of the framework files, you will want to download the whole repository into your machine, edit the files to make the desired changes and then git-push them back to your repository.

mcblog-platform code is open source and you are free to make the changes that you wish under the conditions of the MIT License. Please do not forget to mention the source copyright and read the License [here](https://github.com/manuelcaeiro/mcblog-platform/new/master?readme=1#license).

# Need help?
If you like and want to use mcblog-platform but don't know how to deploy it in order to put it online, I may be able to do it for you. (Contact manuelcaeiro[at]workmail.com)

# License
The MIT License

Copyright [2019] [J. Manuel Caeiro D. P.]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

# TO-DO
+ Add a text search API.
