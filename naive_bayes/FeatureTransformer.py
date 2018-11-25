from tokenizer import  tokenize_sentences


class FeatureTransformer():

    def fit(self, *_):
        return self

    def transform(self, X, y=None, **fit_params):
        result = X.apply(lambda text: tokenize_sentences(text))
        return result
