"""
Visualize CAGED series São Paulo state regions
"""

from typing import Optional

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

CAGED_SERIES_OPTIONS = ['Saldos', 'Estoque', 'Admissões', 'Desligamentos']


def caged_heatmap_by_region(
    caged_with_region_path: str,
    output_path: str,
    region: Optional[str] = None,
    series: str = 'Estoque'
):
    """
    Generate a heatmap by region for CAGED data.

    Args:
        - caged_with_region_path: path to caged CSV data. This data is tracked
        at this repo with the name `annotated_caged.csv`.
        - output_path: path where the plot will be saved.
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

    # Drop rows without values for 'Valor de Display Classificação'
    caged_with_region_df.dropna(subset=['Valor de Display Classificação'],
                                inplace=True)

    # Filter by region if specified
    if region is not None:
        caged_with_region_df = caged_with_region_df.loc[
            caged_with_region_df['Valor de Display Classificação'] == region
        ].copy()

    # Aggregate using SUM
    caged_with_region_df = caged_with_region_df.groupby(
        by=['Valor de Display Classificação']).sum()

    # Filter only selected series and 'Valor de Display Classificação'
    caged_selected_series = caged_with_region_df.filter(regex=(f"{series}."))

    # Remove series name from the dataframe
    columns_map = {key: key.replace(series, '')
                   for key in list(caged_selected_series.columns)}
    caged_selected_series = caged_selected_series.rename(columns=columns_map)

    caged_selected_series = caged_selected_series.transpose()

    # Normalize to be able to compare regions
    if region is None:
        caged_selected_series =\
            (caged_selected_series - caged_selected_series.min(axis=0)) / \
            (caged_selected_series.max(axis=0) - caged_selected_series.min(axis=0))

    # Plot an image, add grid and rotate ticks for better fitting
    sns.set(font_scale=5)
    _, ax = plt.subplots(figsize=(50, 32))

    if series == 'Desligamentos':
        caged_selected_series = -1 * caged_selected_series

    ax = sns.heatmap(caged_selected_series, cmap='RdYlGn',
                     linewidths=0.30, annot=False)

    # Set image title and filename
    if region is None:
        ax.set_title(f'{series} normalizado-CAGED')
        ax.get_figure().savefig(f'{output_path}/caged-{series}-heatmap.png')

    else:
        ax.set_title(f'{series}-CAGED@{region}')
        ax.get_figure().savefig(
            f'{output_path}/caged-{region}-{series}-heatmap.png')


def visualize_caged_by_region(
    caged_with_region_path: str,
    output_path: str,
    region: Optional[str] = None,
    series: str = 'Estoque'
):
    """
    Generate visualizations for CAGED data.

    Args:
        - caged_with_region_path: path to caged CSV data. This data is tracked
        at this repo with the name `annotated_caged.csv`.
        - output_path: path where the plot will be saved.
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

    # Drop rows without values for 'Valor de Display Classificação'
    caged_with_region_df.dropna(subset=['Valor de Display Classificação'],
                                inplace=True)

    # Filter by region if specified
    if region is not None:
        caged_with_region_df = caged_with_region_df.loc[
            caged_with_region_df['Valor de Display Classificação'] == region
        ].copy()

    # Aggregate using SUM
    caged_with_region_df = caged_with_region_df.groupby(
        by=['Valor de Display Classificação']).sum()

    # Filter only selected series and 'Valor de Display Classificação'
    caged_selected_series = caged_with_region_df.filter(regex=(f"{series}."))

    # Remove series name from the dataframe
    columns_map = {key: key.replace(series, '')
                   for key in list(caged_selected_series.columns)}
    caged_selected_series = caged_selected_series.rename(columns=columns_map)

    # Traspose to get a timeseries-like
    caged_selected_series = caged_selected_series.transpose(copy=True)

    # Normalize to be able to compare regions
    if region is None:
        caged_selected_series =\
            (caged_selected_series - caged_selected_series.min(axis=0)) / \
            (caged_selected_series.max(axis=0) - caged_selected_series.min(axis=0))

    # Plot an image, add grid and rotate ticks for better fitting
    plot = caged_selected_series.plot(figsize=(32, 16))
    plot.grid(True)
    plot.tick_params(rotation=15)

    plot.legend(title='DRS', bbox_to_anchor=(1.01, 1),
                loc='upper left', fontsize='xx-small')

    # Set image title and filename
    if region is None:
        plot.set_title(f'{series}-CAGED')
        plot.get_figure().savefig(f'{output_path}/caged-{series}.png')
    else:
        plot.set_title(f'{series}-CAGED@{region}')
        plot.get_figure().savefig(f'{output_path}/caged-{region}-{series}.png')
