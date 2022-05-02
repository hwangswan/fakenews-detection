# Fakenews Detection
Đồ án môn học Xử lý ngôn ngữ tự nhiên ứng dụng - CSC15008

VNUHCM - University of Science, mùa Xuân 2022

## Abstraction
Đối với bài toán Text Classification, nhóm xây dựng ứng dụng phát hiện tin giả (Fakenews Detection), sử dụng một số mô hình máy học để đưa ra dự đoán một mẩu tin là thật (true) hay giả (fake).

## Dataset
Fake and real news dataset (Kaggle): https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

## Model generation
- Đọc kỹ hướng dẫn trong file `model/data-cleaning.ipynb`, sau đó chạy file `model/datacleaning.py`.
- Đọc file `model/model-training.ipynb`, sau đó chạy file `model/train.py`. File model sẽ được lưu trong folder `model/model`.
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

## Tech used
- Flask
- Bootstrap v5 (có jQuery)

## Server
```
pip install -r requirements.txt
```

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
# Chay tung cau lenh trong web/run_server.sh
```
