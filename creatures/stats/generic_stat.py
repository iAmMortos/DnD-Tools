
from creatures.stats.modifier import ModifierType


class Stat(object):
  def __init__(self, value):
    self._base = value
    self._perma_mods = []
    self._temp_mods = []
    
  @property
  def base(self):
    return self._base
    
  def set_base(self, value):
    self._base = value
    
  @property
  def value(self):
    m = 1
    s = 0
    v = self._base
    for pm in self._perma_mods:
      if ModifierType.ADD == pm.mod_type:
        s += pm.value
      elif ModifierType.MUL == pm.mod_type:
        m *= pm.value
    for tm in self._temp_mods:
      if ModifierType.ADD == tm.mod_type:
        s += tm.value
      elif ModifierType.MUL == tm.mod_type:
        m *= tm.value
    return self._base * m + s
    
  def get_description(self):
    s = 'Value: %s\nBase: %s\nPermanent Modifiers:' % (self.value, self.base)
    for pm in self._perma_mods:
      s += '\n  %s%s: %s' % ('+' if pm.value > 0 else '', pm.value, pm.source)
    s += '\nTemporary Modifiers:'
    for tm in self._temp_mods:
      s += '\n  %s%s: %s' % ('+' if tm.value > 0 else '', tm.value, tm.source)
    return s
    
  def add_perma_mod(self, mod):
    mod.parent = self._perma_mods
    self._perma_mods.append(mod)
    
  def add_temp_mod(self, mod):
    mod.parent = self._temp_mods
    self._temp_mods.append(mod)
