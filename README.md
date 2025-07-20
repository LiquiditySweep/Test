# Two-API Demo (API1 → API2) with Docker Compose

This project demonstrates how to chain two simple API services using FastAPI and Docker Compose.  
- **API1** receives a request, forwards it to **API2**, and returns the response.  
- Both services print logs to the console.

---

## 🖥️ Deploy & Run (Windows)

1. **Install [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/)** (Linux containers, WSL2 backend recommended)
2. **Clone this repository**  
    เปิด PowerShell ที่โฟลเดอร์ที่ต้องการ แล้วรัน:
    ```powershell
    git clone <your-repo-url>
    cd two-api-demo
    ```
3. **Build and start the services**
    ```powershell
    docker compose up --build -d
    ```

---

## 🐧 Deploy & Run (Linux)

1. **Install Docker Engine**  
   [Official install guide (Ubuntu)](https://docs.docker.com/engine/install/ubuntu/)
2. **Clone this repository**  
    เปิด Terminal แล้วรัน:
    ```bash
    git clone <your-repo-url>
    cd two-api-demo
    ```
3. **Build and start the services**
    ```bash
    docker compose up --build -d
    ```

---

## 🧪 How to Test

### 1. Test API1 (calls API2)

**ทุกระบบ**: ใช้ curl, httpie, หรือ browser  
```sh
curl "http://localhost:8001/call-api2?name=John"
