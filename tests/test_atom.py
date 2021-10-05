from pytest import mark

from src.atom import concat_atoms


def describe_reduce_atoms():
    @mark.parametrize(
        "molecule, expected",
        [
            ("OO", {"O": 2}),
            ("HHO", {"H": 2, "O": 1}),
            ("CuCuCuPPOOOOOOOO", {"Cu": 3, "P": 2, "O": 8}),
        ],
    )
    def test_reduce_atoms(molecule, expected):
        assert concat_atoms(molecule) == expected
