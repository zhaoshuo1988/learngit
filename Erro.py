import logging

logging.basicConfig(level=logging.INFO)
logger=logging.getLogger()  #日志文件

def func():
    
    i=input()

    if len(i)<8:
        raise Exception('自定义错误')
    else:
        return 1

if __name__=='__main__':
    try:
        r=func()

    except Exception as e:
        print('异常')
        raise
        logger.info('日志记录错误')
    print(r)
