# Fakenews Detection
Đồ án môn học Xử lý ngôn ngữ tự nhiên ứng dụng - CSC15008

Công nghệ sử dụng:
- sklearn
- Flask
- Bootstrap v5

## Dataset
Dataset & example code tham khảo từ https://www.kaggle.com/therealsampat/fake-news-detection

## Model pipeline
```
demo.py --input=<input_file> --classifier=<classifier_name>
```

|classifer_name|Classifier Name|
|--------------|---------------|
|`logistic_regression`|Logistic Regression|
|`sgd_classifier`|SGD Classifier|
|`decision_tree`|Decision Tree|
|`gradient_boosting`|Gradient Boosting|
|`random_forest`|Random Forest|
|`k_neighbors`|K-Nearest Neighbors|
|`naive_bayes`|Naive Bayes|
|`linear_svc`|Linear SVC|

## Server
```
cd web
python3 -m venv venv
# Tren windows thay / bang \
. venv/bin/activate
```

Chú ý: nhớ cài sklearn!
```
pip install sklearn
```

Chạy server:
```
pip install -r requirements.txt
sudo chmod 0700 run_server.sh
./run_server.sh

# Tren windows chay lan luot cac cau len trong run_server.sh
```
