# Reddit Sentiment

Reddit Sentiment takes finance subreddits and analyzes their sentiments to determines whether the market is bearish, bullish, or neutral on the given day.

## Description

Based on finance subreddits, Reddit Sentiment finds suitibly long posts and using Hugging Face Transformers library, analyzes if their sentiment is Negative (0), Neutral (1), or Positive (2). 

 It stores the sentiment integer values for posts that reach a confidence threashold of 0.65 or higher in a database that can be accessed by date. It calculates an average score for a chosen day, and based on this score, it determines whether the market is bearish, bullish, or neutral.

## Getting Started

### Dependencies

* Describe any prerequisites, libraries, OS version, etc., needed before installing program.
* ex. Windows 10

### Installing

* How/where to download your program
* Any modifications needed to be made to files/folders

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
