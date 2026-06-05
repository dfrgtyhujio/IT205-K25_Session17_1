raw_logs = []
processed_logs = []


def clean_raw_logs():
    print("\n--- NẠP DỮ LIỆU LOG ---")

    while True:
        user_input = input("Nhập chuỗi log thô (cách nhau bởi dấu ;): ").strip()

        if user_input == "":
            print("Chuỗi log không được để trống! Vui lòng nhập lại.")
        else:
            break

    cleaned_string = ""
    for char in user_input:
        if char != "!" and char != "@" and char != "#" and char != "$":
            cleaned_string = cleaned_string + char
    global raw_logs
    raw_logs = []
    log_list = cleaned_string.split(";")

    for log in log_list:
        clean_log = log.strip()
        if clean_log != "":
            raw_logs.append(clean_log)

    print(f"Đã làm sạch và lưu {len(raw_logs)} dòng log vào hệ thống.")


def filter_danger_logs():
    print("\n--- LỌC CẢNH BÁO ---")

    if len(raw_logs) == 0:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1.")
        return

    global processed_logs
    processed_logs = [
        log
        for log in raw_logs
        if "ERROR" in log.upper() or "CRITICAL" in log.upper()
    ]

    if len(processed_logs) > 0:
        print(f"Tìm thấy {len(processed_logs)} cảnh báo nguy hiểm:")
        for log in processed_logs:
            print(f"- {log}")
    else:
        print("Không tìm thấy log cảnh báo mức độ ERROR hoặc CRITICAL nào.")


def mask_ip_addresses():
    print("\n--- MÃ HÓA IP ---")

    if len(raw_logs) == 0:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1.")
        return

    if len(processed_logs) == 0:
        print(
            "Danh sách log cảnh báo đang trống. Vui lòng thực hiện chức năng 2 trước."
        )
        return

    print("Báo cáo log an toàn:")
    count = 1

    for log in processed_logs:
        words = log.split()
        masked_words = []

        for word in words:
            dot_count = 0
            for char in word:
                if char == ".":
                    dot_count = dot_count + 1

            if dot_count == 3:
                ip_parts = word.split(".")
                masked_ip = (ip_parts[0] + "." + ip_parts[1] + ".*.*")
                masked_words.append(masked_ip)
            else:
                masked_words.append(word)

        masked_log_line = " ".join(masked_words)
        print(f"{count}. {masked_log_line}")
        count = count + 1


def main():
    while True:
        print("\n============= SECURITY LOG ANALYZER =============")
        print("1. Nhập và làm sạch dữ liệu Log thô")
        print("2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)")
        print("3. Mã hóa địa chỉ IP (Masking)")
        print("4. Đóng hệ thống")
        print("=================================================")

        choice = input("Chọn chức năng (1-4): ").strip()

        if choice == "1":
            clean_raw_logs()
        elif choice == "2":
            filter_danger_logs()
        elif choice == "3":
            mask_ip_addresses()
        elif choice == "4":
            print("Cảm ơn bạn đã sử dụng chương trình!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")


if __name__ == "__main__":
    main()
