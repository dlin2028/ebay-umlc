# ebay-umlc
eBay 2022 University Machine Learning Competition team POOPy  
https://eval.ai/web/challenges/challenge-page/1733/leaderboard/4120  
Finished 9th place  

# Environment Setup
Install VSCode to run the ipynb files

Update/upgrade packages  
` sudo apt update && sudo apt upgrade  `

Download miniconda Installer  
Make sure to tell it to init when the installer prompts you  
`wget https://repo.anaconda.com/miniconda/Miniconda3-py39_4.12.0-Linux-x86_64.sh`  

After installing miniconda close and reopen your terminal. You may need to run  
`source ~/.bashrc  `  

Clone the repo  
`git clone https://github.com/dlin2028/ebay-umlc.git`  
CD Into the directory  
`cd ebay-umlc`  
Create the environment from the environment.yml file (this will take a while)  
`conda env create -f environment.yml`  

# Running the Full Stack (dataset to output)
Create a new directory ebay-umlc/dataset then paste the dataset .tsv files from the google drive  
Make sure you select the poopy environment in VSCode  
Generate the trainset by running generate_dataset.ipynb  
Generate the word vectors by running word_vector.ipynb  
Load the word vectors by running load_word_vector.sh  
Train a model using train.sh (make sure to check the gpu-id option is set correctly, do not include it if you don't have a gpu)  
Generate a prediction output by running predict.ipynb  
