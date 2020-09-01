from flask import Flask, request, jsonify, Response
from flask_restful import Resource, Api
import json
import xlrd


app = Flask(__name__)
api = Api(app)


class AwsModel(Resource):

    def read_excel_data(self,filepath):
        # 读取Excel文件
        workbook = xlrd.open_workbook(filepath)
        # 获取sheet1 单选题库
        sheet = workbook.sheet_by_index(0)
        # 创建一个问题+选项+答案的列表
        question_list = []
        # 根据文件的条数做遍历
        for index in range(0, sheet.nrows):
            # print('index:',index)

            row_value = sheet.row_values(index)  # 获取每行的数据
            question_dict = {}
            question_dict['question'] = row_value[0]
            question_dict['A'] = row_value[1]
            question_dict['B'] = row_value[2]
            question_dict['C'] = row_value[3]
            question_dict['D'] = row_value[4]
            question_dict['answer'] = row_value[5]
            question_list.append(question_dict)

        print(len(question_list))
        return question_list

    def post(self):
        # 获取json数据
        res = request.json
        try:
            if res['TOKEN'] == 'aws-sap-cs':

                question_list = self.read_excel_data('aws.xlsx')
                response = {
                    'data': question_list[int(res['page'])]
                    # 'data': question_list
                }
                return response

        except Exception as e:
            return {'error': e}


api.add_resource(AwsModel, '/aws')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8787, debug=None)
