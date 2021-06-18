# DeepRBP
=============================

DeepRBP: a novel computational approach for accurate identification of RNA-binding proteins by deep learning algorithm
Overview
==============================
We train several deep neural network-based models to computationally identify RNA-binding proteins activity from protein sequence. We design three architectures, namely, convolution neural network (CNN), hybrid neural network that combine CNN and RNN(CNN-RNN),and CNN-RNN-att which adds attention layer on the basis of CNN-RNN. The input data takes the form of a primary sequence of a protein, and output a probability score between 0 and 1. In other words, the input to the models is a sequence of one-letter encoded amino acids. And the output of the models consists of one score which map to the [0, 1] interval, corresponding to the probability of the peptide of interest being an RBP and a non-RBP. Finally,by utilizing the CNN-RNN model, we implement a sequence-based deep learning tool, called DeepACP to accurately identify RBPs.

Files
================================
data file
Training dataset：       RBP2780.txt     (2780 RNA-binding proteins） 
                         non-RBP7093.txt (7093 non-RNA-binding proteins)
Independent test dataset:
A.thaliana-RBP456.txt       (456 A.thaliana RNA-binding proteins） 
A.thaliana-non-RBP37.txt    (37 A.thaliana non-RNA-binding proteins） 
Human-RBP967.txt            (967 Human RNA-binding proteins） 
Human-non-RBP597.txt        (597 Human non-RNA-binding proteins） 
S.cerevisiae-RBP354.txt     (354 S.cerevisiae RNA-binding proteins） 
S.cerevisiae-non-RBP135.txt (135 S.cerevisiae non-RNA-binding proteins）
from Xiaoli Zhang and Shiyong Liu (Zhang Xiaoli,Liu Shiyong. RBPPred: predicting RNA-binding proteins from sequence using SVM.[J]. Bioinformatics (Oxford, England),2017,33(6).)

model file
CNN.py: convolution neural network
CNN-RNN.py: hybrid neural network that combine CNN and RNN
CNN-RNN-att.py: adds attention layer on the basis of CNN-RNN

Usage
=================================
When training a deep leanring model, the user can enter the following commands in the command terminal. Take the RNN architecture as an example:  

For S.cerevisiae data set
python running.py --dataType protein --dataEncodingType onehot --dataTrainFilePaths examples/RNAproteins/data/train/RBP2780.txt examples/RNAproteins/data/train/non-RBP7093.txt --dataTrainLabel 1 0 --dataTestFilePaths examples/RNAproteins/data/test/S.cerevisiae-RBP354.txt examples/RNAproteins/data/test/S.cerevisiae-non-RBP135.txt --dataTestLabel 1 0 --modelLoadFile examples/RNAproteins/model/CNN-RNN.py  --verbose 1 --outSaveFolderPath tmpOut --savePrediction 1 --saveFig 1 --batch_size 25 --epochs 20 --shuffleDataTrain 1 --showFig 1 --modelSaveName tmpMod.json --weightSaveName tmpWeight.bin --noGPU 0 --paraSaveName parameters.txt --spcLen 1000

For A.thaliana data set
python running.py --dataType protein --dataEncodingType onehot --dataTrainFilePaths examples/RNAproteins/data/train/RBP2780.txt examples/RNAproteins/data/train/non-RBP7093.txt --dataTrainLabel 1 0 --dataTestFilePaths examples/RNAproteins/data/test/A.thaliana-RBP456.txt examples/RNAproteins/data/test/A.thaliana-non-RBP37.txt --dataTestLabel 1 0 --modelLoadFile examples/RNAproteins/model/CNN-RNN.py  --verbose 1 --outSaveFolderPath tmpOut --savePrediction 1 --saveFig 1 --batch_size 25 --epochs 20 --shuffleDataTrain 1 --showFig 1 --modelSaveName tmpMod.json --weightSaveName tmpWeight.bin --noGPU 0 --paraSaveName parameters.txt --spcLen 1000

For Human data set
python running.py --dataType protein --dataEncodingType onehot --dataTrainFilePaths examples/RNAproteins/data/train/RBP2780.txt examples/RNAproteins/data/train/non-RBP7093.txt --dataTrainLabel 1 0 --dataTestFilePaths examples/RNAproteins/data/test/Human-RBP967.txt examples/RNAproteins/data/test/Human-non-RBP597.txt --dataTestLabel 1 0 --modelLoadFile examples/RNAproteins/model/CNN-RNN.py  --verbose 1 --outSaveFolderPath tmpOut --savePrediction 1 --saveFig 1 --batch_size 25 --epochs 20 --shuffleDataTrain 1 --showFig 1 --modelSaveName tmpMod.json --weightSaveName tmpWeight.bin --noGPU 0 --paraSaveName parameters.txt --spcLen 1000
