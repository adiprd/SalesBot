
# Sales Analytics Chatbot

Chatbot dengan fitur visualisasi data untuk analitik penjualan dari database MySQL.

## Setup

### 1. Backend (FastAPI)
```bash
cd backend
pip install -r app/requirements.txt
uvicorn app.main:app --reload --port 8000
```

### 2. Frontend (HTML)
Buka file `frontend/index.html` langsung di browser, atau jalankan dengan HTTP server:
```bash
cd frontend
python -m http.server 8080
```

Akses di browser: http://localhost:8080

## Fitur
- 💬 Chat dengan AI untuk query data penjualan
- 📊 Dashboard visualisasi data dengan Chart.js
- 🏆 Top products analysis
- 📦 Sales by category
- 👥 Top customers
- 📈 Sales trend analysis

## Database
Pastikan database `sales_db` sudah terisi dengan data menggunakan script faker yang sudah disediakan.

## Tech Stack
- **Backend**: FastAPI + MySQL
- **Frontend**: HTML + JavaScript + Chart.js
- **AI**: OpenRouter API (sherlock-dash-alpha model)

## API Endpoints
- `POST /api/chat` - Chat dengan AI assistant
- `GET /api/analytics/summary` - Ringkasan penjualan
- `GET /api/analytics/top-products` - Produk terlaris
- `GET /api/analytics/categories` - Penjualan per kategori
- `GET /api/analytics/top-customers` - Pelanggan teratas
- `GET /api/analytics/trend` - Tren penjualan

## Struktur Project
```
sales_chatbot/
├── backend/
│   └── app/
│       ├── __init__.py
│       ├── main.py
│       ├── apirouter.py
│       ├── llm_client.py
│       ├── db_helper.py
│       └── requirements.txt
└── frontend/
    └── index.html
```

## Notes
- Pastikan MySQL service sudah running
- API key sudah hardcoded menggunakan model sherlock-dash-alpha
- UI menggunakan tema kuning sederhana tanpa warna-warni
