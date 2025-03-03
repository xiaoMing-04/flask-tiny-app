# README

## Thông tin cá nhân
- **Họ tên**: Nguyễn Ngọc Minh - 22685841
- **Mã sinh viên**: Trần Khắc Liêm - 22685251

## Mô tả project
Dự án này là một website blog cơ bản, có chức năng đăng ký, đăng nhập

### Tính năng dự kiến:

## Hướng dẫn cài đặt và chạy

### Yêu cầu hệ thống
- Python 3.12.1
- Django 5.0

### Cài đặt
1. Clone repo:
   ```sh
   git clone https://github.com/xiaoMing-04/to-thich-cau.git
   cd anime
   ```
2. Tạo và kích hoạt môi trường ảo:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Trên macOS/Linux
   venv\Scripts\activate  # Trên Windows
   ```
3. Cài đặt các package yêu cầu:
   ```sh
   pip install -r requirements.txt
   ```
4. Chạy cơ sở dữ liệu:
   ```sh
   python manage.py migrate
   ```
5. Chạy server:
   ```sh
   python manage.py runserver
   ```
6. Truy cập trang web tại `http://127.0.0.1:8000/`
- Trang đăng nhập: `http://127.0.0.1:8000/login`
- Trang đăng ký: `http://127.0.0.1:8000/register`

## Link project đã triển khai

