#第三个进度条模式
from tqdm import tqdm
from time import sleep
from tqdm import trange

text = ""

print("祈祷代码不要报错")

#方法一：使用tqdm()封装可迭代对象
#for char in tqdm(["a","b","c","d"]):
#    sleep(0.25)
#    text = text + char
#方法二：trange(i) 特殊的关键字，封装了range的tqdm对象
#for i in trange(100):
#    sleep(0.01)
#方法三：控制进度条显示当前步骤名称：
# pbar = tqdm(["a","b","c","d"])
# for char in pbar:
#     sleep(0.25)
#     pbar.set_description("Processing %s "% char)
for i in tqdm(range(1,500)):
    sleep(0.01)
    sleep(0.5)
        