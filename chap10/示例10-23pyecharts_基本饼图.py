# 导入
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.faker import Faker

# 准备数据
lst=[['华为',1000],['OPPO',1200],['苹果',3000],['小米',980]]

c = (
    Pie()
    # .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
    .add("", lst)
    # .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
    .set_global_opts(title_opts=opts.TitleOpts(title="2028年1月北京手机出库占比情况"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    # .render("pie_base.html")
    .render("phone.html")
)

# print([list(z) for z in zip(Faker.choose(), Faker.values())])

