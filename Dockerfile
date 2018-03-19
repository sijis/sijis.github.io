FROM fedora:27
MAINTAINER Sijis Aviles<sijis.aviles+github@gmail.com>

RUN dnf install -y ruby-devel ruby gcc-c++ redhat-rpm-config rubygem-json && \
    dnf clean all

RUN gem install jekyll

WORKDIR /app/

EXPOSE 4000

CMD ["/usr/local/bin/jekyll", "server", "-H", "0.0.0.0", "--livereload" ]
