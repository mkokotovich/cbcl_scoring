from apps.testing.utils import (
    ItemDescription,
    calculate_raw_scores,
    create_test_items,
    convert_to_return_value,
)


cbcl_6_18_items = [
    ItemDescription('1', description='', group='VI'),
    ItemDescription('2', description='', group='VII'),
    ItemDescription('3', description='', group='VIII'),
    ItemDescription('4', description='', group='VI'),
    ItemDescription('5', description='', group='II'),
    ItemDescription('6', description='', group='other'),
    ItemDescription('7', description='', group='other'),
    ItemDescription('8', description='', group='VI'),
    ItemDescription('9', description='', group='V'),
    ItemDescription('10', description='', group='VI'),
    ItemDescription('11', description='', group='IV'),
    ItemDescription('12', description='', group='IV'),
    ItemDescription('13', description='', group='VI'),
    ItemDescription('14', description='', group='I'),
    ItemDescription('15', description='', group='other'),
    ItemDescription('16', description='', group='VIII'),
    ItemDescription('17', description='', group='VI'),
    ItemDescription('18', description='', group='V'),
    ItemDescription('19', description='', group='VIII'),
    ItemDescription('20', description='', group='VIII'),
    ItemDescription('21', description='', group='VIII'),
    ItemDescription('22', description='', group='VIII'),
    ItemDescription('23', description='', group='VIII'),
    ItemDescription('24', description='', group='other'),
    ItemDescription('25', description='', group='IV'),
    ItemDescription('26', description='', group='VII'),
    ItemDescription('27', description='', group='IV'),
    ItemDescription('28', description='', group='VII'),
    ItemDescription('29', description='', group='I'),
    ItemDescription('30', description='', group='I'),
    ItemDescription('31', description='', group='I'),
    ItemDescription('32', description='', group='I'),
    ItemDescription('33', description='', group='I'),
    ItemDescription('34', description='', group='IV'),
    ItemDescription('35', description='', group='I'),
    ItemDescription('36', description='', group='IV'),
    ItemDescription('37', description='', group='VIII'),
    ItemDescription('38', description='', group='IV'),
    ItemDescription('39', description='', group='VII'),
    ItemDescription('40', description='', group='V'),
    ItemDescription('41', description='', group='VI'),
    ItemDescription('42', description='', group='II'),
    ItemDescription('43', description='', group='VII'),
    ItemDescription('44', description='', group='other'),
    ItemDescription('45', description='', group='I'),
    ItemDescription('46', description='', group='V'),
    ItemDescription('47', description='', group='III'),
    ItemDescription('48', description='', group='IV'),
    ItemDescription('49', description='', group='III'),
    ItemDescription('50', description='', group='I'),
    ItemDescription('51', description='', group='III'),
    ItemDescription('52', description='', group='I'),
    ItemDescription('53', description='', group='other'),
    ItemDescription('54', description='', group='III'),
    ItemDescription('55', description='', group='other'),
    ItemDescription('56a', description='', group='III'),
    ItemDescription('56b', description='', group='III'),
    ItemDescription('56c', description='', group='III'),
    ItemDescription('56d', description='', group='III'),
    ItemDescription('56e', description='', group='III'),
    ItemDescription('56f', description='', group='III'),
    ItemDescription('56g', description='', group='III'),
    ItemDescription('56h', description='', group='other'),
    ItemDescription('57', description='', group='VIII'),
    ItemDescription('58', description='', group='V'),
    ItemDescription('59', description='', group='V'),
    ItemDescription('60', description='', group='V'),
    ItemDescription('61', description='', group='VI'),
    ItemDescription('62', description='', group='IV'),
    ItemDescription('63', description='', group='VII'),
    ItemDescription('64', description='', group='IV'),
    ItemDescription('65', description='', group='II'),
    ItemDescription('66', description='', group='V'),
    ItemDescription('67', description='', group='VII'),
    ItemDescription('68', description='', group='VIII'),
    ItemDescription('69', description='', group='II'),
    ItemDescription('70', description='', group='V'),
    ItemDescription('71', description='', group='I'),
    ItemDescription('72', description='', group='VII'),
    ItemDescription('73', description='', group='VII'),
    ItemDescription('74', description='', group='other'),
    ItemDescription('75', description='', group='II'),
    ItemDescription('76', description='', group='V'),
    ItemDescription('77', description='', group='other'),
    ItemDescription('78', description='', group='VI'),
    ItemDescription('79', description='', group='IV'),
    ItemDescription('80', description='', group='VI'),
    ItemDescription('81', description='', group='VII'),
    ItemDescription('82', description='', group='VII'),
    ItemDescription('83', description='', group='V'),
    ItemDescription('84', description='', group='V'),
    ItemDescription('85', description='', group='V'),
    ItemDescription('86', description='', group='VIII'),
    ItemDescription('87', description='', group='VIII'),
    ItemDescription('88', description='', group='VIII'),
    ItemDescription('89', description='', group='VIII'),
    ItemDescription('90', description='', group='VII'),
    ItemDescription('91', description='', group='I'),
    ItemDescription('92', description='', group='V'),
    ItemDescription('93', description='', group='other'),
    ItemDescription('94', description='', group='VIII'),
    ItemDescription('95', description='', group='VIII'),
    ItemDescription('96', description='', group='VII'),
    ItemDescription('97', description='', group='VIII'),
    ItemDescription('98', description='', group='other'),
    ItemDescription('99', description='', group='VII'),
    ItemDescription('100', description='', group='V'),
    ItemDescription('101', description='', group='VII'),
    ItemDescription('102', description='', group='II'),
    ItemDescription('103', description='', group='II'),
    ItemDescription('104', description='', group='VIII'),
    ItemDescription('105', description='', group='VII'),
    ItemDescription('106', description='', group='VII'),
    ItemDescription('107', description='', group='other'),
    ItemDescription('108', description='', group='other'),
    ItemDescription('109', description='', group='other'),
    ItemDescription('110', description='', group='other'),
    ItemDescription('111', description='', group='II'),
    ItemDescription('112', description='', group='I'),
    ItemDescription('113', description='', group='other'),
]


cbcl_1_5_items = [
    ItemDescription('1', description='', group='III'),
    ItemDescription('2', description='', group='IV'),
    ItemDescription('3', description='', group='other'),
    ItemDescription('4', description='', group='IV'),
    ItemDescription('5', description='', group='VI'),
    ItemDescription('6', description='', group='VI'),
    ItemDescription('7', description='', group='III'),
    ItemDescription('8', description='', group='VII'),
    ItemDescription('9', description='', group='other'),
    ItemDescription('10', description='', group='II'),
    ItemDescription('11', description='', group='other'),
    ItemDescription('12', description='', group='III'),
    ItemDescription('13', description='', group='other'),
    ItemDescription('14', description='', group='other'),
    ItemDescription('15', description='', group='VII'),
    ItemDescription('16', description='', group='VII'),
    ItemDescription('17', description='', group='other'),
    ItemDescription('18', description='', group='VII'),
    ItemDescription('19', description='', group='III'),
    ItemDescription('20', description='', group='VII'),
    ItemDescription('21', description='', group='I'),
    ItemDescription('22', description='', group='V'),
    ItemDescription('23', description='', group='IV'),
    ItemDescription('24', description='', group='III'),
    ItemDescription('25', description='', group='other'),
    ItemDescription('26', description='', group='other'),
    ItemDescription('27', description='', group='VII'),
    ItemDescription('28', description='', group='other'),
    ItemDescription('29', description='', group='VII'),
    ItemDescription('30', description='', group='other'),
    ItemDescription('31', description='', group='other'),
    ItemDescription('32', description='', group='other'),
    ItemDescription('33', description='', group='II'),
    ItemDescription('34', description='', group='other'),
    ItemDescription('35', description='', group='VII'),
    ItemDescription('36', description='', group='other'),
    ItemDescription('37', description='', group='II'),
    ItemDescription('38', description='', group='V'),
    ItemDescription('39', description='', group='III'),
    ItemDescription('40', description='', group='VII'),
    ItemDescription('41', description='', group='other'),
    ItemDescription('42', description='', group='VII'),
    ItemDescription('43', description='', group='II'),
    ItemDescription('44', description='', group='VII'),
    ItemDescription('45', description='', group='III'),
    ItemDescription('46', description='', group='I'),
    ItemDescription('47', description='', group='II'),
    ItemDescription('48', description='', group='V'),
    ItemDescription('49', description='', group='other'),
    ItemDescription('50', description='', group='other'),
    ItemDescription('51', description='', group='I'),
    ItemDescription('52', description='', group='III'),
    ItemDescription('53', description='', group='VII'),
    ItemDescription('54', description='', group='other'),
    ItemDescription('55', description='', group='other'),
    ItemDescription('56', description='', group='VI'),
    ItemDescription('57', description='', group='other'),
    ItemDescription('58', description='', group='VII'),
    ItemDescription('59', description='', group='VI'),
    ItemDescription('60', description='', group='other'),
    ItemDescription('61', description='', group='other'),
    ItemDescription('62', description='', group='IV'),
    ItemDescription('63', description='', group='other'),
    ItemDescription('64', description='', group='V'),
    ItemDescription('65', description='', group='other'),
    ItemDescription('66', description='', group='VII'),
    ItemDescription('67', description='', group='IV'),
    ItemDescription('68', description='', group='II'),
    ItemDescription('69', description='', group='VII'),
    ItemDescription('70', description='', group='IV'),
    ItemDescription('71', description='', group='IV'),
    ItemDescription('72', description='', group='other'),
    ItemDescription('73', description='', group='other'),
    ItemDescription('74', description='', group='V'),
    ItemDescription('75', description='', group='II'),
    ItemDescription('76', description='', group='other'),
    ItemDescription('77', description='', group='other'),
    ItemDescription('78', description='', group='III'),
    ItemDescription('79', description='', group='I'),
    ItemDescription('80', description='', group='other'),
    ItemDescription('81', description='', group='VII'),
    ItemDescription('82', description='', group='I'),
    ItemDescription('83', description='', group='I'),
    ItemDescription('84', description='', group='V'),
    ItemDescription('85', description='', group='VII'),
    ItemDescription('86', description='', group='III'),
    ItemDescription('87', description='', group='II'),
    ItemDescription('88', description='', group='VII'),
    ItemDescription('89', description='', group='other'),
    ItemDescription('90', description='', group='II'),
    ItemDescription('91', description='', group='other'),
    ItemDescription('92', description='', group='I'),
    ItemDescription('93', description='', group='III'),
    ItemDescription('94', description='', group='V'),
    ItemDescription('95', description='', group='VI'),
    ItemDescription('96', description='', group='VII'),
    ItemDescription('97', description='', group='I'),
    ItemDescription('98', description='', group='IV'),
    ItemDescription('99', description='', group='I'),
    ItemDescription('100', description='', group='other'),
]


cbcl_6_18_results_order = [
    'I',
    'II',
    'III',
    'IV',
    'V',
    'VI',
    'VII',
    'VIII',
    'other',
    'a',
    'b',
    'c',
    'total',
]


cbcl_1_5_results_order = [
    'I',
    'II',
    'III',
    'IV',
    'V',
    'VI',
    'VII',
    'other',
    'internal',
    'external',
    'tot prob',
]


def create_cbcl_6_18_test_items(test_id):
    create_test_items(test_id, cbcl_6_18_items)


def create_cbcl_1_5_test_items(test_id):
    create_test_items(test_id, cbcl_1_5_items)


def calculate_cbcl_6_18_test_scores(test):
    raw_scores = calculate_raw_scores(test)
    raw_scores['a'] = raw_scores['I'] + raw_scores['II'] + raw_scores['III']
    raw_scores['b'] = raw_scores['VII'] + raw_scores['VIII']
    raw_scores['c'] = raw_scores['IV'] + raw_scores['V'] + raw_scores['VI'] + raw_scores['other']
    raw_scores['total'] = raw_scores['a'] + raw_scores['b'] + raw_scores['c']
    return convert_to_return_value(raw_scores, cbcl_6_18_results_order, test)


def calculate_cbcl_1_5_test_scores(test):
    raw_scores = calculate_raw_scores(test)
    raw_scores['internal'] = raw_scores['I'] + raw_scores['II'] + raw_scores['III'] + raw_scores['IV']
    raw_scores['external'] = raw_scores['VI'] + raw_scores['VII']
    raw_scores['tot prob'] = raw_scores['V'] + raw_scores['other']
    return convert_to_return_value(raw_scores, cbcl_1_5_results_order, test)
