FROM debian:bullseye-slim

# Install required packages
RUN apt-get update && apt-get install -y fortune-mod cowsay netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Copy app script
WORKDIR /app
COPY wisecow.sh .
RUN chmod +x wisecow.sh

# Expose port
EXPOSE 4499

# Run app
CMD ["./wisecow.sh"]
