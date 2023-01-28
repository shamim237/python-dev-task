# python-dev-task-summarization

The task has been done in two methods-
- **using traditional Python libraries (like NLTK,Sumy)**
- **using pre-trained transformers model**

# Method 1
## using traditional Python libraries
#### Web Scraping Tools:
- Selenium
#### Paraphrasing Tools:
- used [nlpaug](https://github.com/makcedward/nlpaug) library
#### Summarization Tools:
- used [sumy](https://miso-belica.github.io/sumy/) library
#### System Requirements:
- you will find it in the _requirements.txt_ file

## How to test or run this?
- just open this link and follow the instructions: _**https://shamim237-python-dev-task-app-3n18pu.streamlit.app/**_

# Method-2
## Using pre-trained transformers model
#### Web Scraping Tools: 
- ScrapperAPI
- BeautifulSoup
#### Paraphrasing Tools:
- used **"ramsrigouthamg/t5-large-paraphraser-diverse-high-quality"** pre-trained model from HuggingFace
#### Summarization Tools:
- used **/"google/pegasus-cnn_dailymail"/** pre-trained model from HuggingFace
#### System Requirements:
- you will find it in the _Python_Dev_Task.ipynb_ notebook or in the below link.

## How to test or run this?
- Just open the **"Python_Dev_Task.ipynb"** file in Colab _or_ open this link: **_https://colab.research.google.com/drive/1wwaj0TobsnzQL5jMVsYrF5z6rc1944tE?usp=sharing_**
- Run all the cell 
- The summarization output will show up in the last cell of the notebook.
