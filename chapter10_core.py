import pandas as pd
import numpy as np

# Load book numbers for verification and calculations
BOOK_NUMBERS = pd.read_csv('data/book_numbers.csv').set_index('metric')

class Chapter10Core:
    """Core calculations and frameworks for Chapter 10: Epilogue - The Machine in the Mirror."""

    def __init__(self):
        # Initialize key metrics from book_numbers.csv
        self.system_cost_2026 = BOOK_NUMBERS.loc['System Cost - 2026', 'value']
        self.system_cost_2030 = BOOK_NUMBERS.loc['System Cost - 2030', 'value']
        self.renewable_share_2045 = BOOK_NUMBERS.loc['Renewable Share - 2045', 'value'] / 100
        self.grid_stability_2045 = BOOK_NUMBERS.loc['Grid Stability - 2045', 'value'] / 100
        self.protocol_multiplier_storage = BOOK_NUMBERS.loc['Protocol Multiplier - Storage', 'value']
        self.protocol_multiplier_grid_intelligence = BOOK_NUMBERS.loc['Protocol Multiplier - Grid Intelligence', 'value']
        self.protocol_depth_2030 = BOOK_NUMBERS.loc['Protocol Depth - 2030', 'value']
        self.fragility_2026 = BOOK_NUMBERS.loc['Fragility - 2026', 'value']
        self.fragility_2030 = BOOK_NUMBERS.loc['Fragility - 2030', 'value']
        self.tuition_fee_recovery_2040 = BOOK_NUMBERS.loc['Tuition Fee Recovery - 2040', 'value'] / 100

    def calculate_sovereign_efficiency(self, system_cost_legacy, system_cost_protocol):
        """
        Calculates the sovereign efficiency based on the reduction in system cost.
        This proves the book's claim of cost optimization through MCP.
        Insights:
        - Engineers: Highlights the tangible cost benefits of MCP integration.
        - Technicians: Shows the economic value of efficient protocol implementation.
        - Politicians: Demonstrates fiscal responsibility and economic gains from policy.
        """
        if system_cost_legacy == 0: # Avoid division by zero
            return 0
        return (system_cost_legacy - system_cost_protocol) / system_cost_legacy

    def calculate_protocol_dividend(self, system_cost_legacy_2026, system_cost_protocol_2030):
        """
        Calculates the Protocol Dividend, representing the savings achieved by MCP.
        This proves the book's assertion of MCP's financial benefits.
        Insights:
        - Engineers: Quantifies the economic advantage of MCP-driven design.
        - Technicians: Shows the direct financial impact of optimized operations.
        - Politicians: Provides a clear metric for return on investment in protocol adoption.
        """
        return system_cost_legacy_2026 - system_cost_protocol_2030

    def sovereign_horizon_equation(self, renewable_share, protocol_depth, fragility):
        """
        Calculates Civilizational Stability (Sciv) as per the Sovereign Horizon Equation.
        Sciv(t) = RE_Share(t) * Protocol_Depth(t) * (1 - Fragility)
        This proves the book's claim that MCP decouples risk from scale, ensuring stability.
        Insights:
        - Engineers: Emphasizes the critical role of protocol depth in maintaining grid stability with high renewables.
        - Technicians: Shows how MCP integration directly contributes to system robustness.
        - Politicians: Provides a framework for policy decisions that balance renewable targets with national security.
        """
        return renewable_share * protocol_depth * (1 - fragility)

    def success_polynomial(self, asset_factors, protocol_multiplier_storage, protocol_multiplier_grid_intelligence):
        """
        Calculates the Sovereign Success Polynomial (Ssov).
        Ssov = sum(xi * Asseti * ΦMCP)
        This proves the book's assertion that MCP acts as a master variable, amplifying asset value.
        Insights:
        - Engineers: Highlights how MCP enhances the value and performance of physical assets.
        - Technicians: Demonstrates the exponential impact of intelligent integration on system output.
        - Politicians: Shows how strategic investment in protocols maximizes national asset utility and economic growth.
        """
        # Assuming asset_factors is a list or array of (xi * Asseti) values
        # For simplicity, let's assume two main asset types: Storage and Grid Intelligence
        # The book mentions 'Storage' and 'Grid Intelligence' as having exponential multipliers.
        total_ssov = 0
        if len(asset_factors) >= 1:
            total_ssov += asset_factors[0] * protocol_multiplier_storage # Example for Storage
        if len(asset_factors) >= 2:
            total_ssov += asset_factors[1] * protocol_multiplier_grid_intelligence # Example for Grid Intelligence
        # Extend for more asset factors if needed from the book
        return total_ssov

    def scp_framework_description(self):
        """
        Provides a description of the Sovereign Civilization Protocol (SCP) framework.
        This proves the book's vision of MCP as the brain of the new civilization.
        Insights:
        - Engineers: Explains the architectural shift towards autonomous, MCP-governed systems.
        - Technicians: Details the operational paradigm of a protocol-driven grid and society.
        - Politicians: Outlines the strategic implications of adopting SCP for national sovereignty and global leadership.
        """
        return (
            "The Sovereign Civilization Protocol (SCP) framework re-architects the 'Final Tally' by establishing an MCP-enabled Master Agent for national grid governance, promoting autonomous global protocol leadership, and forging a protocol-driven social contract where citizens are sovereign nodes. This ensures that Civilizational Sovereignty is defined by the Protocol commanded, not just energy produced."
        )

    def sep_evolution_explorer_description(self):
        """
        Provides a description of the Sovereign Evolution Protocol (SEP) framework.
        This proves the book's concept of co-evolution and the migration of the sun.
        Insights:
        - Engineers: Illustrates the co-evolutionary design principles for grid and society.
        - Technicians: Describes how MCP facilitates the transition from legacy systems to a high-performance, autonomous future.
        - Politicians: Highlights the long-term vision of economic recovery through global protocol licensing and energy as a sovereign right.
        """
        return (
            "The Sovereign Evolution Protocol (SEP) framework facilitates the co-evolution of the grid and society, replacing old industrial jobs with high-value 'Protocol Engineering' roles. It aims for full recovery of the €1.45 trillion 'Tuition Fee' by 2040 through global licensing of the Sovereign Protocol, transforming energy from a cost into a Sovereign Right guaranteed by the autonomous protocol."
        )

    def spy_mode_claims(self):
        """
        Returns key claims from Chapter 10 for 'Spy Mode'.
        """
        claims = {
            "Machine in the Mirror": "The book describes the 'Machine in the Mirror' as a hardware-centric reflection of a civilization in transition, which MCP transforms into a software-centric solution of Autonomous Sovereignty.",
            "Sovereign First Mover": "Germany's role as the 'Sovereign First Mover' is highlighted, emphasizing that its true legacy is the Sovereign Protocol forged in the 2026 crisis, not just the renewable share.",
            "MCP's Role in Decoupling Risk/Scale": "The Sovereign Horizon Equation explicitly shows how MCP's Protocol Depth decouples renewable growth from system risk, allowing for high renewable penetration with high stability."
        }
        return claims

if __name__ == '__main__':
    core = Chapter10Core()
    print("Chapter 10 Core Initialized.")

    # Example calculations
    sovereign_efficiency = core.calculate_sovereign_efficiency(core.system_cost_2026, core.system_cost_2030)
    print(f"Sovereign Efficiency (Cost Reduction): {sovereign_efficiency:.2%}")

    protocol_dividend = core.calculate_protocol_dividend(core.system_cost_2026, core.system_cost_2030)
    print(f"Protocol Dividend (Trillion Euro): {protocol_dividend:.2f}")

    # Example for Sovereign Horizon Equation
    re_share = 0.8 # 80% renewable share
    protocol_depth = 7 # Example protocol depth
    fragility = 0.3 # Example fragility
    stability = core.sovereign_horizon_equation(re_share, protocol_depth, fragility)
    print(f"Civilizational Stability (example): {stability:.2f}")

    # Example for Success Polynomial
    asset_factors_example = [0.5, 0.3] # Example values for (xi * Asseti)
    ssov = core.success_polynomial(asset_factors_example, core.protocol_multiplier_storage, core.protocol_multiplier_grid_intelligence)
    print(f"Sovereign Success Polynomial (example): {ssov:.2f}")

    print("SCP Framework:", core.scp_framework_description())
    print("SEP Framework:", core.sep_evolution_explorer_description())
    print("Spy Mode Claims:", core.spy_mode_claims())
