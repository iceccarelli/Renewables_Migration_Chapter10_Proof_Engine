import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import os
import sys

# Add the parent directory to the system path to import chapter10_core
script_dir = os.path.dirname(__file__)
sys.path.insert(0, os.path.abspath(os.path.join(script_dir, "..")))
from chapter10_core import Chapter10Core

# Initialize core logic
core = Chapter10Core()

def plot_evolutionary_threshold():
    """
    Reproduces Figure 10.1: The Evolutionary Threshold.
    """
    complexity_range = np.linspace(0, 10, 100)
    legacy_control = 100 * np.exp(-0.2 * complexity_range)  # Example for legacy collapse
    protocol_control = 10 * complexity_range + 30  # Example for protocol growth

    plt.figure(figsize=(10, 6))
    sns.lineplot(x=complexity_range, y=legacy_control, color='red', label='Legacy Control (Experimental)')
    sns.lineplot(x=complexity_range, y=protocol_control, color='blue', label='Protocol Control (Sovereign)')
    plt.xlabel("System Complexity")
    plt.ylabel("Sovereign Control (Index)")
    plt.title("Figure 10.1: The Evolutionary Threshold")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.ylim(0, 100)
    plt.xlim(0, 10)
    plt.legend()
    plt.savefig("../plots/evolutionary_threshold.png")
    plt.close()
    print("Generated evolutionary_threshold.png")

def plot_sovereign_horizon():
    """
    Reproduces Figure 10.2: The Sovereign Horizon.
    This plot shows how MCP decouples renewable growth from system risk.
    """
    years = np.arange(2000, 2046)
    renewable_share_data = {
        2000: 0.1,
        2005: 0.15,
        2010: 0.172, # From Appendix A.1
        2015: 0.25,
        2018: 0.392, # From Appendix A.1
        2020: 0.45,
        2023: 0.591, # From Appendix A.1
        2025: 0.638, # From Appendix A.1
        2026: 0.68, # From book_numbers.csv
        2030: 0.827, # From Appendix A.1
        2035: 0.90,
        2040: 0.94,
        2045: 0.96, # From book_numbers.csv
    }

    # Interpolate renewable share for all years
    renewable_share_interp = pd.Series(renewable_share_data).reindex(years).interpolate(method='linear')

    # Legacy Stability (Risk) - example: decreases as renewables increase without MCP
    legacy_stability = 100 - (renewable_share_interp * 100 * 0.8) # Example inverse relationship
    legacy_stability[legacy_stability < 0] = 0

    # Sovereign Stability (MCP) - example: increases with protocol depth
    # Sciv(t) = RE_Share(t) * Protocol_Depth(t) * (1 - Fragility)
    protocol_depth_interp = pd.Series({
        2000: 0,
        2010: 0,
        2020: 0.1, # Start of MCP influence
        2026: core.protocol_depth_2030 * 0.5, # Example for 2026
        2030: core.protocol_depth_2030, # From book_numbers.csv
        2045: 9, # Higher protocol depth by 2045
    }).reindex(years).interpolate(method='linear')

    fragility_interp = pd.Series({
        2000: 0.9,
        2026: core.fragility_2026, # From book_numbers.csv
        2030: core.fragility_2030, # From book_numbers.csv
        2045: 0.1, # Reduced fragility by 2045
    }).reindex(years).interpolate(method='linear')

    sovereign_stability = [core.sovereign_horizon_equation(rs, pd, fr) * 10 for rs, pd, fr in zip(renewable_share_interp, protocol_depth_interp, fragility_interp)] # Scale for plotting
    sovereign_stability = np.array(sovereign_stability)
    sovereign_stability[sovereign_stability > 100] = 100 # Cap at 100

    plt.figure(figsize=(12, 7))
    sns.lineplot(x=years, y=renewable_share_interp * 100, label='Renewables Share', color='green')
    sns.lineplot(x=years, y=legacy_stability, label='Legacy Stability (Risk)', color='red', linestyle='--')
    sns.lineplot(x=years, y=sovereign_stability, label='Sovereign Stability (MCP)', color='blue')
    plt.xlabel("Year")
    plt.ylabel("Normalized Index (2015=100)")
    plt.title("Figure 10.2: The Sovereign Horizon: Decoupling Renewables from Risk (to 2045)")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.ylim(0, 100)
    plt.legend()
    plt.savefig("../plots/sovereign_horizon.png")
    plt.close()
    print("Generated sovereign_horizon.png")

def plot_sovereign_success_projection():
    """
    Generates a conceptual plot for Sovereign Success Projection.
    This would be based on the Success Polynomial.
    """
    x_values = np.linspace(0, 10, 100) # Represents a factor like 'MCP Integration Level'
    # Assuming asset factors change with MCP integration
    asset_factor1_dynamic = 0.1 + 0.05 * x_values # Example: Storage asset factor increases
    asset_factor2_dynamic = 0.05 + 0.08 * x_values # Example: Grid Intelligence asset factor increases

    ssov_values = [
        core.success_polynomial([af1, af2], core.protocol_multiplier_storage, core.protocol_multiplier_grid_intelligence)
        for af1, af2 in zip(asset_factor1_dynamic, asset_factor2_dynamic)
    ]

    plt.figure(figsize=(10, 6))
    sns.lineplot(x=x_values, y=ssov_values)
    plt.xlabel("MCP Integration Level")
    plt.ylabel("Sovereign Success Index")
    plt.title("Sovereign Success Projection (Conceptual)")
    plt.grid(True, linestyle="--", alpha=0.7)
    plt.savefig("../plots/sovereign_success_projection.png")
    plt.close()
    print("Generated sovereign_success_projection.png")

if __name__ == "__main__":
    # Ensure the plots directory exists
    os.makedirs("../plots", exist_ok=True)

    plot_evolutionary_threshold()
    plot_sovereign_horizon()
    plot_sovereign_success_projection()
