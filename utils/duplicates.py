import re

import utils

from typing import Dict, List


def generateDirectoryChecksums(directoryPath: str, recursive: bool,
                               regexFilter: re.Pattern[str], spinner: utils.ProgressSpinner) -> Dict[str, List[str]]:
    '''Generate the checksum for each file in a given directory.'''
    checksums: dict[str, list[str]] = {}

    def fileCallback(filePath: str) -> None:
        if regexFilter.search(filePath):
            checksum = utils.files.generateChecksum(filePath)
            utils.logger.debug(f'Calculated checksum for {filePath}: {checksum}.')
            if (checksum not in checksums):
                checksums[checksum] = []
            checksums[checksum].append(filePath)
        spinner.update()

    utils.files.parseFilesInDirectory(directoryPath, recursive, fileCallback)
    return checksums


def mergeDirectoryChecksums(mainDirectoryChecksums: Dict[str, List[str]], 
                            secondaryDirectoryChecksums: Dict[str, List[str]]) -> Dict[str, List[str]]:
    '''Merge two directory checksum collections.'''
    secondaryChecksumsWithMainChecksumsWithSharedKeys = {key: (mainDirectoryChecksums[key] + secondaryDirectoryChecksums[key])
                                                         if key in mainDirectoryChecksums.keys()
                                                         else secondaryDirectoryChecksums[key]
                                                         for key in secondaryDirectoryChecksums.keys()}
    return mainDirectoryChecksums | secondaryChecksumsWithMainChecksumsWithSharedKeys


def generateDuplicatesFromDirectoryChecksums(directoryChecksums: Dict[str, List[str]]) -> List[List[str]]:
    '''Generate duplicate files data from directory checksum data.'''
    duplicateFiles: list[list[str]] = []
    
    def generateDuplicates(values: List[str]) -> None:
         if len(values) > 1:
            uniqueValues = []
            for value in values:
                if value not in uniqueValues:
                    uniqueValues.append(value)
            if len(uniqueValues) > 1:
                utils.logger.info(f'Duplicates found: {uniqueValues}.')
                nonlocal duplicateFiles
                duplicateFiles.append(uniqueValues)
    
    for values in directoryChecksums.values():
        generateDuplicates(values)
    return duplicateFiles


def findDuplicatesInDirectory(directoryPath: str, recursive: bool,
                              regexFilter: re.Pattern[str], spinner: utils.ProgressSpinner) -> List[List[str]]:
    '''Find duplicate files in a given directory.'''
    spinner.message = 'Processing files '
    checksums = generateDirectoryChecksums(directoryPath, recursive, regexFilter, spinner)
    return generateDuplicatesFromDirectoryChecksums(checksums)


def findDuplicatesInDirectories(recursive: bool, regexFilter: re.Pattern[str],
                               spinner: utils.ProgressSpinner, *directoryPaths: str) -> List[List[str]]:
    '''Find duplicate files in multiple given directories.'''
    directoryCount = len(directoryPaths)
    if directoryCount == 0:
        return []
    spinner.message = 'Processing files '
    directoryIter = iter(directoryPaths)
    mergedChecksums = generateDirectoryChecksums(next(directoryIter), recursive, regexFilter, spinner)
    for directoryPath in directoryIter:
        additionalChecksums = generateDirectoryChecksums(directoryPath, recursive, regexFilter, spinner)
        mergedChecksums = mergeDirectoryChecksums(mergedChecksums, additionalChecksums)
    return generateDuplicatesFromDirectoryChecksums(mergedChecksums)
