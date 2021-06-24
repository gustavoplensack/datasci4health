"""
Generate datasets starting from processed datasets.
"""

from git import Repo

from data import annotate_caged

REPO_ROOT = Repo(path='.', search_parent_directories=True).git.rev_parse(
    "--show-toplevel")

PROCESSED_DATA_FOLDER = f'{REPO_ROOT}/data/processed'
INTERIM_DATA_FOLDER = f'{REPO_ROOT}/data/interim'


def generate():
    """
    Generate all visualizations.
    """

    processed_caged_path =\
        f'{INTERIM_DATA_FOLDER}/caged_2020_processed_tabela_81.csv'
    sp_drs_map_path =\
        f'{PROCESSED_DATA_FOLDER}/sp_drs_map.csv'
    annotated_caged_path = f'{PROCESSED_DATA_FOLDER}/annotated_caged.csv'

    annotate_caged(processed_caged_path=processed_caged_path,
                   sp_drs_map_path=sp_drs_map_path,
                   annotated_caged_path=annotated_caged_path)


if __name__ == '__main__':
    generate()
