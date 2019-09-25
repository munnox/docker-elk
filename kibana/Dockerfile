ARG ELK_VERSION

# https://github.com/elastic/kibana-docker
FROM docker.elastic.co/kibana/kibana:${ELK_VERSION}
USER root
RUN yum -y -q upgrade
RUN yum -y -q install openssl
USER kibana
# Add your kibana plugins setup here
# Example: RUN kibana-plugin install <name|url>
