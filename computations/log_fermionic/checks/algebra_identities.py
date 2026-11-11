"""Independent finite-matrix Clifford, gamma-placement and epsilon identities."""
from src.algebra import prepare_outputs


def main():
    prepare_outputs()
    import verify_log_two_fermi_canonical as identities
    identities.exact_clifford()
    identities.exact_epsilon()


if __name__ == "__main__":
    main()
