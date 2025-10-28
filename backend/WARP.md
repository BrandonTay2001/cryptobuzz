# WARP.md

This file provides guidance to WARP (warp.dev) when working with the backend code in this directory.

## Backend Overview

**CryptoBuzz Backend** is a Flask API that serves cryptocurrency social media metrics data to the React frontend. The backend provides RESTful endpoints for news and metrics data.

## Project Structure

```
backend/
├── app.py              # Main Flask application
├── routes/             # API route blueprints
│   ├── __init__.py
│   ├── news.py         # News-related endpoints
│   ├── metrics.py      # Metrics-related endpoints
│   └── aggregates.py   # Aggregates data collection endpoints
├── util/               # Utility classes for external APIs
│   ├── coingecko_util.py
│   ├── coinmarketcap_util.py
│   └── ...
├── requirements.txt    # Python dependencies
└── WARP.md            # This file
```

## MongoDB Schema

### Aggregates Collection

The `aggregates` collection stores daily cryptocurrency market data collected via batch jobs at 12:00 AM GMT. Data becomes available starting at 12:30 AM GMT.

**Collection Name:** `aggregates`

**Document Structure:**
```json
{
  "_id": "ObjectId",
  "data_type": "string",     // Type of data: "trending_coins", "trending_topics", "fear_and_greed_index", "total_social_volume"
  "data": "object",          // The actual data payload
  "count": "number",         // Number of items (for arrays)
  "timestamp": "datetime"    // UTC timestamp when data was collected
}
```

**Data Types:**

1. **trending_coins** (from CoinGecko)
   ```json
   {
     "data_type": "trending_coins",
     "data": [
       {"name": "Bitcoin", "symbol": "BTC"},
       {"name": "Ethereum", "symbol": "ETH"},
       ...
     ],
     "count": 5,
     "timestamp": "2024-01-01T00:00:00Z"
   }
   ```

2. **trending_topics** (from CoinMarketCap)
   ```json
   {
     "data_type": "trending_topics",
     "data": [
       {"topic": "Bitcoin ETF"},
       {"topic": "DeFi Protocol"},
       ...
     ],
     "count": 5,
     "timestamp": "2024-01-01T00:00:00Z"
   }
   ```

3. **fear_and_greed_index** (from CoinMarketCap)
   ```json
   {
     "data_type": "fear_and_greed_index",
     "data": {
       "value": 45,
       "classification": "Fear"
     },
     "timestamp": "2024-01-01T00:00:00Z"
   }
   ```

4. **total_social_volume** (from Twitter)
   ```json
   {
     "data_type": "total_social_volume",
     "data": {
       "mention_count": 12345
     },
     "timestamp": "2024-01-01T00:00:00Z"
   }
   ```

## Batch Job Structure

The aggregates system uses a batch job architecture for data collection:

### Data Collection Schedule
- **Collection Time**: 12:00 AM GMT daily
- **Data Availability**: Starting at 12:30 AM GMT
- **Collection Endpoints**: 
  - `/aggregates/getTrendingCoins` - Collects top 5 trending coins from CoinGecko
  - `/aggregates/getTrendingTopics` - Collects top 5 trending topics from CoinMarketCap
  - `/aggregates/getFearAndGreed` - Collects fear and greed index from CoinMarketCap
  - `/aggregates/getTotalSocialVolume` - Collects social volume data from Twitter for major crypto terms

### Data Retrieval
- **Latest Data Endpoint**: `/aggregates/getLatest` - Returns the most recent data for all aggregate types
- **Response Format**: JSON with separate sections for each data type including timestamps

### Batch Job Flow
1. **12:00 AM GMT**: Batch job triggers all four collection endpoints
2. **Data Storage**: Each endpoint stores data in MongoDB `aggregates` collection
3. **12:30 AM GMT**: Data becomes available for frontend consumption via `/getLatest`
4. **Frontend**: Calls `/getLatest` to retrieve all current aggregate data

### Response Structure
The `/getLatest` endpoint returns a consistent structure with all four data types:
```json
{
  "status": "success",
  "data": {
    "trending_coins": { "data": [...], "count": 5, "timestamp": "..." },
    "trending_topics": { "data": [...], "count": 5, "timestamp": "..." },
    "fear_and_greed_index": { "data": {...}, "timestamp": "..." },
    "total_social_volume": { "data": {...}, "timestamp": "..." }
  }
}
```
Empty dictionaries `{}` are returned for data types that don't exist, ensuring consistent response structure.

### API Endpoints

#### Data Collection Endpoints (Batch Job Use)
- `GET /aggregates/getTrendingCoins` - Collects and stores trending coins data
- `GET /aggregates/getTrendingTopics` - Collects and stores trending topics data  
- `GET /aggregates/getFearAndGreed` - Collects and stores fear and greed index data
- `GET /aggregates/getTotalSocialVolume` - Collects and stores social volume data from Twitter

#### Data Retrieval Endpoints (Frontend Use)
- `GET /aggregates/getLatest` - Returns latest data for all aggregate types
- `GET /aggregates/` - Health check endpoint

## Development Guidelines

- Use Flask blueprints for organizing routes
- Enable CORS for frontend communication
- Follow RESTful API conventions
- Return JSON responses with consistent structure
- Use environment variables for configuration
- Implement proper error handling and logging
- Store aggregate data in MongoDB instead of returning it directly
- Use batch jobs for data collection at scheduled times
- Data collection endpoints return success messages, not data
- Data retrieval endpoints return actual data from MongoDB