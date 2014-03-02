---
layout: post
title: A simple script for creating posts
date: 2014-03-01 21:05:31
categories: blog code
---
I'm very new to jekyll. I think the fact that is a simple and lightweight system is appealing to me.
In trying it out, the one thing I wasn't able to find was a an easy way to create _posts entries. I also
noticed that jekyll did not have any built-in capability to create these files for me,
so i create a script for myself to do it easily.

script: [create-post.py][gh-create-post]
{% highlight python %}
# example usage

$ python create-post.py -s 'A new blog entry'

$ python create-post.py -s 'Another entry' -t blogs,code

# help
$ python create-post --help
Usage: create-post.py [options]

Creates a basic template for posts

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -s TITLE, --title=TITLE
                        Title of blog post
  -f FORMAT, --format=FORMAT
                        Format of blog post
  -l LAYOUT, --layout=LAYOUT
                        Template file should use
  -t TAGS, --tags=TAGS  Tags for blog entry

{% endhighlight  %}

If jekyll does do have the ability to create these files in the _posts directory, please let me know.
[gh-create-post]: https://github.com/sijis/sijis.github.io/blob/master/create-post.py
