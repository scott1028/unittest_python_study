# coding:utf-8
# 以下展示如何使用結構化的測試套件 unittest。

import random
import unittest

class tt(unittest.TestCase):

    # 類似測試的建構子
    def setUp(self):
        print 'init'

    # 類似測試的解構子
    def tearDown(self):
        print 'final'

    # 所有測試都必須以 Test.* 命名開始, 之後調用 .main() 會自動執行
    def test_aa(self):
        print 123

        # 可以使用各種斷言來測試！
        # self.assertEqual(self.seq, range(10))
        # self.assertTrue(element in self.seq)
        # self.assertRaises(TypeError, random.shuffle, (1,2,3))
        # self.assertListEqual(......)
        #
        # ...
        #
        # 等很多斷言測試...

#
# 執行測試, 估計會執行 dir() 類似的指令內容估計是查尋有哪些執行 test Function
# 兩種寫法都可以, 效果一樣！
#
if __name__ == '__main__':
    unittest.main()     # 推薦寫法

else:
    suite = unittest.TestLoader().loadTestsFromTestCase(tt)
    unittest.TextTestRunner(verbosity=2).run(suite)