class EngineeringEconomyCalculator:
    """
    Formulas from 'Basics of Engineering Economy' Chapters 1, 2, and 3.
    """
    
    # --- CHAPTER 1: Basic Interest ---
    @staticmethod
    def simple_interest(P, i, n):
        """Calculates total simple interest (Equation 1.3)"""
        return P * n * i

    @staticmethod
    def compound_interest_total(P, i, n):
        """Calculates total due for compound interest (Equation 1.4)"""
        return P * ((1 + i) ** n)

    # --- CHAPTER 2: Factors & Time Value of Money ---
    @staticmethod
    def future_given_present(P, i, n):
        """Find F given P (F/P)"""
        return P * ((1 + i) ** n)

    @staticmethod
    def present_given_future(F, i, n):
        """Find P given F (P/F)"""
        return F / ((1 + i) ** n)

    @staticmethod
    def present_given_annual(A, i, n):
        """Find P given A (P/A)"""
        return A * (((1 + i)**n - 1) / (i * (1 + i)**n))

    @staticmethod
    def annual_given_present(P, i, n):
        """Find A given P (A/P)"""
        return P * ((i * (1 + i)**n) / ((1 + i)**n - 1))

    @staticmethod
    def future_given_annual(A, i, n):
        """Find F given A (F/A)"""
        return A * (((1 + i)**n - 1) / i)

    @staticmethod
    def annual_given_future(F, i, n):
        """Find A given F (A/F)"""
        return F * (i / ((1 + i)**n - 1))

    @staticmethod
    def present_given_arithmetic_gradient(G, i, n):
        """Find P given G (P/G) - Arithmetic Gradient (Equation 2.3)"""
        term1 = ((1 + i)**n - 1) / (i * (1 + i)**n)
        term2 = n / ((1 + i)**n)
        return (G / i) * (term1 - term2)

    @staticmethod
    def present_given_geometric_gradient(A1, g, i, n):
        """Find P given geometric gradient g (Equation 2.7)"""
        if i == g:
            return A1 * (n / (1 + i))
        else:
            return A1 * (1 - ((1 + g) / (1 + i))**n) / (i - g)

    # --- CHAPTER 3: Nominal & Effective Rates ---
    @staticmethod
    def effective_interest_rate(r, m):
        """Find effective annual interest rate given nominal rate r and compounding periods m"""
        return ((1 + (r / m)) ** m) - 1
