# BangumiScoreAnalyzerAndRating

BangumiScoreAnalyzerAndRating，旨在通过随机抽样的方式对评分数据进行分析。它连接到SQLite数据库，读取评分数据，并使用概率加权随机抽样方法生成随机评分。最后，将结果保存至JSON文件，并绘制各分数的数量分布直方图。

## 功能

- **番剧评分分析：** 分析用户对番剧的评分。
- **模拟打分：** 基于历史评分模拟番剧的评分。
- **统计功能：** 计算和展示平均分、分数分布和标准差等统计信息。

## 使用方法

1. **克隆仓库:**
    ```bash
    git clone https://github.com/Adachi-Git/BangumiScoreAnalyzerAndRating.git
    cd BangumiScoreAnalyzerAndRating
    ```

2. **安装依赖:**
    ```bash
    pip install -r requirements.txt
    ```

3. **运行项目:**
    ```bash
    python BangumiScoreAnalyzerAndRating.py
    ```

4. **输出:**
   - 模拟评分保存在 `output.json` 文件中。
   - 统计信息，包括分数分布和标准差，将弹出图表并在控制台打印。