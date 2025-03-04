from tackle.main import tackle
import pytest

BASE_OVERRIDES = {
    "contract_name": "Foo Contract",
    "project_slug": "output",
    "license": "",
    "ci_enable": True,
    "warning": True,
}

CONTRACT_STANDARDS = [
    # ("contract"),
    # ("irc2"),
    ("irc3"),
    # ("irc31"),
]


@pytest.mark.parametrize("contract_standard", CONTRACT_STANDARDS)
def test_defaults(
        change_base_dir,
        assert_paths,
        change_dir,
        test_pytest_output,
        cleanup_output,
        contract_standard,
        compile_contract,
):
    """
    Setting no_input (ie choose the default value, true for the `confirm` hook), this
    test runs through all the contract standards to generate the code.
    """
    overrides = {
        "contract_standard": contract_standard,
    }
    overrides.update(BASE_OVERRIDES)

    tackle(
        no_input=True,
        override=overrides,
    )

    assert_paths(
        [
            "README.md",
            "requirements-dev.txt",
        ],
        "output",
    )


CONTRACT_FEATURES = [
    ("irc2", {
        "is_token": True,
        "features": {
            "mintable": True,
            "burnable": True,
            "pausable": True,
            "permit": True,
            "votes": True,
            "flash_minting": True,
            "snapshots": True,
        }
    }),
    ("irc3", {
        "is_token": True,
        "features": {
            "mintable": True,
            "auto_increment_ids": True,
            "burnable": True,
            "pausable": True,
            "votes": True,
            "enumerable": True,
            "uri_storage": True,
        }
    }),
    ("irc31", {
        "is_token": True,
        "features": {
            "mintable": True,
            "auto_increment_ids": True,
            "burnable": True,
            "pausable": True,
            "votes": True,
            "enumerable": True,
            "uri_storage": True,
        }
    }),
    ("contract", {
        "is_token": True,
        "features": {
            "pausable": True,
        }
    }),
]


@pytest.mark.parametrize("token_standard,options", CONTRACT_FEATURES)
def test_features(
        change_base_dir,
        assert_paths,
        change_dir,
        test_pytest_output,
        cleanup_output,
        token_standard,
        options,
        # compile_contract,
):
    overrides = {
        "contract_standard": token_standard,
        **options,
    }
    overrides.update(BASE_OVERRIDES)

    tackle(override=overrides)

    assert_paths(
        [
            "README.md",
            "requirements-dev.txt",
        ],
        "output",
    )
