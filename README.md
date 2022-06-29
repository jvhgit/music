# Installation steps
1) Clone and install this repository
   
2) Add folders to the repo such as `TECHNO`, `DB` , etc. <br>
   Folder structure should be: <br>
   music <br>
    ----- TECHNO <br>
    ----- DB <br>
    ----- download.py <br>
    ----- README.md

3) Make conda environment:
   1) Open `Anaconda Prompt`
   2) Go to the cloned repo directory
   3) Run the following command: `conda create --name music`
   4) Run the following command: `conda activate music`
   5) Run the following command: `conda install pip` 
   6) Run the following command: `pip install pytube scdl`

4) At last to run the program: <br>
   Windows: `python download.py` <br>
   Linux:   `python3 download.py` 

5) The program asks which folder to work with (`TECHNO`, `DB` , etc.).<br>
   Next, the program asks about the filethreshold (just press enter).<br>
   You are now good to go.

