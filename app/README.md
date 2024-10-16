### Authentication

Below is the list of endpoints and their respective request and response bodies for the backend.

#### Register User
**Endpoint:** `POST /api/auth/register`

**Request Body:**
```json
{
  "email": "user@example.com",
  "name": "John Doe",
  "contact_info": "123-456-7890",
  "password": "securepassword"
}
```

**Response:**
```json
{
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "email": "user@example.com",
  "name": "John Doe",
  "contact_info": "123-456-7890",
  "created_at": "2023-10-01T12:00:00Z",
  "updated_at": "2023-10-01T12:00:00Z"
}
```

#### Login User
**Endpoint:** `POST /api/auth/login`

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

**Response:**
```json
{
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "email": "user@example.com",
  "name": "John Doe",
  "contact_info": "123-456-7890",
  "created_at": "2023-10-01T12:00:00Z",
  "updated_at": "2023-10-01T12:00:00Z"
}
```

### User Profile

#### Create User Profile
**Endpoint:** `POST /api/user_profile/`

**Request Body:**
```json
{
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "investment_preferences": "Stocks",
  "risk_tolerance": "High",
  "budget": 10000,
  "financial_goals": "Retirement"
}
```

**Response:**
```json
{
  "profile_id": 1,
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "investment_preferences": "Stocks",
  "risk_tolerance": "High",
  "budget": 10000,
  "financial_goals": "Retirement"
}
```

#### Read User Profile
**Endpoint:** `GET /api/user_profile/{profile_id}`

**Response:**
```json
{
  "profile_id": 1,
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "investment_preferences": "Stocks",
  "risk_tolerance": "High",
  "budget": 10000,
  "financial_goals": "Retirement"
}
```

### Chat

#### Chat with AI
**Endpoint:** `POST /api/chat`

**Request Body:**
```json
{
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "message": "What are the best stocks to invest in?",
  "context": "Financial advice"
}
```

**Response:**
```json
{
  "response": "Based on current market trends, some of the best stocks to invest in are..."
}
```

### Recommendations

#### Create Recommendation
**Endpoint:** `POST /api/recommendation/`

**Request Body:**
```json
{
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "stock_id": 1,
  "reasoning": "Strong financials and growth potential"
}
```

**Response:**
```json
{
  "recommendation_id": 1,
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "stock_id": 1,
  "reasoning": "Strong financials and growth potential",
  "recommended_at": "2023-10-01T12:00:00Z"
}
```

#### Read Recommendation
**Endpoint:** `GET /api/recommendation/{recommendation_id}`

**Response:**
```json
{
  "recommendation_id": 1,
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "stock_id": 1,
  "reasoning": "Strong financials and growth potential",
  "recommended_at": "2023-10-01T12:00:00Z"
}
```

### Stocks

#### Create Stock
**Endpoint:** `POST /api/stock/`

**Request Body:**
```json
{
  "ticker": "AAPL",
  "name": "Apple Inc.",
  "sector": "Technology",
  "industry": "Consumer Electronics",
  "fundamental_data": {},
  "technical_data": {}
}
```

**Response:**
```json
{
  "stock_id": 1,
  "ticker": "AAPL",
  "name": "Apple Inc.",
  "sector": "Technology",
  "industry": "Consumer Electronics",
  "fundamental_data": {},
  "technical_data": {}
}
```

#### Read Stock
**Endpoint:** `GET /api/stock/{stock_id}`

**Response:**
```json
{
  "stock_id": 1,
  "ticker": "AAPL",
  "name": "Apple Inc.",
  "sector": "Technology",
  "industry": "Consumer Electronics",
  "fundamental_data": {},
  "technical_data": {}
}
```

### Portfolios

#### Create Portfolio
**Endpoint:** `POST /api/portfolio/`

**Request Body:**
```json
{
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "composition": {},
  "current_value": 10000,
  "forecasted_value": 15000
}
```

**Response:**
```json
{
  "portfolio_id": 1,
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "composition": {},
  "current_value": 10000,
  "forecasted_value": 15000,
  "created_at": "2023-10-01T12:00:00Z",
  "updated_at": "2023-10-01T12:00:00Z"
}
```

#### Read Portfolio
**Endpoint:** `GET /api/portfolio/{portfolio_id}`

**Response:**
```json
{
  "portfolio_id": 1,
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "composition": {},
  "current_value": 10000,
  "forecasted_value": 15000,
  "created_at": "2023-10-01T12:00:00Z",
  "updated_at": "2023-10-01T12:00:00Z"
}
```

### Transactions

#### Create Transaction
**Endpoint:** `POST /api/transaction/`

**Request Body:**
```json
{
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "points": 100,
  "transaction_type": "credit",
  "related_nft_id": null
}
```

**Response:**
```json
{
  "transaction_id": 1,
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "points": 100,
  "transaction_type": "credit",
  "related_nft_id": null,
  "timestamp": "2023-10-01T12:00:00Z"
}
```

#### Read Transaction
**Endpoint:** `GET /api/transaction/{transaction_id}`

**Response:**
```json
{
  "transaction_id": 1,
  "user_id": "123e4567-e89b-12d3-a456-426614174000",
  "points": 100,
  "transaction_type": "credit",
  "related_nft_id": null,
  "timestamp": "2023-10-01T12:00:00Z"
}
```

### NFTs

#### Create NFT
**Endpoint:** `POST /api/nft/`

**Request Body:**
```json
{
  "token_id": "abc123",
  "owner_user_id": "123e4567-e89b-12d3-a456-426614174000",
  "metadata": {}
}
```

**Response:**
```json
{
  "nft_id": 1,
  "token_id": "abc123",
  "owner_user_id": "123e4567-e89b-12d3-a456-426614174000",
  "metadata": {},
  "created_at": "2023-10-01T12:00:00Z",
  "transferred_at": null
}
```

#### Read NFT
**Endpoint:** `GET /api/nft/{nft_id}`

**Response:**
```json
{
  "nft_id": 1,
  "token_id": "abc123",
  "owner_user_id": "123e4567-e89b-12d3-a456-426614174000",
  "metadata": {},
  "created_at": "2023-10-01T12:00:00Z",
  "transferred_at": null
}
```

### Rewards

#### Create Reward
**Endpoint:** `POST /api/reward/`

**Request Body:**
```json
{
  "nft_id": 1,
  "reward_type": "discount",
  "details": {}
}
```

**Response:**
```json
{
  "reward_id": 1,
  "nft_id": 1,
  "reward_type": "discount",
  "details": {}
}
```

#### Read Reward
**Endpoint:** `GET /api/reward/{reward_id}`

**Response:**
```json
{
  "reward_id": 1,
  "nft_id": 1,
  "reward_type": "discount",
  "details": {}
}
```

### News Articles

#### Create News Article
**Endpoint:** `POST /api/news_article/`

**Request Body:**
```json
{
  "title": "Market Update",
  "content": "The stock market is up today...",
  "source": "Financial Times",
  "published_at": "2023-10-01T12:00:00Z",
  "category": "Finance"
}
```

**Response:**
```json
{
  "article_id": 1,
  "title": "Market Update",
  "content": "The stock market is up today...",
  "source": "Financial Times",
  "published_at": "2023-10-01T12:00:00Z",
  "category": "Finance"
}
```

#### Read News Article
**Endpoint:** `GET /api/news_article/{article_id}`

**Response:**
```json
{
  "article_id": 1,
  "title": "Market Update",
  "content": "The stock market is up today...",
  "source": "Financial Times",
  "published_at": "2023-10-01T12:00:00Z",
  "category": "Finance"
}
```
