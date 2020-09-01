from flask import Flask, request, jsonify, Response
from flask_restful import Resource, Api
import json
import xlrd

app = Flask(__name__)
api = Api(app)


class AwsModel(Resource):

    def read_excel_data(self, filepath):
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
            option_list = []
            question_dict['question'] = row_value[0]
            option_list.append('A. ' + row_value[1])
            option_list.append('B. ' + row_value[2])
            option_list.append('C. ' + row_value[3])
            option_list.append('D. ' + row_value[4])
            question_dict['option'] = option_list
            question_dict['answer'] = row_value[5]
            question_list.append(question_dict)
        total_number = len(question_list)
        return question_list, total_number

    def post(self):
        # 获取json数据
        res = request.json
        try:
            if res['TOKEN'] == 'aws-sap-cs':
                question_list, total_number = self.read_excel_data('aws.xlsx')
                response = {
                    'data': question_list[int(res['page'])],
                    'total_number': total_number
                }
                return response

        except Exception as e:
            return {'error': e}


api.add_resource(AwsModel, '/aws')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8787, debug=None)
