from pytest import raises, mark

from src.molecule import flatten, flatten_all, flatten_sub_molecule
from src.exceptions.enclosure_exception import EnclosureException


def test_flatten_sub_molecule_bad_enclosures():
    with raises(EnclosureException) as exception:
        flatten_sub_molecule("Mg(OH}2")

    assert exception.value.message == "Something went wrong -> Parsing error"
    assert exception.value.match.group(0) == "(OH}2"


def describe_flatten():
    @mark.parametrize(
        "molecule, expected",
        [
            ("NaCl", "NaCl"),  # Nothing to change
            ("N2O", "NNO"),  # Simple case
            ("K4[ON(SO3)2]2", "KKKK[ON(SOOO)2]2"),  # Complex case inside enclosures
        ],
    )
    def test_flatten(molecule, expected):
        assert flatten(molecule) == expected


def describe_flatten_sub():
    @mark.parametrize(
        "molecule, expected",
        [
            ("Mg2OH", "Mg2OH"),  # Nothing to change
            ("Mg(OH)", "MgOH"),  # Simple case
            ("FeFe(SOOOO)3", "FeFeSOOOOSOOOOSOOOO"),  # Simple case with multiplier
            ("K4[ON(SO3)2]2",  "K4[ON(SO3)2]2"),  # To show we need to flatten sub-molecule inside enclosures
        ],
    )
    def test_flatten_sub_molecule(molecule, expected):
        assert flatten_sub_molecule(molecule) == expected


def describe_flatten_all():
    @mark.parametrize(
        "molecule, expected",
        [
            ("H2O", "HHO"),  # Simple case
            ("Mg(OH)2", "MgOHOH"),  # With sub molecule
            ("K4[ON(SO3)2]2", "KKKKONSOOOSOOOONSOOOSOOO"),  # Complex case
        ],
    )
    def test_flatten_all(molecule, expected):
        assert flatten_all(molecule) == expected
