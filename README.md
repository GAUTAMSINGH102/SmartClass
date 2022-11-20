# SmartClass
Be Smart With Smart Class  

## Motivation
- The main purpose was to reduce the time that we spent on reading content and watching Video Lectures by providing the summary of Video Lecture, Research Paper, PDFs and Images.  
- Sometimes it also very difficult to find the best Recommendation of the things that we are reading or watching and we spent lot of time in finding the relevant Content so we provide the Recommendation of Youtube Videos, Books and Medium Blogs  on the basis of stuff you are reading and watching so that you don't have to search for it on different website.  

## Summary  
- Mainly we can get Summary of:
  - Video Lecture
  - Research Paper/ PDFs
  - Images

- **Video Lectures**  
  - At First we will convert into audio format mp3 or wav.
  - From Audio using **Whisper OpenAI Model** we would convert it into Text.

- **Research Paper / PDF**
  - To convert PDFs into Text we will use **PyPDF2**.

- **Images**
  - To Convert Images into Text we will use **OCR** Method.

- We would find Summary of the text that we have generated using BART Model.  



## Recommendation
- From the Text of Videos, PDFs, Images we will extract Keywords From it using **RAKE Model**.

