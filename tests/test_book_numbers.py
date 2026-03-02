import pandas as pd
import pytest
from chapter10_core import Chapter10Core

# Load book numbers for verification
BOOK_NUMBERS = pd.read_csv("data/book_numbers.csv").set_index("metric")

def test_system_cost_2026():
    """Verify the System Cost for 2026 from the book."""
    expected_value = 1.45
    assert BOOK_NUMBERS.loc["System Cost - 2026", "value"] == expected_value

def test_system_cost_2030():
    """Verify the System Cost for 2030 from the book."""
    expected_value = 1.1
    assert BOOK_NUMBERS.loc["System Cost - 2030", "value"] == expected_value

def test_renewable_share_2025():
    """Verify the Renewable Share for 2025 from the book."""
    expected_value = 68.0
    assert BOOK_NUMBERS.loc["Renewable Share - 2025", "value"] == expected_value

def test_renewable_share_2045():
    """Verify the Renewable Share for 2045 from the book."""
    expected_value = 96.0
    assert BOOK_NUMBERS.loc["Renewable Share - 2045", "value"] == expected_value

def test_grid_stability_2045():
    """Verify the Grid Stability for 2045 from the book."""
    expected_value = 98.0
    assert BOOK_NUMBERS.loc["Grid Stability - 2045", "value"] == expected_value

def test_protocol_multiplier_storage():
    """Verify the Protocol Multiplier for Storage from the book."""
    expected_value = 1.5
    assert BOOK_NUMBERS.loc["Protocol Multiplier - Storage", "value"] == expected_value

def test_protocol_multiplier_grid_intelligence():
    """Verify the Protocol Multiplier for Grid Intelligence from the book."""
    expected_value = 2.0
    assert BOOK_NUMBERS.loc["Protocol Multiplier - Grid Intelligence", "value"] == expected_value

def test_protocol_depth_2030():
    """Verify the Protocol Depth for 2030 from the book."""
    expected_value = 8.0
    assert BOOK_NUMBERS.loc["Protocol Depth - 2030", "value"] == expected_value

def test_fragility_2026():
    """Verify the Fragility for 2026 from the book."""
    expected_value = 0.7
    assert BOOK_NUMBERS.loc["Fragility - 2026", "value"] == expected_value

def test_fragility_2030():
    """Verify the Fragility for 2030 from the book."""
    expected_value = 0.2
    assert BOOK_NUMBERS.loc["Fragility - 2030", "value"] == expected_value

def test_tuition_fee_recovery_2040():
    """Verify the Tuition Fee Recovery for 2040 from the book."""
    expected_value = 100.0
    assert BOOK_NUMBERS.loc["Tuition Fee Recovery - 2040", "value"] == expected_value

# Test for core calculations
def test_calculate_sovereign_efficiency():
    core = Chapter10Core()
    # (1.45 - 1.1) / 1.45 = 0.35 / 1.45 = 0.241379...
    assert core.calculate_sovereign_efficiency(1.45, 1.1) == pytest.approx(0.24137931)

def test_calculate_protocol_dividend():
    core = Chapter10Core()
    # 1.45 - 1.1 = 0.35
    assert core.calculate_protocol_dividend(1.45, 1.1) == pytest.approx(0.35)

def test_sovereign_horizon_equation():
    core = Chapter10Core()
    # Sciv(t) = RE_Share(t) * Protocol_Depth(t) * (1 - Fragility)
    # Using book values for 2045: 0.96 * 8 * (1 - 0.2) = 0.96 * 8 * 0.8 = 6.144
    assert core.sovereign_horizon_equation(0.96, 8, 0.2) == pytest.approx(6.144)

def test_success_polynomial():
    core = Chapter10Core()
    # Ssov = asset_factor1 * protocol_multiplier_storage + asset_factor2 * protocol_multiplier_grid_intelligence
    # 0.5 * 1.5 + 0.3 * 2.0 = 0.75 + 0.6 = 1.35
    assert core.success_polynomial([0.5, 0.3], 1.5, 2.0) == pytest.approx(1.35)
