
import unittest
# from unittest.mock import patch, mock_open, MagicMock
# import json
# import os
from playerInfo import PlayerInfo

class TestPlayerInfo(unittest.TestCase):
    
    def setUp(cls):
        cls.player_tag = '#999002QU'
        cls.filename = 'testData.json'
        cls.player_info = PlayerInfo(cls.player_tag, cls.filename)

    def testGetTag(self):
        # Test getTag method with existing data
        tag = self.player_info.getTag()
        self.assertEqual(tag, "#999002QU")
    
    def testGetName(self):
        # Test getName method with existing data
        name = self.player_info.getName()
        self.assertEqual(name, "PlotoZypresse")
    
    def testWinRate(self):
        # Test tag method with existing data
        winRate = self.player_info.playerWinRate()
        self.assertEqual(winRate, "All Time winrate: 0.46")

    
if __name__ == '__main__':
    unittest.main()
