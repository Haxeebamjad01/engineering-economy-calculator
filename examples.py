from calculator import EngineeringEconomyCalculator 

def solve_all_examples():
    calc = EngineeringEconomyCalculator()
    print("=== BASICS OF ENGINEERING ECONOMY: EXAMPLE SOLUTIONS ===\n")

    # --- CHAPTER 1 EXAMPLES ---
    print("--- Chapter 1: Foundations ---")
    
    # Example 1.4: Simple Interest
    P_14 = 1000000
    i_14 = 0.05
    n_14 = 3
    interest_14 = calc.simple_interest(P_14, i_14, n_14)
    print(f"Example 1.4 (Simple Interest): Total Repayment = ${(P_14 + interest_14):,.2f}")

    # Example 1.5: Compound Interest
    total_15 = calc.compound_interest_total(1000, 0.05, 3)
    print(f"Example 1.5 (Compound Interest): Total Due = ${total_15:,.2f}\n")


    # --- CHAPTER 2 EXAMPLES ---
    print("--- Chapter 2: Factors & Equivalency ---")
    
    # Example 2.1: (F/P)
    F_21 = calc.future_given_present(12000, 0.08, 24)
    print(f"Example 2.1 (F/P): Future Worth = ${F_21:,.2f}")

    # Example 2.4: (P/A)
    P_24 = calc.present_given_annual(600, 0.16, 9)
    print(f"Example 2.4 (P/A): Present Worth = ${P_24:,.2f}")

    # Example 2.5: (F/A)
    F_25 = calc.future_given_annual(1000, 0.14, 8)
    print(f"Example 2.5 (F/A): Future Worth = ${F_25:,.2f}k")

    # Example 2.7: Arithmetic Gradient (P/A + P/G)
    base_A = 5000
    G = 500
    i_27 = 0.10
    n_27 = 10
    P_base = calc.present_given_annual(base_A, i_27, n_27)
    P_grad = calc.present_given_arithmetic_gradient(G, i_27, n_27)
    print(f"Example 2.7 (Arithmetic Gradient): Total Present Worth = ${(P_base + P_grad):,.0f}")

    # Example 2.9: Geometric Gradient
    A1 = 250000
    g = 0.05
    i_29 = 0.12
    n_29 = 5
    P_29 = calc.present_given_geometric_gradient(A1, g, i_29, n_29)
    print(f"Example 2.9 (Geometric Gradient): Present Worth = ${P_29:,.0f}\n")


    # --- CHAPTER 3 EXAMPLES ---
    print("--- Chapter 3: Nominal & Effective Rates ---")
    
    # Example for Effective Rate Calculation
    # E.g., Nominal 12% compounded monthly (m=12)
    r = 0.12
    m = 12
    eff_rate = calc.effective_interest_rate(r, m)
    print(f"Effective Rate (12% compounded monthly): {eff_rate * 100:.2f}%")

if __name__ == '__main__':
    solve_all_examples()
