# this code repeats a string the certain number of times that indicate a chosen integer:

# hello 3 -> hellohellohello
# Fernando 2 -> FernandoFernandoFernando
# Code 4 -> CodeCodeCodeCode


def make_repeater_of(n):
    def repeater(string):
        assert type(string)==str, "can only use strings"
        return string*n
    return repeater

def run():
    repeat_3=make_repeater_of(3)
    print(repeat_3("hello"))
    repeat_2=make_repeater_of(2)
    print(repeat_2("Fernando"))
    repeat_4=make_repeater_of(4)
    print(repeat_4("Code"))


if __name__ =='__main__':
    run()


