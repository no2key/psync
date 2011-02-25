# Copyright 2006 Uberan - All Rights Reserved

class RunTimer:
    def __init__(self, clock, logger):
        self.clock = clock
        self.logger = logger

    def __call__(self, name):
        return RunTime(name, self.clock, self.logger)

class RunTime:
    def __init__(self, name, clock, logger):
        self.name   = name
        self.clock  = clock
        self.logger = logger
        self.before = None
        self.after  = None
        self.result = None

    def __enter__(self):
        self.before = self.clock.unix_fine()
        return self

    def set_result(self, result):
        self.result = result

    def __exit__(self, *args):
        self.after = self.clock.unix_fine()
        self.logger(self)

    @property
    def elapsed(self):
        if self.before is None or self.after is None:
            return None
        else:
            return self.after - self.before
        
