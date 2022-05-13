# Fakenews Detection
Đồ án môn học Xử lý ngôn ngữ tự nhiên ứng dụng - CSC15008

VNUHCM - University of Science, mùa Xuân 2022

## Abstract
Đối với bài toán Text Classification, nhóm xây dựng ứng dụng phát hiện tin giả (Fakenews Detection), sử dụng kết hợp một số mô hình máy học để đưa ra dự đoán một mẩu tin là thật (true) hay giả (fake).

Với báo cáo, nhóm chọn báo cáo mô hình Decision Tree.

## Dataset
Fake and real news dataset (Kaggle): https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset.

Download dataset và giải nén vào folder `model/dataset`.

## Model
### Summarise
|classifier|accuracy|
|----------|--------|
|Gradient Boosting|1.0|
|Decision Tree|1.0|
|Random Forest|1.0|
|Linear SVC|0.99|
|SGD Classifier|0.99|
|Logistic Regression|0.99|
|Naive Bayes|0.93|
|K-Nearest Neighbors|0.79|

- Kích thước tập train: 44798 samples.
- Kích thước tập test: 100 samples (50 random real, 50 random fake).
- TfidfVectorizer vocabulary size: 121613.

Các tham số của từng mô hình, xem trong notebook `model/model-training.py` hoặc `model/train.py`.

### Generate
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

- Data migration sang server: copy `model/model` sang `web/app/model`; hoặc chạy `model/migrate.sh`:
    ```
    cd model
    bash migrate.sh
    ```

## Demo
### Model prediction
Cú pháp:
```
cd model
python predict.py --input=<input_file> --classifier=<classifier_name>
```

- `<input_file>` có nội dung là article cần đánh giá True/Fake.
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

### Server
Yêu cầu:
- Đã cài các package cần thiết.
- Đã generate model.
- Đã migrate model.

Các bước này đã nêu lần lượt bên trên.

#### Linux
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

#### Windows
```
cd web
python -m venv venv
venv\Scripts\activate
```

Chạy server:
```
# Chay tung cau lenh trong web/run_server.sh
```

#### Tech used
- Flask
- Bootstrap v5 (có jQuery)