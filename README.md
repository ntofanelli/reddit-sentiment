# Reddit Based Stock Market Sentiment Tracker

This project analyzes text data gathered from various subreddits to predict whether the stock market sentiment is bullish, bearish, or neutral.

## Description

Using SocialCrawl's API, we collect text from various finance related subreddits and use an AI from Hugging Face's transformers library to judge the sentiment of each post. The model assigns an integer to each post based on how positive(2) or negative(1) the text is. We then find the average rating of all posts checked, which tells us the average market sentiment. The data is then stored in a database using SQLite. The amount of posts, subreddits, and newness of the posts can be configured individually.


## Getting Started

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10


### Executing program

* How to run the program
* Step-by-step bullets
```
code blocks for commands
```

## Help

Any advise for common problems or issues.
```
command to run if program contains helper info
```

## Authors

Contributors names and contact info

ex. Dominique Pizzie  
ex. [@DomPizzie](https://twitter.com/dompizzie)

## Version History

* 0.2
    * Various bug fixes and optimizations
    * See [commit change]() or See [release history]()
* 0.1
    * Initial Release

## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details

## Acknowledgments

Inspiration, code snippets, etc.
* [awesome-readme](https://github.com/matiassingers/awesome-readme)
* [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
* [dbader](https://github.com/dbader/readme-template)
* [zenorocha](https://gist.github.com/zenorocha/4526327)
* [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46)

## References

- **Library:** [Hugging Face Transformers](https://github.com) — Wolf, T. et al. (2020). *Transformers: State-of-the-Art Natural Language Processing*.
- **Model:** [DistilBERT Base Uncased SST-2](https://huggingface.co) — The pre-trained model checkpoint used for sentiment classification inference.
