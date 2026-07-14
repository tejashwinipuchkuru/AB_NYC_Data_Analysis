from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()
    cleaned.columns = [column.strip().lower() for column in cleaned.columns]
    cleaned = cleaned.drop_duplicates().reset_index(drop=True)

    if "price" in cleaned.columns:
        cleaned["price"] = (
            cleaned["price"]
            .astype(str)
            .str.replace("$", "", regex=False)
            .str.replace(",", "", regex=False)
        )
        cleaned["price"] = pd.to_numeric(cleaned["price"], errors="coerce")
        cleaned.loc[cleaned["price"] < 0, "price"] = np.nan
        if cleaned["price"].notna().any():
            upper = cleaned["price"].quantile(0.99)
            cleaned = cleaned[cleaned["price"] <= upper]

    for column in (
        "minimum_nights",
        "number_of_reviews",
        "reviews_per_month",
        "calculated_host_listings_count",
        "availability_365",
    ):
        if column in cleaned.columns:
            cleaned[column] = pd.to_numeric(cleaned[column], errors="coerce")

    if "reviews_per_month" in cleaned.columns:
        cleaned["reviews_per_month"] = cleaned["reviews_per_month"].fillna(0)

    for text_col, default in (("name", "Unknown listing"), ("host_name", "Unknown host")):
        if text_col in cleaned.columns:
            cleaned[text_col] = cleaned[text_col].fillna(default)

    required_columns = [col for col in ("latitude", "longitude", "room_type") if col in cleaned.columns]
    if required_columns:
        cleaned = cleaned.dropna(subset=required_columns)

    return cleaned.reset_index(drop=True)


def build_summary(df: pd.DataFrame) -> pd.DataFrame:
    summary_rows: list[dict[str, object]] = [
        {"metric": "rows", "value": int(df.shape[0])},
        {"metric": "columns", "value": int(df.shape[1])},
    ]

    if "price" in df.columns and df["price"].notna().any():
        summary_rows.extend(
            [
                {"metric": "avg_price", "value": float(df["price"].mean())},
                {"metric": "median_price", "value": float(df["price"].median())},
                {"metric": "max_price", "value": float(df["price"].max())},
            ]
        )

    if "room_type" in df.columns:
        room_mix = df["room_type"].value_counts().sort_index()
        for room_type, count in room_mix.items():
            summary_rows.append({"metric": f"room_type_{room_type}", "value": int(count)})

    return pd.DataFrame(summary_rows)


def create_visualizations(df: pd.DataFrame, output_dir: Path) -> None:
    sns.set_theme(style="whitegrid")

    if "price" in df.columns and df["price"].notna().any():
        plt.figure(figsize=(10, 6))
        sns.histplot(df["price"], bins=40, kde=True, color="steelblue")
        plt.title("Price Distribution")
        plt.xlabel("Price")
        plt.ylabel("Listing Count")
        plt.tight_layout()
        plt.savefig(output_dir / "price_distribution.png")
        plt.close()

    if "room_type" in df.columns:
        plt.figure(figsize=(10, 6))
        order = df["room_type"].value_counts().index
        sns.countplot(data=df, x="room_type", order=order, color="teal")
        plt.title("Room Type Distribution")
        plt.xlabel("Room Type")
        plt.ylabel("Listing Count")
        plt.xticks(rotation=20)
        plt.tight_layout()
        plt.savefig(output_dir / "room_type_distribution.png")
        plt.close()

    if {"neighbourhood_group", "price"}.issubset(df.columns):
        neighbourhood_avg = (
            df.groupby("neighbourhood_group", as_index=False)["price"].mean().sort_values("price", ascending=False)
        )
        plt.figure(figsize=(10, 6))
        sns.barplot(data=neighbourhood_avg, x="neighbourhood_group", y="price", color="coral")
        plt.title("Average Price by Neighbourhood Group")
        plt.xlabel("Neighbourhood Group")
        plt.ylabel("Average Price")
        plt.xticks(rotation=20)
        plt.tight_layout()
        plt.savefig(output_dir / "average_price_by_neighbourhood_group.png")
        plt.close()

    if {"availability_365", "price"}.issubset(df.columns):
        plot_df = df[["availability_365", "price"]].dropna()
        if not plot_df.empty:
            plt.figure(figsize=(10, 6))
            sns.scatterplot(
                data=plot_df.sample(min(len(plot_df), 3000), random_state=42),
                x="availability_365",
                y="price",
                alpha=0.5,
                s=25,
            )
            plt.title("Availability vs Price")
            plt.xlabel("Availability (365 days)")
            plt.ylabel("Price")
            plt.tight_layout()
            plt.savefig(output_dir / "availability_vs_price.png")
            plt.close()


def run_analysis(input_csv: Path, output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    raw_df = pd.read_csv(input_csv)
    cleaned_df = clean_data(raw_df)
    summary_df = build_summary(cleaned_df)

    cleaned_df.to_csv(output_dir / "AB_NYC_2024_cleaned.csv", index=False)
    summary_df.to_csv(output_dir / "eda_summary.csv", index=False)
    create_visualizations(cleaned_df, output_dir)

    print(f"Analysis complete. Files written to: {output_dir}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="AB_NYC_2024 cleaning, EDA, and visualization workflow")
    parser.add_argument("--input", required=True, type=Path, help="Path to AB_NYC_2024 CSV file")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("analysis_outputs"),
        help="Directory where cleaned data, summary, and plots will be saved",
    )
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    run_analysis(args.input, args.output)
