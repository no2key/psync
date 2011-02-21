# Copyright 2006 Uberan - All Rights Reserved

import fnmatch
import re

from util import Record

class PathFilter(Record("patterns_to_ignore", "names_to_ignore", "paths_to_ignore")):
    def __new__(cls, globs_to_ignore, names_to_ignore):
        names_to_ignore = frozenset(names_to_ignore)
        patterns_to_ignore = compile_globs(globs_to_ignore)
        return cls.new(patterns_to_ignore, names_to_ignore, set())

    def ignore_path(self, path):
        if path in self.paths_to_ignore:
            return True
        elif (matches_any_name(path, self.names_to_ignore) or
              matches_any_pattern(path, self.patterns_to_ignore)):
            self.paths_to_ignore.add(path)
            return True
        else:
            return False

def compile_globs(globs):
    return [re.compile(fnmatch.translate(glob), re.IGNORECASE)
            for glob in globs]

def matches_any_name(path, names):
    return frozenset(path.split("/")) & names

def matches_any_pattern(path, patterns):
    return any(pattern.match(path) for pattern in patterns)