import json
import os


# 檢查檔案是否存在
if not os.path.isfile("students.json"):
    print("檔案不存在。")
    os._exit(0)

with open("students.json", "r", encoding="UTF-8") as f:
    students_dict: list[dict] = json.load(f)


def get_student_info(student_id: str):
    """根據學號返回該學生的個人資料字典

    Args:
        student_id (str): 學號

    Raises:
        ValueError: 找不到該學生的錯誤

    Returns:
        dict: 該學生的個人資料字典
    """
    for i in students_dict:
        if i.get("student_id") == student_id:
            return i
    raise ValueError("=>發生錯誤: 學號 " + student_id + " 找不到.")


def add_course(student_id: str, course_name: str, score: str):
    """_su為指定學生添加一門課程及其分數mmary_

    Args:
        student_id (str): 學號
        course_name (str): 欲增加的課程名稱
        score (str): 欲增加的課程分數

    Raises:
        ValueError: 找不到該學生的錯誤
        ValueError: 課程名稱或分數空白的錯誤

    Returns:
        str: "=>課程已成功新增。"
    """
    if not course_name or not score:
        raise ValueError("=>其它例外: 課程名稱或分數不可空白.")
    for i in students_dict:
        if i.get("student_id") == student_id:
            i.get("courses").append({"name": course_name, "score": score})
            return "=>課程已成功新增。"
    raise ValueError("=>發生錯誤: 學號 " + student_id + " 找不到.")


def calculate_average_score(student_id: str):
    """傳入學生的個人資料字典後，計算並返回該學生所有課程的平均分數

    Args:
        student_id (str): 學號

    Raises:
        ValueError: 找不到該學生的錯誤

    Returns:
        str: 所有課程的平均分數
    """
    sum = 0
    for i in students_dict:
        if i.get("student_id") == student_id:
            length = len(i.get("courses"))
            if length == 0:
                return str(0.0)
            else:
                for j in i.get("courses"):
                    sum += int(j.get("score"))
                return str(sum / len(i.get("courses")))
    raise ValueError("=>發生錯誤: 學號 " + student_id + " 找不到.")


while True:
    print("***************選單***************")
    print("1. 查詢指定學號成績")
    print("2. 新增指定學號的課程名稱與分數")
    print("3. 顯示指定學號的各科平均分數")
    print("4. 離開")
    print("**********************************")
    ans = input("請選擇操作項目：")

    match ans:
        case "1":
            student_id = input("請輸入學號: ")
            try:
                result = json.dumps(
                    get_student_info(student_id), ensure_ascii=False, indent=4
                )
                print(result)
            except Exception as e:
                print(e)
        case "2":
            student_id = input("請輸入學號: ")
            course_name = input("請輸入要新增課程的名稱: ")
            course_score = input("請輸入要新增課程的分數: ")
            try:
                result = add_course(student_id, course_name, course_score)
                print(result)
            except Exception as e:
                print(e)
        case "3":
            student_id = input("請輸入學號: ")
            try:
                result = calculate_average_score(student_id)
                print("=>各科平均分數: " + result)
            except Exception as e:
                print(e)
        case "4":
            print("=>程式結束。")
            break
