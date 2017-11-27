from pymol import cmd, stored

def std( selection ):
    cmd.hide("all")
    cmd.show("cartoon",selection)
    cmd.center(selection)
    cmd.zoom(selection)
    cmd.spectrum('count','rainbow',selection)

def _print(resi,resn,name):
    print('%s`%s/%s' % (resn ,resi, name))

def passage( selection ):
    myspace = {'_print': _print}
    cmd.iterate(selection, '_print(resi,resn,name)', space=myspace)

cmd.extend("std",std)
cmd.extend("passage",passage)
