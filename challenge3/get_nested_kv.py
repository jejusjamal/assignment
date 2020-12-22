#!/usr/bin/python

import unittest

def get_nested_kv(obj_dict, obj_key):
    tmp_dict = obj_dict
    error_flag = 0
    for key in obj_key.split('/'):
        try:
            tmp_dict = tmp_dict[key]
        except:
            raise ValueError("Wrong key provided, try again:")
            error_flag = 1

    if not error_flag:
        return tmp_dict


class TestGetNestedKey(unittest.TestCase):
    def test_fun_dict_success1(self):
        object = {"a": {"b": {"c": "d"}}}
        actual = get_nested_kv(object, 'a/b/c')
        expected = 'd'
        self.assertEqual(actual, expected)

    def test_fun_dict_success2(self):
        object = {"a": {"b": {"c": "d"}}}
        actual = get_nested_kv(object, 'a/b')
        expected = {"c": "d"}
        self.assertEqual(actual, expected)

    def test_fun_dict_success3(self):
        object = {"a": {"b": {"c": "d"}}}
        actual = get_nested_kv(object, 'a')
        expected = {"b": {"c": "d"}}
        self.assertEqual(actual, expected)

    def test_fun_dict_success4(self):
        object = {"identity-credentials": {"ec2": {"info": {"Code": "Success","LastUpdated": "2020-12-20T17:45:18Z","AccountId": "556428197880"}}}}
        actual = get_nested_kv(object, 'identity-credentials/ec2/info/AccountId')
        expected = "556428197880"
        self.assertEqual(actual, expected)

    def test_fun_dict_success5(self):
        object = {"identity-credentials": {"ec2": {"info": {"Code": "Success","LastUpdated": "2020-12-20T17:45:18Z","AccountId": "556428197880"}}}}
        actual = get_nested_kv(object, 'identity-credentials/ec2/info')
        expected = {"Code": "Success","LastUpdated": "2020-12-20T17:45:18Z","AccountId": "556428197880"}
        self.assertEqual(actual, expected)

    def test_fun_dict_fail1(self):
        object = {"a": {"b": {"c": "d"}}}
        with self.assertRaises(ValueError) as exception_context:
            get_nested_kv(object, 'ab')
        self.assertEqual(
                str(exception_context.exception),
                "Wrong key provided, try again:" )