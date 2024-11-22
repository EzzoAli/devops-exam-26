# Stage 1: Build the application
FROM maven:3.9.4-eclipse-temurin-17 as builder
WORKDIR /app
COPY pom.xml .
RUN mvn dependency:go-offline

COPY src ./src
RUN mvn package

# Stage 2: Run the application
FROM openjdk:17-jdk-slim
WORKDIR /app

# Copy the JAR file from the builder stage
COPY --from=builder /app/target/imagegenerator-0.0.1-SNAPSHOT.jar app.jar

# Define the command to run the JAR file
ENTRYPOINT ["java", "-jar", "app.jar"]
