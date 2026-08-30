# sentiment.py takes a pretrained model and returns an integer score based on sentiment
from transformers import pipeline

# setting threshold to throw out week confidence responses
THRESHOLD = 0.65

def analyze_sentiment(text):

    # initialize the sentiment analysis pipeline
    classifier = pipeline(
        "text-classification", 
        model="cardiffnlp/twitter-roberta-base-sentiment-latest"
    )

    # gets label back to integer
    label_to_id = classifier.model.config.label2id


    # analysis
    result = classifier(text, truncation=True, max_length=512)
    
    label = result[0]['label']
    
    integer_label = label_to_id[label.lower()] 
    

    # throwing out uncertain results (any confidence level below 0.65)
    if result[0]['score'] < THRESHOLD:
        final_int_label = -1
    else:
        final_int_label = integer_label


    return final_int_label