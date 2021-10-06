"""
    Molecule manipulation module
"""
import logging
from re import compile as compile_regex
from src.utils import replicate_pattern
from src.exceptions.enclosure_exception import EnclosureException

MOLECULE_REGEX = r"([A-Z][a-z]*)(\d*)"
SUB_FLATTEN_MOLECULE_REGEX = r"([([{])([a-zA-Z]*)([\])}])(\d*)"

enclosures = {"{": "}", "[": "]", "(": ")"}

molecule_regex = compile_regex(MOLECULE_REGEX)
sub_flatten_molecule_regex = compile_regex(SUB_FLATTEN_MOLECULE_REGEX)


def __exception_and_replicate_flatten_molecule(match):
    """
    Exception assertion and concat pattern on flatter molecule
    :param match:
    :return: replicated pattern
    """
    begin_enclosure, flatten_molecule, end_enclosure, multiplier = match.groups()

    if enclosures[begin_enclosure] != end_enclosure:
        logging.error("Something went wrong -> Parsing error ")
        raise EnclosureException("Something went wrong -> Parsing error", match)

    logging.info("Applying replicate_pattern")
    return replicate_pattern(flatten_molecule, multiplier)


def __molecule_match():
    """
    Lambda function to concat the pattern to the total provided.
    :return: lambda
    """
    return lambda match: replicate_pattern(match[1], match[2])


def flatten(molecule):
    """
    Replace the atoms and associated number by each times they exist
    ex: Fe2O3 => FeFeOOO
    """
    flatten_molecule = molecule_regex.sub(__molecule_match(), molecule)

    return flatten_molecule


def flatten_sub_molecule(flatten_molecule):
    """
    Same as flatten but works on sub-molecules (elements within enclosures).
    ex: K4(SO3) => K4(SOOO)
    """

    last_molecule = ""
    new_molecule = flatten_molecule

    while last_molecule != new_molecule:
        last_molecule = new_molecule
        new_molecule = sub_flatten_molecule_regex.sub(
            __exception_and_replicate_flatten_molecule,
            last_molecule,
        )

    return new_molecule


def flatten_all(molecule):
    """
    Flatten the whole molecule.
    """

    return flatten_sub_molecule(flatten(molecule))
