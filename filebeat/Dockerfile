ARG ELK_VERSION

# https://github.com/elastic/elasticsearch-docker
FROM docker.elastic.co/beats/filebeat:${ELK_VERSION}

USER root
RUN yum install -y -q -e 0 rsync openssl vim;
# Add your elasticsearch plugins setup here
# Example: RUN elasticsearch-plugin install analysis-icu
