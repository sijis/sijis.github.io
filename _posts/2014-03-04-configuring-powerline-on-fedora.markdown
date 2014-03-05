---
layout: post
title: Configuring powerline on Fedora
date: 2014-03-04 21:24:36
categories: blog
---

I wanted to checkout powerline, as lately I've seen several great looking screenshots.

This is what I had to do to get it working on Fedora 20.

Install the packages
{% highlight bash %}
# yum install powerline
# yum install vim-plugin-powerline
{% endhighlight %}

Setting up for bash shell
{% highlight bash %}
$ vim ~/.bashrc
# add the following to end of file

if [ -f /usr/lib/python2.7/site-packages/powerline/bindings/bash/powerline.sh ]; then
    source /usr/lib/python2.7/site-packages/powerline/bindings/bash/powerline.sh
fi
{% endhighlight %}

Setting up for vim
{% highlight bash %}
$ vim ~/.vimrc

# add to end of file
set rtp+=/usr/lib/python2.7/site-packages/powerline/bindings/vim
set laststatus=2
{% endhighlight %}

Setting up for bash to display git branches
{% highlight bash %}
$ cp -r /usr/lib/python2.7/site-packages/powerline/bindings/config_files/* ~/.config/powerline/
$ vim ~/.config/powerline/config.json
# go to line 28
"theme": "default"
to
"theme": "default_leftonly"
{% endhighlight %}

That should be all!
