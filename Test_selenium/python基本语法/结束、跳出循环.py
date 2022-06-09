"""
try:
    for i in range(10):
        for j in range(10):
            if j==2:
                raise
raise 该方法可直接结束两层循环，抛出异常；
如果用break，则只会结束内层循环，然后继续下一次外层循环；
如果用return，也是直接结束两层循环，该方法必须在函数中用；
continue是不执行后面的程序，进入下一次循环。
sys.exist(0,)表示直接退出程序
except:
    print("循环结束")
"""