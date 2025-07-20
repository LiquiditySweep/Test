# Two-API Demo (API1 → API2) ด้วย Docker Compose

โปรเจกต์นี้เป็นตัวอย่างการสร้าง API 2 ตัวที่เชื่อมต่อกันด้วย FastAPI และรันด้วย Docker Compose  
- **API1** รับ request จากผู้ใช้ แล้วส่งต่อไป **API2** ก่อนจะตอบกลับ  
- ทั้งสอง API มี log ขึ้นบนหน้าจอ

---

## 🖥️ วิธีใช้งานบน Windows

1. **ติดตั้ง [Docker Desktop for Windows](https://www.docker.com/products/docker-desktop/)** (แนะนำให้ใช้ Linux containers + WSL2)
2. **โหลดโค้ดโปรเจกต์มาที่เครื่อง**  
   เปิด PowerShell ที่โฟลเดอร์ที่ต้องการ แล้วรัน
    ```powershell
    git clone [<your-repo-url>](https://github.com/LiquiditySweep/Test)
    cd two-api-demo
    ```
3. **สั่ง Build และ Run ทั้งสอง API**
    ```powershell
    docker compose up --build -d
    ```

---

## 🐧 วิธีใช้งานบน Linux

1. **ติดตั้ง Docker Engine**  
   ดูวิธีติดตั้งได้ที่ [วิธีติดตั้งจากเว็บหลัก(Ubuntu)](https://docs.docker.com/engine/install/ubuntu/)
2. **โหลดโค้ดโปรเจกต์มาที่เครื่อง**  
   เปิด Terminal แล้วรัน
    ```bash
    git clone https://github.com/LiquiditySweep/Test
    cd two-api-demo
    ```
3. **สั่ง Build และ Run ทั้งสอง API**
    ```bash
    docker compose up --build -d
    ```

---

## 🧪 ทดสอบการทำงาน

### 1. ทดสอบ API1 (ซึ่งจะเชื่อมต่อไป API2 ให้เอง)

ไม่ว่าจะใช้ Windows หรือ Linux ให้รันคำสั่งนี้ (หรือใช้ browser ก็ได้)
```sh
curl "http://localhost:8001/call-api2?name=John"
