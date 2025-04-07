def print_fan_pattern(text):
    # 첫 번째 줄: :fan::fan::fan:
    print(":fan::fan::fan:")
    # 두 번째 줄: :fan::입력문자열::fan:
    print(f":fan::{text}::fan:")
    # 세 번째 줄: :fan::fan::fan:
    print(":fan::fan::fan:")

# 입력 받기
user_input = input()
# 함수 호출
print_fan_pattern(user_input)