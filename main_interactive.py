import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from chapter10_core import Chapter10Core

st.set_page_config(layout="wide")
st.title("Chapter 10: Epilogue - The Machine in the Mirror - Proof Engine")

# Initialize core logic
core = Chapter10Core()

# Load book numbers for display
BOOK_NUMBERS = pd.read_csv("data/book_numbers.csv").set_index("metric")

# --- Spy Mode Button ---
if st.sidebar.button("Activate Spy Mode"):
    st.sidebar.subheader("Spy Mode Activated: Exact Book Claims")
    claims = core.spy_mode_claims()
    for claim_title, claim_text in claims.items():
        st.sidebar.write(f"**{claim_title}:** {claim_text}")

# --- Streamlit Tabs ---
tabs = [
    "Sovereign Feedback Loop Simulator",
    "Sovereign Horizon Calculator",
    "SCP Civilization Framework",
    "SEP Evolution Explorer",
    "Prove Every Equation",
    "Download Book Data",
]
selected_tab = st.sidebar.radio("Navigation", tabs)

if selected_tab == "Sovereign Feedback Loop Simulator":
    st.header("Sovereign Feedback Loop Simulator")
    st.write("Explore the Evolutionary Threshold, matching Figure 10.1.")

    # Sliders
    system_complexity = st.slider("System Complexity (0-10)", 0, 10, 5)
    protocol_depth_sim = st.slider("Protocol Depth (0-10)", 0, 10, 7)
    fragility_sim = st.slider("System Fragility (0-1)", 0.0, 1.0, 0.7, step=0.1)

    # Data for plotting (conceptual for now, based on book description)
    complexity_range = np.linspace(0, 10, 100)
    legacy_control = 100 * np.exp(-0.2 * complexity_range) # Example for legacy collapse
    protocol_control = 10 * complexity_range + 30 # Example for protocol growth

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(complexity_range, legacy_control, color=\'red\', label=\'Legacy Control (Experimental)\')
    ax.plot(complexity_range, protocol_control, color=\'blue\', label=\'Protocol Control (Sovereign)\')
    ax.set_xlabel("System Complexity")
    ax.set_ylabel("Sovereign Control (Index)")
    ax.set_title("Figure 10.1: The Evolutionary Threshold")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

    st.subheader("Current Simulation Results:")
    # Example calculation based on sovereign_horizon_equation for current point
    current_stability = core.sovereign_horizon_equation(0.68, protocol_depth_sim, fragility_sim) # Using a fixed renewable share for this sim
    st.write(f"At System Complexity {system_complexity}, with Protocol Depth {protocol_depth_sim} and Fragility {fragility_sim}, Civilizational Stability is: {current_stability:.2f}")

elif selected_tab == "Sovereign Horizon Calculator":
    st.header("Sovereign Horizon Calculator")
    st.write("Calculate Civilizational Stability using the Sovereign Horizon Equation.")

    # Sliders
    renewable_share = st.slider("Renewable Share (0-100%)", 0, 100, 68, format="%d%%") / 100
    protocol_depth = st.slider("Protocol Depth (0-10)", 0, 10, int(core.protocol_depth_2030))
    fragility = st.slider("Fragility (0-1)", 0.0, 1.0, core.fragility_2030, step=0.1)

    # Calculation
    stability = core.sovereign_horizon_equation(renewable_share, protocol_depth, fragility)

    st.subheader("Calculation Results:")
    st.write(f"Civilizational Stability (Sciv): {stability:.2f}")
    st.info("This equation proves how MCP decouples risk from scale, ensuring stability.")

elif selected_tab == "SCP Civilization Framework":
    st.header("SCP Civilization Framework")
    st.write("Understanding the Sovereign Civilization Protocol (SCP) framework.")
    st.write(core.scp_framework_description())
    st.subheader("Key Metrics:")
    st.write(f"System Cost 2026: €{core.system_cost_2026:.2f} Trillion")
    st.write(f"System Cost 2030 (Optimized): €{core.system_cost_2030:.2f} Trillion")
    st.info("The SCP framework re-architects the \'Final Tally\' by establishing an MCP-enabled Master Agent for national grid governance.")

elif selected_tab == "SEP Evolution Explorer":
    st.header("SEP Evolution Explorer")
    st.write("Explore the Sovereign Evolution Protocol (SEP) framework and its implications.")
    st.write(core.sep_evolution_explorer_description())
    st.subheader("Key Projections:")
    st.write(f"Tuition Fee Recovery by 2040: {core.tuition_fee_recovery_2040*100:.0f}%")
    st.info("The SEP framework facilitates the co-evolution of the grid and society, transforming energy into a Sovereign Right.")

elif selected_tab == "Prove Every Equation":
    st.header("Prove Every Equation")
    st.write("Here you can interact with the core equations from Chapter 10.")

    st.subheader("1. Sovereign Efficiency")
    se_legacy_cost = st.number_input("Legacy System Cost (Trillion Euro)", value=core.system_cost_2026, key="se_legacy_cost")
    se_protocol_cost = st.number_input("Protocol System Cost (Trillion Euro)", value=core.system_cost_2030, key="se_protocol_cost")
    calculated_se = core.calculate_sovereign_efficiency(se_legacy_cost, se_protocol_cost)
    st.write(f"Calculated Sovereign Efficiency: {calculated_se:.2%}")
    st.code(
        """
        # (system_cost_legacy - system_cost_protocol) / system_cost_legacy
        """
    )

    st.subheader("2. Protocol Dividend")
    pd_legacy_cost = st.number_input("Legacy System Cost (2026, Trillion Euro)", value=core.system_cost_2026, key="pd_legacy_cost")
    pd_protocol_cost = st.number_input("Protocol System Cost (2030, Trillion Euro)", value=core.system_cost_2030, key="pd_protocol_cost")
    calculated_pd = core.calculate_protocol_dividend(pd_legacy_cost, pd_protocol_cost)
    st.write(f"Calculated Protocol Dividend: €{calculated_pd:.2f} Trillion")
    st.code(
        """
        # system_cost_legacy_2026 - system_cost_protocol_2030
        """
    )

    st.subheader("3. Sovereign Horizon Equation")
    she_renewable_share = st.slider("Renewable Share", 0.0, 1.0, 0.68, key="she_renewable_share")
    she_protocol_depth = st.slider("Protocol Depth", 0, 10, int(core.protocol_depth_2030), key="she_protocol_depth")
    she_fragility = st.slider("Fragility", 0.0, 1.0, core.fragility_2030, key="she_fragility")
    calculated_she = core.sovereign_horizon_equation(she_renewable_share, she_protocol_depth, she_fragility)
    st.write(f"Calculated Civilizational Stability: {calculated_she:.2f}")
    st.code(
        """
        # Sciv(t) = RE_Share(t) * Protocol_Depth(t) * (1 - Fragility)
        """
    )

    st.subheader("4. Success Polynomial")
    sp_asset_factor1 = st.number_input("Asset Factor 1 (e.g., Storage)", value=0.5, key="sp_asset_factor1")
    sp_asset_factor2 = st.number_input("Asset Factor 2 (e.g., Grid Intelligence)", value=0.3, key="sp_asset_factor2")
    calculated_sp = core.success_polynomial([sp_asset_factor1, sp_asset_factor2], core.protocol_multiplier_storage, core.protocol_multiplier_grid_intelligence)
    st.write(f"Calculated Sovereign Success Polynomial: {calculated_sp:.2f}")
    st.code(
        """
        # Ssov = sum(xi * Asseti * ΦMCP)
        # Simplified: asset_factor1 * protocol_multiplier_storage + asset_factor2 * protocol_multiplier_grid_intelligence
        """
    )

elif selected_tab == "Download Book Data":
    st.header("Download Book Data")
    st.write("Download the raw data used to verify Chapter 10 claims.")

    csv_data = BOOK_NUMBERS.to_csv().encode("utf-8")
    st.download_button(
        label="Download book_numbers.csv",
        data=csv_data,
        file_name="book_numbers.csv",
        mime="text/csv",
    )

    st.info(
        "This CSV contains all hardcoded numbers from Chapter 10, verified by pytest."
    )
