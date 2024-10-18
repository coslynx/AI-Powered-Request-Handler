<div class="hero-icon" align="center">
  <img src="https://raw.githubusercontent.com/PKief/vscode-material-icon-theme/ec559a9f6bfd399b82bb44393651661b08aaf7ba/icons/folder-markdown-open.svg" width="100" />
</div>

<h1 align="center">
AI Powered Request Handler System
</h1>
<h4 align="center">A Python backend API for streamlined OpenAI interaction</h4>
<h4 align="center">Developed with the software and tools below.</h4>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Framework-FastAPI-blue" alt="Framework used for the backend API">
  <img src="https://img.shields.io/badge/Language-Python-red" alt="Programming language used">
  <img src="https://img.shields.io/badge/Database-PostgreSQL-blue" alt="Database used for storage">
  <img src="https://img.shields.io/badge/AI-OpenAI-black" alt="AI models integrated">
</div>
<div class="badges" align="center">
  <img src="https://img.shields.io/github/last-commit/coslynx/AI-Powered-Request-Handler?style=flat-square&color=5D6D7E" alt="git-last-commit" />
  <img src="https://img.shields.io/github/commit-activity/m/coslynx/AI-Powered-Request-Handler?style=flat-square&color=5D6D7E" alt="GitHub commit activity" />
  <img src="https://img.shields.io/github/languages/top/coslynx/AI-Powered-Request-Handler?style=flat-square&color=5D6D7E" alt="GitHub top language" />
</div>

## 📑 Table of Contents
- 📍 Overview
- 📦 Features
- 📂 Structure
- 💻 Installation
- 🏗️ Usage
- 🌐 Hosting
- 📄 License
- 👏 Authors

## 📍 Overview
This repository contains the code for the AI Powered Request Handler System, a Python backend API designed to simplify user interactions with OpenAI's powerful language models. This MVP provides a user-friendly interface for accessing OpenAI's capabilities without needing extensive technical knowledge.

## 📦 Features
|    | Feature            | Description                                                                                                        |
|----|--------------------|--------------------------------------------------------------------------------------------------------------------|
| ⚙️ | **Architecture**   | The codebase follows a modular architectural pattern with separate directories for different functionalities, ensuring easier maintenance and scalability.             |
| 📄 | **Documentation**  | The repository includes a README file that provides a detailed overview of the MVP, its dependencies, and usage instructions.|
| 🔗 | **Dependencies**   | The codebase relies on various external libraries and packages such as FastAPI, SQLAlchemy, PyJWT, OpenAI, and Redis, essential for building the API, handling database interactions, and managing user authentication and caching.|
| 🧩 | **Modularity**     | The modular structure allows for easier maintenance and reusability of the code, with separate directories and files for different functionalities such as controllers, services, and models.|
| 🧪 | **Testing**        | Implement unit tests using frameworks like `pytest` to ensure the reliability and robustness of the codebase.       |
| ⚡️  | **Performance**    | Optimizes performance through caching mechanisms (Redis) and efficient database query optimization, ensuring fast and responsive service delivery. |
| 🔐 | **Security**       | Enhances security by implementing measures such as input validation, data encryption, and secure communication protocols.  |
| 🔀 | **Version Control**| Utilizes Git for version control with GitLab CI workflow files for automated build and release processes.|
| 🔌 | **Integrations**   | Interacts with the OpenAI API, PostgreSQL database, and utilizes Redis for caching, enabling robust functionality. |
| 📶 | **Scalability**    | The architecture allows for horizontal scalability by leveraging containerization (Docker) and database sharding. |

## 📂 Structure
```text
├── api
│   ├── src
│   │   ├── controllers
│   │   │   └── request_controller.py
│   │   ├── services
│   │   │   └── request_service.py
│   │   ├── models
│   │   │   └── request_model.py
│   │   ├── main.py
│   │   └── config
│   │       └── settings.py
│   ├── requirements.txt
│   └── startup.sh
├── migrations
│   ├── __init__.py
│   ├── env.py
│   ├── versions.py
│   └── 0001_initial.py
├── tests
│   └── test_request_controller.py
├── celery
│   ├── __init__.py
│   └── tasks.py
├── .env
├── Dockerfile
├── docker-compose.yml
└── .gitlab-ci.yml

```

## 💻 Installation
### 🔧 Prerequisites
- Python 3.9+
- Docker
- PostgreSQL
- Redis

### 🚀 Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/coslynx/AI-Powered-Request-Handler.git
   cd AI-Powered-Request-Handler
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database:
   ```bash
   # Create a PostgreSQL database and user
   # Update the DATABASE_URL in your .env file
   # Run database migrations:
   alembic upgrade head
   ```
4. Configure environment variables:
   ```bash
   cp .env.example .env
   # Fill in necessary environment variables like OPENAI_API_KEY, DATABASE_URL, and JWT_SECRET_KEY (optional)
   ```

## 🏗️ Usage
### 🏃‍♂️ Running the MVP
1. Start the development server using Docker Compose:
   ```bash
   docker-compose up -d
   ```

2. Access the application:
   - API endpoints: `http://localhost:8000/docs` 

### ⚙️ Configuration
- Environment variables are loaded from the `.env` file.
- Configuration settings are defined in `api/src/config/settings.py`.

### 📚 Examples
- **Send a request to GPT-3**: 
  ```bash
  curl -X POST http://localhost:8000/requests \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{"text": "Write a short story about a cat who travels to space"}'
  ```

## 🌐 Hosting
### 🚀 Deployment Instructions
1. **Build the Docker image:**
  ```bash
  docker build -t ai-request-handler:latest .
  ```

2. **Push the image to a container registry (e.g., Docker Hub):**
  ```bash
  docker push your-dockerhub-username/ai-request-handler:latest
  ```

3. **Deploy using Docker Compose (update the image name in the `docker-compose.yml` file):**
  ```bash
  docker-compose up -d
  ```

### 🔑 Environment Variables
- `OPENAI_API_KEY`: Your OpenAI API key.
- `DATABASE_URL`: Connection string for your PostgreSQL database.
- `JWT_SECRET_KEY`: Secret key for JWT token generation (optional).
- `REDIS_URL`: URL for your Redis instance (optional).

## 📜 API Documentation
### 🔍 Endpoints
- **POST /requests**:  
  - Description: Send a request to an OpenAI model.
  - Body: `{ "text": string }`
  - Response: `{ "response": string }`

### 🔒 Authentication
- For the MVP, authentication is optional. You can implement JWT authentication by following the steps in the `auth.py` file.

## 📜 License & Attribution

### 📄 License
This Minimum Viable Product (MVP) is licensed under the [GNU AGPLv3](https://choosealicense.com/licenses/agpl-3.0/) license.

### 🤖 AI-Generated MVP
This MVP was entirely generated using artificial intelligence through [CosLynx.com](https://coslynx.com).

No human was directly involved in the coding process of the repository: AI-Powered-Request-Handler

### 📞 Contact
For any questions or concerns regarding this AI-generated MVP, please contact CosLynx at:
- Website: [CosLynx.com](https://coslynx.com)
- Twitter: [@CosLynxAI](https://x.com/CosLynxAI)

<p align="center">
  <h1 align="center">🌐 CosLynx.com</h1>
</p>
<p align="center">
  <em>Create Your Custom MVP in Minutes With CosLynxAI!</em>
</p>
<div class="badges" align="center">
  <img src="https://img.shields.io/badge/Developers-Drix10,_Kais_Radwan-red" alt="">
  <img src="https://img.shields.io/badge/Website-CosLynx.com-blue" alt="">
  <img src="https://img.shields.io/badge/Backed_by-Google,_Microsoft_&_Amazon_for_Startups-red" alt="">
  <img src="https://img.shields.io/badge/Finalist-Backdrop_Build_v4,_v6-black" alt="">
</div>