def search_for_vowels(phrase:str) -> set: # search_for_vowels 의 함수가 인자를 받아서 word에 넣어줌?
    #word는 문자열을 기대하며 집합으로 반환함
    """Display any vowels found in a supplied word.""" # search_for_vowels의 함수를 설명
    vowels = set('aeiou') # vowels에 'aeiou'의 집합을 할당
    return vowels.intersection(set(phrase)) # vowels와 인자로 받은 word의 값을 집합으로 바꿔 vowels와 word의 교집합을 found에 할당

def search_for_letters(phrase:str, letters:str='aeiou') -> set: # search_for_letters는 두 인자 모두 문자열을 기대하며 집합으로 반환함
    """Return a set of the 'letters' found in 'phrase'.""" # search_for_letters 함수를 설명
    return set(letters).intersection(set(phrase)) # letters의 집합과 phrase 집합의 교집합을 반환함


# 함수의 스위트에서 return을 발견하면 항상 return문 에서 종료되고 함수에서 계산한 값을 호출한 코드로 돌려준다.
# bool 함수는 다른 프로그렘에서 참과 거짓으로 출력함