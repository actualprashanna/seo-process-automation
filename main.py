import logging

# Configure logging to show each agent's step in the console
logging.basicConfig(level=logging.INFO, format='%(message)s')

# -------------------- Agent Definitions --------------------

def keyword_research_agent(seed_term):
    """
    Simulates keyword research by expanding a seed term into 5 sub-topics with mock monthly search volumes.
    """
    logging.info(f"[Keyword Research Agent] Input seed term: '{seed_term}'")
    # Mock keyword research results (would call real API in production)
    subtopics = [
        {"keyword": "best wireless headphones", "volume": 12000},
        {"keyword": "noise cancelling earbuds", "volume": 8800},
        {"keyword": "bluetooth noise cancelling headphones", "volume": 6500},
        {"keyword": "wireless over ear headphones", "volume": 4800},
        {"keyword": "wireless headphones for travel", "volume": 3700},
    ]
    logging.info(f"[Keyword Research Agent] Output sub-topics: {subtopics}")
    return subtopics

def select_best_keyword(subtopics):
    """
    Selects the keyword with the highest monthly search volume.
    """
    best = max(subtopics, key=lambda x: x["volume"])
    logging.info(f"[Selection Logic] Best keyword selected: '{best['keyword']}' with volume {best['volume']}")
    return best["keyword"]

def content_brief_agent(keyword):
    """
    Generates a content brief outline for the chosen keyword, including H1, H2s, and meta description.
    """
    logging.info(f"[Content Brief Agent] Generating outline for keyword: '{keyword}'")
    brief = {
        "H1": f"{keyword.title()} - 2024 Guide",
        "H2s": [
            "What Are Noise Cancelling Headphones?",
            "Top Features to Look For",
            "Comparison of Leading Models",
            "How to Choose the Right Pair",
            "FAQs"
        ],
        "Meta Description": (
            f"Discover the best {keyword} in 2024. Read our expert guide for features, "
            "comparisons, and tips on choosing the perfect pair for your needs."
        )
    }
    logging.info(f"[Content Brief Agent] Output content brief: {brief}")
    return brief

# -------------------- Main Process Flow --------------------

def main():
    # Step 1: Define the seed term as specified
    seed_term = "wireless noise-cancelling headphones"
    logging.info(f"=== Starting SEO Automation for: '{seed_term}' ===\n")

    # Step 2: Keyword research agent discovers sub-topics
    subtopics = keyword_research_agent(seed_term)

    # Step 3: Select the best keyword (highest volume)
    best_keyword = select_best_keyword(subtopics)

    # Step 4: Content brief agent creates an outline for the best keyword
    brief = content_brief_agent(best_keyword)

    # Step 5: Print output to console in user-friendly format
    print("\n--- Output ---")
    print("Sub-topics with Monthly Search Volume:")
    for sub in subtopics:
        print(f"- {sub['keyword']}: {sub['volume']}")
    print("\nContent Brief Outline:")
    print(f"H1: {brief['H1']}")
    print("H2s:")
    for h2 in brief["H2s"]:
        print(f"  - {h2}")
    print(f"Meta Description: {brief['Meta Description']}")

# -------------------- Entry Point --------------------

if __name__ == "__main__":
    main()
