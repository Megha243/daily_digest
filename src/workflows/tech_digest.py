from src.services.db import init_db, save_items, get_items, clear_items
from src.tools.fetch_hn import fetch_hacker_news
from src.tools.fetch_product import fetch_product_news
from src.services.llm_client import query_llm
from src.services.delivery import send_email, send_telegram
from src.models.item import Item


def build_summary_prompt(category: str, title: str, content: str) -> str:
    """
    Build a strict prompt to enforce 150–200 word summaries.
    """
    return f"""
You are an expert technical writer.

Summarize the following {category} article in **150 to 200 words only**.

Rules:
- Do NOT exceed 200 words
- No bullet points
- Clear, concise English
- Focus on key ideas and insights
- Do not add external information

Title:
{title}

Article:
{content}
"""


def main():
    # --- Database Setup ---
    init_db()
    clear_items()

    # --- Fetch News ---
    tech_items = fetch_hacker_news()
    product_items = fetch_product_news()

    save_items(tech_items)
    save_items(product_items)

    # --- Load from DB ---
    db_items = get_items()

    tech_db_items = [i for i in db_items if i["source"] == "Hacker News"]
    product_db_items = [i for i in db_items if i["source"] == "Product Hunt"]

    final_items = []

    # --- Summarize Tech News ---
    for item in tech_db_items:
        print(f"Sending to Ollama (Tech): {item['title']}")
        prompt = build_summary_prompt(
            "tech",
            item["title"],
            item["content"]
        )
        summary = query_llm(prompt)
        print(f"Received summary for (Tech): {item['title']}")

        final_items.append(
            Item(
                title=item["title"],
                source=item["source"],
                link=item["link"],
                summary=summary
            )
        )

    # --- Summarize Product News ---
    for item in product_db_items:
        print(f"Sending to Ollama (Product): {item['title']}")
        prompt = build_summary_prompt(
            "product",
            item["title"],
            item["content"]
        )
        summary = query_llm(prompt)
        print(f"Received summary for (Product): {item['title']}")

        final_items.append(
            Item(
                title=item["title"],
                source=item["source"],
                link=item["link"],
                summary=summary
            )
        )

    # --- Deliver Digest ---
    send_email(final_items)
    send_telegram(final_items)

    print("✅ Digest sent via Email and Telegram successfully.")


if __name__ == "__main__":
    main()
