1. Phương pháp lựa chọn và thu thập dữ liệu
- Do nhóm áp dụng bài toán phân loại cảm xúc(pos, neu, neg) đối với review thức ăn, đồ uống
 nên quyết định crawl data(cụ thể là comment) trên trang foody.
- Công cụ: sử dụng thư viện selenium và scrapy của python để crawl.
- Đối với comment sẽ crawl rate, nội dung. Vì số lượng yêu cầu là 1000 example nên crawl khá nhanh.
- Sau bước crawl sẽ đến gán nhãn. Trên lý thuyết có thể dựa vào lượng rate để gán nhãn. Nhưng trên thực tế có rất nhiều
sai sót nên cần đánh nhãn bằng tay. Với các nhãn là pos, neu, neg.
