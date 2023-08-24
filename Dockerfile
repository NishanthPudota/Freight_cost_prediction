FROM python:3.8
COPY . /Project_Freight_cost_prediction
WORKDIR /Project_Freight_cost_prediction
RUN pip install -r requirements.txt
EXPOSE $PORT
CMD python app.py 
