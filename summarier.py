# import nltk
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize, sent_tokenize

# # method to generate summary of passed text using nltk library
# def summaryGenerator(text):
    
#     # Tokenizing the text
#     stopWords = set(stopwords.words("english"))
#     words = word_tokenize(text)

#     # Creating a frequency table to keep the score of each word
   
#     freqTable = dict()
#     for word in words:
#         word = word.lower()
#         if word in stopWords:
#             continue
#         if word in freqTable:
#             freqTable[word] += 1
#         else:
#             freqTable[word] = 1
    
#     # Creating a dictionary to keep the score of each sentence
#     sentences = sent_tokenize(text)
#     sentenceValue = dict()
   
#     # for sentence in sentences:
#     #     for word, freq in freqTable.items():
#     #         if word in sentence.lower():
#     for sentence in sentences:
#         lower_sentence = sentence.lower()
#         for word, freq in freqTable.items():
#             if word in lower_sentence:

#                 if sentence in sentenceValue:
#                     sentenceValue[sentence] += freq
#                 else:
#                     sentenceValue[sentence] = freq

#     sumValues = 0
#     for sentence in sentenceValue:
#         sumValues += sentenceValue[sentence]

#     # Average value of a sentence from the original text
#     # average = int(sumValues / len(sentenceValue))
#     total_words = sum(len(sentence.split()) for sentence in sentences)
#     average = int(sumValues / total_words) if total_words > 0 else 0


#     # Storing sentences into our summary.
#     summary = ''
#     for sentence in sentences:
#         if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
#             summary += " " + sentence
    
#     print(summary)
#     return summary


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def generate_summary(text):
    # Tokenizing the text
    stop_words = set(stopwords.words("english"))
    words = word_tokenize(text.lower())  # Convert all words to lowercase for consistency

    # Creating a frequency table to keep the score of each word
    freq_table = {word: words.count(word) for word in words if word not in stop_words}

    # Creating a dictionary to keep the score of each sentence
    sentences = sent_tokenize(text)
    sentence_value = {sentence: sum(freq_table.get(word, 0) for word in word_tokenize(sentence.lower())) for sentence in sentences}

    # Print intermediate values for debugging
    print("Frequency Table:", freq_table)
    print("Sentence Value:", sentence_value)

    sum_values = sum(sentence_value[sentence] for sentence in sentence_value)
    
    # Average value of a sentence from the original text
    total_words = sum(len(sentence.split()) for sentence in sentences)
    average = int(sum_values / total_words) if total_words > 0 else 0

    # Print intermediate values for debugging
    print("Sum Values:", sum_values)
    print("Total Words:", total_words)
    print("Average:", average)

    # Storing sentences into our summary
    summary = ' '.join(sentence for sentence in sentences if sentence_value.get(sentence, 0) > (1.2 * average))
    
    print("Final Summary:", summary)
    return summary

# Test your function
text = "Your input text goes here."
generate_summary(text)
