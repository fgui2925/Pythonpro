import datetime

def dt_calc(date_str,dlt_str):
    date=datetime.datetime.strptime(date_str,"%Y%m%d")
    dlt_day=datetime.timedelta(days=dlt_str)
    new_time=date+dlt_day
    print('您推算的日期是：',new_time)

if __name__ == '__main__':
    dt=input('请输入开始日期(如20080501)后按回车:')
    dlt=int(input('请输入间隔数:'))
    dt_calc(dt,dlt)