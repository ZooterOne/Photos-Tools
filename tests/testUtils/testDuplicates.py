import re
import unittest

from utils import duplicates
from utils.progressSpinner import ProgressSpinner


class TestDuplicates(unittest.TestCase):
    def testDirectoryChecksums(self) -> None:
        regexFilter = re.compile(r"\.png$")
        spinner = ProgressSpinner('Processing files ')
        checksums = duplicates.generateDirectoryChecksums('tests', True, regexFilter, spinner)
        expectedChecksums = {'0fc39b203f47463fa651e07e03fd758f5086bafa75b84aca4920dcb13f412702': ['tests/assets/one.png', 'tests/assets/duplicates/four.png'],
                             '1e916b0d4ac220d218733a789810129c0d7cdbe4803fe6825abbf76f94bdc248': ['tests/assets/two.png'],
                             '8cc93a243607d9f0557c7bd33c190a0eae9abb1a4b99d45cab9a12ac6280ae09': ['tests/assets/three.png']}
        spinner.finish()
        self.assertDictEqual(checksums, expectedChecksums)

    def testMergeDirectoryChecksums(self) -> None:
        firstChecksums = {'aa': ['one', 'two'], 'bb': ['one']}
        secondChecksums = {'bb': ['two'], 'cc': ['one']}
        checksums = duplicates.mergeDirectoryChecksums(firstChecksums, secondChecksums)
        expectedChecksums = {'aa': ['one', 'two'], 'bb': ['one', 'two'], 'cc': ['one']}
        self.assertDictEqual(checksums, expectedChecksums)

    def testGenerateDuplicatesFromDirectoryChecksums(self) -> None:
        directoryChecksums = {'aa': ['one', 'two'], 'bb': ['three'], 'cc': ['four', 'four']}
        duplicatesCollection = duplicates.generateDuplicatesFromDirectoryChecksums(directoryChecksums)
        expectedDuplicates = [['one', 'two']]
        self.assertListEqual(duplicatesCollection, expectedDuplicates)

    def testFindDuplicatesInDirectory(self) -> None:
        regexFilter = re.compile(r"\.png$")
        spinner = ProgressSpinner('')
        duplicatePngs = duplicates.findDuplicatesInDirectory('tests', True, regexFilter, spinner)
        spinner.finish()
        expectedDuplicates = [['tests/assets/one.png', 'tests/assets/duplicates/four.png']]
        self.assertListEqual(duplicatePngs, expectedDuplicates)

    def testFindDuplicatesInDirectories(self) -> None:
        regexFilter = re.compile(r"\.png$")
        spinner = ProgressSpinner('')
        self.assertListEqual(duplicates.findDuplicatesInDirectories(False, regexFilter, spinner), [])
        duplicatePngs = duplicates.findDuplicatesInDirectories(False, regexFilter, spinner, 'tests/assets', 'tests/assets/duplicates')
        expectedDuplicates = [['tests/assets/one.png', 'tests/assets/duplicates/four.png']]
        self.assertListEqual(duplicatePngs, expectedDuplicates)
        duplicatePngs = duplicates.findDuplicatesInDirectories(True, regexFilter, spinner, 'tests/assets', 'tests/assets/duplicates')
        spinner.finish()
        self.assertListEqual(duplicatePngs, expectedDuplicates)
