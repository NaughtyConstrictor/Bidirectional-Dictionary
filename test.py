from bidirectional_dict import BidirDict_V1, BidirDict_V2, BidirDict_V3
import unittest


# BidirDict = BidirDict_V1
# BidirDict = BidirDict_V2
BidirDict = BidirDict_V3


class TestCreation(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.expected = {"a": 1, "b": 2, 1: "a", 2: "b"}
        
    def test1(self):
        result = BidirDict({"a": 1, "b": 2})
        self.assertEqual(result, self.expected)
    
    def test2(self):
        result = BidirDict([("a", 1), ("b", 2)])
        self.assertEqual(result, self.expected)
    
    def test3(self):
        result = BidirDict(a=1, b=2)
        self.assertEqual(result, self.expected)

    def test4(self):
        result = BidirDict({"a": 1}, b=2)
        self.assertEqual(result, self.expected)

    def test5(self):
        result = BidirDict([("a", 1)], b=2)
        self.assertEqual(result, self.expected)

    def test6(self):
        with self.assertRaises(TypeError):
            BidirDict({[1, 2, 3]: "a"})
    
    def test7(self):
        with self.assertRaises(TypeError):
            BidirDict({"a": [1, 2, 3]})

    def test8(self):
        result = BidirDict({"a": 1, "b": 1})
        expected = {"b": 1, 1: "b"}
        self.assertEqual(result, expected)
    
    def test9(self):
        result = BidirDict({"a": 1, 1: "b"})
        expected = {"b": 1, 1: "b"}
        self.assertEqual(result, expected)


class TestDeletion(unittest.TestCase):

    def setUp(self):
        self.bi_dict = BidirDict([("a", 1), ("b", 2)])

    def test__delitem___case_1(self):
        del self.bi_dict["a"]
        self.assertEqual(self.bi_dict, {"b": 2, 2: "b"})
    
    def test__delitem___case_2(self):
        del self.bi_dict[2]
        self.assertEqual(self.bi_dict, {"a": 1, 1: "a"})
    
    def test__delitem___key_does_not_exist(self):
        with self.assertRaises(KeyError):
            del self.bi_dict["unknown key"]
    
    def test_pop_case_1(self):
        expected = self.bi_dict.pop("a")
        result = 1
        self.assertEqual(result, expected)
        expected_dict = {"b": 2, 2: "b"}
        self.assertEqual(self.bi_dict, expected_dict)
    
    def test_pop_case_2(self):
        expected = self.bi_dict.pop(2)
        result = "b"
        self.assertEqual(result, expected)
        expected_dict = {"a": 1, 1: "a"}
        self.assertEqual(self.bi_dict, expected_dict)
    
    def test_pop_key_does_not_exist_1(self):
        with self.assertRaises(KeyError):
            self.bi_dict.pop("unknown key")
        expected = {"a": 1, 1: "a", "b": 2, 2: "b"}
        self.assertEqual(self.bi_dict, expected)
    
    def test_pop_key_does_not_exist_2(self):
        expected = "some default value"
        result = self.bi_dict.pop("unknown key", default=expected)
        self.assertEqual(result, expected)
        expected_dict = {"a": 1, 1: "a", "b": 2, 2: "b"}
        self.assertEqual(self.bi_dict, expected_dict)

    def test_popitem(self):
        result = self.bi_dict.popitem()
        expected = [("b", 2), (2, "b")]
        self.assertListEqual(result, expected)


class TestUpdate(unittest.TestCase):

    def setUp(self):
        self.bi_dict = BidirDict([("a", 1), ("b", 2)])

    def test__setitem__case_1(self):
        self.bi_dict["a"] = 3
        expected = {"b": 2, 2: "b", "a": 3, 3: "a"}
        self.assertEqual(self.bi_dict, expected)
    
    def test__setitem__case_2(self):
        self.bi_dict["a"] = 2
        expected = {"a": 2, 2: "a"}
        self.assertEqual(self.bi_dict, expected)

    def test__setitem__case_3(self):
        self.bi_dict[3] = "c"
        expected = {"a": 1, 1: "a", "b": 2, 2: "b", "c": 3, 3: "c"}
        self.assertEqual(self.bi_dict, expected)

    def test_setdefault_existing_key(self):
        result = self.bi_dict.setdefault("a")
        expected = 1
        self.assertEqual(result, expected)
        expected_dict = {"a": 1, 1: "a", "b": 2, 2: "b"}
        self.assertEqual(self.bi_dict, expected_dict)
    
    def test_setdefault_new_key_case1(self):
        result = self.bi_dict.setdefault("new key")
        self.assertIsNone(result)
        expected_dict = {
            "a": 1, 1: "a", 
            "b": 2, 2: "b", 
            None: "new key",
            "new key": None
            }
        self.assertEqual(self.bi_dict, expected_dict)
    
    def test_setdefault_new_key_case2(self):
        result = self.bi_dict.setdefault("new key", "new value")
        expected = "new value"
        self.assertEqual(result, expected)
        expected_dict = {
            "a": 1, 1: "a", 
            "b": 2, 2: "b", 
            "new value": "new key",
            "new key": "new value"
            }
        self.assertEqual(self.bi_dict, expected_dict)
    
    def test_update_case1(self):
        self.bi_dict.update(a=10, b=20)
        expected = {"a": 10, 10: "a", "b": 20, 20: "b"}
        self.assertEqual(self.bi_dict, expected)

    def test_update_case2(self):
        self.bi_dict.update(a=10, c=30)
        expected = {"a": 10, 10: "a", "b": 2, 2: "b", "c": 30, 30: "c"}
        self.assertEqual(self.bi_dict, expected)

    def test_update_case3(self):
        self.bi_dict.update([("b", -5), ("c", 42)])
        expected = {"a": 1, 1: "a", "b": -5, -5: "b", "c": 42, 42: "c"}
        self.assertEqual(self.bi_dict, expected)

    def test_update_case4(self):
        self.bi_dict.update({"b": -1, -1: "c"})
        expected = {"a": 1, 1: "a", "c": -1, -1: "c"}
        self.assertEqual(self.bi_dict, expected)

    def test_update_case5(self):
        self.bi_dict.update({20: "c"}, a=10, b=20)
        expected = {"a": 10, 10: "a", "b": 20, 20: "b"}
        self.assertEqual(self.bi_dict, expected)
    
    def test_fromkeys(self):
        with self.assertRaises(NotImplementedError):
            BidirDict.fromkeys(["a", "b", "c"])