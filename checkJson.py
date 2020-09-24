# -*- coding=utf-8 -*-
import pandas
import json

df_p0 = pandas.read_excel('/Users/wb.xuxiaobing/Desktop/jsontest/场景模板0819-new.xlsx', sheet_name=0)
# df_p1 = pandas.read_excel('/Users/wb.xuxiaobing/Desktop/jsontest/埋点自动化校验规则11112222.xlsx', sheet_name=1)


# print df_p1

def checkJson(strCanbeChecked):
    try:
        json.loads(strCanbeChecked)
    except ValueError as e:
        # print e
        return e
    return True


# resList = []

resList_p0 = df_p0['scene_json_data'].values.tolist()
# resList_p1 = df_p1['canCheckPart'].values.tolist()
print(resList_p0)
print('############################')
# print(resList_p1)
resBool_p0 = []
# resBool_p1 = []
for i in resList_p0:
    aa = checkJson(i)
    # print aa
    resBool_p0.append(str(aa))
print(resBool_p0)

# for j in resList_p1:
#     bb = checkJson(j)
#     resBool_p1.append(str(bb))
# print(resBool_p1)

df_p0['checkRes'] = resBool_p0
# df_p1['checkRes'] = resBool_p1
writer = pandas.ExcelWriter('/Users/wb.xuxiaobing/Desktop/jsontest/0819.xlsx')
df_p0.to_excel(writer, 'scene', index=False, encoding='utf-8')
# df_p1.to_excel(writer, 'P1', index=False, encoding='utf-8')
writer.save()
