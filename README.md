# 💬 Comment Classification Telegram Bot

## 🤖 About the Project

This is a Telegram bot designed to classify text comments as `Positive`, `Negative`, or `Neutral`. 
The bot is built using the `pyTelegramBotAPI` library and a machine learning model trained with `Scikit-learn`.
The core functionality involves a pre-trained model that analyzes any English text sent to the bot and provides a quick sentiment classification.

---

### ✨ Key Features

- **Sentiment Analysis**: Automatically classifies incoming text messages into one of three categories: Positive, Negative, or Neutral.
- **Simple Interface**: The bot is easy to use. Just send a text message, and it will respond with the classification.
- **Start Command**: Users can initiate interaction with the bot using the `/start` command.

---

## 🗂️ Project Structure

```

project-root/
├── 📄 Untitled.ipynb                      # Main notebook: full ML pipeline from preprocessing to submission
├── 📊 negative_comments_1000_raw.csv      # Dataset of negative comments
├── 📊 outubeCommentsDataSet.csv           # Dataset of YouTube comments
├── 📝 model.pkl                           # The trained machine learning model
└── 🚀 bot.py                              # The main script for the Telegram bot  
└── 📜 README.md                           # Project documentation

```

---

## 💻 Technologies Used

- **Language**: Python 3.x  
- **Environment**: Jupyter Notebook
- **Environment**: Visual Studio Code
- **Telegram Bot API**: pyTelegramBotAPI


## 🛠️ Model Development Tools

The model training and development process was performed in a Jupyter Notebook using the following key Python libraries and tools:

- **`NumPy` and `Pandas`**: For data manipulation and analysis.
- **`Matplotlib` and `Seaborn`**: To visualize the results of the data analysis and the model's performance.
- The two raw datasets, `YoutubeCommentsDataSet.csv` and `negative_comments_1000_raw.csv`, were concatenated to create a single, comprehensive training dataset.
- **`Scikit-learn`**: The primary machine learning library. It was used for data preprocessing, model training, and testing. Specifically, the following were used:
  - `TfidfVectorizer`: To convert text data into numerical vectors that the model can understand.
  - `LabelEncoder`: For categorical encoding of the target variable.
  - `Pipeline`: To combine preprocessing and modeling steps into a single, streamlined workflow.
- **`xgboost`**:
  - `XGBClassifier`: A gradient boosting classifier used for building the final predictive model.
- **`GridSearchCV`**: For hyperparameter tuning to find the optimal settings for the model.
- **`Pickle`**: To save the trained model into the `model.pkl` file, allowing it to be used by the bot without retraining every time.
- **`warnings`**: To suppress warnings during the execution of the notebook.

---
## 🚀 How to Set Up and Run

Follow these steps to get the bot up and running on your local machine.

### 📦 Prerequisites

- **Python 3.x**  
- **pip** (Python package manager)  

### ⚙️ Installation Steps

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/DavtianAnna/CommentClassifierBot.git
   cd CommentClassifierBot

2. **Install dependencies:**  
   Install all the required Python libraries using pip:  
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn xgboost

3. **Get Telegram Bot Token:**  
   - Open Telegram and message [@BotFather](https://t.me/BotFather)  
   - Send the `/newbot` command and follow the instructions  
   - Copy the token provided after bot creation  

4. **Configure the bot:**  
   Open `bot.py` and replace the placeholder token with your actual Telegram bot token:  
   ```python
   TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

5. **Run the bot:**  
   Start the bot by executing the following command in your terminal:  
   ```bash
   python bot.py














