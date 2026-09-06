# Reddit Based Stock Market Sentiment Tracker

This project analyzes text data gathered from various subreddits to predict whether the stock market sentiment is bullish, bearish, or neutral.

## Description

Using SocialCrawl's API, we collect text from various finance related subreddits and use an AI from Hugging Face's transformers library to judge the sentiment of each post. The model assigns an integer to each post based on how positive(2) or negative(1) the text is. We then find the average rating of all posts checked, which tells us the average market sentiment. The data is then stored in a database using SQLite. The amount of posts, subreddits, and newness of the posts can be configured individually.


## Getting Started

### Dependencies

* Refer to requirements.txt
* Add a functional API SocialCrawl key to a custom `.env` file


### Executing program

* Clone the repository
* Default subreddits are listed in `main.py`
  * r/wallstreetbets, r/stocks, r/pennystocks
* From the directory call `python3 main.py`


## Authors

[Noah Tofanelli](noahtofanelli@gmail.com)

[Landry Clarke](landry.clarke04@gmail.com)

## License

This project is licensed under the MIT License - see the LICENSE.md file for details


## References

- **Library:** [Hugging Face Transformers](https://github.com/huggingface/transformers) — Wolf, T. et al. (2020). *Transformers: State-of-the-Art Natural Language Processing*.
- **Model:** [DistilBERT Base Uncased SST-2](https://huggingface.co) — The pre-trained model checkpoint used for sentiment classification inference.
