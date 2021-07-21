
def decorator(func):
    def decorated(input_text):
        print('함수 실행')
        func(input_text)
        print('함수 끝')
    return decorated

@decorator
def hello_world(input_text):
    print(input_text)

hello_world('Hello World')

#------------------------------

def check_integer(func):
    def decorated(width, height):
        if width >= 0 and height >= 0 :
            return func(width, height)
        else:
            raise ValueError('input must be positive value')
    return decorated

@check_integer
def rr_area(width, height):
    return width * height

@check_integer
def ttri_area(width, height):
    return ( width * height ) / 2


#--------------------------------------


