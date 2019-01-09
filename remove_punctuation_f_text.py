*** we basically define a function that splits off "&" and removes other punctuation. ***

def clean_text(x):

    x = str(x)
    for punct in "/-'":
        x = x.replace(punct, ' ')
    for punct in '&':
        x = x.replace(punct, f' {punct} ')
    for punct in '?!.,"#$%\'()*+-/:;<=>@[\\]^_`{|}~' + '“”’':
        x = x.replace(punct, '')
    return x


# apply to data frame "example'
train["question_text"] = train["question_text"].progress_apply(lambda x: clean_text(x))

# split to words
sentences = train["question_text"].apply(lambda x: x.split())
