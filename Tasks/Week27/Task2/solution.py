def my_func_1():
    print('In my_func_1')

    def my_func_2():
        print('In my_func_2')

        def my_func_3():
            print('In my_func_3')

            def my_func_4():
                print('In my_func_4')

            my_func_4()

        my_func_3()

    my_func_2()


if __name__ == "__main__":
    my_func_1()
