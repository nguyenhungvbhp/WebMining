1. Phương pháp lựa chọn và thu thập dữ liệu
- Do nhóm áp dụng bài toán phân loại cảm xúc(pos, neu, neg) đối với review thức ăn, đồ uống
 nên quyết định crawl data(cụ thể là comment) trên trang foody.
- Công cụ: sử dụng thư viện selenium và scrapy của python để crawl.
- Đối với comment sẽ crawl rate, nội dung. Vì số lượng yêu cầu là 1000 example nên crawl khá nhanh.
- Sau bước crawl sẽ đến gán nhãn. Trên lý thuyết có thể dựa vào lượng rate để gán nhãn. Nhưng trên thực tế có rất nhiều
sai sót nên cần đánh nhãn bằng tay. Với các nhãn là pos, neu, neg.

2. Phương pháp xử lý và áp dụng NavieBayes
- Bước 1. Tiền xử lý dữ liệu
 Trong bước này bao gồm Loại bỏ kí tự đặc biết, Tách từ, xóa bỏ từ dừng, chuẩn hóa 1 số từ về đúng chính tả.
- Bước 2: Đưa 1 câu về 1 vector. Sử dụng phương pháp Bag of Word kết hợp TF-IDF.
- Bước 3. Áp dụng phương pháp Navies Bayes để phân loại nhãn.

3. Đánh giá
- Sử dụng Precision, Recall và F1.

* Precision = True Positive / (True Positive + False Positive) = True Positive / Total Predicted Positive.
* Recall = True Positive / (True Positive + False Negative) = True Positive/ Total Actual Positive
* F1 = 2 * Precision * Recall / (Precision + Recall)
