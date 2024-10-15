## Getting Started

### Prerequisites

- Python 3.8+
- PostgreSQL (or any other database supported by SQLAlchemy)
- [OpenAI API Key](https://beta.openai.com/signup/)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/investment-app-api.git
    cd investment-app-api
    ```

2. **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the environment variables:**

    Create a `.env` file in the root directory and add the following variables:

    ```env
    DATABASE_URL=postgresql://user:password@localhost/dbname
    SECRET_KEY=your_secret_key
    ALGORITHM=HS256
    ACCESS_TOKEN_EXPIRE_MINUTES=30
    OPENAI_API_KEY=your_openai_api_key
    ```
