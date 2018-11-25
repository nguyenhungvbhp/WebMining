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
Biểu diễn bài toán phân loại (classification problem)•  Một tập học D_train, trong đó mỗi ví dụ học x được biểu diễn là một vectơ n chiều: (x1, x2, ..., xn)•  Một tập xác định các nhãn lớp: C={c1, c2, ..., cm} •  Với một ví dụ mới z, thì z sẽ được phân vào lớp nào?•  Mục tiêu: Xác định phân lớp có thể (phù hợp) nhất đối với z cMAP =argmaxP(ci |z), ci ∈C.
cMAP =argmaxP(ci |z1,z2,...,zn), ci ∈CcMAP =argmaxP(z1,z2,...,zn |ci).P(ci)/P(z1,z2,...,zn), ci∈C 
Để tìm được phân lớp có thể nhất đối với z:cMAP =argmaxP(z1,z2,...,zn |ci).P(ci) ci ∈C(P(z1,z2,...,zn) là như nhau với các lớp)

Giả sử (assumption): Các thuộc tính là độc lập có điều kiện (conditionally independent) đối với các lớp P(z1,z2,...,zn |ci)=Tổng(P(zj |ci)), j=1->n Phân loại Naïve Bayes tìm phân lớp có thể nhất đối với zcNB =argmaxP(ci). Tổng( P(zj |ci)), j=1->n ci ∈C .

GIẢI THUẬT.
* Giai đoạn học (training phase), sử dụng một tập học Đối với mỗi phân lớp có thể (mỗi nhãn lớp) ci∈C•  Tính giá trị xác suất trước: P(ci)•  Đối với mỗi giá trị thuộc tính xj, tính giá trị xác suất xảy racủa giá trị thuộc tính đó đối với một phân lớp ci: P(xj|ci) 
* Giai đoạn phân lớp (classification phase), đối với một ví dụ mới  •  Đối với mỗi phân lớp ci∈C, tính giá trị của biểu thức:	P(ci).Tổng(P(xj |ci)) j=1->n•  Xác định phân lớp của z là lớp có thể nhất c* c* =argmaxP(ci). Tổng(P(xj |ci)), ci∈C j=1->n

3. Đánh giá
- Sử dụng Precision, Recall và F1.

* Precision = True Positive / (True Positive + False Positive) = True Positive / Total Predicted Positive.
* Recall = True Positive / (True Positive + False Negative) = True Positive/ Total Actual Positive
* F1 = 2 * Precision * Recall / (Precision + Recall)
