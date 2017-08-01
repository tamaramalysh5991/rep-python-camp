def _relatives(self, level=0):
    """ method _relatives return instance of Family with level up
    Args:
         level(int): lineage level for how much steps need return
         Local Attributes:
        _relatives.rec(function): is local recursion function for get
                                    instances from parents and save it.
                rec.linage(instance): instance of Family to get item from
                                        mother or father line.
                rec.level_father(int): variable for raise stop iteration
                                        when level is done.
                rec.level_mother(int): variable for raise stop iteration
                                        when level is done.
            Return:
                 relatives(list) contained instance of Family
    """

    def rec(linage):
        if not hasattr(rec, '_level_father'):
            rec._level_father = 0
            rec._level_mother = 0
        else:
            rec._level_father += 1
            rec._level_mother += 1

        if level == 0:
            yield self.root_family

        if self.root_family is not linage:
            yield linage

        if linage.father is not None:
            if level > rec._level_father:
                yield from rec(linage.father.root_family)
                rec._level_mother = 0
        if linage.mother is not None:
            if level > rec._level_mother:
                yield from rec(linage.mother.root_family)

    return [x
            for x in rec(self.root_family)
            if x.father is not None]