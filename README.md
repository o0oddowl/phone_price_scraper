# 📱 Phone Price Scraper                                                                     
In this web-scraper project, I collected data on mobile phones from [rozetka.com](https://rozetka.com.ua/ua/mobile-phones/c80003/), performed data cleaning, and conducted data analysis.

---

## 📄 Data Fields Collected (JSON, CSV):
- **brand** – phone brand  
- **status** – availability of the phone on the website  
- **rating** – phone rating  
- **bonus** – bonuses received upon purchase  
- **price_before_discount** – price before discount (if any)  
- **price** – regular/discounted price  

## 📄 Data Fields Collected (CSV) after Data Cleaning:
- **brand** – phone brand  
- **status** – availability of the phone on the website  
- **rating** – phone rating  
- **bonus** – bonuses received upon purchase  
- **price_before_discount** – price before discount (if any)  
- **price** – regular/discounted price  
- **discount_procent** – discount percentage  

---

## 📊 Data Insights and Analysis
This section provides key insights derived from the cleaned dataset, including pricing trends, brand statistics, and product rankings:
- 🔢 **Number of unique phone brands**
- 💰 **Average (mean) price per brand**
- 📈 **Distribution of phone prices**
- 🏪 **Distribution of phones by availability status on the website**
- 💎 **Top 5 most expensive phones**
- 🪙 **Top 5 most affordable phones**
- ⭐ **Top 5 phones with the highest ratings**
- ⚠️ **Top 5 phones with the lowest ratings**
- 🔻 **Top 5 phones with the highest discounts**

---

## 📁 Project Structure
```text
price_watcher_ua/
├── src/
│   ├── data_analysis/
│   │   ├── clean_data.py
│   │   └── data_analysis.ipynb
│   └── scraper/
│       └── scraper.py
├── data/
│   ├── mobile_price.csv
│   ├── mobile_price.json
│   └── clean_mobile_price.csv
├── html_file/
│   └── rozetkapage1.html, rozetkapage2.html, ..., ~rozetkapage93.html  # HTML pages saved by the script
└── requirements.txt
```

---

## ⚙️ Requirements
- Python 3.11  
- Firefox (used with Selenium — can be replaced with another browser in the code)

### Python Libraries
Install dependencies using:
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Scrapers
To run the scraper:
```bash
python3.11 src/scraper/scraper.py
```
To run the data cleaning:
```bash
python3.11 src/data_analysis/clean_data.py
```
To run the data analysis Jupyter Notebook:
```text
Open the data_analysis.ipynb file using Jupyter Notebook or JupyterLab. 
You can launch Jupyter Notebook with the command:
jupyter notebook
Then navigate to the notebook file in your browser and run the cells step by step to explore data visualizations, statistics,
and insights generated from the cleaned phone pricing dataset.
```
