
# 🐱 Cat Facts API Integration

A simple FastAPI service that integrates with the [Cat Facts API](https://catfact.ninja/fact) to fetch and return random cat facts along with user details.  
It demonstrates asynchronous HTTP requests, structured JSON responses, error handling, and basic logging.

---

## 🚀 Features

- Built with **FastAPI**
- Integrates with **Cat Facts API**
- Uses **async HTTP requests** via `httpx`
- Handles **timeouts and network errors**
- Provides **structured JSON responses**
- Includes **CORS middleware** and **logging**
- Dynamically generates **ISO 8601 UTC timestamps**

---

## ⚙️ Configuration

| Setting | Description |
|----------|--------------|
| **Framework** | FastAPI |
| **Logging** | Writes logs to `app.log` |
| **CORS Policy** | Allows all origins, methods, and headers |
| **External API** | `https://catfact.ninja/fact` (default) |
| **Environment Variable** | `CAT_FACTS_URL` – override external API URL |
| **Host / Port** | `0.0.0.0:8080` by default |

---

## 🧱 Endpoints Overview

| Endpoint | Method | Description | Response Code |
|-----------|---------|--------------|----------------|
| `/` | GET | Returns a greeting message | 200 OK |
| `/health` | GET | Returns API health status | 200 OK |
| `/me` | GET | Returns user info and a random cat fact | 200 OK |

---

## 📍 **1. Root Endpoint**

### **`GET /`**
Returns a simple JSON message to verify that the service is running.

#### Example Response
```json
{
  "message": "Hello, World!"
}
````

---

## 📍 **2. Health Check Endpoint**

### **`GET /health`**

Used to check the application’s health status.
Useful for uptime monitoring and container readiness probes.

#### Example Response

```json
{
  "status": "ok"
}
```

---

## 📍 **3. User & Cat Fact Endpoint**

### **`GET /me`**

Fetches:

* Static user information
* Current UTC timestamp (ISO 8601 format)
* A random cat fact fetched from the Cat Facts API

If the external API fails (timeout or error), a fallback message is returned.

#### Example Success Response

```json
{
  "status": "success",
  "user": {
    "email": "afariogun.john2002@gmail.com",
    "name": "John Afariogun",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-15T18:10:40.673902+00:00",
  "fact": "Cats sleep 70% of their lives."
}
```

#### Example Error Response

If the external API fails or times out:

```json
{
  "status": "success",
  "user": {
    "email": "afariogun.john2002@gmail.com",
    "name": "John Afariogun",
    "stack": "Python/FastAPI"
  },
  "timestamp": "2025-10-15T18:12:21.892303+00:00",
  "fact": "No cats today, External API request failed or timed out"
}
```

---

## ⚙️ Helper Function

### **`call_cat_api()`**

Handles communication with the Cat Facts API.

* Uses `httpx.AsyncClient` with a 5s total timeout and 2s connection timeout.
* Returns either:

  ```python
  {"fact": "A group of cats is called a clowder."}
  ```

  or

  ```python
  {"error": "External API request failed or timed out"}
  ```
* Logs all errors for troubleshooting.

---

## 🧾 Logging

All events and API calls are logged to `app.log` with timestamps and severity levels.

Example log output:

```
2025-10-15 18:05:21,041 - INFO - GET /me called
2025-10-15 18:05:21,920 - INFO - Cat fact fetched successfully
2025-10-15 18:05:22,105 - ERROR - Network error calling Cat Facts API: ConnectTimeout
```

---

## 🔐 CORS Configuration

| Setting               | Value                              |
| --------------------- | ---------------------------------- |
| **Allowed Origins**   | `*` (all origins)                  |
| **Allowed Methods**   | `*` (GET, POST, PUT, DELETE, etc.) |
| **Allowed Headers**   | `*`                                |
| **Allow Credentials** | `True`                             |

---

## 🧠 Summary

| Feature              | Description                                               |
| -------------------- | --------------------------------------------------------- |
| **Tech Stack**       | Python 3.9+, FastAPI, httpx                               |
| **Purpose**          | Demonstrates API integration, error handling, and logging |
| **Response Format**  | JSON only                                                 |
| **Error Handling**   | Graceful fallbacks with logging                           |
| **Timestamp Format** | ISO 8601 UTC                                              |
| **CORS**             | Open (development-friendly)                               |

---

## 🏃‍♂️ Running the App

### 1️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 2️⃣ Run the Server

```bash
uvicorn app:app --reload --port 8080
```

### 3️⃣ Access Endpoints

* [http://127.0.0.1:8080/](http://127.0.0.1:8080/) – Root
* [http://127.0.0.1:8080/health](http://127.0.0.1:8080/health) – Health Check
* [http://127.0.0.1:8080/me](http://127.0.0.1:8080/me) – User + Cat Fact


