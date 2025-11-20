def trim(func):
    # trim decoratro: 문자열 양쪽 공백 제거 후 함수에 전달
    def wrapper(msg: str):
        return func(msg.strip())
    return wrapper

def upcase(func):
    # upcase decorator: 문자열을 대문자로 변환 후 함수에 전달
    def wrapper(msg: str):
        return func(msg.upper())
    return wrapper

# Decorator chain: trim이 먼저 적용되고, upcase가 나중에 적용된다.
# 실제 적용 순서:
# 1) prt_value = trim(prt_value)
# 2) prt_value = upcase(prt_value)
@upcase
@trim
def prt_value(msg: str):
    # trim -> upcase로 가공된 결과가 들어오게 된다.
    print(msg)
    
# 호출: prt_value("     str     ") -> wrapper들이 계층적으로 실행됨
# 실행 흐름:
# input: "      str     "
# 1) trim wrapper -> msg.strip() -> "str"
# 2) upcase wrapper -> msg.upper() -> "STR"
# 3) prt_value("STR") 출력
prt_value("     str     ")