# 📱 Phone Price Scraper                                                                     
In this web-scraper project, I collected data on mobile phones from [rozetka.com](https://rozetka.com.ua/ua/mobile-phones/c80003/), performed data cleaning, and conducted data analysis.

---

## 📄 Data Fields Collected (JSON, CSV):
- **phone_name** – full name of the phone  
- **status** – availability of the phone on the website  
- **rating** – phone rating  
- **bonus** – bonuses received upon purchase  
- **price_before_discount** – price before discount (if any)  
- **price** – regular/discounted price  

## 📄 Data Fields Collected (CSV) after Data Cleaning:
- **phone_name** – full name of the phone  
- **status** – availability of the phone on the website  
- **rating** – phone rating  
- **bonus** – bonuses received upon purchase  
- **price_before_discount** – price before discount (if any)  
- **price** – regular/discounted price  
- **brand** – phone brand  
- **discount_procent** – discount percentage  

---

## Output Data(JSON):
```bash
{
    "brand": "Мобільний телефон Samsung Galaxy S24 FE 8/256GB Graphite (SM-S721BZKGEUC)",
    "status": "Готовий до відправлення",
    "rating": "145",
    "bonus": "234",
    "price_before_discount": "26099",
    "price": "23499"
}
```

## Output Data(CSV):
```bash
phone_name,status,rating,bonus,price_before_discount,price                                                                                                                                                                                
Мобільний телефон Samsung Galaxy S24 FE 8/256GB Graphite (SM-S721BZKGEUC),Готовий до відправлення,145,234,26099,23499
Мобільний телефон Apple iPhone 16 Pro Max 256GB Black Titanium (MYWV3SX/A),Готовий до відправлення,128,627,67999,62799
Мобільний телефон Samsung Galaxy A16 8/256GB Black (SM-A165FZKCEUC),Готовий до відправлення,137,73,8499,7399
Мобільний телефон Samsung Galaxy Fold 7 12/512GB Silver Shadow (SM-F966BZSCSEK),Передзамовлення,1,849,89999,84999
```

## Output Data(CSV) after Data Cleaning:
```bash
phone_name,status,rating,bonus,price_before_discount,price,brand,discount_procent                                                                                                                                                          
samsung galaxy s24 fe 8/256gb graphite (sms721bzkgeuc),Готовий до відправлення,145,234,26099,23499,samsung,10
apple iphone 16 pro max 256gb black titanium (mywv3sx/a),Готовий до відправлення,128,627,67999,62799,apple,8
samsung galaxy a16 8/256gb black (sma165fzkceuc),Готовий до відправлення,137,73,8499,7399,samsung,13
samsung galaxy fold 7 12/512gb silver shadow (smf966bzscsek),Передзамовлення,1,849,89999,84999,samsung,6
```

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
