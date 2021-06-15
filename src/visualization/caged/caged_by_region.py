"""
Visualize CAGED series São Paulo state regions
"""

from typing import Optional

import pandas as pd

CAGED_SERIES_OPTIONS = ['Saldos', 'Estoque', 'Admissões', 'Desligamentos']


def visualize_caged_by_region(
    caged_with_region_path: str,
    region: Optional[str] = None,
    series: str = 'Estoque'
):
    """
    Generate visualizations for CAGED data.

    Args:
        - caged_with_region_path: path to caged CSV data. This data is tracked
        at this repo with the name `annotated_caged.csv`.
        - region: define a given region to plot. If not specified plot
        for all regions.
        - series: value from the series that will
    """

    # Read caged from CSV
    caged_with_region_df = pd.read_csv(caged_with_region_path)

    # Check if the selected series is a valid option
    if series not in CAGED_SERIES_OPTIONS:
        raise KeyError(f'Series {series} is not a valid option! '
                       f'Valid options are {CAGED_SERIES_OPTIONS}')

    # Filter only selected series
    caged_selected_series = caged_with_region_df.filter(regex=(f"{series}."))

    # Filter by region if specified
    if region is not None:
        caged_with_region_df = caged_with_region_df.loc[
            caged_with_region_df['Valor de Display Classificação'] == region
        ].copy()

    caged_selected_series = caged_selected_series.transpose(copy=True)

    plot = caged_selected_series.plot()

    plot.get_figure().savefig('output.png')
