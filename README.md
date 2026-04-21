# 📧 Email Automation Project (Quotes + Weather API)

This project automates sending **personalized email content** by combining:
- 📜 Inspirational quotes (from a scraped dataset)
- 🌤️ Live weather data (from OpenWeatherMap API)

It demonstrates API integration, data reuse from previous projects, and automated email workflows using Python.

---

## 🚀 Overview

The system sends automated emails containing:
- A random inspirational quote  
- Current weather information based on API data  

This project connects multiple components:
- A previous **quotes scraping project**
- External **weather API integration**
- Email automation via SMTP

---

## 📁 Project Structure

```bash id="email-structure"
email-automation/
├── Quotes.csv
├── email_content.py
├── email_main.py
