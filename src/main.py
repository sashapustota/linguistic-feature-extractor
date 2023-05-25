import os
import spacy
import pandas as pd
import warnings

# Ignore all warnings
warnings.filterwarnings("ignore")

def main():
# Loading the spacy model
    if not spacy.util.is_package("en_core_web_md"):
        spacy.cli.download("en_core_web_md")

    nlp = spacy.load("en_core_web_md")

    # Defining paths to the main folder (USEcorpus) and the respective subfolders
    path_to_folder = os.path.join(os.getcwd(), "in", "USEcorpus")
    subfolders = os.listdir(path_to_folder)

    # Making sure .DS_Store does not cause us any troubles
    subfolders = [x for x in subfolders if os.path.isdir(os.path.join(path_to_folder, x))]

    print("Starting to process the files...")

    # Loop over subfolders
    for x in subfolders:

        # Defining path to subfolder
        folder = os.path.join(path_to_folder, x)

        # Creating empty dataframe (1 dataframe per subfolder)
        df = pd.DataFrame(columns=["text_name", "RelFreq_NOUN", "RelFreq_VERB", "RelFreq_ADJ", "RelFreq_ADV", "Unique_PER", "Unique_LOC", "Unique_ORG"])
        
        # Making a list of files in the subfolder
        list_of_files = os.listdir(folder)

        # Making it a bit robust by only selecting .txt files
        list_of_files = [x for x in list_of_files if x.endswith(".txt")]

        # Iterating over the .txt files in the subfolder
        for y in list_of_files:

            # Loading the .txt file
            file_path = os.path.join(folder, y)
            f = open(file_path, "r", encoding="ISO-8859-1")
            file = f.read()
            
            # Convert the file to a spacy object
            file_text = nlp(file)
            
            # Creating empty lists for each word category for counting
            non_words_counter = 0
            nouns = []
            verbs = []
            adjectives = []
            adverbs = []
            PER = []
            LOC = []
            ORG = []

            # Looping over each token in the text and appending the tokens to the correct list
            for token in file_text:
                # This is to make sure that the relative frequencies are calculated correctly (excluding punctuation, spaces, etc.)
                if token.pos_ == "X" or token.pos == "PUNCT" or token.pos == "SPACE" or token.pos == "SYM":
                    non_words_counter += 1
                if token.pos_ == "NOUN":
                    nouns.append(token.text)
                if token.pos_ == "VERB":
                    verbs.append(token.text)
                if token.pos_ == "ADJ":
                    adjectives.append(token.text)
                if token.pos_ == "ADV":
                    adverbs.append(token.text)
                if token.ent_type_ == "PER":
                    PER.append(token.text)
                if token.ent_type_ == "LOC":
                    LOC.append(token.text)
                if token.ent_type_ == "ORG":
                    ORG.append(token.text)
            
            # Calculating the relative frequencies and the amount of unique entities
            RelFreq_NOUN = round(len(nouns) / (len(file_text) - non_words_counter) * 10000, 2)
            RelFreq_VERB = round(len(verbs) / (len(file_text) - non_words_counter) * 10000, 2)
            RelFreq_ADJ = round(len(adjectives) / (len(file_text) - non_words_counter) * 10000, 2)
            RelFreq_ADV = round(len(adverbs) / (len(file_text) - non_words_counter) * 10000, 2)
            Unique_PER = len(set(PER))
            Unique_LOC = len(set(LOC))
            Unique_ORG = len(set(ORG))
            
            # Appending the results to the dataframe
            df = df.append({"text_name": y, "RelFreq_NOUN": RelFreq_NOUN, "RelFreq_VERB": RelFreq_VERB, "RelFreq_ADJ": RelFreq_ADJ, "RelFreq_ADV": RelFreq_ADV, "Unique_PER": Unique_PER, "Unique_LOC": Unique_LOC, "Unique_ORG": Unique_ORG}, ignore_index=True)
        

        # Sort the dataframe by the name of the text
        df = df.sort_values(by=["text_name"], ignore_index=True)

        # Saving the dataframe for a folder as a .csv file
        df.to_csv(os.path.join(os.getcwd(), "out", x + ".csv"))

    print("Done!")

if __name__ == "__main__":
    main()