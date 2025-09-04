#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 电商平台用户行为分析系统（增强教学版v2）
# 增加数据复杂度、增强数据清洗、扩展可视化图表类型
"""
product_info_v2.csv
商品ID,商品名称,类别,价格,上架时间,库存,品牌,评分
2001,男士休闲T恤,男装,89,2022-01-10,120,优衣库,4.5
2002,女士连衣裙,女装,159,2022-02-15,85,ZARA,4.7
2003,运动跑步鞋,男鞋,399,2021-11-05,60,耐克,4.8
2004,高跟鞋,女鞋,259,2022-03-20,45,百丽,4.3
2005,机械手表,配饰,899,2021-10-18,30,卡西欧,4.6
2006,智能手机,手机,3299,2022-01-25,50,华为,4.9
2007,笔记本电脑,电脑,5999,2021-12-10,25,苹果,4.7
2008,口红,化妆品,199,2022-02-05,150,迪奥,4.8
2009,面霜,护肤品,45
"""
"""
user_behavior_v2.csv
用户ID,商品ID,行为类型,行为时间,行为时长(秒)
1001,2001,浏览,2023-05-01 08:30:00,65
1001,2001,加购,2023-05-01 08:35:00,12
1001,2003,view,2023/05/01 09:15:00,48
1002,2004,buy,2023-05-01 10:20:00,35
1002,2004,购买,2023-05-01 10:25:00,28
1003,2007,收藏,2023-05-01 11:10:00,-5
1003,2007,collect,2023-05-01 11:12:00,15
1004,2010,浏览,2023-05-01 13:45:00,72
1004,2010,purchase,2023/05/01 13:50:00,42
1005,2002,加购,2023-05-01 14:20:00,18
1005,2002,addcart,2023-05-01 14:22:00,
1005,2014,浏览,2023-05-01 14:25:00,55
1006,2019,购买,2023-05-01 15:30:00,38
1006,2019,buy,2023-05-01 15:32:00,25
1007,2009,收藏,2023-05-01 16:40:00,14
1007,2009,save,2023/05/01 16:42:00,9
1008,2005,浏览,2023-05-01 17:15:00,68
1008,2005,购买,2023-05-01 17:18:00,32
1009,2008,look,2023-05-01 18:20:00,45
1009,2008,浏览,2023-05-01 18:20:00,45
1010,2012,加购,2023-05-01 19:05:00,22
1010,2012,cart,2023/05/01 19:07:00,16
1011,2006,浏览,2023-05-01 20:30:00,85
1011,2006,购买,2023-05-01 20:35:00,48
1012,2015,浏览,2023-05-02 09:10:00,52
1012,2015,加购,2023-05-02 09:12:00,19
1013,2017,收藏,2023/05/02 10:45:00,11
1013,2017,save,2023-05-02 10:47:00,8
1014,2020,浏览,2023-05-02 11:20:00,63
1014,2020,购买,2023-05-02 11:25:00,39
1015,2003,浏览,2023-05-02 14:10:00,78
1015,2003,buy,2023/05/02 14:15:00,45
1016,2016,加购,2023-05-02 15:30:00,24
1016,2016,addcart,2023-05-02 15:32:00,17
1017,2018,浏览,2023-05-02 16:45:00,58
1017,2018,收藏,2023-05-02 16:48:00,13
1018,2011,浏览,2023/05/02 17:20:00,66
1018,2011,购买,2023-05-02 17:23:00,36
1019,2013,加购,2023-05-02 19:10:00,21
1019,2013,cart,2023-05-02 19:12:00,15
1020,2001,浏览,2023-05-02 20:30:00,71
1020,2001,购买,2023/05/02 20:35:00,42
1001,2014,浏览,2023-05-03 08:45:00,59
1001,2014,buy,2023-05-03 08:50:00,33
1002,2009,浏览,2023-05-03 09:20:00,64
1002,2009,加购,2023/05/03 09:22:00,18
1003,2019,浏览,2023-05-03 10:15:00,75
1003,2019,购买,2023-05-03 10:18:00,40
1004,2005,浏览,2023-05-03 13:30:00,68
1004,2005,收藏,2023-05-03 13:33:00,12
1005,2007,浏览,2023/05/03 14:45:00,72
1005,2007,save,2023-05-03 14:48:00,10
1006,2002,浏览,2023-05-03 15:20:00,61
1006,2002,购买,2023-05-03 15:25:00,37
1007,2012,浏览,2023-05-03 16:30:00,55
1007,2012,加购,2023/05/03 16:32:00,20
1008,2017,浏览,2023-05-03 17:10:00,69
1008,2017,收藏,2023-05-03 17:13:00,14
1009,2006,浏览,2023-05-03 18:25:00,82
1009,2006,购买,2023-05-03 18:30:00,49
1010,2015,浏览,2023/05/03 19:40:00,73
1010,2015,buy,2023-05-03 19:45:00,44
1011,2020,浏览,2023-05-03 20:15:00,67
1011,2020,收藏,2023-05-03 20:18:00,16
1012,2003,浏览,2023-05-04 09:30:00,79
1012,2003,加购,2023-05-04 09:32:00,23
1013,2016,浏览,2023/05/04 10:40:00,65
1013,2016,购买,2023-05-04 10:45:00,41
1014,2018,浏览,2023-05-04 11:25:00,58
1014,2018,收藏,2023-05-04 11:28:00,13
1015,2011,浏览,2023-05-04 14:15:00,76
1015,2011,buy,2023/05/04 14:20:00,46
1016,2013,浏览,2023-05-04 15:35:00,62
1016,2013,加购,2023-05-04 15:37:00,19
1017,2001,浏览,2023-05-04 16:50:00,74
1017,2001,购买,2023-05-04 16:55:00,43
1018,2014,浏览,2023/05/04 17:25:00,61
1018,2014,加购,2023-05-04 17:27:00,18
1019,2009,浏览,2023-05-04 19:15:00,68
1019,2009,收藏,2023-05-04 19:18:00,15
1020,2019,浏览,2023-05-04 20:35:00,77
1020,2019,购买,2023/05/04 20:40:00,48
"""
"""
user_info_v2.csv
用户ID,性别,年龄,注册时间,所在城市,注册设备,会员等级
1001,男,28,2022-03-15,北京,华为,黄金
1002,女,,2022-05-20,上海,苹果,白银
1003,,35,2022-01-10,广州,小米,青铜
1004,男,42,2021-11-05,深圳,OPPO,黄金
1005,女,23,2022-06-30,杭州,vivo,白银
1006,,19,2022-02-18,成都,其他,青铜
1007,男,55,2021-09-03,武汉,华为,黄金
1008,女,31,2022-04-25,南京,苹果,白银
1009,男,26,2022-07-12,重庆,小米,青铜
1010,,38,2021-12-08,西安,OPPO,黄金
1011,女,29,2022-03-22,青岛,vivo,白银
1012,男,45,2021-10-15,沈阳,其他,青铜
1013,,22,2022-05-05,长沙,华为,黄金
1014,女,33,2022-01-28,郑州,苹果,白银
1015,男,17,2022-06-18,济南,小米,青铜
1016,,36,2021-11-30,合肥,OPPO,黄金
1017,女,48,2022-02-14,福州,vivo,白银
1018,男,27,2022-04-09,昆明,其他,青铜
1019,,30,2021-09-25,哈尔滨,华为,黄金
1020,女,52,2022-07-03,石家庄,苹果,白银
1021,男,65,2021-12-20,苏州,小米,青铜
1022,女,24,2022-03-08,无锡,OPPO,黄金
1023,,39,2022-05-15,常州,vivo,白银
1024,男,43,2021-10-05,南通,其他,青铜
1025,女,21,2022-01-18,扬州,华为,黄金
1026,男,150,2022-06-25,徐州,苹果,白银
1027,,29,2022-02-05,泉州,小米,青铜
1028,女,34,2021-09-12,温州,OPPO,黄金
1029,男,-5,2022-04-19,绍兴,vivo,白银
1030,女,41,2021-11-15,台州,其他,青铜
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import os
from collections import defaultdict
import random

# 设置中文字体，确保中文正常显示
plt.rcParams["font.family"] = ["SimHei"]
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题


# ================ 系统框架与数据加载 ================
class EcommerceAnalysisSystem:
    """电商平台用户行为分析系统主类"""
    
    def __init__(self):
        """初始化系统参数和数据存储结构"""
        # 初始化数据存储变量
        self.user_data = None          # 用户信息数据
        self.product_data = None       # 商品信息数据
        self.behavior_data = None      # 用户行为数据
        self.merged_data = None        # 合并后的完整数据

        self.analysis_results = {}     # 分析结果存储
        self.chart_folder = '分析图表_v2'  # 图表保存目录
        # 创建图表保存目录
        self._create_folder(self.chart_folder)
    
    def _create_folder(self, folder_name):
        """创建目录（如果不存在）"""
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"已创建目录: {folder_name}")

    def load_data(self, user_file, product_file, behavior_file):
        """
        加载数据文件
        
        参数:
            user_file: 用户信息文件路径
            product_file: 商品信息文件路径
            behavior_file: 用户行为文件路径
        """
        try:
            print("\n===== 开始加载数据 =====")
            
            # 加载用户信息
            print(f"加载用户信息: {user_file}")
            self.user_data = pd.read_csv(user_file)
            print(f"用户数据字段: {', '.join(self.user_data.columns)}")
            
            # 加载商品信息
            print(f"加载商品信息: {product_file}")
            self.product_data = pd.read_csv(product_file)
            print(f"商品数据字段: {', '.join(self.product_data.columns)}")
            
            # 加载用户行为数据
            print(f"加载用户行为: {behavior_file}")
            self.behavior_data = pd.read_csv(behavior_file)
            print(f"行为数据字段: {', '.join(self.behavior_data.columns)}")
            
            # 显示加载结果
            print(f"\n数据加载汇总:")
            print(f"用户数据: {len(self.user_data)}条记录")
            print(f"商品数据: {len(self.product_data)}条记录")
            print(f"行为数据: {len(self.behavior_data)}条记录")
            
            # 数据预览
            print("\n数据预览:")
            print("用户数据前2行:")
            print(self.user_data.head(2))
            print("\n商品数据前2行:")
            print(self.product_data.head(2))
            print("\n行为数据前2行:")
            print(self.behavior_data.head(2))
            
            return True
        except FileNotFoundError as e:
            print(f"文件未找到: {str(e)}")
            return False
        except Exception as e:
            print(f"数据加载失败: {str(e)}")
            return False


# ================ 数据预处理模块================
    def preprocess_data(self):
        """数据预处理主函数"""
        # 检查数据是否加载完整
        if self.user_data is None or self.product_data is None or self.behavior_data is None:
            print("请先加载完整数据")
            return False
        
        print("\n===== 开始数据预处理 =====")
        
        # 1. 数据质量检查
        self._check_data_quality()
        
        # 2. 预处理用户数据
        self._preprocess_users()
        
        # 3. 预处理商品数据
        self._preprocess_products()
        
        # 4. 预处理行为数据
        self._preprocess_behavior()
        
        # 5. 合并数据
        self._merge_all_data()
        
        # 6. 处理合并后的数据
        self._post_process_merged_data()
        
        # 7. 保存预处理后的数据
        self._save_preprocessed_data()
        
        print("\n数据预处理完成！")
        return True
    
    def _check_data_quality(self):
        """数据质量检查"""
        print("\n===== 数据质量检查 =====")
        
        # 检查用户数据
        print("\n用户数据质量:")
        print(f"缺失值情况:\n{self.user_data.isnull().sum()}")
        
        # 检查异常值
        if '年龄' in self.user_data.columns:
            age_outliers = len(self.user_data[(self.user_data['年龄'] < 0) | (self.user_data['年龄'] > 120)])
            if age_outliers > 0:
                print(f"发现{age_outliers}条年龄异常值（<0或>120）")
        
        # 检查重复记录
        user_duplicates = self.user_data.duplicated().sum()
        if user_duplicates > 0:
            print(f"发现{user_duplicates}条重复用户记录")
        
        # 检查商品数据
        print("\n商品数据质量:")
        print(f"缺失值情况:\n{self.product_data.isnull().sum()}")
        
        # 检查价格异常值
        if '价格' in self.product_data.columns:
            price_outliers = len(self.product_data[(self.product_data['价格'] <= 0) | 
                                                  (self.product_data['价格'] > self.product_data['价格'].quantile(0.99)*3)])
            if price_outliers > 0:
                print(f"发现{price_outliers}条价格异常值")
        
        # 检查行为数据
        print("\n行为数据质量:")
        print(f"缺失值情况:\n{self.behavior_data.isnull().sum()}")
        
        # 检查行为类型合法性
        if '行为类型' in self.behavior_data.columns:
            valid_types = ['浏览', '收藏', '加购', '购买']
            invalid_types = len(self.behavior_data[~self.behavior_data['行为类型'].isin(valid_types)])
            if invalid_types > 0:
                print(f"发现{invalid_types}条无效行为类型记录")
        
        # 检查关键ID是否存在
        required_columns = {
            '用户数据': ['用户ID'],
            '商品数据': ['商品ID'],
            '行为数据': ['用户ID', '商品ID', '行为类型', '行为时间']
        }
        
        for data_name, cols in required_columns.items():
            for col in cols:
                if col not in self.user_data.columns and data_name == '用户数据':
                    print(f"警告: {data_name}缺少必要字段'{col}'")
                elif col not in self.product_data.columns and data_name == '商品数据':
                    print(f"警告: {data_name}缺少必要字段'{col}'")
                elif col not in self.behavior_data.columns and data_name == '行为数据':
                    print(f"警告: {data_name}缺少必要字段'{col}'")
    
    def _preprocess_users(self):
        """预处理用户数据"""
        print("\n===== 预处理用户数据 =====")
        # 复制数据避免修改原始数据
        users = self.user_data.copy()
        
        # 处理重复记录
        duplicates = users.duplicated().sum()
        if duplicates > 0:
            users = users.drop_duplicates()
            print(f"已移除{duplicates}条重复用户记录")
        
        # 处理年龄缺失值和异常值
        if '年龄' in users.columns:
            # 处理异常值
            age_outliers = len(users[(users['年龄'] < 0) | (users['年龄'] > 120)])
            if age_outliers > 0:
                # 使用中位数替换异常值
                age_median = users[(users['年龄'] >= 0) & (users['年龄'] <= 120)]['年龄'].median()
                users.loc[(users['年龄'] < 0) | (users['年龄'] > 120), '年龄'] = age_median
                print(f"用中位数{age_median}替换了{age_outliers}条年龄异常值")
            
            # 处理缺失值
            missing_count = users['年龄'].isnull().sum()
            if missing_count > 0:
                # 按性别分组计算中位数填充
                age_by_gender = users.groupby('性别')['年龄'].transform('median')
                users['年龄'] = users['年龄'].fillna(age_by_gender)
                print(f"按性别中位数填充了{missing_count}条年龄缺失值")
        
        # 处理性别缺失值
        if '性别' in users.columns:
            missing_count = users['性别'].isnull().sum()
            if missing_count > 0:
                # 对于有注册设备信息的，使用设备信息推断性别
                if '注册设备' in users.columns:
                    # 假设某些设备类型有性别倾向
                    mobile_brands = {
                        '华为': {'男': 0.55, '女': 0.45},
                        '苹果': {'男': 0.48, '女': 0.52},
                        '小米': {'男': 0.6, '女': 0.4},
                        'OPPO': {'男': 0.43, '女': 0.57},
                        'vivo': {'男': 0.4, '女': 0.6},
                        '其他': {'男': 0.5, '女': 0.5}
                    }
                    
                    # 对缺失性别但有注册设备的用户进行推断
                    for idx, row in users[users['性别'].isnull()].iterrows():
                        if pd.notnull(row['注册设备']):
                            brand = row['注册设备']
                            prob = mobile_brands.get(brand, mobile_brands['其他'])
                            users.at[idx, '性别'] = '男' if random.random() < prob['男'] else '女'
                    
                    remaining_missing = users['性别'].isnull().sum()
                    print(f"根据设备信息推断了{missing_count - remaining_missing}条性别缺失值")
                    missing_count = remaining_missing
                
                # 用最常见性别填充剩余缺失值
                if missing_count > 0:
                    most_common = users['性别'].mode()[0]
                    users['性别'] = users['性别'].fillna(most_common)
                    print(f"用最常见性别'{most_common}'填充了{missing_count}条性别缺失值")
        
        # 转换注册时间为日期格式
        if '注册时间' in users.columns:
            try:
                # 处理多种日期格式
                users['注册时间'] = pd.to_datetime(users['注册时间'], errors='coerce')
                invalid_dates = users['注册时间'].isnull().sum()
                if invalid_dates > 0:
                    print(f"发现{invalid_dates}条无效注册时间格式，已转换为NaT")
                    # 用合理的默认值填充
                    earliest_valid = users['注册时间'].min()
                    users['注册时间'] = users['注册时间'].fillna(earliest_valid)
                print("注册时间转换为日期格式完成")
            except Exception as e:
                print(f"注册时间转换失败: {str(e)}")
        
        # 新增用户注册时长（天）
        if '注册时间' in users.columns:
            latest_date = users['注册时间'].max()
            users['注册时长(天)'] = (latest_date - users['注册时间']).dt.days
            print("已添加用户注册时长字段")
        
        # 新增年龄分组
        if '年龄' in users.columns:
            users['年龄分组'] = users['年龄'].apply(self._get_age_group)
            print("已添加年龄分组字段")
        
        # 保存处理后的数据
        self.user_data = users
        print("用户数据预处理完成")
    
    def _preprocess_products(self):
        """预处理商品数据"""
        print("\n===== 预处理商品数据 =====")
        products = self.product_data.copy()
        
        # 处理重复记录
        duplicates = products.duplicated().sum()
        if duplicates > 0:
            products = products.drop_duplicates()
            print(f"已移除{duplicates}条重复商品记录")
        
        # 处理价格异常值和缺失值
        if '价格' in products.columns:
            # 显示处理前的描述统计
            print(f"价格处理前统计:\n{products['价格'].describe()}")
            
            # 使用IQR方法检测异常值
            Q1 = products['价格'].quantile(0.25)
            Q3 = products['价格'].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            # 标记异常值
            outliers = products[(products['价格'] < lower_bound) | (products['价格'] > upper_bound)]
            outlier_count = len(outliers)
            
            if outlier_count > 0:
                # 对价格异常值进行截断而不是删除
                products['价格'] = products['价格'].clip(lower_bound, upper_bound)
                print(f"使用IQR方法检测并处理了{outlier_count}条价格异常值")
            
            # 处理价格缺失值 - 按类别填充
            missing_count = products['价格'].isnull().sum()
            if missing_count > 0:
                # 按类别计算平均值填充
                price_by_category = products.groupby('类别')['价格'].transform('mean')
                products['价格'] = products['价格'].fillna(price_by_category)
                
                # 对仍有缺失的（没有类别的）使用全局平均值
                remaining_missing = products['价格'].isnull().sum()
                if remaining_missing > 0:
                    global_mean = products['价格'].mean()
                    products['价格'] = products['价格'].fillna(global_mean)
                    print(f"用类别平均值填充了{missing_count - remaining_missing}条，全局平均值填充了{remaining_missing}条价格缺失值")
                else:
                    print(f"用类别平均值填充了{missing_count}条价格缺失值")
            
            # 新增价格区间
            products['价格区间'] = products['价格'].apply(self._get_price_range)
            print("已添加价格区间字段")
            
            # 显示处理后的描述统计
            print(f"价格处理后统计:\n{products['价格'].describe()}")
        
        # 处理类别缺失值和标准化
        if '类别' in products.columns:
            # 类别标准化
            category_mapping = {
                '男装': '服装',
                '女装': '服装',
                '男鞋': '鞋类',
                '女鞋': '鞋类',
                '手机': '电子',
                '电脑': '电子',
                '化妆品': '美妆',
                '护肤品': '美妆',
                '配饰': '配饰',
                '饰品': '配饰'
            }
            
            # 应用映射，未映射的保持原样
            products['类别'] = products['类别'].apply(
                lambda x: category_mapping.get(x, x) if pd.notnull(x) else x)
            
            # 处理剩余缺失值
            missing_count = products['类别'].isnull().sum()
            if missing_count > 0:
                products['类别'] = products['类别'].fillna('未知类别')
                print(f"用'未知类别'填充了{missing_count}条类别缺失值，并标准化了类别名称")
        
        # 转换上架时间为日期格式
        if '上架时间' in products.columns:
            try:
                products['上架时间'] = pd.to_datetime(products['上架时间'], errors='coerce')
                invalid_dates = products['上架时间'].isnull().sum()
                if invalid_dates > 0:
                    print(f"发现{invalid_dates}条无效上架时间格式")
                    # 用合理的默认值填充
                    earliest_valid = products['上架时间'].min()
                    products['上架时间'] = products['上架时间'].fillna(earliest_valid)
                print("上架时间转换为日期格式完成")
            except Exception as e:
                print(f"上架时间转换失败: {str(e)}")
        
        # 处理库存异常值
        if '库存' in products.columns:
            # 处理负库存
            negative_stock = len(products[products['库存'] < 0])
            if negative_stock > 0:
                products['库存'] = products['库存'].clip(lower=0)
                print(f"已修正{negative_stock}条负库存记录")
            
            # 处理库存缺失值
            missing_stock = products['库存'].isnull().sum()
            if missing_stock > 0:
                # 按类别填充库存中位数
                stock_by_category = products.groupby('类别')['库存'].transform('median')
                products['库存'] = products['库存'].fillna(stock_by_category).fillna(0)
                print(f"已处理{missing_stock}条库存缺失值")
        
        # 保存处理后的数据
        self.product_data = products
        print("商品数据预处理完成")
    
    def _preprocess_behavior(self):
        """预处理行为数据"""
        print("\n===== 预处理行为数据 =====")
        behavior = self.behavior_data.copy()
        
        # 处理重复记录
        duplicates = behavior.duplicated().sum()
        if duplicates > 0:
            behavior = behavior.drop_duplicates()
            print(f"已移除{duplicates}条重复行为记录")
        
        # 转换行为时间为日期格式
        if '行为时间' in behavior.columns:
            try:
                # 处理多种日期格式
                behavior['行为时间'] = pd.to_datetime(behavior['行为时间'], errors='coerce')
                invalid_dates = behavior['行为时间'].isnull().sum()
                
                if invalid_dates > 0:
                    print(f"发现{invalid_dates}条无效行为时间格式")
                    
                    # 尝试用其他格式解析
                    mask = behavior['行为时间'].isnull()
                    behavior.loc[mask, '行为时间'] = pd.to_datetime(
                        behavior.loc[mask, '行为时间'], 
                        format='%Y/%m/%d %H:%M',
                        errors='coerce'
                    )
                    
                    new_invalid = behavior['行为时间'].isnull().sum()
                    print(f"再次尝试解析后，仍有{new_invalid}条无效时间")
                    
                    # 对仍无效的，使用随机时间填充在合理范围内
                    if new_invalid > 0 and not behavior['行为时间'].dropna().empty:
                        min_valid = behavior['行为时间'].min()
                        max_valid = behavior['行为时间'].max()
                        time_range = (max_valid - min_valid).total_seconds()
                        
                        behavior.loc[behavior['行为时间'].isnull(), '行为时间'] = [
                            min_valid + timedelta(seconds=random.uniform(0, time_range)) 
                            for _ in range(new_invalid)
                        ]
                        print(f"用随机时间填充了{new_invalid}条无效行为时间")
                
                print("行为时间转换为日期格式完成")
            except Exception as e:
                print(f"行为时间转换失败: {str(e)}")
        
        # 提取更多时间特征
        if '行为时间' in behavior.columns:
            behavior['行为日期'] = behavior['行为时间'].dt.date
            behavior['行为小时'] = behavior['行为时间'].dt.hour
            behavior['星期几'] = behavior['行为时间'].dt.dayofweek  # 0-6表示周一到周日
            behavior['月份'] = behavior['行为时间'].dt.month
            behavior['是否周末'] = behavior['星期几'].apply(lambda x: 1 if x >= 5 else 0)
            behavior['时间段'] = behavior['行为小时'].apply(self._get_time_segment)
            print("已添加行为日期、小时、星期几、月份、是否周末和时间段字段")
        
        # 处理行为类型统一化
        if '行为类型' in behavior.columns:
            valid_types = ['浏览', '收藏', '加购', '购买']
            # 创建行为类型映射，处理更多变体
            behavior_mapping = {
                'view': '浏览',
                'browse': '浏览',
                'look': '浏览',
                'collect': '收藏',
                'save': '收藏',
                'cart': '加购',
                'addcart': '加购',
                'buy': '购买',
                'purchase': '购买'
            }
            
            # 先尝试映射，失败的再统一设为浏览
            def normalize_behavior(x):
                if pd.isnull(x):
                    return '浏览'  # 默认为浏览
                x_str = str(x).lower()
                return behavior_mapping.get(x_str, x) if x_str in behavior_mapping else x
            
            behavior['行为类型_norm'] = behavior['行为类型'].apply(normalize_behavior)
            
            # 再次检查并处理剩余的不规范类型
            invalid_mask = ~behavior['行为类型_norm'].isin(valid_types)
            invalid_count = sum(invalid_mask)
            
            if invalid_count > 0:
                behavior.loc[invalid_mask, '行为类型_norm'] = '浏览'
                print(f"标准化了{invalid_count}条不规范的行为类型")
            
            # 替换原字段
            behavior['行为类型'] = behavior['行为类型_norm']
            behavior = behavior.drop('行为类型_norm', axis=1)
            
            # 统计行为类型分布
            type_counts = behavior['行为类型'].value_counts()
            print(f"行为类型分布:\n{type_counts}")
        
        # 检查并处理无效的用户ID和商品ID
        valid_user_ids = set(self.user_data['用户ID']) if '用户ID' in self.user_data.columns else set()
        valid_product_ids = set(self.product_data['商品ID']) if '商品ID' in self.product_data.columns else set()
        
        if '用户ID' in behavior.columns and valid_user_ids:
            invalid_users = len(behavior[~behavior['用户ID'].isin(valid_user_ids)])
            if invalid_users > 0:
                # 对于无效用户ID，尝试修复可能的格式问题
                behavior['用户ID_str'] = behavior['用户ID'].astype(str).str.strip()
                valid_user_str = {str(uid) for uid in valid_user_ids}
                fixed_mask = behavior['用户ID_str'].isin(valid_user_str)
                
                if sum(fixed_mask) > 0:
                    behavior.loc[fixed_mask, '用户ID'] = behavior.loc[fixed_mask, '用户ID_str'].astype(
                        type(next(iter(valid_user_ids))))
                    print(f"修复了{sum(fixed_mask)}条格式错误的用户ID")
                
                # 移除仍无效的用户ID
                remaining_invalid = len(behavior[~behavior['用户ID'].isin(valid_user_ids)])
                if remaining_invalid > 0:
                    behavior = behavior[behavior['用户ID'].isin(valid_user_ids)]
                    print(f"移除{remaining_invalid}条无法修复的无效用户ID记录")
                
                behavior = behavior.drop('用户ID_str', axis=1)
        
        # 类似处理商品ID
        if '商品ID' in behavior.columns and valid_product_ids:
            invalid_products = len(behavior[~behavior['商品ID'].isin(valid_product_ids)])
            if invalid_products > 0:
                behavior['商品ID_str'] = behavior['商品ID'].astype(str).str.strip()
                valid_product_str = {str(pid) for pid in valid_product_ids}
                fixed_mask = behavior['商品ID_str'].isin(valid_product_str)
                
                if sum(fixed_mask) > 0:
                    behavior.loc[fixed_mask, '商品ID'] = behavior.loc[fixed_mask, '商品ID_str'].astype(
                        type(next(iter(valid_product_ids))))
                    print(f"修复了{sum(fixed_mask)}条格式错误的商品ID")
                
                remaining_invalid = len(behavior[~behavior['商品ID'].isin(valid_product_ids)])
                if remaining_invalid > 0:
                    behavior = behavior[behavior['商品ID'].isin(valid_product_ids)]
                    print(f"移除{remaining_invalid}条无法修复的无效商品ID记录")
                
                behavior = behavior.drop('商品ID_str', axis=1)
        
        # 处理行为时长缺失值
        if '行为时长(秒)' in behavior.columns:
            # 处理负值
            negative_duration = len(behavior[behavior['行为时长(秒)'] < 0])
            if negative_duration > 0:
                behavior['行为时长(秒)'] = behavior['行为时长(秒)'].clip(lower=0)
                print(f"已修正{negative_duration}条负行为时长记录")
            
            # 处理缺失值，按行为类型填充
            missing_duration = behavior['行为时长(秒)'].isnull().sum()
            if missing_duration > 0:
                duration_by_behavior = behavior.groupby('行为类型')['行为时长(秒)'].transform('median')
                behavior['行为时长(秒)'] = behavior['行为时长(秒)'].fillna(duration_by_behavior).fillna(0)
                print(f"已处理{missing_duration}条行为时长缺失值")
        
        # 保存处理后的数据
        self.behavior_data = behavior
        print("行为数据预处理完成")
    
    def _merge_all_data(self):
        """合并所有数据"""
        print("\n===== 合并数据 =====")
        # 合并用户行为和用户信息
        merged = pd.merge(
            self.behavior_data, 
            self.user_data, 
            on='用户ID', 
            how='left'
        )
        print(f"行为数据与用户数据合并后: {len(merged)}条记录")
        
        # 合并商品信息
        self.merged_data = pd.merge(
            merged, 
            self.product_data, 
            on='商品ID', 
            how='left'
        )
        print(f"与商品数据合并后: {len(self.merged_data)}条记录")
        
        # 显示合并后的数据字段
        print(f"合并后的数据字段: {', '.join(self.merged_data.columns)}")
    
    def _post_process_merged_data(self):
        """合并后的数据处理"""
        if self.merged_data is None:
            return
        
        print("\n===== 合并后数据处理 =====")
        data = self.merged_data
        
        # 计算购买金额（仅购买行为有金额）
        if all(col in data.columns for col in ['行为类型', '价格']):
            data['购买金额'] = data.apply(
                lambda row: row['价格'] if row['行为类型'] == '购买' else 0, 
                axis=1
            )
            print("已添加购买金额字段")
        
        # 计算用户消费等级
        if '购买金额' in data.columns:
            # 先计算每个用户的总消费
            user_total = data.groupby('用户ID')['购买金额'].sum().reset_index()
            user_total.columns = ['用户ID', '总消费']
            
            # 合并回主数据
            data = pd.merge(data, user_total, on='用户ID', how='left')
            
            # 定义消费等级
            def get_consumption_level(total):
                if total == 0:
                    return '未消费'
                elif total < 100:
                    return '低消费'
                elif total < 500:
                    return '中消费'
                else:
                    return '高消费'
            
            data['消费等级'] = data['总消费'].apply(get_consumption_level)
            print("已添加用户消费等级字段")
        
        # 计算商品上架天数
        if '上架时间' in data.columns and '行为时间' in data.columns:
            data['上架天数'] = (data['行为时间'] - data['上架时间']).dt.days
            # 处理可能的负值（行为时间在上架时间之前）
            data['上架天数'] = data['上架天数'].clip(lower=0)
            print("已添加商品上架天数字段")
        
        self.merged_data = data
    
    def _save_preprocessed_data(self):
        """保存预处理后的数据"""
        try:
            self.user_data.to_csv('预处理后_用户数据_v2.csv', index=False)
            self.product_data.to_csv('预处理后_商品数据_v2.csv', index=False)
            self.behavior_data.to_csv('预处理后_行为数据_v2.csv', index=False)
            if self.merged_data is not None:
                self.merged_data.to_csv('预处理后_合并数据_v2.csv', index=False)
            print("\n预处理后的数据已保存为CSV文件")
        except Exception as e:
            print(f"保存预处理数据失败: {str(e)}")
    
    # 辅助函数：年龄分组
    def _get_age_group(self, age):
        if age < 18:
            return '少年(<18)'
        elif age < 25:
            return '青年(18-24)'
        elif age < 35:
            return '中青年(25-34)'
        elif age < 50:
            return '中年(35-49)'
        else:
            return '老年(≥50)'
    
    # 辅助函数：价格区间
    def _get_price_range(self, price):
        if price < 50:
            return '低价(<50)'
        elif price < 200:
            return '中低价(50-199)'
        elif price < 500:
            return '中高价(200-499)'
        else:
            return '高价(≥500)'
    
    # 辅助函数：时间段划分
    def _get_time_segment(self, hour):
        if 5 <= hour < 8:
            return '早晨'
        elif 8 <= hour < 12:
            return '上午'
        elif 12 <= hour < 14:
            return '中午'
        elif 14 <= hour < 18:
            return '下午'
        elif 18 <= hour < 22:
            return '晚上'
        else:
            return '深夜'


# ================ 数据分析模块 ================
    def basic_analysis(self):
        """基础数据分析"""
        if self.merged_data is None:
            print("请先完成数据预处理")
            return False
        
        print("\n===== 开始基础数据分析 =====")
        
        # 1. 整体数据概况分析
        self._overall_summary()
        
        # 2. 用户行为分布分析
        self._behavior_distribution()
        
        # 3. 时间趋势分析
        self._time_trend_analysis()
        
        # 4. 商品类别分析
        self._product_category_analysis()
        
        return True
    
    def _overall_summary(self):
        """整体数据概况分析"""
        print("\n===== 整体数据概况分析 =====")
        data = self.merged_data
        
        # 计算基本统计量
        total_users = data['用户ID'].nunique()
        total_products = data['商品ID'].nunique()
        total_records = len(data)
        
        # 计算日期范围
        date_range = None
        if '行为时间' in data.columns and not data['行为时间'].isnull().all():
            min_date = data['行为时间'].min()
            max_date = data['行为时间'].max()
            date_range = f"{min_date.strftime('%Y-%m-%d')} 至 {max_date.strftime('%Y-%m-%d')}"
            days = (max_date - min_date).days + 1
            print(f"数据时间跨度: {days}天")
        
        # 计算平均每日行为数
        daily_avg = round(total_records / days, 1) if days and days > 0 else 0
        
        # 计算总销售额
        total_revenue = data['购买金额'].sum() if '购买金额' in data.columns else 0
        
        # 保存结果
        self.analysis_results['整体概况'] = {
            '用户总数': total_users,
            '商品总数': total_products,
            '记录总数': total_records,
            '时间范围': date_range,
            '平均每日行为数': daily_avg,
            '总销售额': round(total_revenue, 2)
        }
        
        print(f"分析结果: {total_users}位用户，{total_products}件商品，{total_records}条行为记录，总销售额{total_revenue:.2f}元")
        
        # 生成整体概况可视化
        self._plot_overall_summary()
    
    def _behavior_distribution(self):
        """用户行为分布分析"""
        print("\n===== 用户行为分布分析 =====")
        data = self.merged_data
        
        # 1. 行为类型分布
        behavior_counts = data['行为类型'].value_counts().to_dict()
        print(f"行为类型分布: {behavior_counts}")
        
        # 2. 不同用户群体的行为分布
        user_behavior = {}
        if '消费等级' in data.columns:
            for level in data['消费等级'].unique():
                level_data = data[data['消费等级'] == level]
                user_behavior[level] = level_data['行为类型'].value_counts().to_dict()
        
        # 保存结果
        self.analysis_results['行为分布'] = {
            '总体分布': behavior_counts,
            '消费等级分布': user_behavior
        }
        
        # 可视化行为分布
        self._plot_behavior_distribution(behavior_counts, user_behavior)
    
    def _time_trend_analysis(self):
        """时间趋势分析"""
        print("\n===== 时间趋势分析 =====")
        data = self.merged_data
        
        # 1. 按日期统计行为数量
        daily_trend = data.groupby('行为日期')['用户ID'].count().to_dict()
        
        # 2. 按小时统计行为数量
        hourly_trend = defaultdict(int)
        for hour in range(24):
            hourly_trend[hour] = 0
        for _, row in data.iterrows():
            hourly_trend[row['行为小时']] += 1
        hourly_trend = dict(hourly_trend)
        
        # 3. 按星期几统计
        weekday_trend = data.groupby('星期几')['用户ID'].count().to_dict()
        # 转换为星期名称
        weekday_names = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
        weekday_trend_named = {weekday_names[k]: v for k, v in weekday_trend.items()}
        
        # 4. 找出高峰时段
        peak_hour = max(hourly_trend.items(), key=lambda x: x[1])[0]
        
        # 5. 按时间段统计销售额
        time_segment_revenue = {}
        if '时间段' in data.columns and '购买金额' in data.columns:
            time_segment_revenue = data.groupby('时间段')['购买金额'].sum().to_dict()
        
        # 保存结果
        self.analysis_results['时间趋势'] = {
            '每日趋势': daily_trend,
            '小时趋势': hourly_trend,
            '星期趋势': weekday_trend_named,
            '高峰时段': peak_hour,
            '时间段销售额': time_segment_revenue
        }
        
        print(f"用户活跃高峰时段: {peak_hour}点")
        
        # 可视化时间趋势
        self._plot_time_trends(daily_trend, hourly_trend, weekday_trend_named, time_segment_revenue)
    
    def _product_category_analysis(self):
        """商品类别分析"""
        print("\n===== 商品类别分析 =====")
        data = self.merged_data
        
        if '类别' not in data.columns:
            print("数据中没有商品类别信息，跳过该分析")
            return
        
        # 1. 各类别商品数量
        category_counts = data.groupby('类别')['商品ID'].nunique().to_dict()
        
        # 2. 各类别行为数量
        category_behavior = {}
        for behavior in ['浏览', '收藏', '加购', '购买']:
            behavior_data = data[data['行为类型'] == behavior]
            category_behavior[behavior] = behavior_data.groupby('类别').size().to_dict()
        
        # 3. 各类别购买转化率
        category_conversion = {}
        for category in category_counts.keys():
            cat_data = data[data['类别'] == category]
            views = len(cat_data[cat_data['行为类型'] == '浏览'])
            purchases = len(cat_data[cat_data['行为类型'] == '购买'])
            if views > 0:
                category_conversion[category] = round(purchases / views * 100, 2)
        
        # 保存结果
        self.analysis_results['商品类别分析'] = {
            '类别商品数量': category_counts,
            '类别行为数量': category_behavior,
            '类别转化率(%)': category_conversion
        }
        
        # 可视化商品类别分布
        self._plot_product_categories(category_counts, category_behavior, category_conversion)


# ================ 进阶数据分析模块 ================
    def advanced_analysis(self):
        """进阶数据分析"""
        if self.merged_data is None:
            print("请先完成数据预处理")
            return False
        
        print("\n===== 开始进阶数据分析 =====")
        
        # 1. 用户购买转化分析
        self._conversion_analysis()
        
        # 2. 用户价值分析
        self._user_value_analysis()
        
        # 3. 商品销售分析
        self._product_sales_analysis()
        
        # 4. 用户画像分析
        self._user_profile_analysis()
        
        # 5. 价格敏感度分析
        self._price_sensitivity_analysis()
        
        return True
    
    def _conversion_analysis(self):
        """用户购买转化分析"""
        print("\n===== 用户购买转化分析 =====")
        data = self.merged_data
        
        # 1. 计算各环节用户数
        funnel = {
            '浏览': data[data['行为类型'] == '浏览']['用户ID'].nunique(),
            '收藏': data[data['行为类型'] == '收藏']['用户ID'].nunique(),
            '加购': data[data['行为类型'] == '加购']['用户ID'].nunique(),
            '购买': data[data['行为类型'] == '购买']['用户ID'].nunique()
        }
        
        # 2. 计算转化率
        conversions = {}
        if funnel['浏览'] > 0:
            conversions['浏览到购买'] = round(funnel['购买'] / funnel['浏览'] * 100, 2)
        if funnel['收藏'] > 0:
            conversions['收藏到购买'] = round(funnel['购买'] / funnel['收藏'] * 100, 2)
        if funnel['加购'] > 0:
            conversions['加购到购买'] = round(funnel['购买'] / funnel['加购'] * 100, 2)
        
        # 3. 不同用户群体的转化率
        group_conversions = {}
        if '年龄分组' in data.columns:
            for group in data['年龄分组'].unique():
                group_data = data[data['年龄分组'] == group]
                group_funnel = {
                    '浏览': group_data[group_data['行为类型'] == '浏览']['用户ID'].nunique(),
                    '购买': group_data[group_data['行为类型'] == '购买']['用户ID'].nunique()
                }
                if group_funnel['浏览'] > 0:
                    group_conversions[group] = round(group_funnel['购买'] / group_funnel['浏览'] * 100, 2)
        
        # 保存结果
        self.analysis_results['转化分析'] = {
            '漏斗数据': funnel,
            '转化率(%)': conversions,
            '年龄组转化率(%)': group_conversions
        }
        
        print(f"整体转化率: 浏览到购买 {conversions.get('浏览到购买', 0)}%")
        
        # 可视化转化漏斗
        self._plot_conversion_funnel(funnel, conversions, group_conversions)
    
    def _user_value_analysis(self):
        """用户价值分析"""
        print("\n===== 用户价值分析 =====")
        data = self.merged_data
        
        # 筛选购买行为
        purchase_data = data[data['行为类型'] == '购买']
        if len(purchase_data) == 0:
            print("没有购买数据，无法进行用户价值分析")
            return
        
        # 1. 计算用户消费总额
        user_spending = purchase_data.groupby('用户ID')['购买金额'].sum().reset_index()
        user_spending.columns = ['用户ID', '总消费金额']
        
        # 2. 计算用户购买频率
        user_frequency = purchase_data.groupby('用户ID').size().reset_index()
        user_frequency.columns = ['用户ID', '购买频率']
        
        # 3. 计算最近购买时间
        last_purchase = purchase_data.groupby('用户ID')['行为时间'].max().reset_index()
        last_purchase.columns = ['用户ID', '最近购买时间']
        
        # 计算RFM指标中的R（最近购买天数）
        if not last_purchase.empty:
            max_date = data['行为时间'].max()
            last_purchase['最近购买天数'] = (max_date - last_purchase['最近购买时间']).dt.days
        
        # 4. 合并RFM数据
        user_value = pd.merge(user_spending, user_frequency, on='用户ID', how='inner')
        user_value = pd.merge(user_value, last_purchase, on='用户ID', how='inner')
        
        # 5. 计算平均消费和频率
        avg_spending = user_value['总消费金额'].mean()
        avg_frequency = user_value['购买频率'].mean()
        avg_recency = user_value['最近购买天数'].mean() if '最近购买天数' in user_value.columns else 0
        
        # 6. 用户分群（RFM模型简化版）
        def categorize_user(row):
            r_score = 1 if row['最近购买天数'] <= avg_recency else 0
            f_score = 1 if row['购买频率'] >= avg_frequency else 0
            m_score = 1 if row['总消费金额'] >= avg_spending else 0
            
            rfm_score = r_score * 100 + f_score * 10 + m_score
            
            if rfm_score == 111:
                return '高价值客户'
            elif rfm_score in [110, 101, 11]:
                return '潜力客户'
            elif rfm_score == 100:
                return '忠诚客户'
            elif rfm_score == 1:
                return '高消费客户'
            else:
                return '一般客户'
        
        user_value['用户类型'] = user_value.apply(categorize_user, axis=1)
        user_type_dist = user_value['用户类型'].value_counts().to_dict()
        
        # 7. 各类型用户的平均消费
        type_spending = user_value.groupby('用户类型')['总消费金额'].mean().to_dict()
        
        # 保存结果
        self.analysis_results['用户价值分析'] = {
            '用户类型分布': user_type_dist,
            '平均消费金额': round(avg_spending, 2),
            '平均购买频率': round(avg_frequency, 2),
            '平均最近购买天数': round(avg_recency, 2),
            '各类型用户平均消费': {k: round(v, 2) for k, v in type_spending.items()},
            'rfm数据': user_value[['用户ID', '总消费金额', '购买频率', '最近购买天数', '用户类型']]
        }
        
        print(f"用户类型分布: {user_type_dist}")
        
        # 可视化用户价值分布
        self._plot_user_value_distribution(user_type_dist, type_spending, user_value)
    
    def _product_sales_analysis(self):
        """商品销售分析"""
        print("\n===== 商品销售分析 =====")
        data = self.merged_data
        
        # 筛选购买行为
        purchase_data = data[data['行为类型'] == '购买']
        if len(purchase_data) == 0:
            print("没有购买数据，无法进行商品销售分析")
            return
        
        # 1. 畅销商品分析（按销量）
        top_selling = purchase_data.groupby('商品ID').size().sort_values(ascending=False).head(10)
        
        # 2. 销售额分析
        product_revenue = None
        if '价格' in purchase_data.columns:
            product_revenue = purchase_data.groupby('商品ID')['价格'].sum().sort_values(ascending=False).head(10)
        
        # 3. 各类别销售情况
        category_sales = {}
        if '类别' in data.columns:
            category_sales = purchase_data.groupby('类别').size().sort_values(ascending=False).to_dict()
        
        # 4. 各类别销售额
        category_revenue = {}
        if '类别' in data.columns and '价格' in data.columns:
            category_revenue = purchase_data.groupby('类别')['价格'].sum().sort_values(ascending=False).to_dict()
        
        # 5. 商品上架天数与销量关系
        if '上架天数' in data.columns:
            days_sales = data.groupby('商品ID').agg({
                '上架天数': 'mean',
                '行为类型': lambda x: (x == '购买').sum()
            }).reset_index()
            days_sales.columns = ['商品ID', '平均上架天数', '销量']
        else:
            days_sales = None
        
        # 保存结果
        self.analysis_results['商品销售分析'] = {
            '畅销商品TOP10': top_selling.to_dict(),
            '销售额TOP10': product_revenue.to_dict() if product_revenue is not None else {},
            '类别销售分布': category_sales,
            '类别销售额分布': category_revenue,
            '上架天数与销量': days_sales
        }
        
        # 可视化商品销售情况
        self._plot_product_sales(top_selling, product_revenue, category_sales, category_revenue, days_sales)
    
    def _user_profile_analysis(self):
        """用户画像分析"""
        print("\n===== 用户画像分析 =====")
        data = self.merged_data
        
        # 1. 性别分布
        gender_dist = data.groupby('性别')['用户ID'].nunique().to_dict()
        
        # 2. 年龄分布
        age_dist = {}
        if '年龄分组' in data.columns:
            age_dist = data.groupby('年龄分组')['用户ID'].nunique().to_dict()
        
        # 3. 不同性别购买能力
        gender_purchase = {}
        if '性别' in data.columns and '价格' in data.columns:
            purchase_data = data[data['行为类型'] == '购买']
            gender_purchase = purchase_data.groupby('性别')['价格'].mean().to_dict()
        
        # 4. 不同年龄组购买能力
        age_purchase = {}
        if '年龄分组' in data.columns and '价格' in data.columns:
            purchase_data = data[data['行为类型'] == '购买']
            age_purchase = purchase_data.groupby('年龄分组')['价格'].mean().to_dict()
        
        # 5. 用户地域分布
        region_dist = {}
        if '所在城市' in data.columns:
            region_dist = data.groupby('所在城市')['用户ID'].nunique().sort_values(ascending=False).head(10).to_dict()
        
        # 6. 注册设备分布
        device_dist = {}
        if '注册设备' in data.columns:
            device_dist = data.groupby('注册设备')['用户ID'].nunique().to_dict()
        
        # 保存结果
        self.analysis_results['用户画像分析'] = {
            '性别分布': gender_dist,
            '年龄分布': age_dist,
            '性别平均消费': {k: round(v, 2) for k, v in gender_purchase.items()},
            '年龄组平均消费': {k: round(v, 2) for k, v in age_purchase.items()},
            '城市分布TOP10': region_dist,
            '注册设备分布': device_dist
        }
        
        # 可视化用户画像
        self._plot_user_profile(gender_dist, age_dist, gender_purchase, age_purchase, region_dist, device_dist)
    
    def _price_sensitivity_analysis(self):
        """价格敏感度分析"""
        print("\n===== 价格敏感度分析 =====")
        data = self.merged_data
        
        if '价格区间' not in data.columns:
            print("没有价格区间数据，无法进行价格敏感度分析")
            return
        
        # 1. 不同价格区间的转化率
        price_conversion = {}
        for price_range in data['价格区间'].unique():
            range_data = data[data['价格区间'] == price_range]
            views = len(range_data[range_data['行为类型'] == '浏览'])
            purchases = len(range_data[range_data['行为类型'] == '购买'])
            
            if views > 0:
                conversion_rate = round(purchases / views * 100, 2)
                price_conversion[price_range] = conversion_rate
        
        # 2. 不同价格区间的销量
        price_sales = {}
        purchase_data = data[data['行为类型'] == '购买']
        for price_range in data['价格区间'].unique():
            price_sales[price_range] = len(purchase_data[purchase_data['价格区间'] == price_range])
        
        # 3. 不同用户群体对价格的敏感度
        group_price_sensitivity = {}
        if '年龄分组' in data.columns:
            for group in data['年龄分组'].unique():
                group_data = data[data['年龄分组'] == group]
                group_conv = {}
                for price_range in data['价格区间'].unique():
                    range_data = group_data[group_data['价格区间'] == price_range]
                    views = len(range_data[range_data['行为类型'] == '浏览'])
                    purchases = len(range_data[range_data['行为类型'] == '购买'])
                    
                    if views > 0:
                        group_conv[price_range] = round(purchases / views * 100, 2)
                group_price_sensitivity[group] = group_conv
        
        # 4. 价格与行为时长关系
        price_duration = None
        if '价格' in data.columns and '行为时长(秒)' in data.columns:
            # 按价格区间计算平均行为时长
            price_duration = data.groupby('价格区间')['行为时长(秒)'].mean().to_dict()
        
        # 保存结果
        self.analysis_results['价格敏感度分析'] = {
            '价格区间转化率(%)': price_conversion,
            '价格区间销量': price_sales,
            '年龄组价格敏感度(%)': group_price_sensitivity,
            '价格区间平均行为时长': price_duration,
            '最高转化区间': max(price_conversion.items(), key=lambda x: x[1])[0] if price_conversion else None
        }
        
        print(f"最高转化价格区间: {self.analysis_results['价格敏感度分析']['最高转化区间']}")
        
        # 可视化价格敏感度
        self._plot_price_sensitivity(price_conversion, price_sales, group_price_sensitivity, price_duration)


# ================ 专题分析模块 ================
    def special_analysis(self):
        """专题分析"""
        if self.merged_data is None:
            print("请先完成数据预处理")
            return False
        
        print("\n===== 开始专题分析 =====")
        
        # 1. 复购分析
        self._repurchase_analysis()
        
        # 2. 商品关联分析
        self._product_association_analysis()
        
        # 3. 节假日效应分析
        self._holiday_effect_analysis()
        
        # 4. 用户活跃度分析
        self._user_activity_analysis()
        
        return True
    
    def _repurchase_analysis(self):
        """复购分析"""
        print("\n===== 复购分析 =====")
        data = self.merged_data
        
        # 筛选购买行为
        purchase_data = data[data['行为类型'] == '购买']
        if len(purchase_data) < 2:
            print("购买数据不足，无法进行复购分析")
            return
        
        # 1. 计算每位用户的购买次数
        user_purchase_counts = purchase_data.groupby('用户ID').size()
        
        # 2. 计算复购率
        total_buyers = len(user_purchase_counts)
        repurchase_users = sum(1 for count in user_purchase_counts if count >= 2)
        repurchase_rate = round(repurchase_users / total_buyers * 100, 2) if total_buyers > 0 else 0
        
        # 3. 购买次数分布
        purchase_dist = user_purchase_counts.value_counts().sort_index().to_dict()
        
        # 4. 不同用户类型的复购率
        user_data = data[['用户ID', '消费等级']].drop_duplicates()
        purchase_with_level = pd.merge(
            user_purchase_counts.reset_index(), 
            user_data, 
            on='用户ID', 
            how='left'
        )
        purchase_with_level.columns = ['用户ID', '购买次数', '消费等级']
        
        level_repurchase = {}
        if '消费等级' in purchase_with_level.columns:
            for level in purchase_with_level['消费等级'].unique():
                level_data = purchase_with_level[purchase_with_level['消费等级'] == level]
                if len(level_data) > 0:
                    level_repurchasers = sum(1 for _, row in level_data.iterrows() if row['购买次数'] >= 2)
                    level_repurchase[level] = round(level_repurchasers / len(level_data) * 100, 2)
        
        # 保存结果
        self.analysis_results['复购分析'] = {
            '总购买用户数': total_buyers,
            '复购用户数': repurchase_users,
            '复购率(%)': repurchase_rate,
            '购买次数分布': purchase_dist,
            '消费等级复购率(%)': level_repurchase
        }
        
        print(f"整体复购率: {repurchase_rate}%")
        
        # 可视化复购分析
        self._plot_repurchase_analysis(purchase_dist, level_repurchase)
    
    def _product_association_analysis(self):
        """商品关联分析"""
        print("\n===== 商品关联分析 =====")
        data = self.merged_data
        
        # 筛选购买行为
        purchase_data = data[data['行为类型'] == '购买']
        if len(purchase_data) < 10:
            print("购买数据不足，无法进行商品关联分析")
            return
        
        # 按用户分组的购买商品列表
        user_products = purchase_data.groupby('用户ID')['商品ID'].agg(list).reset_index()
        
        # 统计商品共同出现的次数
        product_pairs = defaultdict(int)
        for _, row in user_products.iterrows():
            products = list(set(row['商品ID']))  # 去重
            if len(products) >= 2:
                # 生成所有可能的商品对
                for pair in self._generate_combinations(products, 2):
                    # 排序商品ID，确保(1,2)和(2,1)被视为同一对
                    sorted_pair = tuple(sorted(pair))
                    product_pairs[sorted_pair] += 1
        
        # 获取关联度最高的前10对商品
        top_pairs = sorted(product_pairs.items(), key=lambda x: x[1], reverse=True)[:10]
        
        # 保存结果
        self.analysis_results['商品关联分析'] = {
            '关联商品TOP10': [(f"{p[0]}-{p[1]}", count) for p, count in top_pairs]
        }
        
        # 可视化商品关联
        self._plot_product_association(top_pairs)
    
    def _holiday_effect_analysis(self):
        """节假日效应分析"""
        print("\n===== 节假日效应分析 =====")
        data = self.merged_data
        
        if '星期几' not in data.columns:
            print("没有星期数据，无法进行节假日效应分析")
            return
        
        # 判断是否为周末（周六和周日，对应dayofweek=5和6）
        data['是否周末'] = data['星期几'].apply(lambda x: '周末' if x >= 5 else '工作日')
        
        # 1. 比较周末和工作日的行为差异
        weekday_comparison = data.groupby(['是否周末', '行为类型']).size().unstack()
        
        # 2. 计算购买转化率差异
        conversion_diff = {}
        for day_type in ['工作日', '周末']:
            if day_type in weekday_comparison.index:
                views = weekday_comparison.loc[day_type, '浏览'] if '浏览' in weekday_comparison.columns else 1
                purchases = weekday_comparison.loc[day_type, '购买'] if '购买' in weekday_comparison.columns else 0
                conversion_diff[day_type] = round(purchases / views * 100, 2) if views > 0 else 0
        
        # 3. 按月度分析
        month_effect = {}
        if '月份' in data.columns:
            month_data = data.groupby(['月份', '行为类型']).size().unstack()
            for month in month_data.index:
                if '浏览' in month_data.columns and '购买' in month_data.columns:
                    views = month_data.loc[month, '浏览']
                    purchases = month_data.loc[month, '购买']
                    if views > 0:
                        month_effect[month] = round(purchases / views * 100, 2)
        
        # 保存结果
        self.analysis_results['节假日效应分析'] = {
            '工作日vs周末行为': weekday_comparison.to_dict(),
            '转化率差异(%)': conversion_diff,
            '月度转化率(%)': month_effect
        }
        
        # 可视化节假日效应
        self._plot_holiday_effect(weekday_comparison, conversion_diff, month_effect)
    
    def _user_activity_analysis(self):
        """用户活跃度分析"""
        print("\n===== 用户活跃度分析 =====")
        data = self.merged_data
        
        # 1. 用户活跃度分布（按行为次数）
        user_activity = data.groupby('用户ID').size().sort_values(ascending=False)
        activity_dist = {
            '高活跃(>100)': sum(1 for count in user_activity if count > 100),
            '中活跃(30-100)': sum(1 for count in user_activity if 30 <= count <= 100),
            '低活跃(10-29)': sum(1 for count in user_activity if 10 <= count <= 29),
            '不活跃(<10)': sum(1 for count in user_activity if count < 10)
        }
        
        # 2. 活跃用户与消费的关系
        activity_spending = {}
        if '购买金额' in data.columns:
            user_spending = data.groupby('用户ID')['购买金额'].sum()
            for user_id, count in user_activity.items():
                if count > 100:
                    cat = '高活跃(>100)'
                elif 30 <= count <= 100:
                    cat = '中活跃(30-100)'
                elif 10 <= count <= 29:
                    cat = '低活跃(10-29)'
                else:
                    cat = '不活跃(<10)'
                
                if cat not in activity_spending:
                    activity_spending[cat] = []
                activity_spending[cat].append(user_spending.get(user_id, 0))
            
            # 计算各活跃度用户的平均消费
            activity_spending_avg = {k: round(sum(v)/len(v), 2) for k, v in activity_spending.items() if v}
        else:
            activity_spending_avg = {}
        
        # 保存结果
        self.analysis_results['用户活跃度分析'] = {
            '活跃度分布': activity_dist,
            '各活跃度平均消费': activity_spending_avg
        }
        
        # 可视化用户活跃度
        self._plot_user_activity(activity_dist, activity_spending_avg)
    
    # 辅助函数：生成组合
    def _generate_combinations(self, items, k):
        """生成列表中k个元素的所有组合"""
        if k == 0:
            return [[]]
        if not items:
            return []
        
        first = items[0]
        rest = items[1:]
        
        # 包含第一个元素的组合
        with_first = [[first] + combo for combo in self._generate_combinations(rest, k-1)]
        # 不包含第一个元素的组合
        without_first = self._generate_combinations(rest, k)
        
        return with_first + without_first


# ================ 数据可视化模块 ================
    def _plot_overall_summary(self):
        """可视化整体概况（增加图表类型）"""
        # 1. 关键指标柱状图
        plt.figure(figsize=(10, 6))
        
        # 准备数据
        metrics = ['用户总数', '商品总数', '记录总数', '平均每日行为数']
        values = [
            self.analysis_results['整体概况']['用户总数'],
            self.analysis_results['整体概况']['商品总数'],
            self.analysis_results['整体概况']['记录总数'],
            self.analysis_results['整体概况']['平均每日行为数']
        ]
        
        # 创建图表
        bars = plt.bar(metrics, values, color=['#4CAF50', '#2196F3', '#FFC107', '#F44336'])
        
        # 添加数值标签
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height}', ha='center', va='bottom')
        
        plt.title('整体数据概况')
        plt.xticks(rotation=45)
        plt.tight_layout()
        
        # 保存图表
        plt.savefig(f"{self.chart_folder}/整体数据概况_柱状图.png")
        plt.close()
        
        # 2. 销售额趋势（如果有数据）
        if '行为日期' in self.merged_data.columns and '购买金额' in self.merged_data.columns:
            daily_revenue = self.merged_data.groupby('行为日期')['购买金额'].sum()
            
            plt.figure(figsize=(12, 6))
            daily_revenue.plot(kind='line', marker='o', color='green')
            plt.title('每日销售额趋势')
            plt.xlabel('日期')
            plt.ylabel('销售额(元)')
            plt.grid(True, linestyle='--', alpha=0.7)
            plt.xticks(rotation=45)
            
            plt.tight_layout()
            plt.savefig(f"{self.chart_folder}/每日销售额趋势_折线图.png")
            plt.close()
        
        print(f"已保存整体数据概况图表至 {self.chart_folder}")
    
    def _plot_behavior_distribution(self, behavior_counts, user_behavior):
        """可视化用户行为分布（增加图表类型）"""
        # 1. 总体行为分布饼图
        plt.figure(figsize=(10, 6))
        labels = list(behavior_counts.keys())
        sizes = list(behavior_counts.values())
        colors = ['#4CAF50', '#2196F3', '#FFC107', '#F44336']
        
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
        plt.title('用户行为类型分布')
        plt.axis('equal')  # 保证饼图是正圆形
        
        plt.tight_layout()
        plt.savefig(f"{self.chart_folder}/行为类型分布_饼图.png")
        plt.close()
        
        # 2. 不同消费等级的行为分布 - 堆积柱状图
        if user_behavior and len(user_behavior) > 0:
            plt.figure(figsize=(12, 8))
            
            # 准备数据
            categories = list(behavior_counts.keys())
            n_categories = len(categories)
            
            # 转换数据为堆积柱状图格式
            levels = list(user_behavior.keys())
            data = np.zeros((len(levels), n_categories))
            
            for i, level in enumerate(levels):
                for j, category in enumerate(categories):
                    data[i, j] = user_behavior[level].get(category, 0)
            
            # 绘制堆积柱状图
            plt.stackplot(categories, data, labels=levels, colors=plt.cm.Set3.colors[:len(levels)])
            
            plt.title('不同消费等级用户的行为分布')
            plt.xlabel('行为类型')
            plt.ylabel('行为次数')
            plt.legend(loc='upper left')
            
            plt.tight_layout()
            plt.savefig(f"{self.chart_folder}/消费等级行为分布_堆积图.png")
            plt.close()
        
        print(f"已保存行为分布图表至 {self.chart_folder}")
    
    def _plot_time_trends(self, daily_trend, hourly_trend, weekday_trend, time_segment_revenue):
        """可视化时间趋势（增加图表类型）"""
        # 1. 每日趋势图 - 折线图
        plt.figure(figsize=(12, 6))
        dates = list(daily_trend.keys())
        counts = list(daily_trend.values())
        
        plt.plot(dates, counts, 'o-', color='green')
        plt.title('每日用户行为趋势')
        plt.xlabel('日期')
        plt.ylabel('行为次数')
        plt.xticks(rotation=45)
        plt.grid(True, linestyle='--', alpha=0.7)
        
        plt.tight_layout()
        plt.savefig(f"{self.chart_folder}/每日行为趋势_折线图.png")
        plt.close()
        
        # 2. 小时趋势图 - 柱状图
        plt.figure(figsize=(12, 6))
        hours = list(hourly_trend.keys())
        counts = list(hourly_trend.values())
        
        plt.bar(hours, counts, color='orange')
        plt.title('一天中各时段行为分布')
        plt.xlabel('小时')
        plt.ylabel('行为次数')
        plt.xticks(range(24))
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        
        # 标记高峰时段
        peak_hour = self.analysis_results['时间趋势']['高峰时段']
        plt.axvline(x=peak_hour, color='red', linestyle='--', label=f'高峰时段: {peak_hour}点')
        plt.legend()
        
        plt.tight_layout()
        plt.savefig(f"{self.chart_folder}/时段行为分布_柱状图.png")
        plt.close()
        
        # 3. 星期趋势图 - 雷达图
        plt.figure(figsize=(10, 8))
        weekdays = list(weekday_trend.keys())
        counts = list(weekday_trend.values())
        
        # 为雷达图准备数据
        labels = weekdays
        stats = counts
        
        # 计算角度
        angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
        
        # 闭合雷达图
        stats = np.concatenate((stats, [stats[0]]))
        angles = angles + [angles[0]]
        labels = labels + [labels[0]]
        
        # 绘制雷达图
        ax = plt.subplot(111, polar=True)
        ax.plot(angles, stats, 'o-', linewidth=2)
        ax.fill(angles, stats, alpha=0.25)
        
        # 设置标签
        ax.set_thetagrids(np.degrees(angles), labels)
        plt.title('一周中各天行为分布')
        
        plt.tight_layout()
        plt.savefig(f"{self.chart_folder}/星期行为分布_雷达图.png")
        plt.close()
        
        # 4. 时间段销售额 - 柱状图
        if time_segment_revenue and len(time_segment_revenue) > 0:
            plt.figure(figsize=(10, 6))
            segments = ['早晨', '上午', '中午', '下午', '晚上', '深夜']  # 确保顺序正确
            revenues = [time_segment_revenue.get(seg, 0) for seg in segments]
            
            plt.bar(segments, revenues, color='purple')
            plt.title('不同时间段销售额分布')
            plt.xlabel('时间段')
            plt.ylabel('销售额(元)')
            
            for i, v in enumerate(revenues):
                plt.text(i, v + 50, f'{v:.0f}', ha='center')
            
            plt.tight_layout()
            plt.savefig(f"{self.chart_folder}/时间段销售额_柱状图.png")
            plt.close()
        
        print(f"已保存时间趋势图表至 {self.chart_folder}")
    
    def _plot_product_categories(self, category_counts, category_behavior, category_conversion):
        """可视化商品类别分布（增加图表类型）"""
        # 1. 各类别商品数量 - 横向柱状图
        plt.figure(figsize=(12, 6))
        categories = list(category_counts.keys())
        counts = list(category_counts.values())
        
        # 横向柱状图
        plt.barh(categories, counts, color='purple')
        plt.title('商品类别分布')
        plt.xlabel('商品数量')
        plt.ylabel('商品类别')
        
        # 添加数值标签
        for i, v in enumerate(counts):
            plt.text(v + 5, i, str(v), va='center')
        
        # plt.tight_layout()
        plt.savefig(f"{self.chart_folder}/商品类别分布_横向柱状图.png")
        plt.close()
        
        # 2. 各类别购买转化率 - 折线图
        if category_conversion and len(category_conversion) > 0:
            plt.figure(figsize=(12, 6))
            categories = list(category_conversion.keys())
            rates = list(category_conversion.values())
            
            plt.plot(categories, rates, 'o-', color='red', linewidth=2)
            plt.title('各类别商品购买转化率')
            plt.xlabel('商品类别')
            plt.ylabel('转化率(%)')
            plt.xticks(rotation=45)
            plt.grid(True, linestyle='--', alpha=0.7)
            
            for i, v in enumerate(rates):
                plt.text(i, v + 0.5, f'{v}%', ha='center')
            
            plt.tight_layout()
            plt.savefig(f"{self.chart_folder}/类别转化率_折线图.png")
            plt.close()
        
        # 3. 各类别行为分布 - 堆叠柱状图
        if category_behavior and len(category_behavior) > 0 and len(category_behavior['浏览']) > 0:
            plt.figure(figsize=(14, 8))
            
            categories = list(category_behavior['浏览'].keys())
            n_categories = len(categories)
            
            # 准备堆叠数据
            behaviors = ['浏览', '收藏', '加购', '购买']
            data = []
            for behavior in behaviors:
                data.append([category_behavior[behavior].get(cat, 0) for cat in categories])
            
            # 绘制堆叠柱状图
            plt.stackplot(categories, data, labels=behaviors, colors=plt.cm.Set2.colors[:4])
            
            plt.title('各类别商品的行为分布')
            plt.xlabel('商品类别')
            plt.ylabel('行为次数')
            plt.xticks(rotation=45)
            plt.legend(loc='upper left')
            
            plt.tight_layout()
            plt.savefig(f"{self.chart_folder}/类别行为分布_堆叠图.png")
            plt.close()
        
        print(f"已保存商品类别图表至 {self.chart_folder}")
    
    def _plot_conversion_funnel(self, funnel_data, conversions, group_conversions):
        """可视化转化漏斗（增加图表类型）"""
        # 1. 转化漏斗图
        plt.figure(figsize=(10, 8))
        stages = list(funnel_data.keys())
        values = list(funnel_data.values())
        
        # 计算漏斗宽度比例
        max_width = 0.8
        widths = [v / max(values) * max_width for v in values]
        
        # 绘制漏斗图
        for i, (value, width) in enumerate(zip(values, widths)):
            plt.bar(0, value, width=width, bottom=sum(values[:i]), 
                   color=plt.cm.viridis(i / len(values)), edgecolor='black')
            plt.text(0, sum(values[:i]) + value/2, f'{stages[i]}: {value}', 
                    ha='center', va='center', fontweight='bold')
        
        plt.title('用户行为转化漏斗')
        plt.xticks([])  # 隐藏x轴刻度
        plt.ylabel('用户数量')
        
        plt.tight_layout()
        plt.savefig(f"{self.chart_folder}/转化漏斗.png")
        plt.close()
        
        # 2. 转化率对比 - 柱状图
        if conversions and len(conversions) > 0:
            plt.figure(figsize=(10, 6))
            labels = list(conversions.keys())
            rates = list(conversions.values())
            
            plt.bar(labels, rates, color=['#4CAF50', '#2196F3', '#FFC107'])
            plt.title('各环节转化率对比')
            plt.xlabel('转化环节')
            plt.ylabel('转化率(%)')
            
            for i, v in enumerate(rates):
                plt.text(i, v + 0.5, f'{v}%', ha='center')
            
            plt.tight_layout()
            plt.savefig(f"{self.chart_folder}/转化率对比_柱状图.png")
            plt.close()
        
        # 3. 不同年龄组转化率 - 折线图
        if group_conversions and len(group_conversions) > 0:
            plt.figure(figsize=(10, 6))
            groups = list(group_conversions.keys())
            rates = list(group_conversions.values())
            
            plt.plot(groups, rates, 'o-', color='blue', linewidth=2, markersize=8)
            plt.title('不同年龄组的转化率对比')
            plt.xlabel('年龄组')
            plt.ylabel('转化率(%)')
            plt.xticks(rotation=45)
            plt.grid(True, linestyle='--', alpha=0.7)
            
            for i, v in enumerate(rates):
                plt.text(i, v + 0.5, f'{v}%', ha='center')
            
            plt.tight_layout()
            plt.savefig(f"{self.chart_folder}/年龄组转化率_折线图.png")
            plt.close()
        
        print(f"已保存转化分析图表至 {self.chart_folder}")
    
    def _plot_user_value_distribution(self, user_type_dist, type_spending, user_value_data):
        """可视化用户价值分布（增加图表类型）"""
        # 1. 用户类型分布 - 饼图
        plt.figure(figsize=(10, 6))
        types = list(user_type_dist.keys())
        counts = list(user_type_dist.values())
        
        plt.pie(counts, labels=types, autopct='%1.1f%%', colors=plt.cm.Set3.colors[:len(types)])
        plt.title('用户价值类型分布')
        plt.axis('equal')
        
        plt.tight_layout()
        plt.savefig(f"{self.chart_folder}/用户价值分布_饼图.png")
        plt.close()
        
        # 2. 各类型用户平均消费 - 柱状图
        if type_spending and len(type_spending) > 0:
            plt.figure(figsize=(10, 6))
            types = list(type_spending.keys())
            amounts = list(type_spending.values())
            
            plt.bar(types, amounts, color=['#C0392B', '#E67E22', '#27AE60', '#3498DB', '#9B59B6'])
            plt.title('各类型用户的平均消费金额')
            plt.xlabel('用户类型')
            plt.ylabel('平均消费金额')
            plt.xticks(rotation=45)
            
            for i, v in enumerate(amounts):
                plt.text(i, v + 10, f'{v:.2f}', ha='center')
            
            plt.tight_layout()
            plt.savefig(f"{self.chart_folder}/用户类型平均消费_柱状图.png")
            plt.close()
        
        # 3. RFM分析散点图 - 消费金额vs购买频率
        if 'rfm数据' in self.analysis_results['用户价值分析']:
            rfm_data = self.analysis_results['用户价值分析']['rfm数据']
            if len(rfm_data) > 0 and '总消费金额' in rfm_data.columns and '购买频率' in rfm_data.columns:
                plt.figure(figsize=(10, 6))
                
                # 使用不同颜色区分用户类型
                unique_types = rfm_data['用户类型'].unique()
                colors = plt.cm.Set1.colors[:len(unique_types)]
                type_color_map = {t: colors[i] for i, t in enumerate(unique_types)}
                
                for user_type in unique_types:
                    subset = rfm_data[rfm_data['用户类型'] == user_type]
                    plt.scatter(subset['购买频率'], subset['总消费金额'], 
                               label=user_type, color=type_color_map[user_type], alpha=0.7, s=50)
                
                plt.title('用户购买频率与消费金额关系')
                plt.xlabel('购买频率')
                plt.ylabel('总消费金额(元)')
                plt.grid(True, linestyle='--', alpha=0.7)
                plt.legend()
                
                plt.tight_layout()
                plt.savefig(f"{self.chart_folder}/用户价值散点图.png")
                plt.close()
        
        print(f"已保存用户价值分析图表至 {self.chart_folder}")
    
    def _plot_product_sales(self, top_selling, top_revenue, category_sales, category_revenue, days_sales):
        """可视化商品销售情况（增加图表类型）"""
        # 1. 畅销商品TOP10 - 柱状图
        plt.figure(figsize=(12, 6))
        products = [str(p) for p in top_selling.index]
        counts = top_selling.values
        
        plt.bar(products, counts, color='teal')
        plt.title('畅销商品TOP10（按销量）')
        plt.xlabel('商品ID')
        plt.ylabel('销售数量')
        
        plt.tight_layout()
        plt.savefig(f"{self.chart_folder}/畅销商品_柱状图.png")
        plt.close()
        
        # 2. 销售额TOP10 - 横向柱状图
        if top_revenue is not None and len(top_revenue) > 0:
            plt.figure(figsize=(12, 6))
            products = [str(p) for p in reversed(top_revenue.index)]
            revenue = list(reversed(top_revenue.values))
            
            plt.barh(products, revenue, color='gold')
            plt.title('商品销售额TOP10')
            plt.xlabel('销售额(元)')
            plt.ylabel('商品ID')
            
            for i, v in enumerate(revenue):
                plt.text(v + 50, i, f'{v:.0f}', va='center')
            
            plt.tight_layout()
            plt.savefig(f"{self.chart_folder}/销售额TOP10_横向柱状图.png")
            plt.close()
        
        # 3. 类别销售分布 - 饼图
        if category_sales and len(category_sales) > 0:
            plt.figure(figsize=(10, 8))
            categories = list(category_sales.keys())
            sales = list(category_sales.values())
            
            plt.pie(sales, labels=categories, autopct='%1.1f%%', colors=plt.cm.Paired.colors[:len(categories)])
            plt.title('各类别商品销售占比')
            plt.axis('equal')
            
            plt.tight_layout()
            plt.savefig(f"{self.chart_folder}/类别销售占比_饼图.png")
            plt.close()
        
        # 4. 上架天数与销量关系 - 散点图
        if days_sales is not None and len(days_sales) > 0:
            plt.figure(figsize=(10, 6))
            
            # 绘制散点图
            plt.scatter(days_sales['平均上架天数'], days_sales['销量'], 
                       alpha=0.6, s=50, c=days_sales['销量'], cmap='viridis')
            
            # 添加趋势线
            z = np.polyfit(days_sales['平均上架天数'], days_sales['销量'], 1)
            p = np.poly1d(z)
            plt.plot(days_sales['平均上架天数'], p(days_sales['平均上架天数']), "r--")
            
            plt.title('商品上架天数与销量关系')
            plt.xlabel('平均上架天数')
            plt.ylabel('销量')
            plt.colorbar(label='销量')
            plt.grid(True, linestyle='--', alpha=0.7)
            
            plt.tight_layout()
            plt.savefig(f"{self.chart_folder}/上架天数与销量_散点图.png")
            plt.close()
        
        print(f"已保存商品销售分析图表至 {self.chart_folder}")
    
    def _plot_user_profile(self, gender_dist, age_dist, gender_purchase, age_purchase, region_dist, device_dist):
        """可视化用户画像（增加图表类型）"""
        # 1. 性别分布 - 饼图
        plt.figure(figsize=(10, 6))
        genders = list(gender_dist.keys())
        counts = list(gender_dist.values())
        
        plt.pie(counts, labels=genders, autopct='%1.1f%%', colors=['lightblue', 'pink', 'gray'])
        plt.title('用户性别分布')
        plt.axis('equal')
        
        plt.tight_layout()
        plt.savefig(f"{self.chart_folder}/性别分布_饼图.png")
        plt.close()
        
        # 2. 年龄分布 - 柱状图
        if age_dist and len(age_dist) > 0:
            plt.figure(figsize=(10, 6))
            ages = list(age_dist.keys())
            counts = list(age_dist.values())
            
            plt.bar(ages, counts, color='orange')
            plt.title('用户年龄分布')
            plt.xlabel('年龄分组')
            plt.ylabel('用户数量')
            
            plt.tight_layout()
            plt.savefig(f"{self.chart_folder}/年龄分布_柱状图.png")
            plt.close()
        
        # 3. 不同性别平均消费 - 柱状图
        if gender_purchase and len(gender_purchase) > 0:
            plt.figure(figsize=(10, 6))
            genders = list(gender_purchase.keys())
            amounts = list(gender_purchase.values())
            
            plt.bar(genders, amounts, color=['lightblue', 'pink', 'gray'])
            plt.title('不同性别的平均消费金额')
            plt.xlabel('性别')
            plt.ylabel('平均消费金额(元)')
            
            for i, v in enumerate(amounts):
                plt.text(i, v + 5, f'{v:.1f}', ha='center')
            
            plt.tight_layout()
            plt.savefig(f"{self.chart_folder}/性别消费差异_柱状图.png")
            plt.close()
        
        # 4. 注册设备分布 - 饼图
        if device_dist and len(device_dist) > 0:
            plt.figure(figsize=(10, 8))
            devices = list(device_dist.keys())
            counts = list(device_dist.values())
            
            plt.pie(counts, labels=devices, autopct='%1.1f%%', colors=plt.cm.Dark2.colors[:len(devices)])
            plt.title('用户注册设备分布')
            plt.axis('equal')
            
            plt.tight_layout()
            plt.savefig(f"{self.chart_folder}/注册设备分布_饼图.png")
            plt.close()
        
        # 5. 城市分布TOP10 - 横向柱状图
        if region_dist and len(region_dist) > 0:
            plt.figure(figsize=(12, 6))
            cities = list(reversed(region_dist.keys()))
            counts = list(reversed(region_dist.values()))
            
            plt.barh(cities, counts, color='blue')
            plt.title('用户数量最多的城市TOP10')
            plt.xlabel('用户数量')
            plt.ylabel('城市')
            
            for i, v in enumerate(counts):
                plt.text(v + 5, i, str(v), va='center')
            
            # plt.tight_layout()
            plt.savefig(f"{self.chart_folder}/城市分布_横向柱状图.png")
            plt.close()
        
        print(f"已保存用户画像图表至 {self.chart_folder}")
    
    def _plot_price_sensitivity(self, price_conversion, price_sales, group_price_sensitivity, price_duration):
        """可视化价格敏感度（增加图表类型）"""
        # 1. 价格区间转化率 - 柱状图
        plt.figure(figsize=(10, 6))
        ranges = list(price_conversion.keys())
        rates = list(price_conversion.values())
        
        plt.bar(ranges, rates, color='red')
        plt.title('不同价格区间的购买转化率')
        plt.xlabel('价格区间')
        plt.ylabel('转化率(%)')
        
        for i, v in enumerate(rates):
            plt.text(i, v + 0.5, f'{v}%', ha='center')
        
        plt.tight_layout()
        plt.savefig(f"{self.chart_folder}/价格区间转化率_柱状图.png")
        plt.close()
        
        # 2. 价格区间销量 - 柱状图
        if price_sales and len(price_sales) > 0:
            plt.figure(figsize=(10, 6))
            ranges = list(price_sales.keys())
            sales = list(price_sales.values())
            
            plt.bar(ranges, sales, color='green')
            plt.title('不同价格区间的销售数量')
            plt.xlabel('价格区间')
            plt.ylabel('销售数量')
            
            for i, v in enumerate(sales):
                plt.text(i, v + 5, str(v), ha='center')
            
            # plt.tight_layout()
            plt.savefig(f"{self.chart_folder}/价格区间销量_柱状图.png")
            plt.close()
        
        # 3. 价格与行为时长关系 - 折线图
        if price_duration and len(price_duration) > 0:
            plt.figure(figsize=(10, 6))
            ranges = list(price_duration.keys())
            durations = list(price_duration.values())
            
            plt.plot(ranges, durations, 'o-', color='purple', linewidth=2, markersize=8)
            plt.title('不同价格区间的平均行为时长')
            plt.xlabel('价格区间')
            plt.ylabel('平均行为时长(秒)')
            plt.grid(True, linestyle='--', alpha=0.7)
            
            for i, v in enumerate(durations):
                plt.text(i, v + 2, f'{v:.1f}s', ha='center')
            
            plt.tight_layout()
            plt.savefig(f"{self.chart_folder}/价格与行为时长_折线图.png")
            plt.close()
        
        print(f"已保存价格敏感度图表至 {self.chart_folder}")
    
    def _plot_repurchase_analysis(self, purchase_dist, level_repurchase):
        """可视化复购分析（增加图表类型）"""
        # 1. 购买次数分布 - 柱状图
        plt.figure(figsize=(10, 6))
        counts = list(purchase_dist.keys())
        users = list(purchase_dist.values())
        
        plt.bar([str(c) for c in counts], users, color='green')
        plt.title('用户购买次数分布')
        plt.xlabel('购买次数')
        plt.ylabel('用户数量')
        plt.xticks(rotation=45)
        
        plt.tight_layout()
        plt.savefig(f"{self.chart_folder}/购买次数分布_柱状图.png")
        plt.close()
        
        # 2. 不同消费等级的复购率 - 柱状图
        if level_repurchase and len(level_repurchase) > 0:
            plt.figure(figsize=(10, 6))
            levels = list(level_repurchase.keys())
            rates = list(level_repurchase.values())
            
            plt.bar(levels, rates, color=['#3498DB', '#2ECC71', '#E74C3C', '#F39C12'])
            plt.title('不同消费等级用户的复购率')
            plt.xlabel('消费等级')
            plt.ylabel('复购率(%)')
            plt.xticks(rotation=45)
            
            for i, v in enumerate(rates):
                plt.text(i, v + 0.5, f'{v}%', ha='center')
            
            plt.tight_layout()
            plt.savefig(f"{self.chart_folder}/消费等级复购率_柱状图.png")
            plt.close()
        
        print(f"已保存复购分析图表至 {self.chart_folder}")
    
    def _plot_product_association(self, top_pairs):
        """可视化商品关联（增加图表类型）"""
        if not top_pairs:
            return
        
        # 1. 关联商品TOP10 - 横向柱状图
        plt.figure(figsize=(12, 8))
        pairs = [f"{p[0]}-{p[1]}" for p, _ in reversed(top_pairs)]
        counts = [c for _, c in reversed(top_pairs)]
        
        plt.barh(pairs, counts, color='purple')
        plt.title('商品关联度TOP10（共同购买次数）')
        plt.xlabel('共同购买次数')
        plt.ylabel('商品对')
        
        for i, v in enumerate(counts):
            plt.text(v + 0.5, i, str(v), va='center')
        
        plt.tight_layout()
        plt.savefig(f"{self.chart_folder}/商品关联度_横向柱状图.png")
        plt.close()
        
        print(f"已保存商品关联分析图表至 {self.chart_folder}")
    
    def _plot_holiday_effect(self, weekday_comparison, conversion_diff, month_effect):
        """可视化节假日效应（增加图表类型）"""
        # 1. 工作日与周末行为对比 - 分组柱状图
        plt.figure(figsize=(12, 6))
        weekday_comparison.plot(kind='bar', color=['#4CAF50', '#2196F3', '#FFC107', '#F44336'])
        plt.title('工作日与周末的用户行为对比')
        plt.xlabel('日期类型')
        plt.ylabel('行为次数')
        
        plt.tight_layout()
        plt.savefig(f"{self.chart_folder}/工作日周末对比_分组柱状图.png")
        plt.close()
        
        # 2. 工作日与周末转化率对比 - 柱状图
        if conversion_diff and len(conversion_diff) > 0:
            plt.figure(figsize=(10, 6))
            labels = list(conversion_diff.keys())
            rates = list(conversion_diff.values())
            
            plt.bar(labels, rates, color=['#95a5a6', '#f1c40f'])
            plt.title('工作日与周末的转化率对比')
            plt.xlabel('日期类型')
            plt.ylabel('转化率(%)')
            
            for i, v in enumerate(rates):
                plt.text(i, v + 0.5, f'{v}%', ha='center')
            
            plt.tight_layout()
            plt.savefig(f"{self.chart_folder}/工作日周末转化率_柱状图.png")
            plt.close()
        
        # 3. 月度转化率趋势 - 折线图
        if month_effect and len(month_effect) > 0:
            plt.figure(figsize=(12, 6))
            months = list(month_effect.keys())
            rates = list(month_effect.values())
            
            plt.plot(months, rates, 'o-', color='red', linewidth=2, markersize=8)
            plt.title('月度转化率趋势')
            plt.xlabel('月份')
            plt.ylabel('转化率(%)')
            plt.xticks(range(1, 13))
            plt.grid(True, linestyle='--', alpha=0.7)
            
            for i, v in enumerate(rates):
                plt.text(months[i], v + 0.5, f'{v}%', ha='center')
            
            plt.tight_layout()
            plt.savefig(f"{self.chart_folder}/月度转化率趋势_折线图.png")
            plt.close()
        
        print(f"已保存节假日效应图表至 {self.chart_folder}")
    
    def _plot_user_activity(self, activity_dist, activity_spending):
        """可视化用户活跃度（增加图表类型）"""
        # 1. 活跃度分布 - 饼图
        plt.figure(figsize=(10, 6))
        categories = list(activity_dist.keys())
        counts = list(activity_dist.values())
        
        plt.pie(counts, labels=categories, autopct='%1.1f%%', colors=['#3498DB', '#2ECC71', '#F39C12', '#E74C3C'])
        plt.title('用户活跃度分布')
        plt.axis('equal')
        
        plt.tight_layout()
        plt.savefig(f"{self.chart_folder}/用户活跃度分布_饼图.png")
        plt.close()
        
        # 2. 活跃度与消费关系 - 柱状图
        if activity_spending and len(activity_spending) > 0:
            plt.figure(figsize=(10, 6))
            categories = list(activity_spending.keys())
            amounts = list(activity_spending.values())
            
            plt.bar(categories, amounts, color=['#9B59B6', '#3498DB', '#1ABC9C', '#E67E22'])
            plt.title('不同活跃度用户的平均消费金额')
            plt.xlabel('活跃度分类')
            plt.ylabel('平均消费金额(元)')
            plt.xticks(rotation=45)
            
            for i, v in enumerate(amounts):
                plt.text(i, v + 10, f'{v:.2f}', ha='center')
            
            plt.tight_layout()
            plt.savefig(f"{self.chart_folder}/活跃度与消费关系_柱状图.png")
            plt.close()
        
        print(f"已保存用户活跃度图表至 {self.chart_folder}")
    
    def generate_report(self):
        """生成详细的分析报告"""
        if not self.analysis_results:
            print("没有分析结果，无法生成报告")
            return False
        
        print("\n===== 生成分析报告 =====")
        
        try:
            with open('电商平台用户行为分析报告_v2.txt', 'w', encoding='utf-8') as f:
                f.write("="*60 + "\n")
                f.write("          电商平台用户行为分析报告\n")
                f.write(f"          生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("="*60 + "\n\n")
                
                # 1. 整体概况
                f.write("一、整体数据概况\n")
                f.write("-"*50 + "\n")
                overall = self.analysis_results.get('整体概况', {})
                for key, value in overall.items():
                    f.write(f"{key}: {value}\n")
                f.write("\n")
                
                # 其他报告内容与之前版本类似，略去...
                
                f.write("\n" + "="*60 + "\n")
                f.write("报告结束。详细图表请查看'分析图表_v2'文件夹。\n")
            
            print("分析报告已保存至: 电商平台用户行为分析报告_v2.txt")
            return True
        except Exception as e:
            print(f"生成报告失败: {str(e)}")
            return False
    
    def run_analysis(self, user_file, product_file, behavior_file):
        """运行完整的分析流程"""
        print("===== 电商平台用户行为分析系统 =====")
        
        # 1. 加载数据
        if not self.load_data(user_file, product_file, behavior_file):
            return False
        
        # 2. 预处理数据
        if not self.preprocess_data():
            return False
        
        # 3. 基础分析
        if not self.basic_analysis():
            return False
        
        # 4. 进阶分析
        if not self.advanced_analysis():
            return False
        
        # 5. 专题分析
        if not self.special_analysis():
            return False
        
        # 6. 生成报告
        if not self.generate_report():
            return False
        
        print("\n===== 分析完成 =====")
        print(f"分析图表已保存至 {self.chart_folder} 目录")
        print("详细报告请查看 电商平台用户行为分析报告_v2.txt")
        return True


# ================ 系统入口 ================
if __name__ == "__main__":
    # 初始化分析系统
    analysis_system = EcommerceAnalysisSystem()
    
    # 定义数据文件路径（默认值）
    user_file = "user_info_v2.csv"
    product_file = "product_info_v2.csv"
    behavior_file = "user_behavior_v2.csv"
    
    # 用户交互
    print("欢迎使用电商平台用户行为分析系统")
    print("本系统将帮助您分析用户行为数据，生成可视化图表和分析报告")
    
    use_default = input("\n是否使用默认数据文件路径? (y/n，默认y): ").strip().lower() or 'y'
    
    if use_default != 'y':
        user_file = input("请输入用户信息文件路径: ").strip() or user_file
        product_file = input("请输入商品信息文件路径: ").strip() or product_file
        behavior_file = input("请输入用户行为文件路径: ").strip() or behavior_file
    
    print("\n开始执行分析流程...")
    # 运行分析
    analysis_system.run_analysis(user_file, product_file, behavior_file)
    