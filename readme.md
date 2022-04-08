# Fakenews Detection
Đồ án môn học Xử lý ngôn ngữ tự nhiên ứng dụng - CSC15008

Công nghệ sử dụng:
- sklearn
- Flask
- Bootstrap v5 (có jQuery)

## Dataset
Fake and real news dataset (Kaggle): https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

## Model generation
- Đọc kỹ hướng dẫn trong file `model/data-cleaning.ipynb`, sau đó chạy file.
- Chạy file `model/model-training.ipynb`. File model sẽ được lưu trong folder `model/model`.
- Chạy `model/migrate.sh` để copy model sang đúng vị trí trên server.

## Demo prediction
```
cd model
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
### Linux
```
cd web
python3 -m venv venv
. venv/bin/activate
```

Copy model vào server directiory:
```
cd model
bash migrate.sh
```

Chạy server:
```
pip install -r requirements.txt
sudo chmod 0700 run_server.sh
./run_server.sh
```

### Windows
```
cd web
python -m venv venv
venv\Scripts\activate
```

Copy model vào server directory (từ `model/model` vào `web/app/model`)

Chạy server:
```
pip install -r requirements.txt
# Chay tung cau lenh trong web/run_server.sh
```
