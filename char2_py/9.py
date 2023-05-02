def parse_string_to_dict(input_str, separator1, separator2):
    """
    입력된 문자열을 구분 문자(separator1, separator2)로 분리하여 딕셔너리로 반환하는 함수
    :param input_str: 분리할 문자열
    :param separator1: 첫 번째 구분 문자
    :param separator2: 두 번째 구분 문자
    :return: 분리된 문자열을 담은 딕셔너리
    """
    result_dict = {}
    items = input_str.split(separator1)
    for item in items:
        key_value = item.split(separator2)
        if len(key_value) == 2:
            key = key_value[0]
            value = key_value[1]
            result_dict[key] = value
    return result_dict


input_str = 'led=on&motor=off&switch=off'
separator1 = '&'
separator2 = '='

# 함수 호출
parsed_dict = parse_string_to_dict(input_str, separator1, separator2)

# 결과 출력
print(parsed_dict)
