# Use an official openjdk runtime as a parent image
FROM openjdk:17-jdk-slim

# Set the working directory in the container
WORKDIR /app

# Copy the Maven build artifact (JAR file) into the container
COPY target/your-app.jar /app/your-app.jar

# Run the JAR file
CMD ["java", "-jar", "your-app.jar"]

# Expose the port that your application listens on
EXPOSE 8080
