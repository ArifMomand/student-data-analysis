import pandas as pd

# خواندن دیتا
students = pd.read_csv("data/students.csv")
marks = pd.read_csv("data/marks.csv")

# ETL (Join)
df = pd.merge(students, marks, left_on="id", right_on="student_id")

# ذخیره Data Warehouse
df.to_csv("data/data_warehouse.csv", index=False)

print("Data Warehouse ساخته شد!")

# تحلیل‌ها
avg_dep = df.groupby("department")["marks"].mean()
top_students = df.sort_values("marks", ascending=False).head(3)
count_dep = df["department"].value_counts()

print("\nAverage Marks by Department:")
print(avg_dep)

print("\nTop Students:")
print(top_students)

print("\nStudent Count by Department:")
print(count_dep)