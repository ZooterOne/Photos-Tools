from logging import getLogger

from .logging import setupBasicLogging, setupWithConfigFile
from .files import generateChecksum, parseFilesInDirectory
from .progressSpinner import ProgressSpinner
from .duplicates import findDuplicatesInDirectory, findDuplicatesInDirectories


all = (setupBasicLogging, setupWithConfigFile,
       generateChecksum, parseFilesInDirectory,
       ProgressSpinner,
       findDuplicatesInDirectory, findDuplicatesInDirectories)


logger = getLogger(__name__)
