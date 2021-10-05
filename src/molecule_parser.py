import logging


from src.molecule import flatten_all
from src.atom import concat_atoms


def parse_molecule(molecule):
    """
    Parses the molecule equation and returns a dictionary counting the number of atoms of each element.
    :param molecule: String
    :return: Dictionary
    """
    logging.info("Flattening the molecule")
    flatten_molecule = flatten_all(molecule)
    logging.info("Parsing the flatted molecule")
    atoms = concat_atoms(flatten_molecule)
    logging.info(atoms)
    return atoms
