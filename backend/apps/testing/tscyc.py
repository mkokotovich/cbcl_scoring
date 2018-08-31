from functools import reduce

from rest_framework.exceptions import APIException

from apps.testing.models import Item, Test
from apps.testing.utils import (
    ItemDescription,
    calculate_raw_scores,
    create_test_items,
    convert_to_return_value,
)


tscyc_items = [
    ItemDescription('1', description='', group='ANG'),
    ItemDescription('2', description='', group='DEP'),
    ItemDescription('3', description='', group='RL'),
    ItemDescription('4', description='', group='PTS-I'),
    ItemDescription('5', description='', group='DIS'),
    ItemDescription('6', description='', group='SC'),
    ItemDescription('7', description='', group='ANX'),
    ItemDescription('8', description='', group='PTS-AV'),
    ItemDescription('9', description='', group='ATR'),
    ItemDescription('10', description='', group='PTS-AR'),
    ItemDescription('11', description='', group='PTS-I'),
    ItemDescription('12', description='', group='SC'),
    ItemDescription('13', description='', group='PTS-AV'),
    ItemDescription('14', description='', group='RL'),
    ItemDescription('15', description='', group='ANG'),
    ItemDescription('16', description='', group='SC'),
    ItemDescription('17', description='', group='PTS-AR'),
    ItemDescription('18', description='', group='DEP'),
    ItemDescription('19', description='', group='PTS-I'),
    ItemDescription('20', description='', group='SC'),
    ItemDescription('21', description='', group='ANX'),
    ItemDescription('22', description='', group='RL'),
    ItemDescription('23', description='', group='ANG'),
    ItemDescription('24', description='', group='PTS-I'),
    ItemDescription('25', description='', group='DIS'),
    ItemDescription('26', description='', group='PTS-AR'),
    ItemDescription('27', description='', group='PTS-I'),
    ItemDescription('28', description='', group='DIS'),
    ItemDescription('29', description='', group='PTS-AV'),
    ItemDescription('30', description='', group='ATR'),
    ItemDescription('31', description='', group='ANX'),
    ItemDescription('32', description='', group='ANX'),
    ItemDescription('33', description='', group='DIS'),
    ItemDescription('34', description='', group='ANG'),
    ItemDescription('35', description='', group='SC'),
    ItemDescription('36', description='', group='PTS-I'),
    ItemDescription('37', description='', group='ATR'),
    ItemDescription('38', description='', group='DIS'),
    ItemDescription('39', description='', group='PTS-AV'),
    ItemDescription('40', description='', group='ATR'),
    ItemDescription('41', description='', group='DEP'),
    ItemDescription('42', description='', group='ANX'),
    ItemDescription('43', description='', group='ANG'),
    ItemDescription('44', description='', group='ANX'),
    ItemDescription('45', description='', group='PTS-AR'),
    ItemDescription('46', description='', group='DIS'),
    ItemDescription('47', description='', group='PTS-AR'),
    ItemDescription('48', description='', group='PTS-AR'),
    ItemDescription('49', description='', group='PTS-AV'),
    ItemDescription('50', description='', group='SC'),
    ItemDescription('51', description='', group='ATR'),
    ItemDescription('52', description='', group='DIS'),
    ItemDescription('53', description='', group='RL'),
    ItemDescription('54', description='', group='DEP'),
    ItemDescription('55', description='', group='PTS-AV'),
    ItemDescription('56', description='', group='PTS-AR'),
    ItemDescription('57', description='', group='ANX'),
    ItemDescription('58', description='', group='ANG'),
    ItemDescription('59', description='', group='SC'),
    ItemDescription('60', description='', group='ATR'),
    ItemDescription('61', description='', group='DEP'),
    ItemDescription('62', description='', group='ANG'),
    ItemDescription('63', description='', group='PTS-I'),
    ItemDescription('64', description='', group='ATR'),
    ItemDescription('65', description='', group='SC'),
    ItemDescription('66', description='', group='RL'),
    ItemDescription('67', description='', group='ANX'),
    ItemDescription('68', description='', group='DEP'),
    ItemDescription('69', description='', group='PTS-I'),
    ItemDescription('70', description='', group='PTS-AV'),
    ItemDescription('71', description='', group='DEP'),
    ItemDescription('72', description='', group='PTS-AV'),
    ItemDescription('73', description='', group='RL'),
    ItemDescription('74', description='', group='PTS-AR'),
    ItemDescription('75', description='', group='SC'),
    ItemDescription('76', description='', group='ANX'),
    ItemDescription('77', description='', group='ATR'),
    ItemDescription('78', description='', group='DIS'),
    ItemDescription('79', description='', group='ATR'),
    ItemDescription('80', description='', group='PTS-I'),
    ItemDescription('81', description='', group='PTS-AV'),
    ItemDescription('82', description='', group='PTS-AR'),
    ItemDescription('83', description='', group='RL'),
    ItemDescription('84', description='', group='DEP'),
    ItemDescription('85', description='', group='DIS'),
    ItemDescription('86', description='', group='RL'),
    ItemDescription('87', description='', group='ANG'),
    ItemDescription('88', description='', group='DEP'),
    ItemDescription('89', description='', group='RL'),
    ItemDescription('90', description='', group='ANG'),
]


tscyc_results_order = [
    'RL',
    'ATR',
    'ANX',
    'DEP',
    'ANG',
    'PTS-I',
    'PTS-AV',
    'PTS-AR',
    'PTS-TOT',
    'DIS',
    'SC',
]


def create_tscyc_test_items(test_id):
    create_test_items(test_id, tscyc_items)


def calculate_tscyc_test_scores(test):
    raw_scores = calculate_raw_scores(test)
    raw_scores['PTS-TOT'] = raw_scores['PTS-I'] + raw_scores['PTS-AV'] + raw_scores['PTS-AR']
    return_obj = convert_to_return_value(raw_scores, tscyc_results_order, test)
    return return_obj