# MindSentiment AI Service

AI Microservice untuk platform **MindSentiment** yang bertugas melakukan:

* Analisis sentimen jurnal harian pengguna
* Deteksi risiko burnout berdasarkan jurnal mingguan
* Generasi feedback personal menggunakan Google Gemini AI
* Penerjemahan otomatis jurnal ke Bahasa Inggris sebelum proses klasifikasi

Dibangun menggunakan **FastAPI**, **TensorFlow/Keras**, dan **Google Gemini API**.

---

## Fitur Utama

### 1. Journal Sentiment Classification

Menganalisis isi jurnal pengguna dan mengklasifikasikannya ke dalam tiga kategori:

* Positive
* Neutral
* Negative

Proses yang dilakukan:

1. Input jurnal pengguna
2. Auto translate ke Bahasa Inggris
3. Text preprocessing
4. Sentiment prediction menggunakan model TensorFlow
5. Mengembalikan label sentimen

---

### 2. Weekly Burnout Analysis

Menganalisis pola emosi pengguna selama 7 hari terakhir berdasarkan hasil klasifikasi jurnal.

State yang dapat dihasilkan:

| State                 | Deskripsi                             |
| --------------------- | ------------------------------------- |
| Healthy               | Kondisi emosional sehat               |
| Stable                | Stabil secara emosional               |
| Adjustment Needed     | Membutuhkan penyesuaian atau refleksi |
| Emotional Instability | Emosi tidak stabil                    |
| Burnout Risk          | Risiko burnout                        |
| Severe Burnout        | Indikasi burnout berat                |

---

### 3. AI Personalized Feedback

Setelah burnout analysis selesai, sistem akan menghasilkan respon personal menggunakan Gemini AI.

Jenis feedback:

* Motivation
* Support
* Adjustment Suggestion
* Congratulations

Prompt akan dipilih secara otomatis berdasarkan kondisi emosional pengguna.

---

## Project Structure

```bash
app/
│
├── main.py
│
├── models/
│   ├── model.keras
│   ├── tokenizer.pkl
│   └── label_encoder.pkl
│
├── routers/
│   ├── classify_router.py
│   └── burnout_router.py
│
├── services/
│   ├── classification_service.py
│   ├── burnout_service.py
│   ├── genai_service.py
│   └── translation_service.py
│
├── schemas/
│   ├── classify_schema.py
│   ├── burnout_schema.py
│   └── response_schema.py
│
├── prompts/
│   ├── motivation_prompt.py
│   ├── support_prompt.py
│   ├── adjustment_prompt.py
│   └── congrats_prompt.py
│
├── utils/
│   ├── preprocessing.py
│   ├── context_builder.py
│   └── burnout_engine.py
│
└── main.py
```

---

## Tech Stack

### Backend

* FastAPI
* Pydantic

### Machine Learning

* TensorFlow
* Keras
* NumPy

### NLP

* Deep Translator
* Custom Text Preprocessing

### Generative AI

* Google Gemini 2.5 Flash

---

## Installation

### Clone Repository

```bash
git clone https://github.com/ALPHARESZ/Mind_Sentiment.git

cd Mind_Sentiment
```

### Create Virtual Environment

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Dapatkan API key Gemini:

1. Kunjungi situs web resmi Google AI Studio
2. Masuk (login) menggunakan akun Google Anda
3. Pada panel navigasi di sebelah kiri, klik menu Get API key (Dapatkan kunci API)
4. Klik tombol Create API key (Buat kunci API)
5. Anda dapat memilih untuk membuat API Key di project baru atau project Google Cloud yang sudah ada
6. Buat file `.env`

```env
GEN_AI_API_KEY=your_gemini_api_key
```

---

## Running Service

```bash
uvicorn app.main:app --reload
```

Server akan berjalan pada:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

ReDoc:

```text
http://localhost:8000/redoc
```

---

# API Documentation

---

## Health Check

### Request

```http
GET /
```

### Response

```json
{
  "message": "AI Service Running"
}
```

---

# Sentiment Classification API

## Endpoint

```http
POST /classify
```

### Request Body

```json
{
  "content": "Hari ini saya merasa sangat lelah dengan pekerjaan."
}
```

### Response

```json
{
  "translated_text": "Today I feel very tired with work.",
  "label": "negative"
}
```

### Response Fields

| Field           | Description                        |
| --------------- | ---------------------------------- |
| translated_text | Hasil terjemahan ke Bahasa Inggris |
| label           | Hasil klasifikasi sentimen         |

---

# Weekly Burnout Analysis API

## Endpoint

```http
POST /analyze-weekly-journal
```

### Request Body

```json
{
  "journals": [
    {
      "translated_text": "I feel tired today.",
      "label": "negative"
    },
    {
      "translated_text": "Work is overwhelming.",
      "label": "negative"
    },
    {
      "translated_text": "I feel exhausted.",
      "label": "negative"
    },
    {
      "translated_text": "Still stressed.",
      "label": "negative"
    },
    {
      "translated_text": "No motivation today.",
      "label": "negative"
    },
    {
      "translated_text": "Feeling down.",
      "label": "negative"
    },
    {
      "translated_text": "Very exhausted.",
      "label": "negative"
    }
  ]
}
```

### Response

```json
{
  "state": "Severe Burnout",
  "message": "Generated motivational response from Gemini AI..."
}
```

### Response Fields

| Field   | Description                          |
| ------- | ------------------------------------ |
| state   | Kondisi emosional pengguna           |
| message | Feedback personal yang dihasilkan AI |

---

# Burnout Detection Logic

Sistem menggunakan beberapa indikator:

### Negative Streak

Jumlah hari negatif berturut-turut.

### Volatility

Frekuensi perubahan emosi selama seminggu.

### Recovery Score

Jumlah transisi dari:

```text
Negative → Positive
```

### Recent Trend

Memberikan bobot lebih tinggi pada hari-hari terbaru.

Contoh bobot:

```text
[1, 2, 3, 4, 5, 6, 7]
```

Sehingga kondisi terbaru memiliki pengaruh lebih besar dibanding hari-hari awal.

---

## AI Feedback Generation

Sistem menggunakan Google Gemini untuk menghasilkan feedback yang lebih personal.

Prompt akan dipilih berdasarkan hasil burnout analysis:

| State                 | Prompt Mode     |
| --------------------- | --------------- |
| Severe Burnout        | Motivation      |
| Burnout Risk          | Motivation      |
| Emotional Instability | Support         |
| Adjustment Needed     | Adjustment      |
| Healthy               | Congratulations |
| Stable                | Support         |

---