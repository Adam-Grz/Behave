FROM adamgrz/my-ubuntu

COPY start.sh /start.sh
RUN chmod +x /start.sh
ENV DISPLAY=:99
ENTRYPOINT bash /start.sh
