#!/usr/bin/env python

__author__ = 'Sijis Aviles'

import datetime
import os
import sys
from optparse import OptionParser


def convert_post_title(title):
    """ Returns a cleaned title """
    post_title = []
    for c in title.lower():
        if not c.isalnum():
            c = c.replace(c, '-')
        post_title.append(c)
    return ''.join(post_title)


if __name__ == '__main__':

    parser = OptionParser(version='%prog 0.1', description='Creates a basic template for posts')
    parser.add_option('-s', '--title', dest='title', metavar='TITLE', default=None, help='Title of blog post')
    parser.add_option(
        '-f', '--format', dest='file_format', metavar='FORMAT', default='markdown', help='Format of blog post')
    parser.add_option(
        '-l', '--layout', dest='layout', metavar='LAYOUT', default='post', help='Template file should use')
    parser.add_option('-t', '--tags', dest='tags', metavar='TAGS', default='blog', help='Tags for blog entry')

    (options, args) = parser.parse_args()
    data = vars(options)

    if not data['title']:
        print('Title is required')
        sys.exit(1)

    title = data['title']
    layout = data['layout']
    file_format = data['file_format']
    tags = ' '.strip().join(data['tags'].split(','))

    rightnow = datetime.datetime.now()

    file_name = rightnow.strftime('%Y-%m-%d-{0}.{1}'.format(convert_post_title(title), file_format))
    file_path = os.path.join('{0}/{1}'.format(os.getcwd(), '_posts'))
    file_full_name = '{0}/{1}'.format(file_path, file_name)
    post_date = rightnow.strftime('%Y-%m-%d %H:%M:%S')
    post_categories = tags
    post_layout = layout
    post_title = title

    file_data = ('---', 'layout: {0}'.format(post_layout), 'title: {0}'.format(post_title),
                 'date: {0}'.format(post_date), 'categories: {0}'.format(post_categories), '---', '')

    print(file_full_name)

    post_file = open(file_full_name, 'w+')
    post_file.write('\n'.join(file_data))
    post_file.close()
