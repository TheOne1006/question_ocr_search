## TODO

1. 科目questions 表
2. elk 搜索
3. 计划任务



### 导入数据
subjectId 对应

```js
/**
 * 学科编号 同
 * https://jdapi.jd100.com/coursemgr/v1/getSubjectList
 */
export const SUBJECT_NO = {
  CHINESE: 1,  // 语文
  MATHEMATICS: 2, // 数学
  ENGLISH: 3, // 英语
  PHYSICS: 4, // 物理
  CHEMISTRY: 5, // 化学
  BIOLOGY: 6, // 生物
  HISTORY: 7, // 历史
  GEOGRAPHY: 8, // 地理
  POLITICS: 9, // 政治
};

/**
 * 中学学科对应的编号
 */
export const SUBJECT_CHINESE_MAPPER = {
  '语文': 1, // 语文
  '数学': 2, // 数学
  '英语': 3, // 英语
  '物理': 4, // 物理
  '化学': 5, // 化学
  '生物': 6, // 生物
  '历史': 7, // 历史
  '地理': 8, // 地理
  '政治': 9, // 政治
};
```


### 设计表结构

