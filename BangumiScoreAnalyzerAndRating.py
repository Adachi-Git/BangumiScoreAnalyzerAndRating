import sqlite3
import json
import numpy as np
import matplotlib.pyplot as plt
import os


# 获取当前脚本所在目录
current_directory = os.path.dirname(os.path.abspath(__file__))

# 拼接数据库文件路径
db_path = os.path.join(current_directory, 'subject.db')
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# 查询数据库获取所有数据
cursor.execute("SELECT id, score_details FROM bgm_subject")
rows = cursor.fetchall()

# 初始化分数和对应人数的列表
scores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 创建一个列表来存储每个 ID 的结果
result = []

# 统计每个分数的人数并计算概率
for id, score_details_json in rows:
    score_details_dict = json.loads(score_details_json)
    
    # 计算每个分数的人数
    counts = [score_details_dict.get(str(score), 0) for score in scores]
    
    # 计算每个分数的概率密度，防止除零错误，设定默认概率
    total_count = sum(counts)
    
    if total_count < 50:
        # 如果评分人数小于50，则跳过该ID
        continue

    probabilities = [count / total_count for count in counts]

    # 使用概率加权随机抽样
    random_score = int(np.random.choice(scores, p=probabilities))
    
    # 添加每个 ID 的结果到列表中
    result.append({
        "id": id,
        "random_score": random_score,
        "average_score": np.average(scores, weights=probabilities),
        "score_counts": dict(zip(scores, counts)),
        "probability_distribution": probabilities
    })

# 关闭数据库连接
conn.close()

# 输出结果
output_file_path = r'C:\Users\Darling\Desktop\output.json'  # 请替换为你希望保存的文件路径
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    json.dump(result, output_file, ensure_ascii=False, indent=2)

print("结果已保存至:", output_file_path)

# 提取分数值
scores_only = [entry["random_score"] for entry in result]

# 统计各个分数的数量
score_counts = {score: scores_only.count(score) for score in scores}

# 计算标准差
std_deviation = np.std(scores_only)

print("各个分数的数量:", score_counts)
print("标准差:", std_deviation)

# 绘制分数的数量直方图
plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置中文显示
plt.rcParams['axes.unicode_minus'] = False  # 解决负号显示问题

plt.bar(score_counts.keys(), score_counts.values())
plt.xlabel("分数", fontsize=14) 
plt.ylabel("数量", fontsize=14) 
plt.title("各分数的数量分布")

# 在图表右侧显示标准差信息
plt.text(len(scores) + 0.5, max(score_counts.values()) / 2, f"标准差: {std_deviation:.2f}", fontsize=12, va='center', ha='left', rotation='vertical')

plt.show()