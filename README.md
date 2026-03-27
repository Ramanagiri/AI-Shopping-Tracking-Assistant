# 🤖 AI Shopping & Tracking Assistant

An intelligent AI agent that monitors e-commerce product prices and tracks shipments in real time, sending smart alerts directly to users via WhatsApp.

---

## 🚀 Features

* 🛍️ Track product prices from multiple platforms (Amazon, Flipkart, Myntra)
* 📉 Detect price drops and best deals using AI
* 🚚 Track shipments via FedEx API
* 💬 Send real-time alerts on WhatsApp
* 🧠 AI-powered insights (Is it a good deal or not?)
* 🔌 Extensible architecture (add more services easily)

---

## 🧠 Tech Stack

* **Backend:** FastAPI (Python)
* **Scraping:** Playwright
* **AI Engine:** OpenAI GPT
* **Messaging:** Twilio WhatsApp API
* **Database (optional):** Firebase / PostgreSQL
* **Scheduler:** Async loop / Cron jobs

---

## 📁 Project Structure

```
ai-shopping-agent/
│
├── app.py                 # FastAPI server
├── config.py              # Environment variables
├── scheduler.py           # Background job runner
│
├── services/
│   ├── amazon.py          # Amazon scraper
│   ├── fedex.py           # FedEx tracking
│   └── ai_engine.py       # AI analysis
│
├── utils/
│   └── whatsapp.py        # WhatsApp messaging
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-shopping-agent.git
cd ai-shopping-agent
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 3. Configure Environment Variables

Create a `.env` file:

```
TWILIO_SID=your_sid
TWILIO_AUTH=your_auth_token
OPENAI_API_KEY=your_openai_key
FEDEX_API_KEY=your_fedex_key
```

---

## ▶️ Running the Application

### Start API Server

```bash
uvicorn app:app --reload
```

### Start Scheduler (Price Monitoring)

```bash
python scheduler.py
```

---

## 🔄 How It Works

1. User sets a product to track
2. Scheduler checks product price periodically
3. AI analyzes if it's a good deal
4. Alert is sent via WhatsApp
5. User receives real-time updates

---

## 📡 API Endpoints

### Health Check

```
GET /
```

### Track Shipment

```
GET /track/{tracking_number}
```

---

## 💬 WhatsApp Integration

* Uses Twilio WhatsApp Sandbox for development
* Requires WhatsApp Business API approval for production

---

## 🚧 Limitations

* Amazon scraping may be blocked without proxies
* Flipkart & Myntra require custom scraping logic
* WhatsApp messaging requires user opt-in

---

## 🔮 Future Enhancements

* Multi-user support with authentication
* Flipkart & Myntra full integration
* Price history & analytics dashboard
* Telegram bot integration
* AI-based “Buy Now vs Wait” prediction
* Dockerized deployment

---

## 🧩 Extending the Project

To add a new platform:

1. Create a new scraper in `/services`
2. Follow the base scraper interface
3. Register it in the main service loader

---

## 🛡️ Disclaimer

This project uses web scraping for educational purposes. Ensure compliance with each platform’s terms of service before using in production.

---

## ⭐ Contributing

Pull requests are welcome! Feel free to fork and improve the project.

---

## 📬 Contact

For queries or collaboration:

* Email: [ramanagiria@gmil.com](mailto:ramanagiria@gmil.com)
* GitHub: ramanagiri

---

## 🏆 Project Title

**AI Shopping & Tracking Assistant**
*Track smarter. Shop better. Stay updated.*

---
