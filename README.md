### 使用scrapy框架对阳光新政官网进行数据爬取到MongoDB数据库

创建项目

```python
scrapy startproject mySpider
```

进入spiders

```
scrapy genspider YGXZ "www.xxx.com"
```

cd到爬虫目录里执行scrapy crawl YGXZ--nolog命令

```
scrapy crawl YGXZ --nolog
```

### 基于numpy pandas 对数据进行清洗 分析

使用jupyter notebookz作为开发工具

下载numpy pandas等第三方库



清洗数据已经放入github仓库中

### 防止对网站服务造成影响 只进行部分数据爬取

