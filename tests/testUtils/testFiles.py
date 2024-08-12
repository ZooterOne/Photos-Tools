import re
import unittest

from parameterized import parameterized # type: ignore

from utils import files


class TestFiles(unittest.TestCase):
    @parameterized.expand([('tests/assets/one.png', '0fc39b203f47463fa651e07e03fd758f5086bafa75b84aca4920dcb13f412702'),
                           ('tests/assets/two.png', '1e916b0d4ac220d218733a789810129c0d7cdbe4803fe6825abbf76f94bdc248'),
                           ('tests/assets/three.png', '8cc93a243607d9f0557c7bd33c190a0eae9abb1a4b99d45cab9a12ac6280ae09'),
                           ('tests/assets/duplicates/four.png', '0fc39b203f47463fa651e07e03fd758f5086bafa75b84aca4920dcb13f412702')])
    def testChecksum(self, filePath: str, checksum: str) -> None:
        self.assertEqual(files.generateChecksum(filePath), checksum)

    def testParseFilesInDirectory(self) -> None:
        fileCount = 0
        def countFile(_):
            nonlocal fileCount
            fileCount += 1
        files.parseFilesInDirectory('./', False, countFile)
        self.assertEqual(fileCount, 5)

    def testParsePngInDirectoryRecursive(self) -> None:
        pngInDirectory = ['./tests/assets/one.png', './tests/assets/two.png', 
                          './tests/assets/three.png', './tests/assets/duplicates/four.png']
        regexFilter = re.compile(r"\.png$")
        def checkFile(filePath: str):
            if regexFilter.search(filePath):
                self.assertIn(filePath, pngInDirectory)
        files.parseFilesInDirectory('./', True, checkFile)
