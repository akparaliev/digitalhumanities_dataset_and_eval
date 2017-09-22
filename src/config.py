import sys

if len(sys.argv) < 2:
    raise Exception("We need two command line arguments!")
if sys.argv[1].lower() == 'asoif':
    BOOK_SERIES="ASIOF"
elif sys.argv[1].lower() == 'hp':
    BOOK_SERIES="HP" ## new
else:
    raise Exception("the book series must be either *ASOIF* or *HP*")


MODEL_PATH="../models/"
# ------------------------------------------------------------

if BOOK_SERIES == "ASIOF":
    METHODS = [
        ('asoif_w2v-default','bin'), ## word 2 vec default settings
        ('asoif_w2v-ww12-300','bin'), ## default and: window-size 12, 300dim, hier.softmax, iter 15 
        ('asoif_w2v-ww12-300-ns','bin'), ## default and: window-size 12, 300dim, hier.softmax, iter 15 
        ('asoif_w2v-CBOW', 'bin'),
        ('asoif_glove', 'vec'), 
        ('asoif_lexvec', 'vec'), 
        ('asoif_fastText', 'vec'), # default and: -epoch 25 -ws 12
    ]

if BOOK_SERIES == "HP":
    METHODS = [
        ('hp_lexvec', 'vec'),
        ('hp_fasttext', 'vec'),  # for paper!, 25 epoch
        ('hp_glove', 'vec'), 
        ('hp_w2v-default', 'bin'),
        ('hp_w2v-ww12-300', 'bin'),
        ('hp_w2v-ww12-300-ns', 'bin'),
        ('hp_w2v-CBOW', 'bin'),
    ]


# -----------------------------------------------------
# for "doesnt_match" evaluation script
# -----------------------------------------------------

if BOOK_SERIES == "ASIOF":
    DOESNT_MATCH_FILE = "../datasets/questions_soiaf_doesn_match.txt"
    ANALOGIES_FILE = "../datasets/questions_soiaf_analogies.txt"

    ### which sections to show in the paper..
    ANALOGIES_SECTIONS = ['firstname-lastname', 'child-father', 'husband-wife', 'geo-name-location', 'houses-seats']
    DOESNT_MATCH_SECTIONS = [': family-siblings',  ': names-of-houses', ': archmaesters', ': rivers', ': free cities']


if BOOK_SERIES == "HP":
    DOESNT_MATCH_FILE = "../datasets/questions_hp_doesn_match.txt"
    ANALOGIES_FILE = "../datasets/questions_hp_analogies.txt"
    
    ANALOGIES_SECTIONS = ['firstname-lastname', 'child-father', 'husband-wife', 'pets-of-Hagrid', 'total']
    DOESNT_MATCH_SECTIONS = [': family-siblings', ': Hogwarts-houses', ': professors', ': wizarding-equipment', ': magic-creatures'] 

