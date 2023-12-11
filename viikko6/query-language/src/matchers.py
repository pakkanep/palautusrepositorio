class All:
    def __init__(self):
        pass
    
    def test(self, player):
        return player


class And:
    def __init__(self, *matchers):
        self._matchers = matchers

    def test(self, player):
        for matcher in self._matchers:
            if not matcher.test(player):
                return False

        return True

class Or:
    def __init__(self, *attr) -> None:
        self._attr = attr
    
    def test(self, player):
        ret_value = False
        for attr_object in self._attr:
            if attr_object.test(player):
                ret_value = True
                break
        return ret_value       

class Not:
    def __init__(self, value):
        self._value = value
    
    def test(self, player):
        return not self._value.test(player)


class PlaysIn:
    def __init__(self, team):
        self._team = team

    def test(self, player):
        return player.team == self._team

class HasFewerThan:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr
    
    def test(self, player):
        player_value = getattr(player, self._attr)
        return player_value <= self._value

class HasAtLeast:
    def __init__(self, value, attr):
        self._value = value
        self._attr = attr

    def test(self, player):
        player_value = getattr(player, self._attr)

        return player_value >= self._value

class QueryBuilder:
    def __init__(self, all_query=All()):
        self._object = all_query

    def oneOf(self, m1, m2):
        return QueryBuilder((Or(m1, m2)))

    def hasAtLeast(self, value, attr):
        return QueryBuilder(
                And(self._object,
                HasAtLeast(value, attr)
                ))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(
                And(self._object,
                HasFewerThan(value, attr)
                ))

    def playsIn(self, team):
        return QueryBuilder(
                And(self._object,
                PlaysIn(team)
                ))

    def build(self):
        return self._object