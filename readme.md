# Fakenews Detection
Đồ án môn học Xử lý ngôn ngữ tự nhiên ứng dụng - CSC15008

VNUHCM - University of Science, mùa Xuân 2022

## Abstraction
Đối với bài toán Text Classification, nhóm xây dựng ứng dụng phát hiện tin giả (Fakenews Detection), sử dụng một số mô hình máy học để đưa ra dự đoán một mẩu tin là thật (true) hay giả (fake).

## Dataset
Fake and real news dataset (Kaggle): https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset.

Download dataset và giải nén vào folder `model/dataset`.

## Model generation
- Cài các package cần thiết:
    ```
    pip install -r requirements.txt
    ```
- Clean data: Đọc kỹ hướng dẫn trong file `model/notebooks/data-cleaning.ipynb`, sau đó chạy notebook hoặc chạy file `model/clean.py`:
    ```
    cd model
    python clean.py
    ```

- Đọc file `model/notebooks/model-training.ipynb`, sau đó chạy notebook hoặc chạy file `model/train.py`:
    ```
    cd model
    python train.py
    ```
    File model sẽ được lưu trong folder `model/model`.

## Data migration
Copy `model/model` sang `web/app/model`. Hoặc:
```
cd model
bash migrate.sh
```

## Demo prediction
Cú pháp:
```
cd model
python predict.py --input=<input_file> --classifier=<classifier_name>
```

- `<input_file>` gồm nhiều dòng, mỗi dòng là 1 article cần đánh giá True/Fake.
- `classifier_name` lấy từ list sau:

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

Predict với tất cả các classifiers hiện có:
```
cd model
python predict.py --input=<input_file> --all
```

## Tech used
- Flask
- Bootstrap v5 (có jQuery)

## Server
Yêu cầu:
- Đã cài các package cần thiết.
- Đã generate model.
- Đã migrate model.

Các bước này đã nêu lần lượt bên trên.

### Linux
```
cd web
python3 -m venv venv
. venv/bin/activate
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

Chạy server:
```
# Chay tung cau lenh trong web/run_server.sh
```
