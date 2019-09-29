FROM ruby
RUN gem install jekyll
WORKDIR /app/
EXPOSE 4000
CMD ["/usr/local/bundle/bin/jekyll", "server", "-H", "0.0.0.0", "--livereload" ]
