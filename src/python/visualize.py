"""
Generate visualizations
"""

from git import Repo

from visualization import caged_heatmap_by_region, visualize_caged_by_region

REPO_ROOT = Repo(path='.', search_parent_directories=True).git.rev_parse(
    "--show-toplevel")

PROCESSED_DATA_FOLDER = f'{REPO_ROOT}/data/processed'
GENERATED_IMAGES_FOLDER = f'{REPO_ROOT}/assets/img'


def visualize():
    """
    Generate all visualizations.
    """

    caged_with_region_path = f'{PROCESSED_DATA_FOLDER}/annotated_caged.csv'

    # Generate caged visualization per
    visualize_caged_by_region(
        caged_with_region_path=caged_with_region_path,
        output_path=GENERATED_IMAGES_FOLDER,
        # region='DRS XIII - Ribeirão Preto',
        series='Estoque'
    )

    # Generate caged visualization per
    caged_heatmap_by_region(
        caged_with_region_path=caged_with_region_path,
        output_path=GENERATED_IMAGES_FOLDER,
        # region='DRS XIII - Ribeirão Preto',
        series='Desligamentos'
    )


if __name__ == '__main__':
    visualize()
