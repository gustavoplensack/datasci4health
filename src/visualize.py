"""
Generate visualizations
"""

from git import Repo

from visualization import visualize_caged_by_region

REPO_ROOT = Repo(path='.', search_parent_directories=True).git.rev_parse(
    "--show-toplevel")

PROCESSED_DATA_FOLDER = f'{REPO_ROOT}/data/processed'


def _visualize_ipt():
    """
    Provides visualization to IPT data
    """


def visualize():
    """
    Generate all visualizations.
    """

    caged_with_region_path = f'{PROCESSED_DATA_FOLDER}/annotated_caged.csv'

    # Generate caged visualization per
    visualize_caged_by_region(
        caged_with_region_path=caged_with_region_path,
        series='Estoque'
    )


if __name__ == '__main__':
    visualize()
