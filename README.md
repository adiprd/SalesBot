# Sales Analytics Chatbot

Sistem chatbot dengan fitur visualisasi data untuk analitik penjualan dari database MySQL. Platform ini menggabungkan kecerdasan buatan dengan dashboard interaktif untuk memberikan insights bisnis yang komprehensif.

## Gambaran Umum

Sales Analytics Chatbot adalah solusi all-in-one untuk analisis data penjualan yang memungkinkan pengguna untuk:
- Berinteraksi dengan AI assistant melalui chat natural
- Memvisualisasikan data penjualan dengan grafik interaktif
- Menganalisis performa produk, kategori, dan pelanggan
- Melihat tren penjualan secara real-time

## Fitur Utama

### AI Chat Assistant
- Percakapan natural dalam Bahasa Indonesia dan Inggris
- Pemahaman konteks untuk query data penjualan
- Respons berbasis data real-time dari database
- Formatting angka dengan pemisah ribuan

### Dashboard Analitik
- **Ringkasan Penjualan**: Total penjualan, revenue, average order value, jumlah pelanggan
- **Produk Terlaris**: Analisis performa produk berdasarkan revenue dan quantity
- **Kategori Produk**: Distribusi penjualan across product categories
- **Pelanggan Teratas**: Customer segmentation berdasarkan nilai transaksi
- **Tren Penjualan**: Analisis time series untuk identifikasi pola

### Visualisasi Data
- Chart.js untuk visualisasi interaktif
- Multiple chart types (bar, line, doughnut)
- Responsive design untuk berbagai device
- Real-time data updates

## Arsitektur Teknis

```
sales_chatbot/
├── backend/
│   └── app/
│       ├── main.py              # FastAPI application
│       ├── apirouter.py         # API endpoints definition
│       ├── llm_client.py        # OpenRouter API integration
│       ├── db_helper.py         # MySQL database operations
│       └── requirements.txt     # Python dependencies
├── frontend/
│   └── index.html              # Single-page web application
├── database/
│   ├── schema.sql              # Database schema
│   └── seeder.py               # Data population script
├── start_backend.py            # Backend launcher
├── start_frontend.py           # Frontend launcher
└── README.md                   # Documentation
```

## Teknologi yang Digunakan

### Backend
- **FastAPI**: Modern web framework for Python
- **MySQL**: Relational database management
- **OpenRouter API**: AI model gateway (sherlock-dash-alpha)
- **Uvicorn**: ASGI server implementation

### Frontend
- **HTML5**: Markup structure
- **CSS3**: Styling and responsive design
- **Vanilla JavaScript**: Client-side functionality
- **Chart.js**: Data visualization library

### AI & Data
- **OpenRouter Sherlock Dash Alpha**: Language model for natural language processing
- **MySQL Connector**: Database connectivity
- **Pandas**: Data manipulation and analysis

## Persyaratan Sistem

### Software Requirements
- Python 3.8+
- MySQL 5.7+
- Web browser modern (Chrome, Firefox, Safari)

### Python Dependencies
- fastapi
- uvicorn[standard]
- requests
- python-dotenv
- mysql-connector-python
- pydantic
- pandas
- python-multipart

## Instalasi dan Setup

### 1. Persiapan Environment

```bash
# Clone atau extract project
cd sales_chatbot

# Setup virtual environment (optional)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate    # Windows
```

### 2. Setup Database MySQL

```bash
# Import database schema
mysql -u root -p < database/schema.sql

# Populate dengan sample data
python database/seeder.py
```

### 3. Konfigurasi Backend

```bash
# Install dependencies
pip install -r backend/app/requirements.txt

# Jalankan backend
cd backend/app
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Atau gunakan script otomatis:
```bash
python start_backend.py
```

### 4. Jalankan Frontend

```bash
# Method 1: Python HTTP server
cd frontend
python -m http.server 8080

# Method 2: Gunakan script otomatis
python start_frontend.py
```

### 5. Akses Aplikasi

Buka browser dan akses: `http://localhost:8080`

Backend API akan berjalan di: `http://localhost:8000`

## Konfigurasi Database

Edit koneksi database di `db_helper.py` jika diperlukan:

```python
def get_connection():
    return mysql.connector.connect(
        host=os.environ.get("MYSQL_HOST", "localhost"),
        user=os.environ.get("MYSQL_USER", "root"),
        password=os.environ.get("MYSQL_PASSWORD", ""),
        database=os.environ.get("MYSQL_DATABASE", "sales_db")
    )
```

## API Endpoints

### Chat Endpoints
- `POST /api/chat` - Berinteraksi dengan AI assistant

### Analytics Endpoints
- `GET /api/analytics/summary` - Ringkasan metrics penjualan
- `GET /api/analytics/top-products` - Produk terlaris
- `GET /api/analytics/categories` - Penjualan per kategori
- `GET /api/analytics/top-customers` - Pelanggan teratas
- `GET /api/analytics/trend` - Tren penjualan time series

### Contoh Penggunaan API

```javascript
// Chat dengan AI
const response = await fetch('http://localhost:8000/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ 
        message: 'Tampilkan produk terlaris bulan ini' 
    })
});

// Ambil data ringkasan
const summary = await fetch('http://localhost:8000/api/analytics/summary')
    .then(r => r.json());
```

## Struktur Database

### Tabel Customers
- customer_id, name, email, phone, address, created_at

### Tabel Products  
- product_id, product_name, category, price, stock, created_at

### Tabel Sales
- sale_id, customer_id, sale_date, payment_method, total_amount, created_at

### Tabel Sale Items
- item_id, sale_id, product_id, quantity, price_each

## Penggunaan

### 1. Mode Chat
- Ketik pertanyaan natural tentang data penjualan
- Contoh: "Berapa total penjualan bulan ini?"
- AI akan merespons dengan insights berdasarkan data aktual

### 2. Dashboard Analytics
- Navigasi melalui menu sidebar untuk berbagai tipe analisis
- Visualisasi grafik interaktif untuk pemahaman data yang lebih baik
- Data tables untuk detail numerik

### 3. Query Examples
- "Tampilkan 5 produk dengan revenue tertinggi"
- "Bagaimana tren penjualan 30 hari terakhir?"
- "Siapa pelanggan dengan nilai transaksi terbesar?"
- "Distribusi penjualan berdasarkan kategori produk"

## Customization

### Mengubah Model AI
Edit `llm_client.py` untuk mengganti model OpenRouter:

```python
payload = {
    "model": "openrouter/sherlock-dash-alpha",  # Ganti dengan model lain
    # ... konfigurasi lainnya
}
```

### Menambah Analisis Baru
1. Tambahkan function di `db_helper.py`
2. Buat endpoint di `apirouter.py` 
3. Implement UI component di `index.html`

### Styling
Edit CSS dalam `index.html` untuk mengubah tampilan:
- Warna tema (current: #ffc107)
- Layout dan spacing
- Chart colors dan configurations

## Troubleshooting

### Masalah Umum

1. **Database Connection Error**
   - Pastikan MySQL service running
   - Periksa credentials di db_helper.py
   - Verify database 'sales_db' exists

2. **Backend Tidak Berjalan**
   - Check port 8000 tidak digunakan
   - Verify Python dependencies terinstall
   - Periksa error log di console

3. **Frontend Tidak Load Data**
   - Pastikan backend berjalan di port 8000
   - Check CORS configuration
   - Verify API endpoints accessible

4. **AI Responses Error**
   - Check OpenRouter API key validity
   - Verify model availability
   - Monitor API rate limits

### Debug Mode

Aktifkan debug dengan menambahkan print statements di kode:

```python
# Di db_helper.py
print(f"Executing query: {query}")

# Di llm_client.py  
print(f"API Response: {data}")
```

## Pengembangan Lanjutan

### Fitur yang Dapat Ditambahkan
- User authentication dan authorization
- Data export (PDF, Excel reports)
- Real-time notifications
- Advanced filtering dan segmentation
- Predictive analytics
- Multi-tenant support

### Performance Optimization
- Database indexing untuk query besar
- Caching frequent queries
- Async database operations
- Frontend lazy loading

### Security Enhancements
- Input validation dan sanitization
- API rate limiting
- SQL injection prevention
- HTTPS enforcement

## Kontribusi

Kontribusi untuk pengembangan dipersilakan. Area pengembangan potensial:

1. **AI Enhancements**: Fine-tuning model untuk domain spesifik
2. **Visualization**: Chart types tambahan dan customizations
3. **Integration**: Connectors untuk platform e-commerce
4. **Mobile**: Responsive mobile application

## Lisensi

Project ini menggunakan MIT License.

## Support

Untuk issues dan pertanyaan teknis:
1. Check troubleshooting section terlebih dahulu
2. Review error messages di browser console dan backend logs
3. Pastikan semua requirements terpenuhi

## Catatan Versi

### v1.0.0
- Implementasi dasar AI chat assistant
- Dashboard analytics dengan 5 visualization types
- MySQL database integration
- Responsive web interface
- OpenRouter API integration

---

**Sales Analytics Chatbot** - Transformasi data penjualan menjadi insights bisnis yang actionable melalui AI dan visualisasi interaktif.
