# Dog_Breed-Classification
Classifies Dog breed using Resnet50 CNN model

Steps to run files:

1. Run the Jupiter Notebook file to train the model and save the trained model in disc location. Then performs prediction on few test sample. As, labels are not present for the test dataset thus couldnot perform accuracy checking and other matrices checking. ##NOTE: change epochs as per need.

2. Steps to run API :
    ## NOTE: Kindly change file locations as per your requirement.
    1. Run base_64_.py --> Will produce testfile.txt
    2. Run classification_API.py --> API will produce {Score(probability), Breed}. [Create a folder in the same directory named templates and store index.html and display.html in it]
    
