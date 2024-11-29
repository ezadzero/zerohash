import hashlib
import math
import random
import string
import argparse
import hmac
import os

# دیکشنری برای ذخیره داده‌ها و هش‌های آنها
hash_dict = {}

# تابع برای تولید رشته تصادفی از حروف و اعداد
def random_string(length=20):
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for _ in range(length))

# تابع هش با استفاده از SHA-512
def sha512_hash(data):
    return hashlib.sha512(data.encode('utf-8')).hexdigest()

# تابع هش با استفاده از MD5
def md5_hash(data):
    return hashlib.md5(data.encode('utf-8')).hexdigest()

# تابع هش با استفاده از توابع ریاضی پیچیده‌تر
def math_based_hash(data):
    numeric_value = sum(ord(char) for char in data)
    hashed_value = math.sin(numeric_value) * math.pi  # استفاده از سینوس و پی برای پیچیدگی بیشتر
    return hex(int(abs(hashed_value) * 1000000000000))  # تبدیل به هگزادسیمال

# تابع برای اعمال تغییرات تصادفی و پیچیدگی بیشتر
def complex_transformation(data):
    random_value = random_string(random.randint(10, 50))  # تولید رشته تصادفی از حروف و اعداد
    random_int = random.randint(1, 1000)
    
    # استفاده از عملیات ریاضی پیچیده با مقدار تصادفی
    transformed_data = str(random_int) + data + random_value
    return transformed_data

# تابع ترکیبی با عملیات تصادفی و چندین الگوریتم هش
def combined_hash(data):
    # تغییر داده با استفاده از عملیات تصادفی
    transformed_data = complex_transformation(data)
    
    # استفاده از چندین الگوریتم هش
    sha512_result = sha512_hash(transformed_data)
    md5_result = md5_hash(transformed_data)
    math_result = math_based_hash(transformed_data)
    
    # ترکیب نتایج
    combined = sha512_result + md5_result + math_result
    
    return combined

# ذخیره‌سازی داده و هش ترکیبی در دیکشنری
def store_hash(data):
    # تولید هش ترکیبی
    hash_value = combined_hash(data)
    # ذخیره داده و هش در دیکشنری
    hash_dict[hash_value] = data
    print(f"Data: '{data}' has been hashed and stored with hash: {hash_value}")
    return hash_value

# بررسی هش و برگرداندن داده اصلی
def unhash(hashed_value):
    # برگرداندن داده اصلی از هش ذخیره‌شده
    if hashed_value in hash_dict:
        return hash_dict[hashed_value]
    else:
        return "Hash not found!"

# تابع برای پردازش دستورات
def main():
    parser = argparse.ArgumentParser(description="ZeroHash CLI Tool for Secure Hashing and Unhashing")
    parser.add_argument("command", help="Command to run: hash or unhash", choices=["hash", "unhash"])
    parser.add_argument("value", help="The value to hash or the hash to unhash")
    args = parser.parse_args()

    if args.command == "hash":
        # عملیات هش کردن
        data = args.value
        store_hash(data)
    elif args.command == "unhash":
        # عملیات آن هش کردن
        hashed_value = args.value
        original_data = unhash(hashed_value)
        print(f"Original data: {original_data}")

if __name__ == "__main__":
    main()
