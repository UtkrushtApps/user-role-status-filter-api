# User Role and Status Filter API

## Task Overview

A user management system at a growing SaaS company allows administrators to view and manage user accounts. Recently, the API's user listing endpoint has been returning incorrect results when filtering users by both role (such as 'admin' or 'member') and status (such as 'active' or 'inactive'). The business requires that admins can filter users accurately based on multiple criteria to ensure proper access control and operational oversight, but the current implementation combines filters incorrectly, leading to confusing and unreliable results.

## Guidance

- Focus on implementing robust filtering logic in the API that accurately combines multiple query parameters using SQLAlchemy ORM with PostgreSQL.
- Ensure all API endpoints are asynchronous and leverage FastAPI best practices for dependency injection and data validation.
- Use Pydantic models to serialize and validate responses.
- Organize project files by separating routers, models, services, and database logic for maintainability.
- Configure environment variables for database connections securely and leverage Docker Compose for local development.
- Maintain proper error handling and return appropriate HTTP status codes for all endpoints.

## Objectives

- Implement an endpoint that lists users and allows filtering by both role and status.
- Combine the role and status filters using AND logic in the database query to ensure only users matching all provided criteria are returned.
- Use SQLAlchemy ORM for database operations and ensure all operations are asynchronous.
- Structure the project according to the provided directory layout and ensure the application is fully containerized using Docker and Docker Compose.
- Provide clear response models using Pydantic and ensure OpenAPI documentation is generated automatically.

## How to Verify

- Deploy the stack using Docker Compose and ensure both the application and PostgreSQL database start successfully.
- Test the user listing API endpoint by passing different combinations of role and status query parameters and confirm that only users matching all specified criteria are included in the response.
- Verify that the API returns the correct HTTP status codes and handles missing or invalid parameters gracefully.
- Check that the OpenAPI documentation reflects the correct request and response schemas for the filtering endpoint.
