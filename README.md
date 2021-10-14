# Project Goals:
>    - Create documented files to clean and prepare H4 Nucleosome Occupancy dataset for processing by modeling via a multiple classification ML and ANN algorithms.
>   - Use K-mers to create datasets from the raw genetic sequence data
>   - Pass K-mer datasets to a Bag of Words CountVectorizer
>   - Pass dataframes with new vectorized features and nucleotide counts to classification models.
>   - Find a model that hopefully outpreforms both the modal baseline and the best preforming model from the origin website

## Plan:
- [x] Create repo on github to save all files related to the project.
- [x] Create README.md with goals, initial hypotheses, data dictionary, and outline plans for the project in a trello board.
- [x] Acqiure H4 data using acquire.py file drawing directly from www.jaist.ac `H4` dataset.
- [x] Clean, tidy, and veectorize data in such a way that it is usable in a machine learning classification algorithm. Includes dropping unneccesary columns, cleaning IDs, checking for uniform length across sequences
- [x] Vectorize data by at least two different word sizes for classification
- [x] Look into the distribution of target variable and the frequency of nucleotide occurrances and frequency of vectors.
- [x] Scale data for better accuracy in models.
- [x] Establish a baseline accuracy.
- [x] Create models to classify vectorized datasets including Artificial Neural Network models.
- [x] Train different classification models testing a variety of hyper-parameters on at least two different vectorized datasets
- [x] Evaluate models using accuracy score on in-sample and out-of-sample datasets.
- [x] Once a single, best preforming model has been chosen, evaluate the preformance of the model on the test dataset.


## What is Histone-4 Occupancy?:
- Histones are protein structures that DNA winds tightly around, these structures condense DNA into chromatin.
- Histone-4 specifically is linked to long-term and short-term regulation of gene expression.
- If a DNA sequence is wound around a histone, the sequence is less likely to be expressed.


## Data dictionary
Target  | Description   | Data Type
--|--|--
label    | Indicative of whether or not a sequence will be wound around the H4 histone | int64, one-hot encoded

Features   | Description |    Data Type
--|--|--
id  | ID of the given sequence | object
sequence  | Nucleotide sequence, mostly uniform length of 500 with the exception of chromosome ids | object

Engineered Features  | Description   | Data Type
--|--|--
adenine |    Derrived from sequence, denotes the count of A bases    | int64
cytosine |    Derrived from sequence, denotes the count of C bases    | int64
guanine |    Derrived from sequence, denotes the count of G bases    | int64
thymine |    Derrived from sequence, denotes the count of T bases    | int64


# Conclusion:
## My Reccomendation
> I reccomend that the model used by www.jaist.ac be used in lieu of my own models. Additionally, the hexamer dataset seemed to be more indicative of positive or negative labels than the codon dataset. If pursuing the ANN models further I reccomend using a model with at least one hidden layer as it outpreformed the single layer model slightly with the codon dataset and significantly improved with the hexamer dataset.

## Key Takeaways:
> - I achieved a ~84.4% accuracy on test data using a Multinomial Naive Bayes test.
> - I did beat baseline but did not beat the best model from www.jaist.ac
>     - My best model lost by roughly 4 points

## Future Iterations:
> For any future iterations I would like to further develop my ANN models to try and minimize the prevalent overfitting issue present in my ANN models. I would like to try different vector lengths instead of 3 and 6 and would try to maximize model preformance with further tinkering with model hyperparameters. 


## Reproduce This Project:
- [x] Read this README
- [] Clone/pull/fork the acquire.py, preprocessing.py, explore.py, model.py, and Histone-4-Classification.ipynb files.
- [] Run the Histone-4-Classification.ipynb notebook
