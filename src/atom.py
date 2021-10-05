"""
    Atom manipulation module
"""
from re import compile as compile_regex

EXTRACT_ATOMS_REGEX = r"[A-Z][a-z]*"
extract_atoms_regex = compile_regex(EXTRACT_ATOMS_REGEX)


def __reduce_atoms(dic, atom):
    dic[atom] = (dic.get(atom) or 0) + 1
    return dic


def concat_atoms(molecule):
    """ Creates dict by applying the helper function over the molecule"""
    result = {}
    atoms = extract_atoms_regex.findall(molecule)
    for atom in atoms:
        result = __reduce_atoms(result, atom)
    return result
