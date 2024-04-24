FROM python
WORKDIR /app
COPY stopwords.py .
COPY paragraphs.txt .

RUN pip install nltk
RUN python -m nltk.downloader stopwords punkt

CMD [ "python" , "stopwords.py" ]

