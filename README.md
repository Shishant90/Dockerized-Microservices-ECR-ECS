# Microservices Platform

[![Build Status](https://github.com/Shishant90/Dockerized-Microservices-ECR-ECS/workflows/CI/badge.svg)](https://github.com/Shishant90/Dockerized-Microservices-ECR-ECS/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

## Overview

Enterprise-grade microservices platform built with Python FastAPI, containerized with Docker, and deployed on AWS ECS/ECR. This platform follows Domain-Driven Design (DDD) principles and implements clean architecture patterns for scalable, maintainable microservices.

## Architecture

### System Architecture
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Load Balancer │    │   API Gateway   │    │   Service Mesh  │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
┌─────────────────────────────────────────────────────────────────┐
│                    Microservices Layer                         │
├─────────────────┬─────────────────┬─────────────────────────────┤
│ Weather Service │ Another Service │      Future Services        │
└─────────────────┴─────────────────┴─────────────────────────────┘
         │                       │                       │
┌─────────────────────────────────────────────────────────────────┐
│                    Infrastructure Layer                        │
├─────────────────┬─────────────────┬─────────────────────────────┤
│   AWS ECS/ECR   │   RDS/DynamoDB  │    CloudWatch/X-Ray         │
└─────────────────┴─────────────────┴─────────────────────────────┘
```

### Service Structure
```
src/
├── service.weatherforecast/
│   ├── WeatherForecast/              # Core Business Logic
│   │   ├── Features/                 # Use Cases (CQRS Pattern)
│   │   ├── Domain/                   # Domain Models & Business Rules
│   │   ├── Database/                 # Data Access Layer
│   │   └── Gateways/                 # External Service Integration
│   ├── WeatherForecast.Api/          # API Layer (Clean Architecture)
│   │   └── Endpoints/                # REST API Endpoints
│   ├── WeatherForecast.Messaging/    # Event Handling & Messaging
│   ├── Dockerfile                    # Container Configuration
│   └── requirements.txt              # Dependencies
└── service.anothermicroservice/      # Additional Services
    └── Dockerfile
```

## Technology Stack

### Core Technologies
- **Runtime**: Python 3.11+
- **Framework**: FastAPI (Async/Await)
- **Containerization**: Docker & Docker Compose
- **Cloud Platform**: AWS (ECS, ECR, RDS, CloudWatch)

### Development Tools
- **Code Quality**: Black, Flake8, MyPy
- **Testing**: Pytest, Coverage.py
- **Documentation**: Swagger/OpenAPI 3.0
- **Monitoring**: Prometheus, Grafana, AWS X-Ray

### Architecture Patterns
- **Domain-Driven Design (DDD)**
- **Clean Architecture**
- **CQRS (Command Query Responsibility Segregation)**
- **Event-Driven Architecture**
- **Microservices Pattern**

## Getting Started

### Prerequisites
- Python 3.11+
- Docker & Docker Compose
- AWS CLI configured
- Git

### Local Development Setup

1. **Clone Repository**
   ```bash
   git clone https://github.com/Shishant90/Dockerized-Microservices-ECR-ECS.git
   cd Dockerized-Microservices-ECR-ECS
   ```

2. **Environment Setup**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements-dev.txt
   ```

3. **Run Services Locally**
   ```bash
   docker-compose up --build
   ```

4. **Access Services**
   - Weather Service: http://localhost:8000
   - API Documentation: http://localhost:8000/docs
   - Health Check: http://localhost:8000/health

## Development Guidelines

### Code Standards
- Follow PEP 8 style guidelines
- Use type hints for all functions
- Maintain 90%+ test coverage
- Document all public APIs

### Git Workflow
- Feature branches: `feature/TICKET-description`
- Hotfix branches: `hotfix/TICKET-description`
- Pull requests required for main branch
- Conventional commits format

### Testing Strategy
```bash
# Unit Tests
pytest tests/unit/

# Integration Tests
pytest tests/integration/

# End-to-End Tests
pytest tests/e2e/

# Coverage Report
pytest --cov=src --cov-report=html
```

## Deployment

### AWS ECS Deployment
```bash
# Build and push to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account>.dkr.ecr.us-east-1.amazonaws.com

# Deploy to ECS
aws ecs update-service --cluster production --service weather-service --force-new-deployment
```

### Environment Configuration
- **Development**: Local Docker Compose
- **Staging**: AWS ECS (Fargate)
- **Production**: AWS ECS (Fargate) with Auto Scaling

## Monitoring & Observability

### Health Checks
- **Liveness**: `/health/live`
- **Readiness**: `/health/ready`
- **Metrics**: `/metrics` (Prometheus format)

### Logging
- Structured JSON logging
- Correlation IDs for request tracing
- Centralized logging with CloudWatch

### Monitoring
- Application metrics via Prometheus
- Infrastructure monitoring via CloudWatch
- Distributed tracing with AWS X-Ray

## Security

### Security Measures
- Container image scanning
- Secrets management with AWS Secrets Manager
- Network security with VPC and Security Groups
- Authentication via JWT tokens
- Input validation and sanitization

### Compliance
- GDPR compliant data handling
- SOC 2 Type II controls
- Regular security audits

## API Documentation

### OpenAPI Specification
- Interactive docs: `/docs`
- ReDoc format: `/redoc`
- OpenAPI JSON: `/openapi.json`

### API Versioning
- URL versioning: `/api/v1/`
- Backward compatibility maintained
- Deprecation notices for old versions

## Contributing

### Development Process
1. Create feature branch from `main`
2. Implement changes with tests
3. Run quality checks: `make lint test`
4. Submit pull request
5. Code review and approval
6. Merge to main

### Code Review Checklist
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] Security considerations addressed
- [ ] Performance impact assessed
- [ ] Breaking changes documented

## Support & Maintenance

### Team Contacts
- **Tech Lead**: [Your Name] - [email]
- **DevOps**: [DevOps Team] - [email]
- **Security**: [Security Team] - [email]

### Issue Reporting
- Bug reports: GitHub Issues
- Feature requests: GitHub Discussions
- Security issues: [security@company.com]

### SLA & Support
- **Production Issues**: 2-hour response time
- **Non-critical Issues**: 24-hour response time
- **Maintenance Windows**: Sundays 2-4 AM UTC

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Changelog

See [CHANGELOG.md](CHANGELOG.md) for version history and release notes.

---

**Last Updated**: January 2025  
**Version**: 1.0.0  
**Maintained by**: Platform Engineering Team